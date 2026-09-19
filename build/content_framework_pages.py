"""
Reviews, case-results, and attorney-authority pages (PHASES 8, 9, 10).

Reviews and case results render from the approval-gated framework (empty by
default). The attorney authority page expands the existing bio schema with
education, licensure, admissions, and memberships — stated factually. No awards
or rankings are asserted unless verifiable and approved.

These pages are rendered by a dedicated function (not the practice renderer)
because they compose framework output rather than a body/faq spec.
"""
import partials as P
import schema as S
import framework_reviews as FR


def _page(slug, title, description, h1, lede, main_html, *, breadcrumb,
          schema_blocks=None):
    url = f"{P.SITE}/{slug}.html"
    blocks = [S.breadcrumbs([("Home", f"{P.SITE}/"), (breadcrumb, url)])]
    blocks += (schema_blocks or [])
    out = P.head(title, description, url, schema_blocks=blocks)
    out += "\n" + P.header()
    out += f"""
  <main>
    <section class="hero">
      <div class="container">
        <h1>{h1}</h1>
        <p class="lede">{lede}</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="/contact.html#consult" data-cta="consult">Request a free consultation</a>
          <a class="btn btn-outline" href="tel:{P.PHONE_TOLL}" data-cta="call">Call {P.PHONE_TOLL_DISPLAY}</a>
        </div>
      </div>
    </section>
    <section class="alt">
      <div class="container article-body">
{main_html}
      </div>
    </section>
  </main>"""
    out += "\n" + P.footer()
    out += "\n" + P.mobile_call_bar()
    out += "\n" + P.scripts()
    return out


def render_reviews():
    cards, items = FR.reviews_section()
    rating_schema = []
    # Only emit AggregateRating if approved data carries verified counts.
    # (Empty by default -> no rating schema, never fabricated.)
    disc = P.disclaimer_block(["attorney_advertising", "no_relationship"])
    main = f"""        <h2>Client reviews</h2>
{cards}
        <div style="margin-top:24px;">{disc}</div>"""
    return _page(
        "reviews",
        "Client Reviews | Newark Law Offices",
        "Client reviews of Newark Law Offices. The firm does not post fabricated or incentivized reviews; no review is published automatically.",
        "Client reviews",
        "What clients say about working with the firm. Reviews are published only after verification — the firm never posts fabricated or incentivized reviews.",
        main, breadcrumb="Reviews")


def render_results():
    body = FR.results_section()
    disc = P.disclaimer_block(["past_results", "no_guarantee", "attorney_advertising"])
    main = f"""        <h2>Case results</h2>
        <p>Representative matters, published only after review. Results depend entirely on the facts of each case.</p>
{body}
        <div style="margin-top:24px;">{disc}</div>"""
    return _page(
        "case-results",
        "Case Results | Newark Law Offices",
        "Representative case results from Newark Law Offices, published only after administrator and legal review. Prior results do not guarantee a similar outcome.",
        "Case results",
        "Representative outcomes across bankruptcy, injury, criminal, and immigration matters — published only after review, and never a promise of a similar result.",
        main, breadcrumb="Case Results")


def render_attorney_authority():
    # Expanded Attorney schema for the responsible attorney, stated factually.
    attorney_schema = S._dump({
        "@context": "https://schema.org",
        "@type": "Attorney",
        "@id": f"{P.SITE}/attorney-robert-newark.html#robert-newark",
        "name": "Robert C. Newark, III",
        "jobTitle": "Responsible Attorney",
        "url": f"{P.SITE}/attorney-robert-newark.html",
        "image": f"{P.SITE}/rob-headshot.jpg",
        "worksFor": {"@type": "LegalService", "name": P.FIRM, "url": f"{P.SITE}/"},
        "knowsAbout": ["Consumer bankruptcy", "Chapter 7", "Chapter 13",
                       "Personal injury", "Criminal defense", "Immigration",
                       "Foreclosure defense"],
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "Bar admission",
             "recognizedBy": {"@type": "Organization", "name": "State Bar of Texas"}},
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "Bar admission",
             "recognizedBy": {"@type": "Organization", "name": "Oklahoma Bar Association"}},
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "Federal court admission",
             "recognizedBy": {"@type": "Organization",
                              "name": "U.S. District Courts (Texas, Oklahoma, Colorado, New Mexico, Arkansas)"}},
        ],
        "sameAs": ["https://www.linkedin.com/in/robert-newark-52575614"],
    })
    main = """        <h2>Robert C. Newark, III</h2>
        <p><strong>Responsible attorney</strong> &middot; Dallas, Texas</p>
        <p>Robert C. Newark, III directs the firm's bankruptcy, injury, criminal defense, and immigration matters, representing clients across Texas and Oklahoma.</p>

        <h3>Licensure</h3>
        <ul>
          <li>State Bar of Texas</li>
          <li>Oklahoma Bar Association</li>
        </ul>

        <h3>Court admissions</h3>
        <ul>
          <li>Texas and Oklahoma state courts</li>
          <li>U.S. District Courts in Texas, Oklahoma, Colorado, New Mexico, and Arkansas (federal admissions; not state-bar licensure in CO, NM, or AR)</li>
          <li>U.S. Bankruptcy Courts in the districts where the firm files consumer cases</li>
        </ul>

        <h3>Practice focus</h3>
        <ul>
          <li>Consumer bankruptcy (Chapter 7 and Chapter 13)</li>
          <li>Personal injury</li>
          <li>Criminal defense</li>
          <li>Immigration and removal defense</li>
          <li>Foreclosure defense and creditor/debtor matters</li>
        </ul>

        <div class="authority-placeholder disclaimer-inline">
          <p><strong>Publications, presentations, media mentions, and professional memberships</strong> are listed here only when verified. This section is maintained through the firm's content-approval workflow; unverified honors, awards, and rankings are not posted.</p>
        </div>

        <p style="margin-top:20px;"><a class="link" href="/people.html">See all attorneys and staff</a> &middot; <a class="link" href="mailto:robert@newarkfirm.com">robert@newarkfirm.com</a></p>"""
    return _page(
        "attorney-robert-newark",
        "Robert C. Newark, III | Attorney | Newark Law Offices",
        "Robert C. Newark, III — responsible attorney at Newark Law Offices. Licensure, court admissions, and practice focus across Texas and Oklahoma.",
        "Robert C. Newark, III — attorney profile",
        "Responsible attorney for the firm's bankruptcy, injury, criminal defense, and immigration practices across Texas and Oklahoma.",
        main, breadcrumb="Attorney: Robert C. Newark, III",
        schema_blocks=[attorney_schema])


def all_pages():
    """Returns list of (slug, html) — rendered directly, not via PageSpec."""
    return [
        ("reviews", render_reviews()),
        ("case-results", render_results()),
        ("attorney-robert-newark", render_attorney_authority()),
    ]
