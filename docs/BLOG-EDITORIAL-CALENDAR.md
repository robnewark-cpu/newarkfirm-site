# Blog / Insights Editorial Calendar

Newark Law Offices — a sustainable publishing cadence that builds topical
authority, gives Google fresh reasons to recrawl, and feeds AI answer-engines.

## Why cadence matters (the business case)
- **Fresh content = crawl priority.** A site that publishes regularly gets
  crawled more often, which speeds indexing of the whole site.
- **Topical authority.** Clusters of related articles around each practice area
  signal expertise to Google and to AI engines (ChatGPT/Perplexity/Claude).
- **Long-tail capture.** Articles rank for specific questions ("can I keep my
  car in Chapter 7 in Texas") that practice pages don't target directly, and
  funnel readers to the practice page + consultation.

## Publishing rules (compliance)
- Every article routes through the same workflow as all content:
  draft → internal review → **legal review** → approved → published → archived.
- Informational only; every article carries the informational + no-advice +
  attorney-advertising disclaimers (reuse `partials.DISCLAIMERS`).
- No client-identifying facts, no outcome claims, no statistics that aren't
  verifiable. Link each article to its practice hub/spoke and to a consultation CTA.

## Cadence
- **Target: 2 articles/month** (sustainable for a small firm). One "evergreen"
  practice explainer + one timely/seasonal or local piece.
- Publish into `/insights/` (the existing library; `/blog` redirects there).
- Repurpose each article into a short **video script** (see video slots) and a
  social/GBP post.

## 12-month calendar (24 articles) — outline bank

### Bankruptcy (cluster: /bankruptcy-lawyer.html)
1. **"Can I keep my car and house if I file Chapter 7 in Texas?"** — exemptions
   explained; link Ch.7 + exemptions. (evergreen)
2. **"Chapter 7 vs Chapter 13: which is right for me?"** — decision guide; link both.
3. **"What happens at the 341 meeting of creditors?"** — demystify the hearing.
4. **"Medical debt and bankruptcy in Texas and Oklahoma"** — timely (healthcare costs).
5. **"Rebuilding credit in the first year after bankruptcy"** — link life-after.
6. **"Business owners: Chapter 11 vs closing the doors"** — link business/creditor hub.

### Personal injury (cluster: /personal-injury.html)
7. **"What is my Texas car accident claim worth?"** — how value is calculated (no promises).
8. **"Do I have a case? Comparative negligence in Texas and Oklahoma"** — link car-accidents.
9. **"Uninsured driver hit me — now what?"** — UM/UIM explainer.
10. **"The recorded statement trap after an accident"** — link accident checklist guide.
11. **"Truck accident claims: why they're different"** — link truck-accidents.
12. **"Storm season: underpaid wind and hail claims"** — seasonal; link insurance-disputes.

### Criminal defense (cluster: /criminal-defense-lawyer.html)
13. **"Arrested in Texas: your first 24 hours"** — link after-arrest guide.
14. **"DWI vs DUI in Texas and Oklahoma: license deadlines"** — link DUI/DWI.
15. **"Can I get this off my record? Expungement vs sealing"** — link expungement/sealing.
16. **"First-offense drug charge: diversion and dismissal options"** — link drug-charges.
17. **"What a protective order actually does"** — link protective-orders.

### Immigration & crimigration (cluster: /immigration-lawyer.html)
18. **"What happens in immigration court, step by step"** — link removal-defense.
19. **"My relative was detained by ICE — what to do in the first 48 hours"** — link bond/detainers.
20. **"Green card through marriage: adjustment vs consular processing"** — link adjustment.
21. **"Crimigration: how a guilty plea can trigger deportation"** — link crimigration (high-value).
22. **"Missed your immigration hearing? Motions to reopen"** — link motions-to-reopen.

### Local / seasonal
23. **"Dallas County court guide: where your case is heard"** — link Dallas/Dallas County.
24. **"Oklahoma City metro: bankruptcy, injury, criminal, immigration courts"** — link OKC pages.

## Article template (each post)
- H1 = the exact question/searched phrase
- Opening 2–3 sentence plain-language answer (AI-extractable)
- 3–6 short sections with H2s
- 1 FAQ block (FAQPage schema)
- Internal links to the relevant practice hub + spoke
- Consultation CTA + phone
- Disclaimer block
- (Optional) embedded video using the same script

## How to publish (mechanics)
Insights articles are hand-authored HTML in `/insights/` today. If volume grows,
add an `insights` content module to `build/` (same pattern as the practice
clusters) so articles compose from the shared partials + schema. Add each new
article URL to `EXISTING_PAGES` in `build/build.py` (or generate it) so it
enters `sitemap.xml`.
