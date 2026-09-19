"""
Insights/blog article renderer.

Renders a publish-ready article into /insights/ using the shared partials +
schema. Each article gets Article + BreadcrumbList + (optional) FAQPage schema,
an answer-first intro, internal links to the relevant practice pages, a
consultation CTA, and the standard disclaimers. Content is general legal
information — no fabricated facts, stats, or outcomes. Routed through the
firm's approval workflow before publication.
"""
from dataclasses import dataclass, field
import json

import partials as P
import schema as S


@dataclass
class Article:
    slug: str                    # file name under /insights/
    title: str
    description: str
    h1: str
    dek: str                     # one-line standfirst
    body_html: str               # h2/p/ul + answer blocks
    faqs: list = field(default_factory=list)
    cta_practice: tuple = None   # (label, href) primary related practice
    related: list = field(default_factory=list)
    date: str = "2026-09-19"
    knows_about: list = field(default_factory=list)


def render(a: Article) -> str:
    url = f"{P.SITE}/insights/{a.slug}.html"
    article_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a.h1,
        "description": a.description,
        "datePublished": a.date,
        "dateModified": a.date,
        "author": {"@type": "Organization", "name": P.FIRM, "url": f"{P.SITE}/"},
        "publisher": {"@type": "Organization", "name": P.FIRM,
                      "logo": {"@type": "ImageObject", "url": f"{P.SITE}/rob-headshot.jpg"}},
        "mainEntityOfPage": url,
        "image": f"{P.SITE}/rob-headshot.jpg",
    }, indent=2, ensure_ascii=False)

    schema_blocks = [
        article_schema,
        S.breadcrumbs([("Home", f"{P.SITE}/"), ("Insights", f"{P.SITE}/insights.html"),
                       (a.h1, url)]),
    ]
    if a.faqs:
        schema_blocks.append(S.faq_page(a.faqs))

    faq_html = ""
    if a.faqs:
        items = "".join(
            f"          <dt>{q}</dt>\n          <dd>{ans}</dd>\n" for q, ans in a.faqs)
        faq_html = f"""
        <h2>Frequently asked questions</h2>
        <dl class="faq">
{items}        </dl>"""

    related_html = ""
    if a.related:
        links = " &middot; ".join(f'<a class="link" href="{h}">{l}</a>' for l, h in a.related)
        related_html = f'\n        <p class="related-links">Related: {links}</p>'

    cta_html = ""
    if a.cta_practice:
        label, href = a.cta_practice
        cta_html = (f'\n        <p class="article-cta"><a class="btn btn-gold" '
                    f'href="{href}" data-cta="consult">{label}</a> '
                    f'<a class="btn btn-outline" href="tel:{P.PHONE_TOLL}" '
                    f'data-cta="call">Call {P.PHONE_TOLL_DISPLAY}</a></p>')

    disc = P.disclaimer_block(["informational", "no_relationship", "past_results",
                               "attorney_advertising"])

    out = P.head(a.title, a.description, url, schema_blocks=schema_blocks)
    out += "\n" + P.header(active_href="/insights.html")
    out += f"""
  <main>
    <section class="hero">
      <div class="container">
        <p class="article-meta">Insights &middot; {a.date}</p>
        <h1>{a.h1}</h1>
        <p class="lede">{a.dek}</p>
      </div>
    </section>
    <section class="alt">
      <div class="container">
        <div class="article-body">
{a.body_html}
{cta_html}
        <div class="fee-callout">{disc}</div>
{faq_html}{related_html}
        </div>
      </div>
    </section>
  </main>"""
    out += "\n" + P.footer()
    out += "\n" + P.mobile_call_bar()
    out += "\n" + P.scripts()
    return out
