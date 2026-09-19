"""Insights articles batch 1 — bankruptcy + PI.

State-specific topics (keep house/car, sued by collector) are split into
separate Texas and Oklahoma articles because the law differs. General/federal
topics (Chapter 7 vs 13, claim value, recorded statement) stay state-neutral
but name major cities naturally for local-SEO reach without implying the law
is city-specific. No fabricated facts or outcomes; approval workflow first.
"""
from render_article import Article

def a(q, ans):
    return (f'        <div class="answer-block">\n'
            f'          <h3 class="answer-q">{q}</h3>\n'
            f'          <div class="answer-a">{ans}</div>\n'
            f'        </div>')

TX_CITIES = "Dallas, Fort Worth, Arlington, Plano, Houston, San Antonio, and across Texas"
OK_CITIES = "Oklahoma City, Edmond, Norman, Moore, Lawton, and across Oklahoma"

ARTICLES = []

# 1a. Keep house/car — TEXAS
ARTICLES.append(Article(
    slug="keep-house-car-bankruptcy-texas",
    title="Can I Keep My House and Car if I File Bankruptcy in Texas? | Newark Law Offices",
    description="Texas has one of the strongest homestead exemptions in the country. Here's how most Texans keep their home and car in Chapter 7 and Chapter 13 bankruptcy.",
    h1="Can I keep my house and car if I file bankruptcy in Texas?",
    dek="For most Texas filers, the answer is yes — Texas exemptions are among the most protective in the nation. Here's why.",
    cta_practice=("Talk to a Texas bankruptcy lawyer — free consultation", "/bankruptcy-lawyer.html"),
    knows_about=["Texas homestead exemption", "keep car bankruptcy Texas", "bankruptcy exemptions"],
    related=[("Chapter 7", "/chapter-7-bankruptcy.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
             ("Oklahoma version", "/insights/keep-house-car-bankruptcy-oklahoma.html")],
    body_html=f"""{a("Will I lose my house and car if I file bankruptcy in Texas?", "Usually no. Texas has one of the most protective homestead exemptions in the country — your primary residence is protected regardless of value, within acreage limits (10 urban acres, up to 100/200 rural). Texas also protects a large amount of personal property, including a vehicle. As long as you stay current on the loans, most Texans keep their home and car in both Chapter 7 and Chapter 13.")}
        <h2>The Texas homestead — nation-leading protection</h2>
        <p>Texas protects your primary residence regardless of its value, subject only to acreage limits. That's stronger than most states. For clients in {TX_CITIES}, this is usually why the home is safe. The exemption protects your <em>equity</em>, not the mortgage — so to keep the house you keep paying the loan, or use <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a> to catch up if you're behind.</p>
        <h2>Personal property and your vehicle</h2>
        <p>Texas allows a generous personal-property exemption (a set dollar cap per household) that typically covers a vehicle, household goods, and tools of a trade. A financed car is kept by staying current on the loan.</p>
        <h2>Chapter 7 vs. Chapter 13 in Texas</h2>
        <p>In <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a>, exempt property is protected. In <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a>, you keep everything and pay a plan — often the right choice when you're behind on the house or car.</p>
        <h2>Where it gets fact-specific</h2>
        <p>How long you've lived in Texas and whether you're current on secured loans affect the result. A free consultation sorts it out before you file.</p>
        <p><em>In Oklahoma? See the <a class="link" href="/insights/keep-house-car-bankruptcy-oklahoma.html">Oklahoma version</a> — the exemptions differ.</em></p>""",
    faqs=[
        ("Does the Texas homestead exemption cover my mortgage?",
         "No — it protects your equity, not the loan. To keep the home you keep paying the mortgage, or use Chapter 13 to catch up on missed payments."),
        ("Is there a value limit on the Texas homestead?",
         "No value cap — Texas protects the homestead regardless of value, subject to acreage limits (10 urban acres, up to 100/200 rural)."),
    ],
))

# 1b. Keep house/car — OKLAHOMA
ARTICLES.append(Article(
    slug="keep-house-car-bankruptcy-oklahoma",
    title="Can I Keep My House and Car if I File Bankruptcy in Oklahoma? | Newark Law Offices",
    description="Oklahoma protects a homestead and essential personal property in bankruptcy. Here's how most Oklahomans keep their home and car in Chapter 7 and Chapter 13.",
    h1="Can I keep my house and car if I file bankruptcy in Oklahoma?",
    dek="For most Oklahoma filers, the answer is yes — the state's homestead and property exemptions protect what matters. Here's how.",
    cta_practice=("Talk to an Oklahoma bankruptcy lawyer — free consultation", "/bankruptcy-lawyer.html"),
    knows_about=["Oklahoma homestead exemption", "keep car bankruptcy Oklahoma", "bankruptcy exemptions"],
    related=[("Chapter 7", "/chapter-7-bankruptcy.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
             ("Texas version", "/insights/keep-house-car-bankruptcy-texas.html")],
    body_html=f"""{a("Will I lose my house and car if I file bankruptcy in Oklahoma?", "Usually no. Oklahoma protects a homestead (your primary residence, within acreage limits) and a range of essential personal property, including a vehicle up to a set value. As long as you stay current on the loans, most Oklahomans keep their home and car in both Chapter 7 and Chapter 13. Which property is fully protected depends on the specific facts.")}
        <h2>The Oklahoma homestead</h2>
        <p>Oklahoma protects your primary residence as a homestead, within acreage limits (generally 1 acre urban, up to 160 rural). For clients in {OK_CITIES}, this is usually why the home is safe. As with any state, the exemption protects equity, not the loan — you keep paying the mortgage, or use <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a> to catch up.</p>
        <h2>Vehicle and personal property</h2>
        <p>Oklahoma exempts a motor vehicle up to a set value plus essential household goods and tools of a trade. A financed car is kept by staying current on the loan.</p>
        <h2>Chapter 7 vs. Chapter 13 in Oklahoma</h2>
        <p>In <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a>, exempt property is protected. In <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a>, you keep everything and pay a plan — often the right choice when you're behind on the house or car.</p>
        <p><em>In Texas? See the <a class="link" href="/insights/keep-house-car-bankruptcy-texas.html">Texas version</a> — the homestead there is even broader.</em></p>""",
    faqs=[
        ("Is there a value limit on the Oklahoma homestead?",
         "Oklahoma protects the homestead within acreage limits (about 1 acre urban, up to 160 rural). The specifics of your property should be reviewed in a consultation."),
        ("Can I keep a financed car in Oklahoma bankruptcy?",
         "Usually yes, if you stay current on the loan. If you're behind, Chapter 13 can cure the default over the plan."),
    ],
))

# 2a. Sued by collector — TEXAS
ARTICLES.append(Article(
    slug="sued-by-debt-collector-texas",
    title="Sued by a Debt Collector in Texas? What to Do First | Newark Law Offices",
    description="Sued by a debt collector in Texas? Texas prohibits wage garnishment for most consumer debts, but a bank account can still be levied. Here's what to do before the deadline.",
    h1="Sued by a debt collector in Texas? What to do first",
    dek="Texas protects your wages from most consumer creditors — but a lawsuit still has a short deadline you can't ignore.",
    cta_practice=("Talk to us before your deadline — free consultation", "/debt-collection-defense.html"),
    knows_about=["debt collection lawsuit Texas", "Texas wage garnishment", "default judgment"],
    related=[("Debt collection defense", "/debt-collection-defense.html"),
             ("Stop wage garnishment", "/stop-wage-garnishment.html"),
             ("Oklahoma version", "/insights/sued-by-debt-collector-oklahoma.html")],
    body_html=f"""{a("What happens if a debt collector sues me in Texas?", "You have a short window — often a few weeks — to file a written answer, or the collector takes a default judgment. Texas is unusual: it constitutionally prohibits wage garnishment for most consumer debts (credit cards, medical bills, personal loans). But a judgment creditor can still freeze and levy your bank account. Responding preserves defenses; bankruptcy's automatic stay can stop the suit entirely.")}
        <h2>The Texas advantage — and its limit</h2>
        <p>Texas does <strong>not</strong> allow wage garnishment for most consumer debts. That's a real protection for people in {TX_CITIES}. But it's not total: a creditor with a judgment can still <strong>freeze and levy your bank account</strong>, and wages can be garnished for child support, taxes, and federal student loans.</p>
        <h2>The deadline still matters</h2>
        <p>Ignoring the suit produces a default judgment — and then the bank levy. The citation states your answer deadline; don't miss it.</p>
        <h2>Your options</h2>
        <ul>
          <li><strong>Defend</strong> — collectors that bought old debt often can't prove they own it; Texas debts may be time-barred after four years.</li>
          <li><strong>Bankruptcy</strong> — a <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> filing stops the suit and discharges the debt. See <a class="link" href="/bankruptcy-and-lawsuits.html">bankruptcy and lawsuits</a>.</li>
        </ul>
        <p><em>In Oklahoma? Garnishment rules are different — see the <a class="link" href="/insights/sued-by-debt-collector-oklahoma.html">Oklahoma version</a>.</em></p>""",
    faqs=[
        ("Can a debt collector garnish my wages in Texas?",
         "Not for most consumer debts — Texas prohibits it. They can still levy a bank account, and wages can be garnished for child support, taxes, and federal student loans."),
        ("How long do I have to respond to a Texas debt lawsuit?",
         "It's short — the exact date is on the citation you were served. Missing it becomes a default judgment."),
    ],
))

# 2b. Sued by collector — OKLAHOMA
ARTICLES.append(Article(
    slug="sued-by-debt-collector-oklahoma",
    title="Sued by a Debt Collector in Oklahoma? What to Do First | Newark Law Offices",
    description="Sued by a debt collector in Oklahoma? Oklahoma allows wage garnishment on consumer judgments within federal limits. Here's what to do before the deadline.",
    h1="Sued by a debt collector in Oklahoma? What to do first",
    dek="Oklahoma allows wage garnishment on a consumer judgment — so the answer deadline matters even more. Here's the move.",
    cta_practice=("Talk to us before your deadline — free consultation", "/debt-collection-defense.html"),
    knows_about=["debt collection lawsuit Oklahoma", "Oklahoma wage garnishment", "default judgment"],
    related=[("Debt collection defense", "/debt-collection-defense.html"),
             ("Stop wage garnishment", "/stop-wage-garnishment.html"),
             ("Texas version", "/insights/sued-by-debt-collector-texas.html")],
    body_html=f"""{a("What happens if a debt collector sues me in Oklahoma?", "You have a short window to file a written answer, or the collector takes a default judgment. Unlike Texas, Oklahoma allows wage garnishment on a consumer judgment, capped by federal law (generally the lesser of 25% of disposable earnings or the amount above 30 times the federal minimum wage), and a bank account can also be levied. Responding preserves defenses; bankruptcy's automatic stay can stop the suit and the garnishment.")}
        <h2>Oklahoma allows wage garnishment — so act fast</h2>
        <p>For people in {OK_CITIES}, this is the key difference from Texas: a creditor who wins a consumer judgment in Oklahoma <strong>can garnish your wages</strong>, within federal limits, and levy your bank account. That makes the answer deadline critical.</p>
        <h2>Your options</h2>
        <ul>
          <li><strong>Defend</strong> — the collector may not be able to prove it owns the debt or the amount; older debts may be time-barred.</li>
          <li><strong>Bankruptcy</strong> — filing triggers the automatic stay, which stops the lawsuit and any garnishment, and a <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> can discharge the debt. See <a class="link" href="/stop-wage-garnishment.html">stop wage garnishment</a>.</li>
        </ul>
        <p><em>In Texas? Wages are far better protected — see the <a class="link" href="/insights/sued-by-debt-collector-texas.html">Texas version</a>.</em></p>""",
    faqs=[
        ("Can a debt collector garnish my wages in Oklahoma?",
         "Yes, on a consumer judgment, within federal limits (generally the lesser of 25% of disposable earnings or the amount above 30x the federal minimum wage). Bankruptcy's automatic stay stops it."),
        ("How do I stop an Oklahoma wage garnishment?",
         "Filing bankruptcy triggers an automatic stay that stops it immediately. Responding to the underlying lawsuit before judgment can also prevent it."),
    ],
))

# 4. Chapter 7 vs 13 (neutral, cities sprinkled)
ARTICLES.append(Article(
    slug="chapter-7-vs-chapter-13-which-is-right",
    title="Chapter 7 vs. Chapter 13: Which Is Right for Me? | Newark Law Offices",
    description="A plain-language comparison of Chapter 7 and Chapter 13 bankruptcy — income, property, timeline, and which fits — for filers across Texas and Oklahoma.",
    h1="Chapter 7 vs. Chapter 13: which is right for me?",
    dek="The two consumer bankruptcy chapters solve different problems. Here's how to tell which one fits.",
    cta_practice=("Find out which chapter fits — free consultation", "/bankruptcy-lawyer.html"),
    knows_about=["Chapter 7 vs Chapter 13", "means test", "bankruptcy comparison"],
    related=[("Chapter 7", "/chapter-7-bankruptcy.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
             ("Bankruptcy timeline", "/bankruptcy-timeline.html")],
    body_html=f"""{a("What's the difference between Chapter 7 and Chapter 13 bankruptcy?", "Chapter 7 erases (discharges) qualifying unsecured debt in about three to four months, with no repayment plan — it fits people with lower income and little non-exempt property. Chapter 13 reorganizes debt into a three-to-five-year repayment plan, which fits people who are behind on a mortgage or car, or whose income is too high to qualify for Chapter 7. Both are federal and work the same way whether you file in Texas or Oklahoma; the state's exemptions determine what you keep.")}
        <h2>Chapter 7 in one line</h2>
        <p>A fast liquidation that wipes out qualifying unsecured debt in a few months. Best when income is below the state median and you want a clean slate.</p>
        <h2>Chapter 13 in one line</h2>
        <p>A 3–5 year plan that lets you catch up on a house or car and protect property. Best when you're behind on secured payments or earn too much for Chapter 7.</p>
        <h2>How to tell which</h2>
        <ul>
          <li><strong>Behind on your mortgage?</strong> Usually Chapter 13.</li>
          <li><strong>Mostly unsecured debt, modest income?</strong> Usually Chapter 7.</li>
          <li><strong>Income above the state median?</strong> The means test may push you to Chapter 13.</li>
        </ul>
        <h2>Same federal law, whether you're in Dallas or Oklahoma City</h2>
        <p>Bankruptcy itself is federal — the chapters work the same for filers in Dallas, Fort Worth, Houston, Oklahoma City, Edmond, or anywhere in either state. What changes by state is the <strong>exemptions</strong> (what you keep), which we cover in the state-specific guides. See the <a class="link" href="/bankruptcy-timeline.html">bankruptcy timeline</a> for the steps.</p>""",
    faqs=[
        ("Can I choose Chapter 7 if I want to?",
         "Only if you qualify under the means test. If your income is too high, Chapter 13 is generally the path."),
        ("Does it matter whether I file in Texas or Oklahoma?",
         "The chapters are federal and work the same way. What differs by state is the exemptions — what property you keep — covered in the state-specific guides."),
    ],
))

# 5. Car accident claim worth (neutral, cities sprinkled)
ARTICLES.append(Article(
    slug="what-is-my-car-accident-claim-worth",
    title="What Is My Car Accident Claim Worth? | Texas & Oklahoma | Newark Law Offices",
    description="How car accident claim value is actually calculated — medical bills, lost income, coverage limits — for injured drivers across Texas and Oklahoma. No magic number.",
    h1="What is my car accident claim worth?",
    dek="There's no calculator that spits out a number — but there is a method. Here's how claim value is actually built.",
    cta_practice=("Get a free case evaluation", "/personal-injury.html"),
    knows_about=["car accident claim value", "damages", "UM UIM"],
    related=[("Car accidents", "/car-accidents.html"), ("Insurance disputes", "/insurance-disputes.html"),
             ("Personal injury", "/personal-injury.html")],
    body_html=f"""{a("How is a car accident claim's value calculated?", "Claim value is built from the losses the crash caused: medical bills (past and future), lost income and lost earning capacity, property damage, and pain and suffering — measured against who was at fault and the available insurance coverage. There is no fixed formula or guaranteed number; the value depends on the specific facts, and an early insurer offer often comes before the full medical picture is known. Texas and Oklahoma both use at-fault and comparative-negligence rules.")}
        <h2>Why nobody can quote a number up front</h2>
        <p>Anyone who promises a figure before reviewing your facts is guessing. Real value comes from the components below — and from whether there's coverage to pay it.</p>
        <h2>The components</h2>
        <ul>
          <li><strong>Medical expenses</strong> — past treatment plus future care.</li>
          <li><strong>Lost income and earning capacity.</strong></li>
          <li><strong>Property damage.</strong></li>
          <li><strong>Pain and suffering</strong> — varies widely by facts.</li>
        </ul>
        <h2>Coverage is the ceiling</h2>
        <p>A claim is only worth what someone can pay, so we map every policy — the at-fault driver's liability, your own PIP/med-pay, and <a class="link" href="/car-accidents.html">uninsured/underinsured motorist coverage</a>. This is the same whether the wreck was in Dallas, Fort Worth, Houston, Oklahoma City, or anywhere across Texas and Oklahoma.</p>
        <h2>Fault reduces it</h2>
        <p>Texas and Oklahoma use comparative negligence: if you're partly at fault, recovery is reduced (and barred past a threshold).</p>
        <h2>Why the first offer is low</h2>
        <p>Early offers arrive before future care and full coverage are known. Signing early can leave real losses uncovered.</p>""",
    faqs=[
        ("Do you pay a fee if there's no recovery?",
         "In appropriate cases these matters are handled on a contingent fee: the attorney fee is a percentage of any recovery, and no attorney fee is charged if there is no recovery. Expenses are separate and set out in a written agreement."),
        ("Is claim value different in Texas vs Oklahoma?",
         "The method is the same; both are at-fault comparative-negligence states. Specific limitations periods and thresholds can differ, which is fact-specific."),
    ],
))

# 6. Recorded statement (neutral, cities sprinkled)
ARTICLES.append(Article(
    slug="recorded-statement-insurance-adjuster-trap",
    title="The Recorded-Statement Trap: What Not to Say to an Insurance Adjuster | Newark Law Offices",
    description="After a crash, the adjuster's recorded statement can be used to reduce your claim. What to know before you talk to insurance — for drivers across Texas and Oklahoma.",
    h1="What not to say to an insurance adjuster",
    dek="The friendly call asking for a 'quick recorded statement' is not there to help you. Here's why.",
    cta_practice=("Talk to us before you talk to the adjuster", "/personal-injury.html"),
    knows_about=["recorded statement", "insurance adjuster", "car accident claim"],
    related=[("Car accidents", "/car-accidents.html"),
             ("After a car crash (practice note)", "/insights/after-a-car-crash-texas-oklahoma.html"),
             ("Personal injury", "/personal-injury.html")],
    body_html=f"""{a("Do I have to give the insurance company a recorded statement after a car accident?", "Generally you are not required to give the at-fault driver's insurer a recorded statement, and doing so early can hurt your claim. Adjusters use recorded statements to lock in your words before the full injury picture is clear, then use inconsistencies to reduce or deny the claim. It is reasonable to decline and to have your claim reviewed first. Your own insurer may require cooperation under your policy — that is different.")}
        <h2>Why they call so fast</h2>
        <p>The adjuster often calls within days — before you've finished treatment. A recorded statement freezes your account at its least-informed moment. "I feel okay," said in shock, becomes evidence you weren't hurt. This plays out the same in Dallas, Houston, Oklahoma City, and everywhere in between.</p>
        <h2>What to avoid</h2>
        <ul>
          <li>Don't speculate about fault or speed.</li>
          <li>Don't minimize injuries — many surface days later.</li>
          <li>Don't guess. "I don't recall" is honest and safe.</li>
          <li>Don't agree to a recorded statement with the other driver's insurer without advice.</li>
        </ul>
        <h2>What you can do</h2>
        <p>Politely decline a recorded statement with the at-fault insurer, provide basic facts in writing, and have the claim reviewed first. See our <a class="link" href="/insights/after-a-car-crash-texas-oklahoma.html">post-crash practice note</a>.</p>""",
    faqs=[
        ("Can I refuse to give a recorded statement?",
         "To the at-fault driver's insurer, generally yes. Your own policy may require cooperation — understand the difference before the call, and consider a review first."),
        ("What if I already gave a statement?",
         "It's not necessarily fatal to your claim, but bring exactly what you said to a review so it can be addressed."),
    ],
))
