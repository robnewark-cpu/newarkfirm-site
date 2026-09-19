"""
Business & creditor bankruptcy sub-hub + crimigration page.

- Business/creditor sub-hub gathers the existing Ch.11 debtor/creditor pages
  (which were orphaned from the consumer hub) and adds a creditor-representation
  page, with B2B framing distinct from the consumer funnel.
- Crimigration: the criminal-defense/immigration overlap — a real, high-value
  practice the firm is uniquely positioned for (it handles both in-house).

Process-only, no fabricated outcomes. Video slots are inert (video=None) until
real videos exist.
"""
from render_practice import PageSpec

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

PAGES = []

# Business & creditor bankruptcy sub-hub
PAGES.append(PageSpec(
    slug="business-creditor-bankruptcy",
    title="Business & Creditor Bankruptcy Attorney | Chapter 11 | Newark Law Offices",
    description="Chapter 11 reorganization for businesses and creditor representation in bankruptcy court across Texas, Oklahoma, and federal districts. Call 866-230-7236.",
    h1="Business reorganization and creditor representation in bankruptcy",
    lede="Beyond consumer filings, Newark Law Offices represents businesses reorganizing under Chapter 11 and creditors protecting their position in bankruptcy court — proofs of claim, plan objections, relief from stay, and collateral. Texas, Oklahoma, and admitted federal districts.",
    meta_tags=["Chapter 11", "Creditor rights", "Business reorganization"],
    breadcrumb_name="Business & Creditor Bankruptcy",
    cluster="Bankruptcy", cluster_hub="/bankruptcy-lawyer.html",
    source="business-creditor-bk", matter="Bankruptcy — business/creditor",
    rail_heading="Business or creditor matter?",
    rail_lede="Tell us whether you are a business considering reorganization or a creditor protecting a claim, and the deadline you face.",
    chat_greeting="Business facing reorganization, or a creditor in a bankruptcy case? Tell me the situation and any deadline and I can point you to the right counsel.",
    knows_about=["Chapter 11 reorganization", "Subchapter V", "creditor representation",
                 "proof of claim", "relief from stay", "plan objection"],
    related=[("Chapter 11 debtor (TX)", "/ch11-debtor-texas.html"),
             ("Chapter 11 creditor (TX)", "/ch11-creditor-texas.html"),
             ("Chapter 11 debtor (OK)", "/ch11-debtor-oklahoma.html"),
             ("Consumer bankruptcy", "/bankruptcy-lawyer.html")],
    body_html=f"""            <h2>Two sides of the bankruptcy courtroom</h2>
            <p>Consumer Chapter 7 and 13 are one part of this firm's bankruptcy practice. The other is business and creditor work: helping a company reorganize under <strong>Chapter 11</strong>, and representing <strong>creditors</strong> who need to protect a claim when someone else files. These are B2B matters with different stakes and deadlines from a consumer filing.</p>

{ans("What is Chapter 11 bankruptcy?", "Chapter 11 is a reorganization bankruptcy, most often used by businesses, that lets a company restructure its debts under a court-approved plan while continuing to operate. A streamlined version, Subchapter V, is available to smaller businesses. Filing triggers the automatic stay, halting collection and lawsuits, while the business negotiates a plan with its creditors.")}

            <h2>Business reorganization (Chapter 11 &amp; Subchapter V)</h2>
            <p>For a business under creditor pressure, Chapter 11 can stop enforcement, restructure debt, and keep the doors open. We handle debtor-side reorganization in:</p>
            <ul>
              <li>Texas — <a class="link" href="/ch11-debtor-texas.html">Chapter 11 debtor reorganization</a></li>
              <li>Oklahoma — <a class="link" href="/ch11-debtor-oklahoma.html">Chapter 11 debtor reorganization</a></li>
              <li>Federal districts where the firm is admitted — <a class="link" href="/ch11-debtor-colorado.html">Colorado</a>, <a class="link" href="/ch11-debtor-new-mexico.html">New Mexico</a>, <a class="link" href="/ch11-debtor-arkansas.html">Arkansas</a></li>
            </ul>

            <h2>Creditor representation</h2>
{ans("Can a lawyer represent creditors in bankruptcy court?", "Yes. When a debtor files bankruptcy, creditors have rights that must be actively protected — filing a proof of claim, objecting to a reorganization plan that undervalues the debt, seeking relief from the automatic stay to pursue collateral, and challenging preferential transfers. A creditor that does nothing often recovers less. Newark Law Offices represents creditors in these proceedings.")}
            <p>Creditor-side matters we handle:</p>
            <ul>
              <li>Proofs of claim and claim disputes</li>
              <li>Relief-from-stay motions to reach collateral</li>
              <li>Plan objections and adequate-protection demands</li>
              <li>Texas — <a class="link" href="/ch11-creditor-texas.html">creditor representation</a>; Oklahoma — <a class="link" href="/ch11-creditor-oklahoma.html">creditor representation</a></li>
              <li>Federal districts — <a class="link" href="/ch11-creditor-colorado.html">Colorado</a>, <a class="link" href="/ch11-creditor-new-mexico.html">New Mexico</a>, <a class="link" href="/ch11-creditor-arkansas.html">Arkansas</a></li>
            </ul>

            <h2>Who this is for</h2>
            <p>Business owners facing insolvency who want to reorganize rather than liquidate; and banks, lenders, vendors, and other creditors who need to protect a claim in someone else's bankruptcy. If you are an individual dealing with personal debt, start with <a class="link" href="/bankruptcy-lawyer.html">consumer bankruptcy</a> instead.</p>""",
    faqs=[
        ("What is the difference between Chapter 11 and Chapter 7 or 13?",
         "Chapter 7 and 13 are primarily for individuals (liquidation and repayment plans). Chapter 11 is a reorganization, most often used by businesses, that lets a company restructure debt under a court-approved plan while continuing to operate. Subchapter V is a streamlined Chapter 11 for smaller businesses."),
        ("I am owed money by a company that filed bankruptcy — what should I do?",
         "Act promptly. You generally must file a proof of claim by a deadline (the bar date), and you may need to object to a plan or seek relief from the stay to protect collateral. A creditor that does nothing often recovers less. Contact the firm with the case details."),
        ("Can you represent both debtors and creditors?",
         "The firm handles both debtor reorganization and creditor representation, but not on opposite sides of the same case — that would be a conflict. Each engagement is screened for conflicts before it begins."),
    ],
    video=None,
))

# Crimigration
PAGES.append(PageSpec(
    slug="crimigration-immigration-consequences",
    title="Crimigration Lawyer | Criminal Charges & Immigration Consequences | Newark Law Offices",
    description="Crimigration: how criminal charges affect immigration status — deportation, inadmissibility, and defense that protects a non-citizen. Both practices in-house. Call 866-230-7236.",
    h1="Crimigration: criminal charges and immigration consequences",
    lede="For a non-citizen, a criminal charge is also an immigration case. A plea that seems minor can trigger deportation or bar relief. Newark Law Offices handles both criminal defense and immigration in-house, so the two are coordinated — not left to chance.",
    meta_tags=["Crimigration", "Criminal + immigration", "Protect your status"],
    breadcrumb_name="Crimigration",
    cluster="Immigration", cluster_hub="/immigration-lawyer.html",
    source="crimigration", matter="Crimigration — criminal + immigration",
    rail_heading="Non-citizen facing charges?",
    rail_lede="If you or a loved one is a non-citizen facing a criminal charge, tell us the charge and status before any plea. This is time-sensitive.",
    chat_greeting="Is a non-citizen facing a criminal charge? The plea can affect immigration status. Tell me the charge and status and I can point you to coordinated help.",
    knows_about=["crimigration", "immigration consequences of crimes", "crimes involving moral turpitude",
                 "aggravated felony", "deportation from plea", "Padilla v. Kentucky"],
    related=[("Criminal defense", "/criminal-defense-lawyer.html"),
             ("Immigration & removal defense", "/immigration-lawyer.html"),
             ("Removal defense", "/removal-defense.html"),
             ("Drug charges", "/drug-charges.html")],
    body_html=f"""            <h2>Why a criminal case is an immigration case</h2>
{ans("How can a criminal charge affect my immigration status?", "For a non-citizen, a criminal conviction — and sometimes just a plea or even an arrest — can trigger deportation, make you inadmissible (unable to re-enter or adjust status), or bar you from relief like cancellation of removal or naturalization. Certain offenses (aggravated felonies and crimes involving moral turpitude, including some drug and theft offenses) carry the harshest immigration consequences, even when the criminal penalty itself is minor. This overlap is called crimigration.")}

            <h2>The trap: a 'good' criminal outcome can be an immigration disaster</h2>
            <p>A plea deal that a criminal lawyer would call a win — probation, deferred adjudication, a reduced charge — can still be a <strong>deportable offense</strong> under immigration law. The U.S. Supreme Court held in <em>Padilla v. Kentucky</em> that defense counsel must advise a non-citizen of the immigration consequences of a plea. A lawyer who handles only the criminal side may not see the immigration cliff coming.</p>

            <h2>How handling both in-house protects you</h2>
            <p>Because Newark Law Offices handles <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a> and <a class="link" href="/immigration-lawyer.html">immigration</a> together, we evaluate every criminal option for its immigration effect before you decide:</p>
            <ul>
              <li>Whether a charge is a crime involving moral turpitude or an aggravated felony</li>
              <li>Whether an alternative plea or charge avoids the immigration trigger</li>
              <li>How a disposition affects <a class="link" href="/removal-defense.html">removal defense</a>, bond, and future relief</li>
              <li>Coordinating the criminal case and any immigration proceeding as one strategy</li>
            </ul>

            <h2>Who needs crimigration counsel</h2>
            <p>Any non-citizen — green-card holder, visa holder, DACA recipient, or undocumented — facing any criminal charge, however minor it seems. The time to get this right is <strong>before</strong> a plea, because a conviction is very hard to undo for immigration purposes afterward.</p>""",
    faqs=[
        ("I have a green card — can a misdemeanor get me deported?",
         "Possibly. Some misdemeanors are crimes involving moral turpitude or controlled-substance offenses that carry immigration consequences even for lawful permanent residents. The specific charge and disposition matter enormously — get advice before pleading."),
        ("My criminal lawyer got me a good plea deal — am I safe?",
         "Not necessarily. A plea that is good under criminal law can still be a deportable offense under immigration law. The two systems are separate. This is exactly why coordinating criminal defense with immigration analysis matters."),
        ("Should I tell my lawyer I am not a citizen?",
         "Yes, absolutely, and early. Your immigration status changes the entire criminal strategy — what pleas are safe, what to avoid. Counsel must know to protect you (Padilla v. Kentucky requires that advice)."),
    ],
    video=None,
))
