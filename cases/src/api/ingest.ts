/**
 * Queue ingestion: writes CourtListener dockets into the correct desk's D1
 * table after enforcing the NOS filter.
 *
 * Phase 2: NOS filter is enforced at ingestion so non-matching filings never
 * enter the queue (fixes Maritime NOS 463/625 contamination and similar).
 */

import {
  CourtListenerClient,
  CLDocket,
  CLParty,
  extractDefendantCounsel,
  extractPlaintiffCounsel,
} from "./courtlistener";
import { DeskConfig } from "../desks/config";

export interface QueueRow {
  id: string;
  docket_id: number;
  case_number: string;
  case_name: string;
  court: string;
  nos_code: number;
  date_filed: string;
  date_ingested: string;
  plaintiff_counsel: string | null;
  defendant_counsel: string | null;
  status: string;
  source_alert_id: number | null;
  raw_json: string;
}

/** Parse NOS code from CourtListener's textual nature_of_suit field. */
function parseNosCode(raw: string): number | null {
  const m = raw.match(/\d+/);
  return m ? parseInt(m[0], 10) : null;
}

/**
 * Ingest a single docket into the desk's queue.
 *
 * Returns true if the row was inserted, false if it already existed or was
 * rejected by the NOS filter.
 *
 * Phase 2 NOS filter: any docket whose parsed NOS code is not in the desk's
 * nosFilter list is silently dropped (not inserted). This prevents the Maritime
 * NOS 463/625 contamination from recurring on future ingests.
 */
export async function ingestDocket(
  db: D1Database,
  desk: DeskConfig,
  docket: CLDocket,
  alertId: number | null,
  cl: CourtListenerClient
): Promise<boolean> {
  const nosCode = parseNosCode(docket.nature_of_suit);

  // Phase 2: enforce NOS filter at ingestion
  if (nosCode === null || !desk.nosFilter.includes(nosCode)) {
    return false;
  }

  const id = `${desk.id}-${docket.id}`;

  // Check for duplicate
  const existing = await db
    .prepare(`SELECT id FROM ${desk.queueTable} WHERE id = ?`)
    .bind(id)
    .first<{ id: string }>();

  if (existing) return false;

  // Fetch parties for counsel attribution (Phase 3)
  let plaintiffCounsel: string | null = null;
  let defendantCounsel: string | null = null;

  if (docket.parties) {
    plaintiffCounsel = extractPlaintiffCounsel(docket.parties);
    defendantCounsel = extractDefendantCounsel(docket.parties);
  } else {
    try {
      const full = await cl.getDocketWithParties(docket.id);
      if (full.parties) {
        plaintiffCounsel = extractPlaintiffCounsel(full.parties);
        defendantCounsel = extractDefendantCounsel(full.parties);
      }
    } catch {
      // Best-effort; leave null if unavailable
    }
  }

  const now = new Date().toISOString();

  await db
    .prepare(
      `INSERT INTO ${desk.queueTable}
         (id, docket_id, case_number, case_name, court, nos_code,
          date_filed, date_ingested, plaintiff_counsel, defendant_counsel,
          status, source_alert_id, raw_json)
       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)`
    )
    .bind(
      id,
      docket.id,
      docket.docket_number ?? "",
      docket.case_name ?? "",
      typeof docket.court === "string" ? docket.court : (docket.court as { id: string }).id,
      nosCode,
      docket.date_filed,
      now,
      plaintiffCounsel,
      defendantCounsel,
      "new",
      alertId,
      JSON.stringify(docket)
    )
    .run();

  // Update desk_meta overview_count and last_ingest_at
  await db
    .prepare(
      `UPDATE desk_meta
          SET overview_count = (SELECT COUNT(*) FROM ${desk.queueTable}),
              last_ingest_at = ?,
              updated_at = ?
        WHERE desk_id = ?`
    )
    .bind(now, now, desk.id)
    .run();

  return true;
}

/**
 * Live-refresh a desk by querying CourtListener directly.
 *
 * Phase 1: this is the "Refresh this desk" path. All four stalled desks
 * use the same search API / token path as the working desks.
 *
 * Returns the number of new rows inserted.
 */
export async function refreshDesk(
  db: D1Database,
  desk: DeskConfig,
  cl: CourtListenerClient
): Promise<{ inserted: number; rejected: number }> {
  let inserted = 0;
  let rejected = 0;
  let cursor: string | undefined;

  // Fetch up to 3 pages (300 results) per refresh to avoid timeout
  for (let page = 0; page < 3; page++) {
    const result = await cl.searchDockets({
      nosCodes: desk.nosFilter,
      courts: desk.courtsFilter,
      pageSize: 100,
      cursor,
    });

    for (const doc of result.results) {
      const ok = await ingestDocket(db, desk, doc, desk.courtListenerAlertId, cl);
      if (ok) inserted++;
      else rejected++;
    }

    if (!result.next) break;
    const nextUrl = new URL(result.next);
    cursor = nextUrl.searchParams.get("cursor") ?? undefined;
  }

  return { inserted, rejected };
}

/**
 * List a desk's queue with cursor-based pagination.
 *
 * Phase 2 PI cap fix: uses desk.queuePageSize (250 for PI) so the full
 * indexed set is surfaced. Accepts an offset for forward-paging.
 */
export async function listQueue(
  db: D1Database,
  desk: DeskConfig,
  opts: { limit?: number; offset?: number } = {}
): Promise<{ rows: QueueRow[]; total: number }> {
  const limit = opts.limit ?? desk.queuePageSize;
  const offset = opts.offset ?? 0;

  const [rowsResult, countResult] = await Promise.all([
    db
      .prepare(
        `SELECT * FROM ${desk.queueTable}
          ORDER BY date_filed DESC
          LIMIT ? OFFSET ?`
      )
      .bind(limit, offset)
      .all<QueueRow>(),

    db
      .prepare(`SELECT COUNT(*) AS cnt FROM ${desk.queueTable}`)
      .first<{ cnt: number }>(),
  ]);

  return {
    rows: rowsResult.results,
    total: countResult?.cnt ?? 0,
  };
}

/**
 * Phase 2 count consistency: read the canonical total from D1 and sync
 * desk_meta.overview_count to match.
 */
export async function syncOverviewCount(
  db: D1Database,
  desk: DeskConfig
): Promise<number> {
  const row = await db
    .prepare(`SELECT COUNT(*) AS cnt FROM ${desk.queueTable}`)
    .first<{ cnt: number }>();

  const cnt = row?.cnt ?? 0;

  await db
    .prepare(
      `UPDATE desk_meta SET overview_count = ?, updated_at = ? WHERE desk_id = ?`
    )
    .bind(cnt, new Date().toISOString(), desk.id)
    .run();

  return cnt;
}
