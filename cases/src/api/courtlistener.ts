/**
 * CourtListener REST API v4 client.
 *
 * Covers:
 *  - Docket search (live refresh)
 *  - Alert registration / status check
 *  - Party/attorney lookup for counsel attribution (Phase 3)
 */

export interface CLDocket {
  id: number;
  docket_number: string;
  case_name: string;
  court: string; // slug, e.g. "txnd"
  date_filed: string; // ISO date
  nature_of_suit: string; // textual, e.g. "350"
  /** Populated when fetched from /dockets/{id}/parties/ */
  parties?: CLParty[];
}

export interface CLParty {
  name: string;
  party_types: CLPartyType[];
  attorneys: CLAttorney[];
}

export interface CLPartyType {
  docket: string;
  name: string; // e.g. "Plaintiff", "Defendant", "Petitioner", "Respondent"
  date_terminated: string | null;
}

export interface CLAttorney {
  name: string;
  contact_raw: string;
  roles: { role: string; date_action: string | null }[];
}

export interface CLSearchResult {
  count: number;
  next: string | null;
  results: CLDocket[];
}

export interface CLAlertStatus {
  id: number;
  name: string;
  query: string;
  alert_frequency: string; // "rt" | "dly" | "wly" | "mly" | "off"
  date_created: string;
  date_modified: string;
}

export class CourtListenerClient {
  private base: string;
  private token: string;

  constructor(base: string, token: string) {
    this.base = base.replace(/\/$/, "");
    this.token = token;
  }

  private headers(): HeadersInit {
    return {
      Authorization: `Token ${this.token}`,
      "Content-Type": "application/json",
    };
  }

  /**
   * Search dockets by NOS codes and optional court filter.
   * Returns up to pageSize results ordered by date_filed descending.
   *
   * Phase 1 fix: all stalled desks use this same search path and token.
   */
  async searchDockets(opts: {
    nosCodes: number[];
    courts: string[];
    pageSize: number;
    cursor?: string;
  }): Promise<CLSearchResult> {
    const params = new URLSearchParams();
    params.set("type", "r"); // RECAP/dockets
    params.set("order_by", "-date_filed");
    params.set("page_size", String(Math.min(opts.pageSize, 100)));

    // NOS filter — multiple values passed as repeated params
    for (const nos of opts.nosCodes) {
      params.append("nature_of_suit", String(nos));
    }

    // Court filter
    for (const court of opts.courts) {
      params.append("court", court);
    }

    if (opts.cursor) {
      params.set("cursor", opts.cursor);
    }

    const url = `${this.base}/dockets/?${params}`;
    const res = await fetch(url, { headers: this.headers() });

    if (!res.ok) {
      throw new Error(`CourtListener search failed: ${res.status} ${await res.text()}`);
    }

    return (await res.json()) as CLSearchResult;
  }

  /**
   * Fetch a single docket with its parties/attorneys expanded.
   * Used by counsel attribution (Phase 3).
   */
  async getDocketWithParties(docketId: number): Promise<CLDocket> {
    const res = await fetch(
      `${this.base}/dockets/${docketId}/?fields=id,docket_number,case_name,court,date_filed,nature_of_suit,parties`,
      { headers: this.headers() }
    );

    if (!res.ok) {
      throw new Error(`CourtListener docket fetch failed: ${res.status}`);
    }

    return (await res.json()) as CLDocket;
  }

  /**
   * Check an alert's status (live / paused / deleted).
   * Returns null when the alert does not exist.
   *
   * Phase 0 audit use: call this for each desk's alertId.
   */
  async getAlertStatus(alertId: number): Promise<CLAlertStatus | null> {
    const res = await fetch(`${this.base}/alerts/${alertId}/`, {
      headers: this.headers(),
    });

    if (res.status === 404) return null;
    if (!res.ok) throw new Error(`Alert status check failed: ${res.status}`);
    return (await res.json()) as CLAlertStatus;
  }

  /**
   * Register (create) a new CourtListener alert for a desk.
   * Returns the new alert ID.
   *
   * Phase 1: used to re-register stalled desks' alerts.
   */
  async registerAlert(opts: {
    name: string;
    nosCodes: number[];
    courts: string[];
    webhookUrl: string;
  }): Promise<number> {
    const queryParts: string[] = [];
    for (const nos of opts.nosCodes) {
      queryParts.push(`nature_of_suit:${nos}`);
    }
    for (const court of opts.courts) {
      queryParts.push(`court:${court}`);
    }

    const body = {
      name: opts.name,
      query: queryParts.join(" OR "),
      rate: "rt", // real-time
      alert_type: "docket",
    };

    const res = await fetch(`${this.base}/alerts/`, {
      method: "POST",
      headers: this.headers(),
      body: JSON.stringify(body),
    });

    if (!res.ok) {
      throw new Error(`Alert registration failed: ${res.status} ${await res.text()}`);
    }

    const data = (await res.json()) as { id: number };
    return data.id;
  }
}

// ── Counsel attribution (Phase 3) ─────────────────────────────────────────────

/**
 * Extract defendant counsel from a docket's parties list.
 *
 * Bug fixed: previously the code returned the first attorney found regardless
 * of party role, which caused plaintiff counsel to appear in the "Counsel:"
 * field (e.g. Aguilar v. Newcontainer 1667A Shipping, Pacific Basin SG v.
 * SwissMarine, Fratinardo v. Poppins Payroll, Wilson v. Ampex Brands of OKC).
 *
 * Now: only attorneys whose party has a current (not terminated) "Defendant"
 * or "Respondent" role are included. Returns "not listed" when no such
 * attorney exists.
 */
export function extractDefendantCounsel(parties: CLParty[]): string {
  const DEFENDANT_ROLES = new Set([
    "defendant",
    "respondent",
    "appellee",
    "cross-defendant",
    "counter-defendant",
  ]);

  const names: string[] = [];

  for (const party of parties) {
    const isDefendant = party.party_types.some(
      (pt) =>
        !pt.date_terminated &&
        DEFENDANT_ROLES.has(pt.name.toLowerCase())
    );

    if (!isDefendant) continue;

    for (const atty of party.attorneys) {
      const trimmed = atty.name.trim();
      if (trimmed && !names.includes(trimmed)) {
        names.push(trimmed);
      }
    }
  }

  return names.length > 0 ? names.join("; ") : "not listed";
}

/**
 * Extract plaintiff counsel from a docket's parties list.
 * Kept for completeness but not surfaced in the UI "Counsel:" field.
 */
export function extractPlaintiffCounsel(parties: CLParty[]): string {
  const PLAINTIFF_ROLES = new Set([
    "plaintiff",
    "petitioner",
    "appellant",
    "cross-plaintiff",
    "counter-plaintiff",
  ]);

  const names: string[] = [];

  for (const party of parties) {
    const isPlaintiff = party.party_types.some(
      (pt) =>
        !pt.date_terminated &&
        PLAINTIFF_ROLES.has(pt.name.toLowerCase())
    );

    if (!isPlaintiff) continue;

    for (const atty of party.attorneys) {
      const trimmed = atty.name.trim();
      if (trimmed && !names.includes(trimmed)) {
        names.push(trimmed);
      }
    }
  }

  return names.length > 0 ? names.join("; ") : "not listed";
}
