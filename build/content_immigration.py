"""
Immigration & removal-defense spoke cluster (PHASE 4).

Links back to /immigration-lawyer.html. Immigration courts are federal and
nationwide; representation is not limited by state bar licensure. Content is
process-only, urges early action on hard deadlines, and contains no fabricated
outcomes or statistics.
"""
from render_practice import PageSpec

HUB = "/immigration-lawyer.html"

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

def im(slug, title, desc, h1, lede, tags, bc, body, faqs, source, matter, related, knows,
       urgent=False):
    return PageSpec(
        slug=slug, title=title, description=desc, h1=h1, lede=lede, meta_tags=tags,
        breadcrumb_name=bc, cluster="Immigration", cluster_hub=HUB,
        source=source, matter=matter,
        rail_heading="Facing removal? Act now" if urgent else "Free immigration consultation",
        rail_lede=("If there is a court date, a detainer, or an ICE hold, tell us the date immediately — immigration deadlines are strict."
                   if urgent else "Tell us your situation, status, and any date or notice you have received."),
        chat_greeting="Facing removal, detention, or an immigration deadline? Tell me your situation and any court date and I can point you to help.",
        knows_about=knows, related=related, body_html=body, faqs=faqs)

PAGES = []

PAGES.append(im(
    "removal-defense",
    "Removal Defense Lawyer | Immigration Court | Newark Law Offices",
    "Removal defense in immigration court — relief options, hearings, and deadlines. Facing removal? Call 866-230-7236 now. Free consultation.",
    "Removal defense in immigration court",
    "If you are in removal proceedings, the court date controls everything — missing it usually means an automatic removal order. We identify defenses and relief and appear before the immigration court. Free, confidential consultation.",
    ["Removal defense", "Immigration court", "Strict deadlines"], "Removal Defense",
    f"""            <h2>The court date controls everything</h2>
{ans("What is removal defense?", "Removal defense is representation in immigration court when the government seeks to deport (remove) someone. The government must prove removability; the person can contest it and apply for relief such as cancellation of removal, asylum, adjustment of status, or waivers. Proceedings run through master calendar hearings (scheduling and pleadings) to an individual merits hearing. Missing a hearing usually results in an in-absentia removal order, so appearing and being prepared is critical.")}
            <h2>Relief we evaluate</h2>
            <ul>
              <li>Cancellation of removal (for certain residents and non-residents)</li>
              <li>Asylum, withholding, and protection under the Convention Against Torture</li>
              <li><a class="link" href="/adjustment-of-status.html">Adjustment of status</a> where eligible</li>
              <li><a class="link" href="/waivers.html">Waivers</a> of specific grounds of removability</li>
              <li><a class="link" href="/bond-hearings.html">Bond</a> if detained; <a class="link" href="/motions-to-reopen.html">motions to reopen</a> for prior orders</li>
            </ul>""",
    [("What happens if I miss my immigration court hearing?",
      "Missing a hearing usually results in an in-absentia order of removal. A motion to reopen may be possible on limited grounds and short deadlines — call immediately if this has happened."),
     ("Can I fight deportation?",
      "Often yes. Depending on your history and status, relief such as cancellation, asylum, adjustment, or waivers may be available. A consultation evaluates what applies.")],
    "im-removal", "Immigration — removal defense",
    [("Deportation defense", "/deportation-defense.html"),
     ("Immigration court representation", "/immigration-court-representation.html"),
     ("Bond hearings", "/bond-hearings.html")],
    ["removal defense", "cancellation of removal", "immigration court", "in absentia order"],
    urgent=True))

PAGES.append(im(
    "deportation-defense",
    "Deportation Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Deportation defense — stopping removal, relief options, and detained cases. Facing deportation? Call 866-230-7236 now. Free consultation.",
    "Deportation defense",
    "Deportation and removal are the same court process under different names. Whether you or a loved one is detained or facing a hearing, we move quickly to identify relief and protect your rights. Free, confidential consultation.",
    ["Deportation defense", "Detained cases", "Act fast"], "Deportation Defense",
    f"""            <h2>Deportation is the removal process</h2>
{ans("What is the difference between deportation and removal?", "They are the same thing. 'Removal' is the current legal term for what most people call deportation — the process in immigration court by which the government seeks to make someone leave the country. Defenses and relief (cancellation, asylum, adjustment, waivers) are pursued in that proceeding. If the person is detained, a bond hearing can seek release while the case proceeds.")}
            <h2>What we do first</h2>
            <ul>
              <li>Locate a detained family member and check for a bond</li>
              <li>Identify the charging document and hearing date</li>
              <li>Evaluate every available form of relief</li>
              <li>Advise against signing anything agreeing to removal before a consultation</li>
            </ul>""",
    [("My family member was detained by ICE — what do I do?",
      "Act immediately: find where they are held and whether there is a bond. A bond hearing can seek release. Do not let them sign an agreement to removal without talking to a lawyer."),
     ("Is deportation the same as removal?",
      "Yes. 'Removal' is the legal term; 'deportation' is the common one. Both refer to the immigration-court process to make someone leave the country.")],
    "im-deportation", "Immigration — deportation defense",
    [("Removal defense", "/removal-defense.html"), ("Bond hearings", "/bond-hearings.html"),
     ("ICE detainers", "/ice-detainers.html")],
    ["deportation defense", "removal", "ICE detention", "bond"],
    urgent=True))

PAGES.append(im(
    "immigration-court-representation",
    "Immigration Court Representation | Newark Law Offices",
    "Representation in immigration court — master calendar and merits hearings, evidence, and relief applications. Call 866-230-7236. Free consultation.",
    "Immigration court representation",
    "Immigration court is unfamiliar and unforgiving. We appear at master calendar and merits hearings, prepare the record, and present the applications for relief that fit your case. Free consultation.",
    ["Immigration court", "Hearings", "Federal court"], "Immigration Court Representation",
    f"""            <h2>How immigration court works</h2>
{ans("What happens at an immigration court hearing?", "Immigration court proceedings have two main stages: master calendar hearings, where scheduling and pleadings happen and the judge sets deadlines, and an individual merits hearing, where evidence and testimony are presented and the judge decides. Because immigration courts are federal, representation is not limited by state bar licensure. Preparing applications, evidence, and witnesses to the court's deadlines is what shapes the outcome.")}
            <h2>What representation includes</h2>
            <ul>
              <li>Appearing at master calendar and merits hearings</li>
              <li>Filing applications for relief and supporting evidence</li>
              <li>Preparing testimony and witnesses</li>
              <li>Meeting the court's filing deadlines</li>
            </ul>""",
    [("Do I need a lawyer for immigration court?",
      "There is no government-appointed lawyer in immigration court, so representation is up to you — and the process, deadlines, and evidence rules are complex. Representation is strongly advisable."),
     ("Can you represent me if you are not licensed in my state?",
      "Immigration courts are federal, so representation there is not limited by state bar licensure. We coordinate with the court handling your matter.")],
    "im-court", "Immigration — court representation",
    [("Removal defense", "/removal-defense.html"), ("Motions to reopen", "/motions-to-reopen.html"),
     ("Bond hearings", "/bond-hearings.html")],
    ["immigration court", "master calendar hearing", "merits hearing"]))

PAGES.append(im(
    "adjustment-of-status",
    "Adjustment of Status Lawyer | Green Card | Newark Law Offices",
    "Adjustment of status to a green card — eligibility, process, and common obstacles. Call 866-230-7236. Free consultation.",
    "Adjustment of status (green card)",
    "Adjustment of status lets eligible people become lawful permanent residents without leaving the U.S. We assess eligibility, prepare the application, and handle interviews and obstacles. Free consultation.",
    ["Adjustment of status", "Green card", "Stay in the U.S."], "Adjustment of Status",
    f"""            <h2>Becoming a permanent resident from inside the U.S.</h2>
{ans("What is adjustment of status?", "Adjustment of status is the process by which an eligible person already in the United States applies to become a lawful permanent resident (green card holder) without returning to their home country for consular processing. Eligibility usually requires an approved or concurrent immigrant petition (often family- or employment-based), a lawful basis, and admissibility — with waivers available for some grounds. It is filed with USCIS and typically includes an interview.")}
            <h2>What we handle</h2>
            <ul>
              <li>Eligibility analysis and the right filing basis</li>
              <li><a class="link" href="/family-immigration.html">Family-based</a> and other petitions</li>
              <li>Admissibility issues and <a class="link" href="/waivers.html">waivers</a></li>
              <li>Interview preparation</li>
            </ul>""",
    [("Can I get a green card without leaving the U.S.?",
      "Often yes, through adjustment of status, if you are eligible and have a lawful basis. The alternative is consular processing abroad — see that page."),
     ("What can make adjustment harder?",
      "Certain immigration or criminal history, unlawful presence, or entry issues can create obstacles, some of which have waivers. A consultation evaluates your specific situation.")],
    "im-adjustment", "Immigration — adjustment of status",
    [("Family immigration", "/family-immigration.html"), ("Consular processing", "/consular-processing.html"),
     ("Waivers", "/waivers.html")],
    ["adjustment of status", "green card", "lawful permanent resident", "USCIS"]))

PAGES.append(im(
    "family-immigration",
    "Family Immigration Lawyer | Petitions & Visas | Newark Law Offices",
    "Family immigration — petitions for spouses, children, parents, and relatives, and the path to a green card. Call 866-230-7236. Free consultation.",
    "Family immigration",
    "Family is the most common path to lawful status. We handle petitions for spouses, children, parents, and other relatives, and map the route from petition to green card. Free consultation.",
    ["Family immigration", "Petitions", "Keep family together"], "Family Immigration",
    f"""            <h2>Bringing family through the system</h2>
{ans("How does family-based immigration work?", "A U.S. citizen or lawful permanent resident files a petition (Form I-130) to establish a qualifying family relationship — spouse, child, parent, or sibling depending on the sponsor's status. Immediate relatives of citizens (spouses, unmarried minor children, parents) generally have visas available without waiting for a quota; other categories wait for a visa to become current. The relative then either adjusts status in the U.S. or completes consular processing abroad.")}
            <h2>Who can be petitioned</h2>
            <ul>
              <li>Spouses and fianc&eacute;(e)s</li>
              <li>Children (rules differ by age and marital status)</li>
              <li>Parents of adult U.S. citizens</li>
              <li>Siblings of U.S. citizens (longer waits)</li>
            </ul>""",
    [("How long does family immigration take?",
      "Immediate relatives of U.S. citizens often move fastest; other categories wait for a visa number to become current, which varies by category and country. A consultation gives a realistic timeline."),
     ("Can I petition for my spouse who is already in the U.S.?",
      "Often yes, through a petition combined with adjustment of status, if eligible. Entry history and status affect the path — see the adjustment page.")],
    "im-family", "Immigration — family immigration",
    [("Adjustment of status", "/adjustment-of-status.html"), ("Consular processing", "/consular-processing.html"),
     ("Waivers", "/waivers.html")],
    ["family immigration", "I-130 petition", "immediate relative", "family visa"]))

PAGES.append(im(
    "consular-processing",
    "Consular Processing Lawyer | Immigrant Visas | Newark Law Offices",
    "Consular processing — obtaining an immigrant visa at a U.S. consulate abroad, interviews, and waivers. Call 866-230-7236. Free consultation.",
    "Consular processing",
    "When adjustment of status is not available, consular processing obtains an immigrant visa through a U.S. consulate abroad. We prepare the case, the interview, and any needed waivers. Free consultation.",
    ["Consular processing", "Immigrant visa", "Abroad"], "Consular Processing",
    f"""            <h2>Getting the visa abroad</h2>
{ans("What is consular processing?", "Consular processing is the path to a green card for someone outside the United States (or ineligible to adjust status inside it): after an approved immigrant petition and a current visa, the applicant completes the National Visa Center stage and attends an immigrant-visa interview at a U.S. consulate abroad. Grounds of inadmissibility — such as prior unlawful presence — may require a waiver, sometimes a provisional waiver filed before departure to reduce time apart from family.")}
            <h2>What we manage</h2>
            <ul>
              <li>The National Visa Center document stage</li>
              <li>Interview preparation</li>
              <li>Inadmissibility issues and <a class="link" href="/waivers.html">waivers</a> (including provisional waivers)</li>
            </ul>""",
    [("When is consular processing required instead of adjustment?",
      "Generally when the person is outside the U.S. or is not eligible to adjust status inside it. Which path applies depends on entry history and status."),
     ("What is a provisional waiver?",
      "For certain unlawful-presence grounds, a provisional waiver can be approved before the person leaves for their consular interview, reducing the time separated from family. Eligibility is fact-specific.")],
    "im-consular", "Immigration — consular processing",
    [("Adjustment of status", "/adjustment-of-status.html"), ("Waivers", "/waivers.html"),
     ("Family immigration", "/family-immigration.html")],
    ["consular processing", "immigrant visa", "provisional waiver", "National Visa Center"]))

PAGES.append(im(
    "bond-hearings",
    "Immigration Bond Hearing Lawyer | Release from Detention | Newark Law Offices",
    "Immigration bond hearings — seeking release from ICE detention, eligibility, and factors. Detained? Call 866-230-7236 now. Free consultation.",
    "Immigration bond hearings",
    "If a loved one is in ICE detention, a bond hearing can seek their release while their case proceeds. Eligibility and timing matter. We move quickly. Free, confidential consultation.",
    ["Bond hearings", "Release from detention", "Act now"], "Bond Hearings",
    f"""            <h2>Seeking release from detention</h2>
{ans("How does an immigration bond hearing work?", "For many detained people who are not subject to mandatory detention, an immigration judge can set a bond at a hearing. The judge weighs whether the person is a flight risk and whether they are a danger to the community, considering family ties, employment, length of residence, and immigration and criminal history. If bond is granted and paid, the person is released while their removal case continues. Some cases involve mandatory detention where no bond is available, which is why an early eligibility check matters.")}
            <h2>What we prepare</h2>
            <ul>
              <li>Whether the person is bond-eligible or subject to mandatory detention</li>
              <li>Evidence of ties, stability, and non-dangerousness</li>
              <li>Sponsor and address documentation</li>
            </ul>""",
    [("Can my detained relative be released on bond?",
      "Possibly, if they are bond-eligible (not subject to mandatory detention). A judge weighs flight risk and danger. Gathering evidence of family ties and stability helps."),
     ("How fast can a bond hearing happen?",
      "It varies by court and detention facility, but these cases move quickly and preparation matters. Contact the firm as soon as someone is detained.")],
    "im-bond", "Immigration — bond hearing",
    [("Deportation defense", "/deportation-defense.html"), ("ICE detainers", "/ice-detainers.html"),
     ("Removal defense", "/removal-defense.html")],
    ["immigration bond hearing", "ICE detention release", "mandatory detention"],
    urgent=True))

PAGES.append(im(
    "motions-to-reopen",
    "Motion to Reopen Lawyer | Immigration | Newark Law Offices",
    "Motions to reopen an immigration case — reversing an in-absentia removal order, new evidence, and strict deadlines. Call 866-230-7236. Free consultation.",
    "Motions to reopen an immigration case",
    "A prior removal order is not always the end. A motion to reopen can, on limited grounds and short deadlines, reopen a case — including one decided in your absence. Timing is everything. Free consultation.",
    ["Motions to reopen", "Prior orders", "Strict deadlines"], "Motions to Reopen",
    f"""            <h2>Reopening a closed case</h2>
{ans("Can an immigration case be reopened after a removal order?", "Sometimes. A motion to reopen asks the immigration court or Board of Immigration Appeals to reopen a case based on new facts or evidence, changed circumstances, or lack of proper notice. There are strict deadlines (often 90 days, with exceptions) and numerical limits, but an in-absentia removal order — one entered because the person missed a hearing they were not properly notified of — can sometimes be reopened outside the usual time limit. Because the deadlines are unforgiving, act immediately.")}
            <h2>Common grounds</h2>
            <ul>
              <li>Lack of proper notice of the original hearing</li>
              <li>New, previously unavailable evidence</li>
              <li>Changed country conditions for asylum-type relief</li>
              <li>Ineffective assistance of prior counsel</li>
            </ul>""",
    [("I was ordered removed in absentia — can it be undone?",
      "Sometimes. If you were not properly notified of the hearing, a motion to reopen may be possible, in some cases outside the usual deadline. Call immediately — timing is critical."),
     ("Is there a deadline to file a motion to reopen?",
      "Yes — often 90 days, with important exceptions. The deadlines are strict, so do not wait to seek advice.")],
    "im-reopen", "Immigration — motion to reopen",
    [("Removal defense", "/removal-defense.html"),
     ("Immigration court representation", "/immigration-court-representation.html"),
     ("Deportation defense", "/deportation-defense.html")],
    ["motion to reopen", "in absentia removal order", "BIA", "changed country conditions"],
    urgent=True))

PAGES.append(im(
    "waivers",
    "Immigration Waivers Lawyer | Inadmissibility | Newark Law Offices",
    "Immigration waivers — overcoming grounds of inadmissibility for a green card or visa, including unlawful-presence waivers. Call 866-230-7236. Free consultation.",
    "Immigration waivers",
    "A ground of inadmissibility does not always block a green card or visa. A waiver can forgive certain grounds where you qualify. We assess eligibility and build the hardship case. Free consultation.",
    ["Waivers", "Inadmissibility", "Overcome a bar"], "Waivers",
    f"""            <h2>Forgiving a ground of inadmissibility</h2>
{ans("What is an immigration waiver?", "An immigration waiver asks the government to forgive a specific ground of inadmissibility — such as certain unlawful presence, misrepresentation, or some criminal grounds — so a person can still qualify for a green card or visa. Many waivers require showing that a qualifying U.S. citizen or permanent resident relative would suffer 'extreme hardship' if the applicant were denied. Eligibility and the evidence needed depend on the specific ground, so a careful analysis comes first.")}
            <h2>Common waivers</h2>
            <ul>
              <li>Unlawful-presence waivers (including provisional waivers)</li>
              <li>Waivers of certain misrepresentation grounds</li>
              <li>Certain criminal-ground waivers where available</li>
            </ul>""",
    [("What is 'extreme hardship' for a waiver?",
      "Many waivers require showing a qualifying relative would face extreme hardship if the applicant were refused. It is more than ordinary separation and is proven with detailed evidence."),
     ("Can a prior immigration violation be waived?",
      "Some grounds can be waived if you qualify and meet the requirements; others cannot. Which applies depends on the specific ground — a consultation evaluates it.")],
    "im-waivers", "Immigration — waivers",
    [("Consular processing", "/consular-processing.html"), ("Adjustment of status", "/adjustment-of-status.html"),
     ("Removal defense", "/removal-defense.html")],
    ["immigration waiver", "inadmissibility", "extreme hardship", "unlawful presence waiver"]))

PAGES.append(im(
    "ice-detainers",
    "ICE Detainer Lawyer | Holds & Detention | Newark Law Offices",
    "ICE detainers and holds — what a detainer means, your rights, and what to do fast. Call 866-230-7236 now. Free consultation.",
    "ICE detainers and holds",
    "An ICE detainer (hold) asks a jail to keep someone for immigration authorities. It can be the first step toward removal — and there is a short window to act. Free, confidential consultation.",
    ["ICE detainers", "Holds", "Time-critical"], "ICE Detainers",
    f"""            <h2>What a detainer means</h2>
{ans("What is an ICE detainer?", "An ICE detainer (Form I-247) is a request from Immigration and Customs Enforcement asking a jail or law-enforcement agency to hold a person for up to 48 hours beyond when they would otherwise be released, so ICE can take custody. A detainer is a request, not a judicial warrant, and there are limits on how long someone can be held on one. Because a detainer often precedes transfer to immigration detention and the start of removal proceedings, getting counsel involved immediately can shape what happens next.")}
            <h2>What to do quickly</h2>
            <ul>
              <li>Do not sign anything agreeing to removal or waiving rights</li>
              <li>Identify where the person is held and the detainer status</li>
              <li>Prepare for a possible transfer and <a class="link" href="/bond-hearings.html">bond hearing</a></li>
            </ul>""",
    [("What should I do if ICE placed a detainer on my relative?",
      "Act immediately. Do not let them sign anything agreeing to removal. Find out where they are held, and prepare for a possible transfer to ICE and a bond hearing."),
     ("Is an ICE detainer a warrant?",
      "No. A detainer is a request to a jail to hold someone briefly for ICE, not a judicial warrant. There are legal limits on holding someone on a detainer.")],
    "im-detainers", "Immigration — ICE detainer",
    [("Bond hearings", "/bond-hearings.html"), ("Deportation defense", "/deportation-defense.html"),
     ("Removal defense", "/removal-defense.html")],
    ["ICE detainer", "immigration hold", "I-247", "48 hour hold"],
    urgent=True))

PAGES.append(im(
    "immigration-faq",
    "Immigration FAQ | Removal, Green Cards, Detention | Newark Law Offices",
    "Answers to common immigration questions — removal proceedings, green cards, detention and bond, and deadlines. Free consultation. Call 866-230-7236.",
    "Immigration FAQ",
    "Straight answers about removal, green cards, detention, and the deadlines that decide cases. General information, not legal advice — every case turns on its own facts. Free, confidential consultation.",
    ["FAQ", "Plain answers", "Immigration & removal"], "Immigration FAQ",
    """            <h2>The questions people ask most</h2>
            <p>These are general answers. What applies to your situation depends on your status, history, and any deadlines — which is what the consultation is for.</p>""",
    [("What happens in deportation (removal) proceedings?",
      "They take place in immigration court, where the government must prove removability and you can present defenses and apply for relief like cancellation, asylum, adjustment, or waivers. Missing a hearing usually means an automatic removal order."),
     ("My relative was detained by ICE — what do I do?",
      "Act immediately: find where they are held and whether there is a bond, and do not let them sign an agreement to removal. A bond hearing can seek release."),
     ("Can I get a green card without leaving the U.S.?",
      "Often through adjustment of status, if eligible. Otherwise consular processing abroad applies. Entry history and status determine the path."),
     ("Do I need a lawyer for immigration court?",
      "There is no government-appointed lawyer in immigration court, and the process and deadlines are complex. Representation is strongly advisable."),
     ("Can you help if you are not licensed in my state?",
      "Immigration courts are federal, so representation there is not limited by state bar licensure.")],
    "im-faq", "Immigration — general question",
    [("Immigration hub", HUB), ("Removal defense", "/removal-defense.html"),
     ("Bond hearings", "/bond-hearings.html")],
    ["immigration FAQ", "removal proceedings", "green card", "ICE detention"]))
