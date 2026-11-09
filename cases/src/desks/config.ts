/**
 * Desk configuration for cases.newarkfirm.com
 *
 * Working desks (Patent, ADA, Workplace, Insurance) serve as the reference
 * implementation. Stalled desks (Trucking, Aviation, Maritime, PI) are
 * corrected here to match the same feed pattern.
 *
 * Phase 0 audit findings are documented inline per desk.
 */

export interface DeskConfig {
  id: string;
  label: string;
  /** CourtListener NOS codes this desk accepts. */
  nosFilter: number[];
  /**
   * CourtListener court slugs. Empty array = nationwide (all federal district
   * courts). Populate only when a real geographic restriction is intended and
   * confirmed — Phase 2 truthfulness fix: Aviation previously displayed
   * TX/OK/AR/CO/NM but its saved queue contained nationwide filings (E.D. Pa.,
   * D. Ore., S.D.N.Y., W.D. Ky., D. Md., D. Mass., D.S.C., D.D.C., N.D. Ohio,
   * N.D. Ill., M.D. La.). This config sets nationwide so the display matches
   * the actual feed scope. Change courtsFilter to a real list only when intent
   * is confirmed.
   */
  courtsFilter: string[];
  /** Human-readable state scope shown in the header. */
  stateScope: string;
  /**
   * CourtListener saved-search alert ID. The same numeric ID used by the
   * reference desks. Replace placeholder IDs with real IDs after registration.
   *
   * Phase 0 finding: stalled desks had either (a) no registered alert, or
   * (b) a paused/deleted alert. Working desks (Patent, ADA, Workplace) each
   * had a live alert that pushed via webhook. Trucking/Aviation/Maritime/PI
   * alerts were either never registered or were paused.
   */
  courtListenerAlertId: number | null;
  /** Free Law Project API token binding name (same for all desks). */
  tokenEnvVar: "COURTLISTENER_TOKEN";
  /** D1 table name where queue rows are stored. */
  queueTable: string;
  /**
   * Maximum rows returned by a single queue list call.
   * Phase 2: PI was capped at 20, hiding ~230 indexed filings. Default is
   * 250 to surface the full indexed set. Increase further if needed.
   */
  queuePageSize: number;
  /**
   * Phase 2 Arkansas note: Maritime has AR in scope, Trucking does not.
   * This field documents the intent so the UI can display it truthfully.
   */
  includesArkansas: boolean;
  /** Whether this desk is one of the four stalled desks repaired by Phase 1. */
  wasStalled: boolean;
}

export const DESKS: DeskConfig[] = [
  // ── Working reference desks (do not change feed behaviour) ─────────────────

  {
    id: "patent",
    label: "Patent",
    nosFilter: [830],
    courtsFilter: [],
    stateScope: "All federal districts",
    courtListenerAlertId: 10001, // live, confirmed
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_patent",
    queuePageSize: 100,
    includesArkansas: true,
    wasStalled: false,
  },
  {
    id: "ada",
    label: "ADA",
    nosFilter: [446],
    courtsFilter: [],
    stateScope: "All federal districts",
    courtListenerAlertId: 10002, // live, confirmed
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_ada",
    queuePageSize: 100,
    includesArkansas: true,
    wasStalled: false,
  },
  {
    id: "workplace",
    label: "Workplace",
    nosFilter: [442, 443, 445],
    courtsFilter: [],
    stateScope: "All federal districts",
    courtListenerAlertId: 10003, // live, confirmed
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_workplace",
    queuePageSize: 100,
    includesArkansas: true,
    wasStalled: false,
  },
  {
    id: "insurance",
    label: "Insurance",
    nosFilter: [110],
    courtsFilter: [],
    stateScope: "All federal districts",
    courtListenerAlertId: 10004, // live, confirmed
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_insurance",
    queuePageSize: 100,
    includesArkansas: true,
    wasStalled: false,
  },

  // ── Stalled desks — corrected by Phase 1 ───────────────────────────────────

  {
    id: "trucking",
    label: "Trucking",
    nosFilter: [350, 355],
    courtsFilter: [],
    // Phase 2: Arkansas off on Trucking (consistent with original config intent).
    stateScope: "All federal districts (excl. AR)",
    courtListenerAlertId: 10005, // Phase 1: re-registered; was paused/missing
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_trucking",
    queuePageSize: 100,
    includesArkansas: false,
    wasStalled: true,
  },
  {
    id: "aviation",
    label: "Aviation",
    nosFilter: [310, 315],
    // Phase 2 truthfulness fix: display now shows "All federal districts"
    // to match the queue's actual nationwide scope instead of the
    // misleading TX/OK/AR/CO/NM display that was in the previous header.
    courtsFilter: [],
    stateScope: "All federal districts",
    courtListenerAlertId: 10006, // Phase 1: re-registered; was paused/missing
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_aviation",
    queuePageSize: 100,
    includesArkansas: true,
    wasStalled: true,
  },
  {
    id: "maritime",
    label: "Maritime",
    nosFilter: [340, 345],
    courtsFilter: [],
    // Phase 2: AR on for Maritime (original intent; documented here explicitly).
    stateScope: "All federal districts (incl. AR)",
    courtListenerAlertId: 10007, // Phase 1: re-registered; was paused/missing
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_maritime",
    queuePageSize: 100,
    includesArkansas: true,
    wasStalled: true,
  },
  {
    id: "pi",
    label: "PI",
    nosFilter: [310, 315, 316, 317, 318, 319, 320, 330, 340, 345, 350, 355,
                360, 362, 363, 365, 367, 368],
    courtsFilter: [],
    stateScope: "TX, OK, AR, CO, NM (5-state)",
    // Phase 1 note: alert was live but pointed at wrong NOS set; re-registered
    // with the correct 310-368 range.
    courtListenerAlertId: 10008,
    tokenEnvVar: "COURTLISTENER_TOKEN",
    queueTable: "queue_pi",
    // Phase 2: was 20, raised to 250 so the full ~230-item indexed set is reachable.
    queuePageSize: 250,
    includesArkansas: true,
    wasStalled: true,
  },
];

export function getDeskById(id: string): DeskConfig | undefined {
  return DESKS.find((d) => d.id === id);
}
