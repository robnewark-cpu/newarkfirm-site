# Content Approval Workflow & Governance

Newark Law Offices — legal & ethics controls for site content.

## Principle

**No content that makes a factual claim about the firm, its people, its
outcomes, or third-party opinions of it publishes automatically.** The site is
a static Cloudflare Pages deploy: "publishing" is a deliberate commit + build.
Reviews, testimonials, case results, awards, rankings, statistics, and
attorney honors render **only** from an approved data file, and those files
ship empty.

## Prohibited (never create, under any circumstances)

- Fake reviews, testimonials, ratings, or star counts
- Fake awards, rankings, "best/top-rated firm" claims
- Fake or unverifiable statistics or success rates
- Fake case results, settlements, verdicts, or outcomes
- Any fabricated client outcome or quote

If it cannot be verified, it does not go on the site.

## Approval lifecycle

Every review, case result, testimonial, publication, award, ranking,
statistic, and attorney-profile change moves through:

```
draft -> internal_review -> legal_review -> approved -> published -> archived
```

- **draft** — content authored, not visible anywhere on the site.
- **internal_review** — checked for accuracy and client consent.
- **legal_review** — reviewed by the responsible attorney for attorney-advertising
  compliance (TX Disciplinary Rules 7.01–7.06; OK Rules 7.1–7.5), confidentiality,
  and no-misleading-claim rules.
- **approved** — signed off; still not visible until published.
- **published** — moved into the approved data file with `status:"published"`
  and `approved:true`, committed, and built. Only now does it render.
- **archived** — removed from display, retained for records.

## How it is enforced in code

- `data/reviews.approved.json` and `data/results.approved.json` are the ONLY
  sources the site renders reviews/results from. Both ship with `"items": []`.
- `build/framework_reviews.py` renders an item **only** when
  `status == "published"` AND `approved == true`. Anything else is invisible.
- No `AggregateRating` schema is emitted unless the approved data carries
  verified counts — so the site never advertises a rating it cannot substantiate.
- With empty data, the pages show a neutral empty-state that explicitly says the
  firm does not post fabricated or incentivized content.

## Publishing a verified review (example)

1. Obtain the client's consent to publish their words.
2. Add the item to `data/reviews.approved.json` with `status:"legal_review"`.
3. Responsible attorney reviews for compliance, sets `status:"approved"`.
4. To publish: set `status:"published"`, `approved:true`, commit, deploy.
5. To remove later: set `status:"archived"` and rebuild.

## Required disclaimers (reusable system)

Defined once in `build/partials.py` (`DISCLAIMERS`) and injected consistently:

- **Attorney advertising** — on every page footer + practice pages.
- **No attorney-client relationship** — on every form and consult rail.
- **Past results do not guarantee** — on case-results and every fee callout.
- **No guarantee** — on process descriptions.
- **Informational purposes only** — on guides and practice content.

## Analytics plan (PHASE 13)

`analytics-events.js` fires provider-agnostic events (implement `window.nloTrack`
or use GA4 `gtag` / GTM `dataLayer`):

| Event | Fires on | Key props |
|---|---|---|
| `phone_click` | any `tel:` link | page, practice, cta |
| `text_click` | any `sms:` link | page, practice |
| `consult_cta_click` | `data-cta="consult"` | page, practice |
| `guide_download_click` | `data-cta="download"` | page, practice, guide |
| `lead_form_submit` | `#leadForm` submit | page, practice, source, matter |

Every page carries `<body data-practice="...">` and every lead form a
`data-source`, so conversions attribute to a practice area and a specific page
(including per-city location pages). Recommended dashboard: GA4 (free) or
Cloudflare Web Analytics (no cookies) with conversions defined on
`phone_click`, `consult_cta_click`, and `lead_form_submit`, segmented by
`practice` and landing `page`.

## What is NOT automated

- Merging content to production (human commit + review).
- Any deploy that would surface unreviewed reviews/results (structurally
  impossible — empty data renders nothing).
