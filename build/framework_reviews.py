"""
Reviews & case-results framework (PHASE 9, 10, 13).

DESIGN: content-gated-by-approval. Reviews and case results render ONLY from
approved data files (data/reviews.approved.json, data/results.approved.json).
Both ship EMPTY. Nothing publishes automatically; an item appears on the site
only after a human moves it to the approved file (Draft -> Internal Review ->
Legal Review -> Approved -> Published), which is a deliberate commit + build.

PROHIBITED: fabricated reviews, testimonials, awards, rankings, statistics,
case results, success rates, settlements. This module NEVER invents entries —
it only renders what an approved file contains, and refuses to emit a rating
summary unless the approved data carries verified counts.
"""
import json
import os

import partials as P
import schema as S

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")


def _load(name):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        try:
            doc = json.load(f)
        except json.JSONDecodeError:
            return []
    # Only items explicitly marked approved+published are ever rendered.
    return [x for x in doc.get("items", [])
            if x.get("status") == "published" and x.get("approved") is True]


def reviews_section():
    items = _load("reviews.approved.json")
    if not items:
        return ("""            <div class="empty-state">
              <p>Verified client reviews will appear here as they are approved for publication. The firm does not post fabricated or incentivized reviews, and no review is published automatically.</p>
              <p>You can read the firm's reviews on its Google Business Profile. To leave one, ask the office for the link.</p>
            </div>""", None)
    cards = ""
    for it in items:
        stars = "&#9733;" * int(it.get("rating", 0))
        cards += (f'            <blockquote class="review-card">\n'
                  f'              <div class="review-stars" aria-label="{it.get("rating","")} out of 5">{stars}</div>\n'
                  f'              <p>{it["text"]}</p>\n'
                  f'              <cite>&mdash; {it.get("author","Verified client")}'
                  f'{(", " + it["practice"]) if it.get("practice") else ""}</cite>\n'
                  f'            </blockquote>\n')
    return (cards, items)


def results_section():
    items = _load("results.approved.json")
    if not items:
        return """            <div class="empty-state">
              <p>Representative case results will appear here as they are reviewed and approved for publication. Each result requires administrator and legal review before it is posted, and every result is published with the disclaimer that prior results do not guarantee a similar outcome.</p>
            </div>"""
    rows = ""
    for it in items:
        rows += (f'            <div class="result-card">\n'
                 f'              <span class="result-practice">{it.get("practice","")}</span>\n'
                 f'              <h3>{it.get("headline","")}</h3>\n'
                 f'              <p>{it.get("summary","")}</p>\n'
                 f'              <p class="result-disc">{P.DISCLAIMERS["past_results"]}</p>\n'
                 f'            </div>\n')
    return rows
