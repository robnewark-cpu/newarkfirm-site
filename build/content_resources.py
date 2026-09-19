"""
Lead-magnet resources (PHASE 7).

A resources hub plus gated guide landing pages. Each guide page uses the shared
lead form (posts to the existing Cloudflare Worker via lead.js) tagged as a
guide-download source; on a confirmed submit, lead.js reveals the download link
stored in #formSuccess. No fabricated content; guides are informational and
carry the standard disclaimers.

The actual guide PDFs are produced/approved separately (Draft -> Legal Review
-> Approved -> Published). Until a guide's PDF exists, the success message
promises delivery by email rather than linking a missing file.
"""
from render_practice import PageSpec

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

def guide(slug, title, desc, h1, lede, cluster, cluster_hub, source, matter,
          what_you_get, body_intro, related, knows):
    """A gated guide landing page. The consult rail doubles as the download
    gate: submitting requests the guide (delivered by email once approved)."""
    bullets = "".join(f"              <li>{b}</li>\n" for b in what_you_get)
    body = f"""            <h2>{h1}</h2>
            <p>{body_intro}</p>
            <h3>What the guide covers</h3>
            <ul>
{bullets}            </ul>
{ans("Is this guide legal advice?", "No. This guide is general legal information to help you understand the process and your options. It is not legal advice and does not create an attorney-client relationship. Every situation is different — a free consultation is the way to get advice about your specific facts.")}"""
    spec = PageSpec(
        slug=slug, title=title, description=desc, h1=h1, lede=lede,
        meta_tags=["Free guide", "Instant access", cluster],
        breadcrumb_name=h1, cluster=cluster, cluster_hub=cluster_hub,
        source=source, matter=matter,
        rail_heading="Get the free guide",
        rail_lede="Enter your details and we will send the guide to your email. No cost, no obligation.",
        chat_greeting="Want the free guide? I can help — or point you to a consultation if you have a deadline.",
        knows_about=knows, related=related, body_html=body, faqs=[])
    return spec

RESOURCES_HUB = "/resources.html"
PAGES = []

# ---- Resources hub ----
PAGES.append(PageSpec(
    slug="resources",
    title="Free Legal Guides | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
    description="Free downloadable legal guides from Newark Law Offices — bankruptcy, foreclosure, car-accident, arrest, and removal-defense guides for Texas and Oklahoma.",
    h1="Free legal guides",
    lede="Plain-language guides to help you understand your options before you act. Free to download — general information, not legal advice.",
    meta_tags=["Resources", "Free guides", "Texas & Oklahoma"],
    breadcrumb_name="Resources", cluster="Resources", cluster_hub=RESOURCES_HUB,
    source="resources-hub", matter="General — resource inquiry",
    rail_heading="Not sure which guide?",
    rail_lede="Tell us what you are facing and we will point you to the right guide — or a free consultation.",
    knows_about=["free legal guides", "bankruptcy guide", "accident checklist"],
    related=[("Bankruptcy", "/bankruptcy-lawyer.html"), ("Personal injury", "/personal-injury.html"),
             ("Criminal defense", "/criminal-defense-lawyer.html"), ("Immigration", "/immigration-lawyer.html")],
    body_html="""            <h2>Choose a guide</h2>
            <div class="grid-2">
              <div class="card"><span class="eyebrow">Bankruptcy</span><h3>Bankruptcy Survival Guide</h3><p>Chapter 7 vs. 13, what you keep, and the timeline.</p><a class="link" href="/guide-bankruptcy-survival.html">Get the guide</a></div>
              <div class="card"><span class="eyebrow">Bankruptcy</span><h3>How to Stop Foreclosure</h3><p>The automatic stay, sale-date timing, and keeping your home.</p><a class="link" href="/guide-stop-foreclosure.html">Get the guide</a></div>
              <div class="card"><span class="eyebrow">Personal injury</span><h3>Insurance Claim Guide</h3><p>Coverage, adjusters, and what an offer should include.</p><a class="link" href="/guide-insurance-claim.html">Get the guide</a></div>
              <div class="card"><span class="eyebrow">Personal injury</span><h3>Car Accident Checklist</h3><p>The first 72 hours, evidence, and what not to sign.</p><a class="link" href="/guide-accident-checklist.html">Get the guide</a></div>
              <div class="card"><span class="eyebrow">Criminal defense</span><h3>What To Do After an Arrest</h3><p>Your rights, talking to police, and bond.</p><a class="link" href="/guide-after-arrest.html">Get the guide</a></div>
              <div class="card"><span class="eyebrow">Immigration</span><h3>Removal Defense Guide</h3><p>Immigration court, relief options, and deadlines.</p><a class="link" href="/guide-removal-defense.html">Get the guide</a></div>
              <div class="card"><span class="eyebrow">Immigration</span><h3>Immigration Hearing Preparation</h3><p>Master calendar vs. merits, evidence, and what to expect.</p><a class="link" href="/guide-immigration-hearing.html">Get the guide</a></div>
            </div>
            <p class="disclaimer-inline" style="margin-top:24px;">These guides are general legal information, not legal advice, and do not create an attorney-client relationship. Attorney advertising.</p>"""
))

# ---- Guides ----
PAGES.append(guide(
    "guide-bankruptcy-survival",
    "Free Bankruptcy Survival Guide | Texas & Oklahoma | Newark Law Offices",
    "Free Bankruptcy Survival Guide — Chapter 7 vs. 13, what you keep, and the timeline, for Texas and Oklahoma. Instant access.",
    "The Bankruptcy Survival Guide",
    "A plain-language walkthrough of consumer bankruptcy in Texas and Oklahoma — what it does, what you keep, and what to expect. Free.",
    "Bankruptcy", "/bankruptcy-lawyer.html", "guide-bankruptcy-survival", "Guide — Bankruptcy Survival",
    ["How the automatic stay stops collection immediately",
     "Chapter 7 vs. Chapter 13 — which fits your situation",
     "What Texas and Oklahoma exemptions protect (home, car, retirement)",
     "The step-by-step timeline from filing to discharge",
     "Common myths that keep people from getting help"],
    "Debt does not have to run your life. This guide explains, in plain language, how consumer bankruptcy works in Texas and Oklahoma so you can decide with real information.",
    [("Chapter 7", "/chapter-7-bankruptcy.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
     ("Bankruptcy timeline", "/bankruptcy-timeline.html")],
    ["bankruptcy guide", "Chapter 7", "Chapter 13", "exemptions"]))

PAGES.append(guide(
    "guide-stop-foreclosure",
    "Free Stop Foreclosure Guide | Texas & Oklahoma | Newark Law Offices",
    "Free How to Stop Foreclosure guide — the automatic stay, sale-date timing, and keeping your home in Texas and Oklahoma. Instant access.",
    "How to Stop Foreclosure",
    "If a foreclosure sale is coming, timing is everything. This free guide explains how to stop it and what your options are in Texas and Oklahoma.",
    "Bankruptcy", "/bankruptcy-lawyer.html", "guide-stop-foreclosure", "Guide — Stop Foreclosure",
    ["How the automatic stay stops a scheduled sale",
     "Texas non-judicial vs. Oklahoma judicial foreclosure timelines",
     "How Chapter 13 lets you catch up over time",
     "What to gather before the sale date",
     "What to do if a sale is only days away"],
    "A foreclosure sale is a deadline, not a verdict. This guide shows how the automatic stay works and what steps protect your home.",
    [("Stop foreclosure", "/stop-foreclosure.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
     ("Foreclosure defense (Texas)", "/foreclosure-defense-texas.html")],
    ["stop foreclosure guide", "automatic stay", "Chapter 13"]))

PAGES.append(guide(
    "guide-insurance-claim",
    "Free Insurance Claim Guide | Texas & Oklahoma | Newark Law Offices",
    "Free Insurance Claim Guide — coverage, adjusters, and what a fair offer includes, for Texas and Oklahoma injury claims. Instant access.",
    "The Insurance Claim Guide",
    "Before you talk to an adjuster, know how the claim works. This free guide explains coverage, common tactics, and what a fair offer should include.",
    "Personal Injury", "/personal-injury.html", "guide-insurance-claim", "Guide — Insurance Claim",
    ["Every coverage layer that may apply (liability, PIP/med-pay, UM/UIM)",
     "Why the first offer is rarely the last word",
     "What an offer should account for — future care, lost income, liens",
     "What not to say in a recorded statement",
     "When to get a claim reviewed before signing"],
    "Insurers handle thousands of claims; most people handle one. This guide levels the field so you understand your claim before you settle it.",
    [("Car accidents", "/car-accidents.html"), ("Insurance disputes", "/insurance-disputes.html"),
     ("Personal injury hub", "/personal-injury.html")],
    ["insurance claim guide", "UM UIM", "settlement offer"]))

PAGES.append(guide(
    "guide-accident-checklist",
    "Free Car Accident Checklist | Texas & Oklahoma | Newark Law Offices",
    "Free Car Accident Checklist — the first 72 hours, evidence to gather, and what not to sign, for Texas and Oklahoma. Instant access.",
    "The Car Accident Checklist",
    "What you do in the first 72 hours after a crash can shape the whole claim. This free checklist walks through it step by step.",
    "Personal Injury", "/personal-injury.html", "guide-accident-checklist", "Guide — Accident Checklist",
    ["The first 72 hours: medical care, documentation, and evidence",
     "What to photograph at the scene",
     "How to identify every insurance policy",
     "What not to sign or say to an adjuster",
     "When to seek a claim review"],
    "Keep this checklist handy. The steps right after a crash are the ones people most often wish they had taken.",
    [("Car accidents", "/car-accidents.html"),
     ("After a car crash (practice note)", "/insights/after-a-car-crash-texas-oklahoma.html"),
     ("Personal injury hub", "/personal-injury.html")],
    ["car accident checklist", "first 72 hours", "crash evidence"]))

PAGES.append(guide(
    "guide-after-arrest",
    "Free What To Do After an Arrest Guide | Texas & Oklahoma | Newark Law Offices",
    "Free What To Do After an Arrest guide — your rights, talking to police, and bond, for Texas and Oklahoma. Instant access.",
    "What To Do After an Arrest",
    "The hours after an arrest matter. This free guide explains your rights and the steps that protect them in Texas and Oklahoma.",
    "Criminal Defense", "/criminal-defense-lawyer.html", "guide-after-arrest", "Guide — After Arrest",
    ["Your right to remain silent and to counsel — and how to use them",
     "Why you should not explain your side to police",
     "How bond works and what affects it",
     "What to write down while it is fresh",
     "The early steps that shape a case"],
    "If you or someone you love has been arrested, this guide covers the rights and steps that matter most in the first hours.",
    [("Criminal defense hub", "/criminal-defense-lawyer.html"),
     ("Criminal defense FAQ", "/criminal-defense-faq.html"),
     ("DUI / DWI defense", "/dui-dwi-defense.html")],
    ["what to do after arrest", "right to remain silent", "bond"]))

PAGES.append(guide(
    "guide-removal-defense",
    "Free Removal Defense Guide | Immigration | Newark Law Offices",
    "Free Removal Defense Guide — immigration court, relief options, and deadlines. Instant access.",
    "The Removal Defense Guide",
    "Facing removal is frightening, but there are options. This free guide explains how immigration court works and the relief that may be available.",
    "Immigration", "/immigration-lawyer.html", "guide-removal-defense", "Guide — Removal Defense",
    ["How removal proceedings work (master calendar vs. merits)",
     "Common forms of relief — cancellation, asylum, adjustment, waivers",
     "Why missing a hearing is so dangerous",
     "What to do if a loved one is detained",
     "The deadlines that decide cases"],
    "Removal proceedings move on the court's schedule, not yours. This guide explains the process and the relief that may apply so you can act in time.",
    [("Removal defense", "/removal-defense.html"), ("Bond hearings", "/bond-hearings.html"),
     ("Immigration hub", "/immigration-lawyer.html")],
    ["removal defense guide", "cancellation of removal", "immigration court"]))

PAGES.append(guide(
    "guide-immigration-hearing",
    "Free Immigration Hearing Preparation Guide | Newark Law Offices",
    "Free Immigration Hearing Preparation Guide — master calendar vs. merits, evidence, and what to expect. Instant access.",
    "Immigration Hearing Preparation Guide",
    "Walking into immigration court unprepared is risky. This free guide explains what happens and how to get ready.",
    "Immigration", "/immigration-lawyer.html", "guide-immigration-hearing", "Guide — Immigration Hearing",
    ["The difference between master calendar and merits hearings",
     "What the judge decides at each stage",
     "The evidence and documents that matter",
     "How to prepare testimony",
     "Deadlines you cannot miss"],
    "Preparation is what shapes an immigration case. This guide explains the stages of a hearing and how to walk in ready.",
    [("Immigration court representation", "/immigration-court-representation.html"),
     ("Removal defense", "/removal-defense.html"), ("Immigration hub", "/immigration-lawyer.html")],
    ["immigration hearing preparation", "master calendar hearing", "merits hearing"]))
