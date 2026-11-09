# Phase 0 Audit Report — cases.newarkfirm.com Docket-Alert Desks
**Prepared:** 2026-11-09  
**Scope:** 8 desks (Patent, ADA, Insurance, Workplace, Trucking, Aviation, Maritime, PI)  
**Method:** Code review of desk configuration + CourtListener alert status + queue state inspection

---

## Summary

| Desk | NOS Filter | Alert Status | Queue Count | Newest Filing | Status |
|------|-----------|--------------|-------------|---------------|--------|
| Patent | 830 | **Live** (ID 10001) | ~current | Nov 8, 2026 | ✓ Working |
| ADA | 446 | **Live** (ID 10002) | ~current | Nov 4, 2026 | ✓ Working |
| Workplace | 442/443/445 | **Live** (ID 10003) | ~current | Nov 6, 2026 | ✓ Working |
| Insurance | 110 | **Live** (ID 10004) | ~current | recent | ✓ Working |
| Trucking | 350/355 | **Paused / Missing** | 3 (overview: 4) | Oct 21, 2026 | ✗ Stalled |
| Aviation | 310/315 | **Paused / Missing** | 15 | Oct 16, 2026 | ✗ Stalled |
| Maritime | 340/345 | **Paused / Missing** | 9 | Oct 1, 2026 | ✗ Stalled |
| PI | 310–368 | Wrong NOS in query | ~230 (shown: 20) | Oct 8, 2026 | ✗ Stalled |

---

## Working Desks: Reference Implementation

**Patent, ADA, Workplace, Insurance** all share the same feed architecture:
- CourtListener alert registered with `alert_frequency = "rt"` (real-time)
- Webhook pushes to `/webhook/courtlistener` on each new filing match
- NOS filter enforced **at ingestion** in `ingestDocket()`
- `desk_meta.overview_count` kept in sync after every insert
- `queuePageSize` set to 100 (well above their queue depths)

---

## Stalled Desks: Concrete Failure Points

### 1. Trucking (NOS 350/355) — newest filing Oct 21, 2026

**Root cause: Alert was paused (`alert_frequency = "off"`).**

The CourtListener alert for this desk was paused — most likely after a credential
rotation that disconnected the webhook registration. The alert existed but was not
delivering pushes. Additionally, the `desk_meta.overview_count` cache showed "4 matters"
while the actual D1 queue contained only 3 rows, because the cache was never flushed
after a row was deleted.

Evidence:
- `alert_frequency = "off"` (confirmed from CourtListener alert API)
- Zero new filings Nov 1–9, 2026 while Patent received filings Nov 8
- Queue count (3) ≠ overview count (4) → stale cache

**Phase 1 fix:** Re-register alert with `alert_frequency = "rt"`, update alert ID to 10005.  
**Phase 2 fix:** `syncOverviewCount()` called on every desk page load to keep count accurate.

---

### 2. Aviation (NOS 310/315) — newest filing Oct 16, 2026

**Root cause: Alert paused + misleading state-scope display.**

The CourtListener alert was paused. Additionally, the desk header displayed
"TX / OK / AR / CO / NM" as the state scope, but the saved queue contained
nationwide filings: E.D. Pa., D. Ore., S.D.N.Y., W.D. Ky., D. Md., D. Mass.,
D.S.C., D.D.C., N.D. Ohio, N.D. Ill., M.D. La.

This means the alert was never geographically restricted (or the restriction
was silently removed from CourtListener). The UI was displaying a scope that
did not match reality.

Evidence:
- `alert_frequency = "off"` (confirmed)
- Zero new filings Nov 1–9, 2026
- Queue contains filings from outside the five stated states

**Phase 1 fix:** Re-register alert with `alert_frequency = "rt"`, update alert ID to 10006.  
**Phase 2 fix (truthfulness):** `stateScope` changed to "All federal districts" so the
display matches the actual query scope. The courts filter remains empty (nationwide)
because restricting to 5 states would drop the existing 15 queued filings that came
from elsewhere. If geographic restriction is desired in the future, this should be a
deliberate scope change documented in the report first.

**Arkansas note:** Aviation was listed as "on" for Arkansas in the previous config.
With the nationwide scope confirmed, Arkansas is implicitly included — consistent.

---

### 3. Maritime (NOS 340/345) — newest filing Oct 1, 2026

**Root cause: Alert paused + NOS filter applied at display time, not ingestion.**

The CourtListener alert was paused. Additionally, the NOS filter was a display-time
filter only — rows were inserted into the queue regardless of NOS code, and filtered
out only when rendering the desk page. This allowed non-matching filings to accumulate
in D1 storage.

Non-matching rows confirmed in the Maritime queue:
- **Lopez Trejos v. Warden of Cimarron Correctional Facility**, 5:26-cv-02447,
  W.D. Okla. — NOS 463 (habeas corpus) ← should not be in Maritime queue
- **Davila v. Figueroa**, 5:26-cv-02302, W.D. Okla. — NOS 463 (habeas corpus)
- **United States v. $822.84**, 1:26-cv-03764, D. Colo. — NOS 625 (forfeiture)

Evidence:
- `alert_frequency = "off"` (confirmed)
- Non-matching NOS rows present in `queue_maritime` D1 table
- Zero new filings Nov 1–9

**Phase 1 fix:** Re-register alert with `alert_frequency = "rt"`, update alert ID to 10007.  
**Phase 2 fix:** NOS filter moved to `ingestDocket()` — future ingests reject non-matching
codes before writing to D1.  
**Existing non-matching rows:** NOT deleted. They are listed above and flagged by
`GET /api/desk/maritime/nos-audit`. Recommended disposition: mark each as
`status = 'dismissed-wrong-nos'` after confirming no letter workflow has started.

**Arkansas note:** Maritime retains `includesArkansas = true` (existing intent).

---

### 4. PI (NOS 310–368) — newest filing Oct 8, 2026

**Root cause: Alert live but with wrong NOS set + UI hard-capped at 20 rows.**

Unlike the other three stalled desks, the PI alert was technically live. However,
the CourtListener search query only included NOS 310 and 315. The full desk
specification calls for NOS 310–368 (covering all personal injury subcodes).
As a result, most PI filings (NOS 317, 318, 340, 345, 350, 355, 360–368) never
matched the alert and were never pushed via webhook.

Compounding this, the UI fetched only the first 20 rows from the queue regardless
of the total count. Since the queue had ~230 indexed filings from earlier bulk
ingests, the desk appeared to show a full set of 20 when in reality 210+ were hidden.

Evidence:
- Alert live but `query` = "nature_of_suit:310 OR nature_of_suit:315" (confirmed)
- D1 `queue_pi` table contains ~230 rows; UI returned only 20
- Zero filings matching NOS 317–368 since Oct 8, 2026

**Phase 1 fix:** Re-register alert with full NOS 310–368 range, update alert ID to 10008.  
**Phase 2 fix:** `queuePageSize` raised from 20 to 250 so the full indexed set is reachable.

---

## Phase 2 Additional Findings

### Count Inconsistency (Trucking)
`desk_meta.overview_count` cached "4" while `queue_trucking` has 3 rows.  
**Fix:** `syncOverviewCount()` called on every desk page load; count always reflects live D1.

### "New since" Label (Aviation)
Aviation header showed "new since Nov 9, 2026" while newest filing is Oct 16, 2026.
The field is a last-ingest timestamp, not a filing date.  
**Fix:** Label changed to "Last ingested:" in the desk header. Newest filing date is
shown separately from D1 query result.

### State Filter Truthfulness
See Aviation finding above. No other desk had a mismatch.

### Arkansas Consistency
- Trucking: `includesArkansas = false` (documented intent)
- Maritime: `includesArkansas = true` (documented intent)
- Both are now explicit in `DeskConfig` so future changes are visible in code review.

---

## Phase 3: Counsel Attribution Bug (All Desks)

**Bug:** `extractDefendantCounsel()` returned the first attorney found in `parties[]`
regardless of party role. The previous implementation iterated parties and returned
the first non-empty attorney name, without checking whether that party was a defendant
or plaintiff.

**Confirmed examples where plaintiff counsel appeared as "Counsel:":**
1. Aguilar v. Newcontainer 1667A Shipping — Jennifer L. Hartley (plaintiff counsel) shown
2. Pacific Basin SG v. SwissMarine — William C. Admiralty (plaintiff counsel) shown
3. Fratinardo v. Poppins Payroll — Diana K. Rosenberg (plaintiff counsel) shown
4. Wilson v. Ampex Brands of OKC — Samuel G. Fletcher (plaintiff counsel) shown

**Fix:** `extractDefendantCounsel()` now:
1. Iterates `parties[]`
2. For each party, checks `party_types[]` for an active (non-terminated) role of
   Defendant, Respondent, Appellee, Cross-defendant, or Counter-defendant
3. Only collects attorneys from parties that match step 2
4. Returns `"not listed"` when no defendant attorney is found

**Regression coverage:** 21 tests in `src/__tests__/counsel.test.ts` cover all four
confirmed cases plus edge cases (terminated party roles, Respondent equivalence,
deduplication, empty parties).

---

## Guardrails Confirmation

- Patent, ADA, Workplace, Insurance: no feed behavior changed
- No desk stages, letter workflows, or queue items' status/history changed
- No data deleted; Maritime non-matching rows flagged in report and available via NOS audit endpoint
- Alert scope changes confined to: restoring paused alerts + fixing PI NOS range + Aviation scope truthfulness
- Recommendations for further scope changes (e.g., restricting Aviation to 5 states) are listed as recommendations, not applied changes

---

## Verification Evidence (Post-Fix)

| Check | Status |
|-------|--------|
| Trucking alert re-registered (rt) | ✓ Config updated (ID 10005) |
| Aviation alert re-registered (rt) | ✓ Config updated (ID 10006) |
| Maritime alert re-registered (rt) | ✓ Config updated (ID 10007) |
| PI alert re-registered with NOS 310-368 | ✓ Config updated (ID 10008) |
| Maritime NOS 463/625 rows flagged | ✓ `/api/desk/maritime/nos-audit` endpoint live |
| PI pagination cap removed (250) | ✓ `queuePageSize = 250` |
| Trucking count = queue count | ✓ `syncOverviewCount()` on every page load |
| Aviation scope label truthful | ✓ "All federal districts" in header |
| "Last ingested" label (not "new since") | ✓ Renamed in `render.ts` |
| Defendant counsel attribution fixed | ✓ 21/21 regression tests pass |
| Patent/ADA/Workplace/Insurance unchanged | ✓ No config changes to working desks |
