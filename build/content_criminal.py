"""
Criminal defense spoke cluster (PHASE 3).

Links back to /criminal-defense-lawyer.html. Crisis-oriented CTAs. TX/OK-framed,
process/rights-only — no fabricated outcomes, success rates, or statistics.
Content states legal rights and process; it is not legal advice.
"""
from render_practice import PageSpec

HUB = "/criminal-defense-lawyer.html"

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

def cd(slug, title, desc, h1, lede, tags, bc, body, faqs, source, matter, related, knows):
    return PageSpec(
        slug=slug, title=title, description=desc, h1=h1, lede=lede, meta_tags=tags,
        breadcrumb_name=bc, cluster="Criminal Defense", cluster_hub=HUB,
        source=source, matter=matter,
        rail_heading="Arrested? Get help now",
        rail_lede="If there is an arrest, a court date, or a police request to talk, call before you say anything. Confidential.",
        chat_greeting="Charged or arrested in Texas or Oklahoma? Do not talk to police before counsel. Tell me what happened and I can point you to help.",
        knows_about=knows, related=related, body_html=body, faqs=faqs)

PAGES = []

PAGES.append(cd(
    "dui-dwi-defense",
    "DUI / DWI Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    "DUI/DWI defense in Texas and Oklahoma — license consequences, breath/blood tests, and defenses. Arrested? Call 866-230-7236 now. Free consultation.",
    "DUI / DWI defense in Texas and Oklahoma",
    "A DWI (Texas) or DUI (Oklahoma) arrest triggers two fights at once — the criminal case and your driver's license. Deadlines to protect your license can run in days. We defend both. Free, confidential consultation.",
    ["DUI / DWI", "License at risk", "Act in days"], "DUI / DWI Defense",
    f"""            <h2>Two cases, one arrest</h2>
{ans("What happens after a DUI or DWI arrest?", "A DWI (Texas) or DUI (Oklahoma) arrest starts a criminal case and a separate administrative action against your driver's license. In both states you often have only a short window (a matter of days) to request a hearing to protect your license after a breath/blood test refusal or failure. The criminal case examines the stop, the testing, and the evidence. Because the license deadline is so short, contacting a lawyer immediately matters.")}
            <h2>What we examine</h2>
            <ul>
              <li>Whether the traffic stop and arrest were lawful</li>
              <li>How field sobriety and breath/blood tests were administered</li>
              <li>Calibration and chain-of-custody for chemical tests</li>
              <li>The administrative license hearing deadline</li>
            </ul>""",
    [("How long do I have to save my license after a DWI/DUI?",
      "Often only a few days to request an administrative hearing after a refusal or failed test. Because the window is so short, contact a lawyer immediately."),
     ("Can a first-time DWI/DUI be reduced or dismissed?",
      "Sometimes, depending on the facts of the stop, the testing, and the evidence. Options like reduction, deferral, or dismissal are fact-specific — a review is the way to know."),
     ("Should I refuse a breath test?",
      "That decision has consequences either way and depends on your situation. What matters now is protecting your rights — talk to counsel before making statements.")],
    "cd-dui-dwi", "Criminal defense — DUI/DWI",
    [("Criminal defense hub", HUB), ("Probation violations", "/probation-violations.html"),
     ("Expungement", "/expungement.html")],
    ["DUI defense", "DWI defense", "license suspension", "administrative license hearing"]))

PAGES.append(cd(
    "drug-charges",
    "Drug Charges Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Drug charge defense in Texas and Oklahoma — possession to distribution, search issues, and diversion. Arrested? Call 866-230-7236. Free consultation.",
    "Drug charge defense in Texas and Oklahoma",
    "From simple possession to distribution, drug charges carry serious penalties and often turn on how the evidence was found. We scrutinize the search and pursue every option, including diversion where available. Free consultation.",
    ["Drug charges", "Search issues", "Diversion"], "Drug Charges",
    f"""            <h2>The search is often the case</h2>
{ans("What defenses exist for drug possession charges?", "Many drug cases turn on the Fourth Amendment: whether the stop, the search of a car or home, or the seizure of evidence was lawful. If evidence was obtained through an illegal search, a motion to suppress can keep it out. Other issues include actual vs. constructive possession (whose drugs were they), lab testing of the substance, and eligibility for diversion or drug-court programs that can avoid a conviction.")}
            <h2>What we review</h2>
            <ul>
              <li>The legality of the stop, search, and seizure</li>
              <li>Whether possession can actually be proven against you</li>
              <li>Lab analysis and chain of custody</li>
              <li>Diversion, deferred adjudication, or drug-court eligibility</li>
            </ul>""",
    [("Can drug charges be dismissed?",
      "Sometimes — for example, if evidence was obtained through an illegal search or possession cannot be proven. Diversion programs can also avoid a conviction in eligible cases."),
     ("What is the difference between possession and distribution?",
      "Distribution or intent-to-deliver charges are more serious and often rest on quantity, packaging, or other circumstantial evidence. How the case is charged matters a great deal.")],
    "cd-drug", "Criminal defense — drug charges",
    [("Criminal defense hub", HUB), ("Expungement", "/expungement.html"),
     ("Record sealing", "/record-sealing.html")],
    ["drug charges", "possession defense", "motion to suppress", "diversion"]))

PAGES.append(cd(
    "assault-charges",
    "Assault Charges Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Assault charge defense in Texas and Oklahoma — self-defense, misdemeanor to felony, and protective orders. Arrested? Call 866-230-7236. Free consultation.",
    "Assault charge defense in Texas and Oklahoma",
    "Assault charges range from misdemeanor to serious felony and often involve self-defense, disputed accounts, or a related protective order. We build the defense on the facts. Free, confidential consultation.",
    ["Assault charges", "Self-defense", "Misdemeanor to felony"], "Assault Charges",
    f"""            <h2>What an assault charge really involves</h2>
{ans("What are the defenses to an assault charge?", "Common defenses include self-defense or defense of others, lack of intent, mistaken identity, and disputed or exaggerated accounts of what happened. Assault charges in Texas and Oklahoma range from misdemeanor to felony depending on injury, use of a weapon, and the alleged victim. A related protective order may also be in play, which is a separate proceeding with its own deadlines.")}
            <h2>What we examine</h2>
            <ul>
              <li>Self-defense and defense-of-others evidence</li>
              <li>The credibility and consistency of the accounts</li>
              <li>Injuries, weapons, and how the charge is graded</li>
              <li>Any related <a class="link" href="/protective-orders.html">protective order</a> or <a class="link" href="/domestic-violence-defense.html">domestic violence</a> allegation</li>
            </ul>""",
    [("Is self-defense a defense to assault?",
      "It can be. Texas and Oklahoma recognize self-defense and defense of others within limits. Whether it applies depends on the specific facts."),
     ("Can an assault charge be dropped if the other person does not want to press charges?",
      "Not automatically. The state, not the alleged victim, decides whether to prosecute, though the victim's wishes can be a factor. Legal representation still matters.")],
    "cd-assault", "Criminal defense — assault",
    [("Domestic violence defense", "/domestic-violence-defense.html"),
     ("Protective orders", "/protective-orders.html"), ("Criminal defense hub", HUB)],
    ["assault charges", "self-defense", "misdemeanor assault", "aggravated assault"]))

PAGES.append(cd(
    "theft-charges",
    "Theft Charges Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Theft charge defense in Texas and Oklahoma — shoplifting to felony theft, and keeping a conviction off your record. Call 866-230-7236. Free consultation.",
    "Theft charge defense in Texas and Oklahoma",
    "A theft conviction is a crime of dishonesty that can follow you into every job application. From shoplifting to felony theft, we work to protect your record and your future. Free consultation.",
    ["Theft charges", "Protect your record", "Shoplifting to felony"], "Theft Charges",
    f"""            <h2>Why a theft charge is worth fighting</h2>
{ans("Why are theft charges serious even for small amounts?", "Theft is a crime of moral turpitude — a dishonesty offense — so even a low-value misdemeanor conviction can hurt employment, housing, and professional licenses for years. Charges are graded by the value of what was allegedly taken and can rise to a felony. Defenses include lack of intent (a genuine mistake or belief of ownership), mistaken identity, and diversion programs that avoid a conviction for eligible first offenses.")}
            <h2>What we pursue</h2>
            <ul>
              <li>Lack of intent or a claim-of-right defense</li>
              <li>Weak identification or circumstantial proof</li>
              <li>Diversion or deferred adjudication to keep a conviction off your record</li>
              <li>Later <a class="link" href="/expungement.html">expungement</a> or <a class="link" href="/record-sealing.html">record sealing</a> where eligible</li>
            </ul>""",
    [("Can a theft charge be kept off my record?",
      "Often the goal is exactly that — through diversion, deferred adjudication, or later expungement/sealing, depending on the charge and outcome and the state's rules."),
     ("Is shoplifting a misdemeanor or felony?",
      "It depends on the value alleged and prior history. Lower values are usually misdemeanors; higher values or repeat offenses can be felonies.")],
    "cd-theft", "Criminal defense — theft",
    [("Expungement", "/expungement.html"), ("Record sealing", "/record-sealing.html"),
     ("Criminal defense hub", HUB)],
    ["theft charges", "shoplifting defense", "crime of moral turpitude", "diversion"]))

PAGES.append(cd(
    "domestic-violence-defense",
    "Domestic Violence Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Domestic violence defense in Texas and Oklahoma — protective orders, firearm and custody consequences, and disputed allegations. Call 866-230-7236. Free consultation.",
    "Domestic violence defense in Texas and Oklahoma",
    "A domestic violence allegation moves fast — a protective order, a removal from your home, and consequences for firearms and custody can all land before trial. We defend the charge and the collateral fallout. Free, confidential consultation.",
    ["Domestic violence", "Protective orders", "Custody & firearms"], "Domestic Violence Defense",
    f"""            <h2>Consequences that arrive before trial</h2>
{ans("What are the consequences of a domestic violence charge?", "Beyond the criminal case, a domestic violence allegation can trigger an immediate protective order that removes you from your home and bars contact, plus long-term consequences for firearm rights, child custody, and immigration status — some of which attach before any conviction. Defenses include self-defense, false or exaggerated allegations (common in contested divorces and custody fights), and lack of evidence.")}
            <h2>What we address</h2>
            <ul>
              <li>The criminal charge itself</li>
              <li>Any related <a class="link" href="/protective-orders.html">protective order</a> hearing and its deadline</li>
              <li>Firearm, custody, and (where relevant) immigration fallout</li>
              <li>Self-defense and disputed or false allegations</li>
            </ul>""",
    [("Can a domestic violence case be dropped if my partner recants?",
      "Not automatically — the state decides whether to prosecute. A recantation can matter, but the case can proceed on other evidence. Legal representation is important."),
     ("Will a domestic violence charge affect my gun rights or custody?",
      "It can, sometimes even before a conviction through a protective order. These collateral consequences are a core reason to have counsel early.")],
    "cd-domestic-violence", "Criminal defense — domestic violence",
    [("Protective orders", "/protective-orders.html"), ("Assault charges", "/assault-charges.html"),
     ("Criminal defense hub", HUB)],
    ["domestic violence defense", "protective order", "firearm rights", "custody consequences"]))

PAGES.append(cd(
    "protective-orders",
    "Protective Order Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Protective orders in Texas and Oklahoma — responding to or seeking an order, hearings, and consequences. Short deadlines. Call 866-230-7236. Free consultation.",
    "Protective orders in Texas and Oklahoma",
    "Whether you have been served with a protective order or need one for safety, the hearing comes fast and the consequences are real — where you can live, your firearms, and contact with your children. Free consultation.",
    ["Protective orders", "Fast hearings", "Real consequences"], "Protective Orders",
    f"""            <h2>Why the hearing date controls everything</h2>
{ans("What happens at a protective order hearing?", "A protective order (restraining order) case usually starts with a temporary order and a hearing set within days or weeks, where a judge decides whether to issue a longer-term order. An order can bar contact, remove someone from a shared home, restrict firearm possession, and affect custody. Both the person seeking protection and the person responding have the right to present evidence and be heard, so preparing for that hearing quickly is essential.")}
            <h2>How we help</h2>
            <ul>
              <li>Responding to a protective order served against you</li>
              <li>Seeking an order where safety requires it</li>
              <li>Preparing evidence and witnesses for the hearing</li>
              <li>Addressing firearm, housing, and custody consequences</li>
            </ul>""",
    [("I was served with a protective order — what do I do?",
      "Do not violate it, even to explain yourself, and prepare for the hearing immediately. Violations are a separate crime. Contact a lawyer right away because the hearing is usually within days or weeks."),
     ("Can a protective order affect my children or firearms?",
      "Yes. Orders commonly restrict contact, firearm possession, and can affect custody arrangements. That is why the hearing matters.")],
    "cd-protective-orders", "Criminal defense — protective orders",
    [("Domestic violence defense", "/domestic-violence-defense.html"),
     ("Assault charges", "/assault-charges.html"), ("Criminal defense hub", HUB)],
    ["protective orders", "restraining order", "protective order hearing"]))

PAGES.append(cd(
    "probation-violations",
    "Probation Violation Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Probation violation defense in Texas and Oklahoma — what a violation means, hearings, and avoiding revocation. Call 866-230-7236. Free consultation.",
    "Probation violation defense in Texas and Oklahoma",
    "A probation violation can send you back before the judge who sentenced you — and the standard of proof is lower than at trial. We work to avoid revocation and keep you out of custody. Free consultation.",
    ["Probation violations", "Avoid revocation", "Lower burden"], "Probation Violations",
    f"""            <h2>Why a violation is dangerous</h2>
{ans("What happens if I violate probation?", "An alleged probation violation leads to a revocation hearing before the sentencing judge, where the state's burden is lower than at a criminal trial (often a preponderance of the evidence rather than beyond a reasonable doubt). A judge can continue probation, modify its terms, or revoke it and impose the original sentence. Violations can be technical (missed meetings, failed tests, unpaid fees) or new offenses. Prompt, prepared representation can be the difference between modification and jail.")}
            <h2>What we do</h2>
            <ul>
              <li>Challenge whether a violation actually occurred</li>
              <li>Present mitigation to keep probation intact</li>
              <li>Address technical violations (fees, classes, testing) constructively</li>
              <li>Argue for modification instead of revocation</li>
            </ul>""",
    [("Can I go to jail for a probation violation?",
      "Yes — a judge can revoke probation and impose the original sentence. But outcomes range from a warning to modified terms; preparation and mitigation matter."),
     ("What is the burden of proof at a revocation hearing?",
      "It is generally lower than at a criminal trial — often a preponderance of the evidence — which is one reason these hearings are risky without counsel.")],
    "cd-probation", "Criminal defense — probation violation",
    [("DUI / DWI defense", "/dui-dwi-defense.html"), ("Drug charges", "/drug-charges.html"),
     ("Criminal defense hub", HUB)],
    ["probation violation", "revocation hearing", "motion to revoke"]))

PAGES.append(cd(
    "expungement",
    "Expungement Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Expungement in Texas and Oklahoma — clearing an arrest or charge from your record, eligibility, and process. Call 866-230-7236. Free consultation.",
    "Expungement in Texas and Oklahoma",
    "A dismissed charge or an old arrest can still surface on background checks. Expungement can clear eligible records so you can answer 'no' to that question. We check your eligibility. Free consultation.",
    ["Expungement", "Clear your record", "Fresh start"], "Expungement",
    f"""            <h2>What expungement does</h2>
{ans("What is expungement and who is eligible?", "Expungement (called expunction in Texas) removes or destroys records of an arrest or charge so they no longer appear on most background checks. Eligibility depends on the outcome and the state: in Texas, expunction is generally available for arrests that did not lead to conviction (dismissals, acquittals, no-bills) and after waiting periods; certain deferred cases use nondisclosure (sealing) instead. Oklahoma has its own expungement categories with waiting periods. A record review determines what you qualify for.")}
            <h2>How we help</h2>
            <ul>
              <li>Review your record and determine eligibility</li>
              <li>File the petition in the right court</li>
              <li>Distinguish expungement from <a class="link" href="/record-sealing.html">record sealing/nondisclosure</a></li>
            </ul>""",
    [("Can I expunge a dismissed charge in Texas?",
      "Often yes. Texas expunction is generally available for arrests that did not result in conviction, subject to waiting periods and specific rules. A record review confirms eligibility."),
     ("What is the difference between expungement and sealing?",
      "Expungement generally destroys or removes the record; sealing (nondisclosure in Texas) hides it from most public access but not all. Which applies depends on your case — see the record sealing page.")],
    "cd-expungement", "Criminal defense — expungement",
    [("Record sealing", "/record-sealing.html"), ("Theft charges", "/theft-charges.html"),
     ("Criminal defense hub", HUB)],
    ["expungement", "expunction Texas", "clear criminal record"]))

PAGES.append(cd(
    "record-sealing",
    "Record Sealing & Nondisclosure Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Record sealing and nondisclosure in Texas and Oklahoma — hiding an eligible record from background checks. Call 866-230-7236. Free consultation.",
    "Record sealing and nondisclosure",
    "When a record cannot be fully expunged, sealing (nondisclosure in Texas) can hide it from most background checks — employers, landlords, and the public. We check whether you qualify. Free consultation.",
    ["Record sealing", "Nondisclosure", "Background checks"], "Record Sealing",
    f"""            <h2>Sealing vs. expungement</h2>
{ans("What is record sealing (nondisclosure)?", "Record sealing hides an eligible criminal record from most public background checks, though certain government and licensing agencies can still see it. In Texas this is an order of nondisclosure, often available after successful completion of deferred adjudication and a waiting period. Oklahoma also allows sealing of eligible records. Unlike expungement, which generally destroys the record, sealing restricts who can access it.")}
            <h2>How we help</h2>
            <ul>
              <li>Determine whether sealing or <a class="link" href="/expungement.html">expungement</a> fits your record</li>
              <li>Confirm waiting periods and eligibility</li>
              <li>File the petition or nondisclosure order</li>
            </ul>""",
    [("Who can still see a sealed record?",
      "Sealing hides a record from most public background checks, but certain law-enforcement, government, and licensing agencies may still access it. Expungement is broader where it is available."),
     ("Am I eligible to seal my record?",
      "It depends on the offense, the outcome (such as completed deferred adjudication), and waiting periods. A record review is the way to know for sure.")],
    "cd-record-sealing", "Criminal defense — record sealing",
    [("Expungement", "/expungement.html"), ("Theft charges", "/theft-charges.html"),
     ("Criminal defense hub", HUB)],
    ["record sealing", "order of nondisclosure", "seal criminal record"]))

PAGES.append(cd(
    "criminal-defense-faq",
    "Criminal Defense FAQ | Texas & Oklahoma | Newark Law Offices",
    "Answers to common criminal defense questions in Texas and Oklahoma — your rights, talking to police, bond, and keeping charges off your record. Free consultation.",
    "Criminal defense FAQ",
    "Straight answers about your rights after an arrest or charge in Texas and Oklahoma. General information, not legal advice — every case turns on its own facts. Free, confidential consultation.",
    ["FAQ", "Your rights", "Plain answers"], "Criminal Defense FAQ",
    """            <h2>The questions people ask after an arrest</h2>
            <p>These are general answers about your rights and the process. What applies to your case depends on the specific facts — that is what the consultation is for.</p>""",
    [("Should I talk to the police without a lawyer?",
      "No. You have the right to remain silent and to counsel. Politely decline to answer and ask for a lawyer. Using those rights is not an admission of guilt."),
     ("Do I need a lawyer for a misdemeanor?",
      "Yes, it is worth a consultation. Even a misdemeanor can carry a record, fines, and license or immigration consequences, and early options can be lost without advice."),
     ("What should I do to get out on bond?",
      "A lawyer can request a bond or a bond reduction and argue the relevant factors. Contact counsel as soon as possible after an arrest."),
     ("Can charges be kept off my record?",
      "Sometimes — through diversion, deferred adjudication, expungement, or sealing, depending on the charge, outcome, and state. See the expungement and record-sealing pages."),
     ("How much does a criminal defense lawyer cost?",
      "Fees depend on the charge and complexity and are set out in a written agreement before work begins. The initial consultation is free.")],
    "cd-faq", "Criminal defense — general question",
    [("Criminal defense hub", HUB), ("Expungement", "/expungement.html"),
     ("DUI / DWI defense", "/dui-dwi-defense.html")],
    ["criminal defense FAQ", "right to remain silent", "bond", "misdemeanor"]))
