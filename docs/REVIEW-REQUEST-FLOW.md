# Client Review Request Flow

Newark Law Offices — how to ethically request, moderate, and publish client
reviews. Ties into the reviews framework (`data/reviews.approved.json` +
`build/framework_reviews.py`): nothing publishes to the site automatically, and
no review is fabricated or incentivized.

---

## Ethics guardrails (read first)

Texas DRPC 7.01–7.06 and Oklahoma RPC 7.1–7.5 govern lawyer communications and
advertising. Testimonials/reviews are permitted but must not be **false or
misleading**, and must not create **unjustified expectations** about results.

**Rules for this firm:**
- **Never offer anything of value** (discounts, gift cards, fee credits) in
  exchange for a review. That's an incentivized review — prohibited, and against
  Google's policy too.
- **Never write, edit, or fabricate** a review, and never ask someone who isn't a
  real client to post one.
- **Never suppress** negative reviews selectively (don't only ask happy clients
  in a way that gates by rating — "review-gating" violates Google policy). Ask
  broadly; let clients say what they will.
- **Confidentiality:** a client's review may reveal the representation. Only
  request/publish with the client's informed consent, and never respond to a
  review in a way that discloses confidential information (a public reply that
  confirms facts of the matter can breach confidentiality — keep replies generic).
- **No results-based claims** you can't substantiate. If a review names a specific
  outcome ("they got my case dismissed"), that's the client's statement, but
  publishing it prominently as a firm claim can imply an expectation — flag such
  reviews for extra legal review before featuring.
- Reviews rendered on the site carry the attorney-advertising + prior-results
  disclaimers already built into the reviews page.

---

## When to ask

Ask at a natural moment of satisfaction, when the matter (or a milestone) has
concluded well and the client has expressed thanks. Do **not** ask:
- while a matter is ongoing (pressure/coercion risk),
- from a client whose outcome was adverse (don't cherry-pick, but don't pressure),
- via any channel the client hasn't consented to.

---

## The flow

```
1. Identify  → 2. Ask (with consent) → 3. Client posts on Google
                                          │
                                          ▼
4. Optional: client agrees to feature it on the site
                                          │
                                          ▼
5. draft → internal_review → legal_review → approved → published  (framework)
```

### Step 1 — Identify
At matter close, the responsible attorney flags clients who (a) had a positive
experience and (b) would be appropriate to ask (no confidentiality/pressure issue).

### Step 2 — Ask (email/text template)
Neutral, no incentive, no rating-gating. Example:

> **Subject: A quick favor from Newark Law Offices**
>
> Hi [First name],
>
> Thank you for trusting us with your matter. If you have a moment, an honest
> review of your experience helps others find us when they need help. There's no
> obligation, and of course no benefit to you either way — we just appreciate the
> feedback.
>
> You can leave a review here: [Google review link]
>
> If you'd rather share privately, just reply to this email.
>
> Thank you,
> Newark Law Offices · 866-230-7236

Notes:
- Send the **same** ask to all appropriate clients (no gating by expected rating).
- Include the direct Google review link (from your Google Business Profile).
- Never say "leave us a 5-star review" — ask for an **honest** review.

### Step 3 — Client posts on Google
Google is the primary, most valuable place (it feeds the map pack). This is
independent of the website.

### Step 4 — Optional: feature on the website (requires consent)
If the firm wants to feature a Google review on the site, get the client's
consent to reproduce it, then move it through the framework.

### Step 5 — Moderation workflow (framework)
Add the item to `data/reviews.approved.json` and move it through:
- `draft` — captured, not visible.
- `internal_review` — accuracy + consent confirmed.
- `legal_review` — responsible attorney checks for misleading/expectation issues
  and confidentiality.
- `approved` — signed off.
- `published` — set `status:"published"`, `approved:true`, commit, build. Now it
  renders on `/reviews.html`.
- `archived` — remove from display, retain record.

Example approved item (only after the steps above):
```json
{
  "author": "J.M.",
  "rating": 5,
  "text": "They explained my options clearly and kept me informed the whole way.",
  "practice": "Bankruptcy",
  "source": "Google",
  "status": "published",
  "approved": true
}
```

---

## Responding to reviews (all reviews, good or bad)

- Reply publicly in a **generic, professional** tone. Thank the reviewer.
- **Never** confirm someone was a client in a way that reveals the matter, and
  **never** disclose any fact about the representation — even to correct a
  negative review. If a negative review is factually wrong, the safe reply is
  something like: "Thank you for the feedback. We take concerns seriously; please
  contact our office at 866-230-7236 so we can discuss it directly." Then move
  the conversation offline.
- Do not argue, and do not reveal confidential information to defend the firm —
  confidentiality survives a bad review.

---

## What NOT to do (summary)

- ❌ Offer money/discounts/gifts for reviews
- ❌ Write or edit reviews yourself
- ❌ Ask only clients you expect to leave 5 stars (rating-gating)
- ❌ Publish a review on the site without the client's consent
- ❌ Reveal confidential matter details in a public reply
- ❌ Auto-publish anything — every featured review clears legal review first
