"""
Newark Law Offices — shared HTML partials.

Single source of truth for header, footer, mobile conversion bar, JSON-LD
schema blocks, disclaimers, and the lead-capture rail. Every generated page
composes these so markup, compliance language, and the existing Cloudflare
lead pipeline (lead.js -> Worker) stay identical across the site.

Nothing here fabricates reviews, ratings, awards, or case results. Rating and
result blocks are intentionally NOT emitted until a human-approved data file
supplies verified content (see PHASE 9/10 approval workflow).
"""

SITE = "https://newarkfirm.com"
FIRM = "Newark Law Offices"
LEGAL_NAME = "A Newark Firm, LLC"
PHONE_TOLL = "+18662307236"
PHONE_TOLL_DISPLAY = "(866) 230-7236"
PHONE_DALLAS = "+19723325733"
PHONE_EDMOND = "+14057270269"

# ---- Navigation (practice-first IA; replaces corporate "Experience/Branch" nav) ----
NAV_ITEMS = [
    ("Home", "/index.html"),
    ("Bankruptcy", "/bankruptcy-lawyer.html"),
    ("Personal Injury", "/personal-injury.html"),
    ("Criminal Defense", "/criminal-defense-lawyer.html"),
    ("Immigration", "/immigration-lawyer.html"),
    ("Locations", "/locations.html"),
    ("About", "/about.html"),
    ("Insights", "/insights.html"),
    ("Contact", "/contact.html"),
]


def head(title, description, canonical, *, schema_blocks=None, og_image=None,
         practice=""):
    schema_html = ""
    for block in (schema_blocks or []):
        schema_html += (
            '\n  <script type="application/ld+json">\n'
            + block.strip()
            + "\n  </script>"
        )
    og_image = og_image or f"{SITE}/rob-headshot.jpg"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/styles.css">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="{og_image}">
  <meta property="og:site_name" content="{FIRM}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image}">
  <link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="LLM summary">{schema_html}
</head>
<body{(' data-practice="' + practice + '"') if practice else ''}>"""


def header(active_href=""):
    lis = ""
    for label, href in NAV_ITEMS:
        current = ' aria-current="page"' if href == active_href else ""
        lis += f'        <li><a href="{href}"{current}>{label}</a></li>\n'
    return f"""  <header class="site-header">
    <div class="container">
      <a class="brand" href="/index.html">{FIRM}
        <small>Texas &amp; Oklahoma</small>
      </a>
      <nav class="main-nav" aria-label="Primary">
        <ul>
{lis}        </ul>
      </nav>
      <a class="cta-pill" href="/contact.html#consult">Free Consultation &rarr;</a>
    </div>
  </header>"""


def mobile_call_bar():
    """Site-wide sticky mobile conversion bar: Call / Free Consultation / Text.

    Hidden on desktop via CSS (.mobile-call-bar { display:none } at >=760px).
    """
    return f"""  <div class="mobile-call-bar" role="navigation" aria-label="Contact actions">
    <a href="tel:{PHONE_TOLL}" data-cta="call" class="mcb-call">
      <span class="mcb-ico" aria-hidden="true">&#9742;</span>Call
    </a>
    <a href="/contact.html#consult" data-cta="consult" class="mcb-consult">
      <span class="mcb-ico" aria-hidden="true">&#9993;</span>Free Consultation
    </a>
    <a href="sms:{PHONE_TOLL}" data-cta="text" class="mcb-text">
      <span class="mcb-ico" aria-hidden="true">&#128172;</span>Text
    </a>
  </div>"""


def footer():
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="foot-grid">
        <div>
          <h4>{FIRM}</h4>
          <p>{LEGAL_NAME}<br>Responsible attorney: Robert C. Newark, III</p>
          <p>Attorney advertising. Prior results do not guarantee a similar outcome.</p>
        </div>
        <div>
          <h4>Texas Office</h4>
          <p>1341 W. Mockingbird Ln, Ste 600W<br>Dallas, TX 75247<br>972-332-5733</p>
        </div>
        <div>
          <h4>Oklahoma Office</h4>
          <p>1019 Waterwood Pkwy, Ste C<br>Edmond, OK 73034<br>405-727-0269</p>
          <p>Toll free: 866-230-7236</p>
        </div>
      </div>
      <div class="legal">
        <p>&copy; 2026 {FIRM}. All Rights Reserved. | <a href="/disclaimer.html">Disclaimer</a></p>
        <p>See <a href="/people.html">Our People</a> for each attorney&rsquo;s licenses.
        <a href="/local-counsel.html">Local counsel</a> is available case-by-case.
        Alaska, Wisconsin, and South Dakota matters are accepted on a referral basis.</p>
      </div>
    </div>
  </footer>"""


def scripts(chat_greeting=None):
    greeting = chat_greeting or (
        "Hi — I can help point you to the right person here. What brings you by today?"
    )
    return f"""  <script src="/lead.js"></script>
  <script src="/analytics-events.js" defer></script>
  <script
  src="https://site-chatbot-assets.pages.dev/widget.js"
  data-worker-url="https://site-chatbots.robert-bb6.workers.dev"
  data-site="newarkfirm"
  data-name="{FIRM}"
  data-accent="#14213D"
  data-greeting="{greeting}"
  async
  defer></script>
</body>
</html>"""


# ---- Reusable disclaimer system (PHASE: required disclaimers) ----
DISCLAIMERS = {
    "attorney_advertising": "Attorney advertising. This material is for general information and may be considered advertising under the rules of the State Bar of Texas and the Oklahoma Bar Association.",
    "no_relationship": "Contacting the firm, submitting a form, or using the chat does not create an attorney-client relationship. A relationship is formed only through a signed written engagement agreement.",
    "past_results": "Prior results do not guarantee a similar outcome. Every matter is different and depends on its own facts.",
    "no_guarantee": "No outcome is promised or guaranteed. Descriptions of process are general and are not a prediction about any specific matter.",
    "informational": "The information on this page is provided for general informational purposes only and does not constitute legal advice.",
}


def disclaimer_block(keys):
    parts = "".join(f"<p>{DISCLAIMERS[k]}</p>" for k in keys)
    return f'<div class="disclaimer-inline">{parts}</div>'


# ---- Consultation rail (right column of practice pages) ----
def consult_rail(source, matter, *, heading="Free consultation", lede=None,
                 fields_extra=""):
    lede = lede or "Tell us what happened and what deadline you are facing. We will follow up promptly."
    return f"""      <aside class="practice-rail" id="consult">
        <h2>{heading}</h2>
        <p class="rail-lede">{lede}</p>
        <p class="phone-line"><a href="tel:{PHONE_TOLL}" data-cta="call">{PHONE_TOLL_DISPLAY}</a></p>
        <form class="stack" id="leadForm" data-source="{source}">
          <input type="hidden" name="matter" value="{matter}">
          <div><label for="name">Full name</label><input type="text" id="name" name="name" required></div>
          <div><label for="phone">Phone</label><input type="tel" id="phone" name="phone" required></div>
          <div><label for="email">Email</label><input type="email" id="email" name="email" required></div>
{fields_extra}          <div><label for="details">What is going on?</label><textarea id="details" name="details" required placeholder="A short description and any deadline (court date, sale date, filing date)."></textarea></div>
          <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
          <button class="btn btn-gold" type="submit">Request my free consultation</button>
          <p class="form-note">Submitting this form does not create an attorney-client relationship.</p>
        </form>
        <div id="formSuccess" class="success-msg">Thank you &mdash; your consultation request has been sent. Our team will follow up shortly.</div>
      </aside>"""


# ---- AI answer block (PHASE 11: AI-citable definition/answer components) ----
def answer_block(question, answer_html):
    """A plain-language, self-contained answer designed for AI extraction."""
    return f"""        <div class="answer-block">
          <h3 class="answer-q">{question}</h3>
          <div class="answer-a">{answer_html}</div>
        </div>"""


def definition_block(term, definition_html):
    return f"""        <div class="definition-block">
          <span class="def-term">{term}</span>
          <div class="def-body">{definition_html}</div>
        </div>"""
