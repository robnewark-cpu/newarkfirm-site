/**
 * Phase 3 regression tests — counsel attribution.
 *
 * Verified examples from the live site where plaintiff counsel was
 * incorrectly shown as defendant counsel:
 *  1. Aguilar v. Newcontainer 1667A Shipping (Maritime/PI)
 *  2. Pacific Basin SG v. SwissMarine (Maritime)
 *  3. Fratinardo v. Poppins Payroll (PI)
 *  4. Wilson v. Ampex Brands of OKC (PI)
 *
 * Each test constructs a minimal parties[] array that reflects the
 * real party/attorney structure of those dockets and asserts that:
 *  a) Plaintiff counsel is NOT returned by extractDefendantCounsel()
 *  b) Defendant counsel IS returned when present
 *  c) "not listed" is returned when no defendant attorney exists
 */

import { describe, it, expect } from "vitest";
import { extractDefendantCounsel, extractPlaintiffCounsel } from "../api/courtlistener";
import type { CLParty } from "../api/courtlistener";

// ── Helper to build minimal party fixtures ────────────────────────────────────

function makeParty(
  name: string,
  roleNames: string[],
  attorneys: { name: string }[]
): CLParty {
  return {
    name,
    party_types: roleNames.map((r) => ({
      docket: "https://www.courtlistener.com/api/rest/v4/dockets/1/",
      name: r,
      date_terminated: null,
    })),
    attorneys: attorneys.map((a) => ({
      name: a.name,
      contact_raw: "",
      roles: [],
    })),
  };
}

// ── Case 1: Aguilar v. Newcontainer 1667A Shipping (Maritime/PI) ──────────────

describe("Aguilar v. Newcontainer 1667A Shipping", () => {
  const parties: CLParty[] = [
    makeParty("Maria Aguilar", ["Plaintiff"], [{ name: "Jennifer L. Hartley" }]),
    makeParty("Newcontainer 1667A Shipping LLC", ["Defendant"], []),
  ];

  it("should NOT return plaintiff counsel as defendant counsel", () => {
    expect(extractDefendantCounsel(parties)).toBe("not listed");
  });

  it("should return plaintiff counsel correctly", () => {
    expect(extractPlaintiffCounsel(parties)).toBe("Jennifer L. Hartley");
  });
});

describe("Aguilar v. Newcontainer — with defendant counsel", () => {
  const parties: CLParty[] = [
    makeParty("Maria Aguilar", ["Plaintiff"], [{ name: "Jennifer L. Hartley" }]),
    makeParty("Newcontainer 1667A Shipping LLC", ["Defendant"], [
      { name: "Robert T. Mercer" },
    ]),
  ];

  it("returns only defendant counsel", () => {
    expect(extractDefendantCounsel(parties)).toBe("Robert T. Mercer");
  });

  it("does not include plaintiff counsel in defendant result", () => {
    const result = extractDefendantCounsel(parties);
    expect(result).not.toContain("Jennifer L. Hartley");
  });
});

// ── Case 2: Pacific Basin SG v. SwissMarine (Maritime) ───────────────────────

describe("Pacific Basin SG v. SwissMarine", () => {
  const parties: CLParty[] = [
    makeParty("Pacific Basin SG Pte Ltd", ["Plaintiff"], [
      { name: "William C. Admiralty" },
    ]),
    makeParty("SwissMarine Corporation Ltd", ["Defendant"], []),
  ];

  it("should NOT show plaintiff counsel (William C. Admiralty) as defendant counsel", () => {
    const result = extractDefendantCounsel(parties);
    expect(result).not.toContain("William C. Admiralty");
    expect(result).toBe("not listed");
  });
});

// ── Case 3: Fratinardo v. Poppins Payroll (PI) ───────────────────────────────

describe("Fratinardo v. Poppins Payroll", () => {
  const parties: CLParty[] = [
    makeParty("Angela Fratinardo", ["Plaintiff"], [
      { name: "Diana K. Rosenberg" },
    ]),
    makeParty("Poppins Payroll Inc.", ["Defendant"], [
      { name: "Marcus O. Delaney" },
    ]),
  ];

  it("returns defendant counsel, not plaintiff counsel", () => {
    expect(extractDefendantCounsel(parties)).toBe("Marcus O. Delaney");
  });

  it("plaintiff counsel is separate", () => {
    expect(extractPlaintiffCounsel(parties)).toBe("Diana K. Rosenberg");
  });

  it("does not mix plaintiff into defendant result", () => {
    expect(extractDefendantCounsel(parties)).not.toContain("Diana K. Rosenberg");
  });
});

// ── Case 4: Wilson v. Ampex Brands of OKC (PI) ───────────────────────────────

describe("Wilson v. Ampex Brands of OKC", () => {
  const parties: CLParty[] = [
    makeParty("Darnell Wilson", ["Plaintiff"], [
      { name: "Samuel G. Fletcher" },
    ]),
    makeParty("Ampex Brands of OKC LLC", ["Defendant"], []),
  ];

  it("returns 'not listed' when defendant has no attorney on record", () => {
    expect(extractDefendantCounsel(parties)).toBe("not listed");
  });

  it("does not use plaintiff counsel as fallback", () => {
    expect(extractDefendantCounsel(parties)).not.toContain("Samuel G. Fletcher");
  });
});

// ── Edge cases ────────────────────────────────────────────────────────────────

describe("counsel attribution edge cases", () => {
  it("handles terminated party roles correctly", () => {
    const parties: CLParty[] = [
      {
        name: "Former Defendant LLC",
        party_types: [
          {
            docket: "",
            name: "Defendant",
            date_terminated: "2025-06-01", // terminated
          },
        ],
        attorneys: [{ name: "Ghost Attorney", contact_raw: "", roles: [] }],
      },
      makeParty("Active Plaintiff", ["Plaintiff"], [{ name: "Active Counsel" }]),
    ];

    // Terminated defendant party should not contribute counsel
    expect(extractDefendantCounsel(parties)).toBe("not listed");
  });

  it("handles Respondent role as equivalent to Defendant", () => {
    const parties: CLParty[] = [
      makeParty("Petitioner Corp", ["Petitioner"], [{ name: "Petitioner Counsel" }]),
      makeParty("Respondent Agency", ["Respondent"], [{ name: "Agency Counsel" }]),
    ];
    expect(extractDefendantCounsel(parties)).toBe("Agency Counsel");
    expect(extractDefendantCounsel(parties)).not.toContain("Petitioner Counsel");
  });

  it("deduplicates attorney names when same attorney represents multiple defendants", () => {
    const parties: CLParty[] = [
      makeParty("Defendant A", ["Defendant"], [{ name: "Shared Counsel" }]),
      makeParty("Defendant B", ["Defendant"], [{ name: "Shared Counsel" }]),
    ];
    const result = extractDefendantCounsel(parties);
    expect(result).toBe("Shared Counsel");
    // Should not appear twice
    expect(result.split("Shared Counsel").length - 1).toBe(1);
  });

  it("returns empty parties as 'not listed'", () => {
    expect(extractDefendantCounsel([])).toBe("not listed");
  });
});

// ── NOS filter tests ──────────────────────────────────────────────────────────

import { DESKS } from "../desks/config";

describe("NOS filter configuration", () => {
  it("Maritime desk only contains NOS 340 and 345", () => {
    const maritime = DESKS.find((d) => d.id === "maritime")!;
    expect(maritime.nosFilter).toEqual([340, 345]);
  });

  it("PI desk contains all NOS codes from 310-368 range", () => {
    const pi = DESKS.find((d) => d.id === "pi")!;
    // Must include 310, 315, 350, 355, 360, 362, 363, 365, 367, 368
    const required = [310, 315, 350, 355, 360, 362, 363, 365, 367, 368];
    for (const nos of required) {
      expect(pi.nosFilter).toContain(nos);
    }
  });

  it("Maritime NOS filter does NOT include 463 or 625", () => {
    const maritime = DESKS.find((d) => d.id === "maritime")!;
    expect(maritime.nosFilter).not.toContain(463);
    expect(maritime.nosFilter).not.toContain(625);
  });

  it("Trucking NOS filter is exactly 350 and 355", () => {
    const trucking = DESKS.find((d) => d.id === "trucking")!;
    expect(trucking.nosFilter).toEqual([350, 355]);
  });

  it("Aviation NOS filter is exactly 310 and 315", () => {
    const aviation = DESKS.find((d) => d.id === "aviation")!;
    expect(aviation.nosFilter).toEqual([310, 315]);
  });

  it("PI queue page size is raised above 20", () => {
    const pi = DESKS.find((d) => d.id === "pi")!;
    expect(pi.queuePageSize).toBeGreaterThan(20);
  });

  it("Aviation state scope is nationwide (Phase 2 truthfulness fix)", () => {
    const aviation = DESKS.find((d) => d.id === "aviation")!;
    expect(aviation.stateScope.toLowerCase()).toContain("all federal");
  });
});
