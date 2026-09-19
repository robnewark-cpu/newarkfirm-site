#!/usr/bin/env python3
"""
Newark Law Offices — static page generator.

Generates practice-cluster pages from content modules and (re)writes
sitemap.xml from the union of generated pages + existing hand-authored pages.
Run from the build/ directory:  python3 build.py

Design constraints honored:
- Output is plain static HTML into the repo root (Cloudflare Pages serves it).
- Reuses the existing styles.css, lead.js, and chat widget unchanged.
- Never fabricates reviews, ratings, awards, or results.
"""
import os
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import render_practice  # noqa: E402
import content_bankruptcy  # noqa: E402
import content_hubs  # noqa: E402
import content_pi  # noqa: E402
import content_locations  # noqa: E402
import content_criminal  # noqa: E402
import content_immigration  # noqa: E402
import content_cities  # noqa: E402
import content_counties  # noqa: E402
import content_resources  # noqa: E402
import content_business_crimigration  # noqa: E402
import content_framework_pages  # noqa: E402
import render_article  # noqa: E402
import content_insights_1  # noqa: E402
import content_insights_2  # noqa: E402

TODAY = datetime.date.today().isoformat()

ARTICLES = content_insights_1.ARTICLES + content_insights_2.ARTICLES

# Cluster modules -> list of PageSpec
CLUSTERS = {
    "bankruptcy": content_bankruptcy.PAGES,
    "hubs": content_hubs.PAGES,
    "pi": content_pi.PAGES,
    "locations": content_locations.PAGES,
    "criminal": content_criminal.PAGES,
    "immigration": content_immigration.PAGES,
    "cities": content_cities.PAGES,
    "counties": content_counties.PAGES,
    "resources": content_resources.PAGES,
    "business_crimigration": content_business_crimigration.PAGES,
}

# Existing hand-authored pages that stay in the sitemap.
EXISTING_PAGES = [
    "index.html", "about.html", "experience.html", "people.html",
    "insights.html", "personal-injury.html", "local-counsel.html",
    "texas.html", "oklahoma.html", "contact.html", "case-eligibility.html",
    "disclaimer.html",
    "foreclosure-defense-texas.html", "foreclosure-defense-oklahoma.html",
    "ch11-creditor-texas.html", "ch11-debtor-texas.html",
    "ch11-debtor-oklahoma.html", "ch11-creditor-oklahoma.html",
    "ch11-creditor-arkansas.html", "ch11-creditor-colorado.html",
    "ch11-creditor-new-mexico.html",
    "ch11-debtor-arkansas.html", "ch11-debtor-colorado.html",
    "ch11-debtor-new-mexico.html",
    "wind-hail-damage-claim-texas.html", "wind-hail-damage-claim-oklahoma.html",
    "insights/local-counsel-licensed-courts.html",
    "insights/after-a-car-crash-texas-oklahoma.html",
    "insights/foreclosure-timelines-texas-oklahoma.html",
    "insights/chapter-11-small-business.html",
    "insights/chapter-11-creditor-strategy.html",
    "insights/wind-hail-claim-denials.html",
    "insights/texas-oklahoma-corporate-transactions.html",
    "insights/texas-oklahoma-jurisdictional-briefing.html",
    "funnels/corporate-litigation-defense.html",
    "funnels/financial-institution-advisory.html",
    "funnels/complex-civil-litigation-dispute-resolution.html",
    "funnels/texas-oklahoma-cross-border-corporate-transactions.html",
    "funnels/car-accident-injury-texas.html",
    "funnels/car-accident-injury-oklahoma.html",
]


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text if text.endswith("\n") else text + "\n")
    return path


def build_pages():
    generated = []
    for cluster, pages in CLUSTERS.items():
        for spec in pages:
            html = render_practice.render(spec)
            generated.append(write(f"{spec.slug}.html", html))
    # Framework pages (reviews, case-results, attorney authority) render
    # directly rather than via a PageSpec.
    for slug, html in content_framework_pages.all_pages():
        generated.append(write(f"{slug}.html", html))
    # Insights/blog articles render into /insights/.
    for art in ARTICLES:
        generated.append(write(f"insights/{art.slug}.html", render_article.render(art)))
    return generated


def build_sitemap(generated):
    urls = []
    seen = set()
    for p in generated + EXISTING_PAGES:
        if p in seen:
            continue
        seen.add(p)
        loc = "https://newarkfirm.com/" + ("" if p == "index.html" else p)
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>")
    body = "\n".join(urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    return write("sitemap.xml", xml)


def main():
    generated = build_pages()
    build_sitemap(generated)
    print(f"Generated {len(generated)} pages:")
    for p in generated:
        print(f"  {p}")
    print("Rebuilt sitemap.xml "
          f"({len(set(generated + EXISTING_PAGES))} URLs)")


if __name__ == "__main__":
    main()
