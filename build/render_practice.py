"""
Practice-page renderer.

Composes a full, self-contained practice page from a PageSpec using the shared
partials + schema builders. Output markup matches the live site's
.practice-layout pattern (main copy + sticky consult rail) so the existing
styles.css and lead.js work unchanged.
"""
from dataclasses import dataclass, field

import partials as P
import schema as S


@dataclass
class PageSpec:
    slug: str                      # e.g. "chapter-7-bankruptcy"
    title: str                     # <title>
    description: str               # meta description
    h1: str
    lede: str
    meta_tags: list = field(default_factory=list)  # hero pill labels
    body_html: str = ""            # main article HTML (h2/p/ul/ol/answer blocks)
    faqs: list = field(default_factory=list)        # (question, answer) pairs
    breadcrumb_name: str = ""      # short name for breadcrumb trail
    cluster: str = "Bankruptcy"    # cluster label for breadcrumb + rail
    cluster_hub: str = "/bankruptcy-lawyer.html"
    source: str = ""               # lead form data-source
    matter: str = ""               # hidden matter field value
    rail_heading: str = "Free consultation"
    rail_lede: str = None
    chat_greeting: str = None
    related: list = field(default_factory=list)     # (label, href) internal links
    knows_about: list = field(default_factory=list)
    video: dict = None                               # optional {title,url,...}


def render(spec: PageSpec) -> str:
    url = f"{P.SITE}/{spec.slug}.html"

    geo = getattr(spec, "geo", None)
    if geo is not None:
        primary_schema = S.local_business(
            f"{P.FIRM} — {getattr(spec, 'city', spec.breadcrumb_name)}", url,
            getattr(spec, "city", ""), getattr(spec, "region", "TX"),
            spec.description, geo=geo)
    else:
        primary_schema = S.legal_service(
            f"{P.FIRM} — {spec.breadcrumb_name or spec.h1}", url,
            spec.description, knows_about=spec.knows_about or None)

    schema_blocks = [
        primary_schema,
        S.breadcrumbs([
            ("Home", f"{P.SITE}/"),
            (spec.cluster, f"{P.SITE}{spec.cluster_hub}"),
            (spec.breadcrumb_name or spec.h1, url),
        ]),
    ]
    if spec.faqs:
        schema_blocks.append(S.faq_page(spec.faqs))

    video_html, video_schema = P.video_embed(spec.video)
    if video_schema:
        schema_blocks.append(video_schema)

    pills = "".join(f"<span>{m}</span>" for m in spec.meta_tags)

    # FAQ HTML (visible, mirrors the FAQ schema)
    faq_html = ""
    if spec.faqs:
        items = "".join(
            f"              <dt>{q}</dt>\n              <dd>{a}</dd>\n"
            for q, a in spec.faqs)
        faq_html = f"""
            <h2>Frequently asked questions</h2>
            <dl class="faq">
{items}            </dl>"""

    related_html = ""
    if spec.related:
        links = " &middot; ".join(
            f'<a class="link" href="{href}">{label}</a>' for label, href in spec.related)
        related_html = f'\n            <p class="related-links">Related: {links}</p>'

    fee_disc = P.disclaimer_block(
        ["past_results", "no_guarantee", "informational", "attorney_advertising"])

    rail = P.consult_rail(spec.source, spec.matter,
                          heading=spec.rail_heading, lede=spec.rail_lede)

    out = P.head(spec.title, spec.description, url, schema_blocks=schema_blocks,
                 practice=spec.cluster.lower())
    out += "\n" + P.header(active_href=spec.cluster_hub)
    out += f"""
  <main>
    <section class="hero">
      <div class="container">
        <div class="practice-hero-meta">{pills}</div>
        <h1>{spec.h1}</h1>
        <p class="lede">{spec.lede}</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="#consult" data-cta="consult">Request a free consultation</a>
          <a class="btn btn-outline" href="tel:{P.PHONE_TOLL}" data-cta="call">Call {P.PHONE_TOLL_DISPLAY}</a>
        </div>
      </div>
    </section>

    <section class="alt">
      <div class="container">
        <div class="practice-layout">
          <div class="practice-copy">
{spec.body_html}
{video_html}
            <div class="fee-callout">{fee_disc}</div>
{faq_html}{related_html}
          </div>
{rail}
        </div>
      </div>
    </section>
  </main>"""
    out += "\n" + P.footer()
    out += "\n" + P.mobile_call_bar()
    out += "\n" + P.scripts(chat_greeting=spec.chat_greeting)
    return out
