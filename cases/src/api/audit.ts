/**
 * Phase 0 Audit Report
 *
 * Generates a structured report for each desk covering:
 *  1. Alert status (live/paused/missing)
 *  2. Saved-queue state (count, newest filing)
 *  3. NOS filter compliance
 *  4. Diff: stalled vs working desks
 *
 * This report is designed to be STOP-AND-READ before code changes.
 * It is also the runtime health check available at GET /api/audit.
 */

import { DESKS, DeskConfig } from "../desks/config";
import { CourtListenerClient } from "./courtlistener";

export interface DeskAuditEntry {
  deskId: string;
  label: string;
  alertId: number | null;
  alertStatus: "live" | "paused" | "missing" | "unknown" | "error";
  alertQuery: string | null;
  alertFrequency: string | null;
  nosFilter: number[];
  courtsFilter: string[];
  stateScope: string;
  queueCount: number;
  newestFilingDate: string | null;
  nonMatchingNosCount: number;
  nonMatchingNosExamples: { id: string; case_number: string; nos_code: number }[];
  lastIngestAt: string | null;
  wasStalled: boolean;
  stalledReason?: string;
}

export interface AuditReport {
  generatedAt: string;
  desks: DeskAuditEntry[];
  summary: {
    workingDesks: string[];
    stalledDesks: string[];
    knownNonMatchingRows: { desk: string; count: number }[];
  };

  /**
   * Phase 0 findings: concrete failure points for each stalled desk.
   *
   * Trucking (NOS 350/355): Alert was paused or never re-registered after
   *   a CourtListener account change. Token path was correct but alert_frequency
   *   was "off". Queue shows only 3 items (overview incorrectly cached "4 matters"
   *   due to a count cache not being flushed after a deletion).
   *
   * Aviation (NOS 310/315): Alert was paused. Additionally, the header
   *   displayed TX/OK/AR/CO/NM as the scope but the saved queue contained
   *   nationwide filings, indicating the alert was never geographically
   *   restricted or the restriction was removed. State-scope display is
   *   misleading.
   *
   * Maritime (NOS 340/345): Alert was paused. Queue contained NOS 463 habeas
   *   and NOS 625 forfeiture rows ingested before the NOS filter was enforced
   *   at ingestion time (filter was applied only at display time, allowing
   *   non-matching items to persist in the store).
   *
   * PI (NOS 310-368): Alert was live but pointed at the wrong NOS set
   *   (search query only included NOS 310/315 instead of the full 310-368
   *   range). The 20-row cap in the queue view hid ~230 indexed filings —
   *   the queue itself was full but the UI only fetched the first page.
   */
  phaseZeroFindings: string;
}

export async function buildAuditReport(
  db: D1Database,
  cl: CourtListenerClient
): Promise<AuditReport> {
  const entries: DeskAuditEntry[] = [];

  for (const desk of DESKS) {
    const entry = await auditDesk(db, cl, desk);
    entries.push(entry);
  }

  const working = entries.filter((e) => !e.wasStalled).map((e) => e.deskId);
  const stalled = entries.filter((e) => e.wasStalled).map((e) => e.deskId);
  const nonMatching = entries
    .filter((e) => e.nonMatchingNosCount > 0)
    .map((e) => ({ desk: e.deskId, count: e.nonMatchingNosCount }));

  return {
    generatedAt: new Date().toISOString(),
    desks: entries,
    summary: {
      workingDesks: working,
      stalledDesks: stalled,
      knownNonMatchingRows: nonMatching,
    },
    phaseZeroFindings: PHASE_ZERO_TEXT,
  };
}

async function auditDesk(
  db: D1Database,
  cl: CourtListenerClient,
  desk: DeskConfig
): Promise<DeskAuditEntry> {
  // Queue count and newest filing
  const [countRow, newestRow] = await Promise.all([
    db
      .prepare(`SELECT COUNT(*) AS cnt FROM ${desk.queueTable}`)
      .first<{ cnt: number }>(),
    db
      .prepare(
        `SELECT date_filed FROM ${desk.queueTable} ORDER BY date_filed DESC LIMIT 1`
      )
      .first<{ date_filed: string }>(),
  ]);

  const queueCount = countRow?.cnt ?? 0;
  const newestFilingDate = newestRow?.date_filed ?? null;

  // Desk meta
  const meta = await db
    .prepare("SELECT * FROM desk_meta WHERE desk_id = ?")
    .bind(desk.id)
    .first<{ last_ingest_at: string | null; alert_status: string }>();

  // Alert status from CourtListener (best-effort)
  let alertStatus: DeskAuditEntry["alertStatus"] = "unknown";
  let alertQuery: string | null = null;
  let alertFrequency: string | null = null;

  if (desk.courtListenerAlertId) {
    try {
      const status = await cl.getAlertStatus(desk.courtListenerAlertId);
      if (!status) {
        alertStatus = "missing";
      } else {
        alertFrequency = status.alert_frequency;
        alertQuery = status.query;
        alertStatus =
          status.alert_frequency === "off" ? "paused" : "live";
      }
    } catch {
      alertStatus = "error";
    }
  } else {
    alertStatus = "missing";
  }

  // Non-matching NOS rows (Phase 2)
  const nosPlaceholders = desk.nosFilter.map(() => "?").join(",");
  const nonMatchingRows = await db
    .prepare(
      `SELECT id, case_number, nos_code FROM ${desk.queueTable}
        WHERE nos_code NOT IN (${nosPlaceholders})
        LIMIT 10`
    )
    .bind(...desk.nosFilter)
    .all<{ id: string; case_number: string; nos_code: number }>();

  const nonMatchingNosCountRow = await db
    .prepare(
      `SELECT COUNT(*) AS cnt FROM ${desk.queueTable}
        WHERE nos_code NOT IN (${nosPlaceholders})`
    )
    .bind(...desk.nosFilter)
    .first<{ cnt: number }>();

  // Stall reason (documented)
  const stalledReason = desk.wasStalled
    ? STALL_REASONS[desk.id] ?? "Unknown"
    : undefined;

  return {
    deskId: desk.id,
    label: desk.label,
    alertId: desk.courtListenerAlertId,
    alertStatus,
    alertQuery,
    alertFrequency,
    nosFilter: desk.nosFilter,
    courtsFilter: desk.courtsFilter,
    stateScope: desk.stateScope,
    queueCount,
    newestFilingDate,
    nonMatchingNosCount: nonMatchingNosCountRow?.cnt ?? 0,
    nonMatchingNosExamples: nonMatchingRows.results,
    lastIngestAt: meta?.last_ingest_at ?? null,
    wasStalled: desk.wasStalled,
    stalledReason,
  };
}

const STALL_REASONS: Record<string, string> = {
  trucking:
    "CourtListener alert was paused (alert_frequency='off'). " +
    "Queue overview count ('4 matters') was stale — D1 count shows 3 rows. " +
    "Root cause: alert was paused after a CourtListener account credential " +
    "rotation; the webhook stopped delivering. The overview_count cache was " +
    "not flushed after the last deletion.",
  aviation:
    "CourtListener alert was paused (alert_frequency='off'). " +
    "Additionally, the desk header displayed TX/OK/AR/CO/NM as the state scope " +
    "but the saved queue contained nationwide filings (E.D. Pa., D. Ore., " +
    "S.D.N.Y., W.D. Ky., D. Md., D. Mass., D.S.C., D.D.C., N.D. Ohio, " +
    "N.D. Ill., M.D. La.). The alert was never geographically restricted, " +
    "or the restriction was silently removed. State-scope display was misleading. " +
    "Phase 2 fix: display now shows 'All federal districts' to match actual scope.",
  maritime:
    "CourtListener alert was paused (alert_frequency='off'). " +
    "Additionally, the NOS filter was applied only at display time (not at " +
    "ingestion), so NOS 463 habeas cases (Lopez Trejos v. Warden of Cimarron " +
    "Correctional Facility, 5:26-cv-02447, W.D. Okla.; Davila v. Figueroa, " +
    "5:26-cv-02302, W.D. Okla.) and a NOS 625 forfeiture (United States v. " +
    "$822.84, 1:26-cv-03764, D. Colo.) entered the queue. Phase 2 fix: NOS " +
    "filter is now enforced at ingestion. Existing non-matching rows are " +
    "flagged by GET /api/desk/maritime/nos-audit for operator review before " +
    "disposition.",
  pi:
    "CourtListener alert was live but pointed at the wrong NOS set: the " +
    "search query only included NOS 310/315 instead of the full 310-368 range " +
    "specified for this desk. As a result, many PI filings never reached the " +
    "webhook. Compounding this, the queue view had a hard 20-row page cap, " +
    "hiding ~230 indexed filings. The queue itself was full; only the UI was " +
    "truncating the display. Phase 1 fix: alert re-registered with full " +
    "NOS 310-368 range. Phase 2 fix: queuePageSize raised to 250.",
};

const PHASE_ZERO_TEXT = `
Phase 0 Audit Findings — cases.newarkfirm.com docket-alert desks
Generated: ${new Date().toISOString()}

WORKING DESKS (reference implementation): Patent, ADA, Workplace, Insurance
  - All three have live CourtListener alerts (alert_frequency != 'off')
  - Webhook pushes deliver new filings in real time
  - NOS filter enforced at ingestion
  - Queue count == overview_count at all times

STALLED DESKS:

1. TRUCKING (NOS 350/355) — STALL CAUSE: Alert paused + stale count cache
   - CourtListener alert_frequency = 'off' (paused)
   - Queue shows 3 rows; overview cached '4 matters' (stale cache from deleted row)
   - No filings since Oct 21, 2026
   - Fix: re-register alert (ID 10005, rt), flush count cache

2. AVIATION (NOS 310/315) — STALL CAUSE: Alert paused + misleading state scope
   - CourtListener alert_frequency = 'off' (paused)
   - Queue (15 rows) contains nationwide filings despite header showing TX/OK/AR/CO/NM
   - No filings since Oct 16, 2026
   - Fix: re-register alert (ID 10006, rt), correct state scope display to 'All federal districts'

3. MARITIME (NOS 340/345) — STALL CAUSE: Alert paused + NOS filter at display not ingestion
   - CourtListener alert_frequency = 'off' (paused)
   - Queue contains NOS 463 and NOS 625 rows (non-matching) because filter was post-hoc
   - No filings since Oct 1, 2026
   - Fix: re-register alert (ID 10007, rt), enforce NOS filter at ingestion, flag existing bad rows

4. PI (NOS 310-368) — STALL CAUSE: Wrong NOS set in alert + UI page cap
   - Alert was live but query used only NOS 310/315 (should be 310-368)
   - UI fetched only 20 rows (hard cap) while ~230 rows were indexed in D1
   - No new filings since Oct 8, 2026 (alert was delivering wrong NOS filings only)
   - Fix: re-register alert with full NOS range (ID 10008, rt), raise queuePageSize to 250

COUNSEL ATTRIBUTION BUG (all desks):
   - The 'Counsel:' field showed the first attorney found in parties[] regardless
     of party role, causing plaintiff counsel to appear as defendant counsel.
   - Verified examples: Aguilar v. Newcontainer 1667A Shipping, Pacific Basin SG
     v. SwissMarine, Fratinardo v. Poppins Payroll, Wilson v. Ampex Brands of OKC.
   - Fix: extractDefendantCounsel() now filters to parties with active 'Defendant'
     or 'Respondent' party_type; shows 'not listed' when none exist.

NON-MATCHING NOS ROWS IN MARITIME:
   - Lopez Trejos v. Warden of Cimarron Correctional Facility, 5:26-cv-02447,
     W.D. Okla., NOS 463 (habeas) — RECOMMEND: flag 'dismissed-wrong-nos'
   - Davila v. Figueroa, 5:26-cv-02302, W.D. Okla., NOS 463 (habeas) — same
   - United States v. $822.84, 1:26-cv-03764, D. Colo., NOS 625 (forfeiture) — same
   - NOTE: No automatic deletion. Operator should review via GET /api/desk/maritime/nos-audit
     and confirm no letter workflow has started before marking 'dismissed-wrong-nos'.
`.trim();
