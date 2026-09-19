"""Insights articles batch 1 — bankruptcy + personal injury (articles 1-5).

Publish-ready, plain-language, TX/OK-framed. General legal information only —
no fabricated facts, statistics, or outcomes. Routed through the approval
workflow before publication.
"""
from render_article import Article

def a(q, ans):
    return (f'        <div class="answer-block">\n'
            f'          <h3 class="answer-q">{q}</h3>\n'
            f'          <div class="answer-a">{ans}</div>\n'
            f'        </div>')

ARTICLES = []

# 1. Keep my house and car
ARTICLES.append(Article(
    slug="keep-house-car-bankruptcy-texas-oklahoma",
    title="Can I Keep My House and Car if I File Bankruptcy in Texas or Oklahoma? | Newark Law Offices",
    description="Most people keep their home and car in bankruptcy thanks to Texas and Oklahoma exemptions. Here's how it works in Chapter 7 and Chapter 13.",
    h1="Can I keep my house and car if I file bankruptcy?",
    dek="It's the fear that stops most people from getting help. For the majority of filers in Texas and Oklahoma, the answer is yes — here's why.",
    cta_practice=("Talk to a bankruptcy lawyer — free consultation", "/bankruptcy-lawyer.html"),
    knows_about=["bankruptcy exemptions", "Texas homestead", "keep car in bankruptcy"],
    related=[("Chapter 7", "/chapter-7-bankruptcy.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
             ("Bankruptcy lawyer", "/bankruptcy-lawyer.html")],
    body_html=f"""{a("Will I lose my house and car if I file bankruptcy in Texas or Oklahoma?", "Usually no. Both states have generous exemptions that protect your home and a vehicle. Texas protects an unlimited-value homestead (within acreage limits) and a broad set of personal property; Oklahoma also protects a homestead and essential personal property. As long as you stay current on the loans, most people keep their home and car in both Chapter 7 and Chapter 13.")}
        <h2>The short answer</h2>
        <p>The single biggest myth about bankruptcy is that you lose everything. In reality, bankruptcy law is built around <strong>exemptions</strong> — categories of property the law lets you keep. For most consumer filers in Texas and Oklahoma, that means the home, a vehicle, retirement accounts, and household goods are protected.</p>
        <h2>The homestead — where Texas is especially strong</h2>
        <p>Texas has one of the most protective homestead exemptions in the country: your primary residence is protected regardless of its value, subject to acreage limits (10 acres urban, up to 100/200 rural). Oklahoma likewise protects a homestead. The catch is the mortgage itself — an exemption protects your <em>equity</em>, not the loan. To keep the house, you keep paying the mortgage (or, if you're behind, <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a> lets you catch up over time).</p>
        <h2>Your vehicle</h2>
        <p>A financed car is kept the same way: stay current on the loan and the car is yours. If you're behind, Chapter 13 can cure the default over the plan. If you own the car outright, exemptions protect it up to the applicable limit.</p>
        <h2>Chapter 7 vs. Chapter 13 for keeping property</h2>
        <p>In <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a>, exempt property is protected and non-exempt property (rare for most consumers) could be sold by the trustee. In <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a>, you keep everything and pay a plan — which is often the right choice specifically <em>because</em> it protects property while curing missed payments.</p>
        <h2>Where it gets fact-specific</h2>
        <p>How long you've lived in the state, how much equity you have, and whether you're current on secured loans all affect the outcome. That's exactly what a free consultation sorts out — before you file, not after.</p>""",
    faqs=[
        ("Does the homestead exemption cover my mortgage?",
         "No — it protects your equity, not the loan. To keep the home you keep paying the mortgage, or use Chapter 13 to catch up on missed payments over the plan."),
        ("What if I have a lot of equity in my home?",
         "In Texas the homestead is protected regardless of value (within acreage limits). Other states and situations vary; bring the details to a consultation."),
        ("Can I keep a car I'm still making payments on?",
         "Usually yes, if you stay current on the loan. If you're behind, Chapter 13 can cure the default so you keep the vehicle."),
    ],
))

# 2. Ch7 vs Ch13
ARTICLES.append(Article(
    slug="chapter-7-vs-chapter-13-which-is-right",
    title="Chapter 7 vs. Chapter 13: Which Is Right for Me? | Newark Law Offices",
    description="A plain-language comparison of Chapter 7 and Chapter 13 bankruptcy for Texas and Oklahoma — income, property, timeline, and which fits your situation.",
    h1="Chapter 7 vs. Chapter 13: which is right for me?",
    dek="The two consumer bankruptcy chapters solve different problems. Here's how to tell which one fits.",
    cta_practice=("Find out which chapter fits — free consultation", "/bankruptcy-lawyer.html"),
    knows_about=["Chapter 7 vs Chapter 13", "means test", "bankruptcy comparison"],
    related=[("Chapter 7", "/chapter-7-bankruptcy.html"), ("Chapter 13", "/chapter-13-bankruptcy.html"),
             ("Bankruptcy timeline", "/bankruptcy-timeline.html")],
    body_html=f"""{a("What's the difference between Chapter 7 and Chapter 13 bankruptcy?", "Chapter 7 erases (discharges) qualifying unsecured debt in about three to four months, with no repayment plan — it fits people with lower income and little non-exempt property. Chapter 13 reorganizes debt into a three-to-five-year repayment plan, which fits people who are behind on a mortgage or car and need to catch up, or whose income is too high to qualify for Chapter 7.")}
        <h2>Chapter 7 in one line</h2>
        <p>A fast liquidation that wipes out qualifying unsecured debt — credit cards, medical bills, personal loans — usually in a few months. Best when your income is below the state median and you mainly want a clean slate.</p>
        <h2>Chapter 13 in one line</h2>
        <p>A 3–5 year repayment plan that lets you catch up on a house or car, protect non-exempt property, and pay a portion of unsecured debt. Best when you're behind on secured payments or earn too much for Chapter 7.</p>
        <h2>How to tell which one</h2>
        <ul>
          <li><strong>Behind on your mortgage and want to keep the house?</strong> Usually Chapter 13.</li>
          <li><strong>Mostly unsecured debt and modest income?</strong> Usually Chapter 7.</li>
          <li><strong>Income above the state median?</strong> The means test may push you to Chapter 13.</li>
          <li><strong>Facing repossession you want to undo?</strong> Chapter 13 can cure the default.</li>
        </ul>
        <h2>The means test</h2>
        <p>Chapter 7 eligibility runs through a means test comparing your income to the state median for your household size. If you're below, Chapter 7 is generally available; if above, a more detailed calculation — or Chapter 13 — applies. We run this with you on the first call.</p>
        <h2>Timeline difference</h2>
        <p>Chapter 7 typically closes in about three to four months. Chapter 13 runs the length of the plan (three to five years), with a discharge at the end. See the <a class="link" href="/bankruptcy-timeline.html">bankruptcy timeline</a> for the step-by-step.</p>""",
    faqs=[
        ("Can I choose Chapter 7 if I want to?",
         "Only if you qualify under the means test. If your income is too high, Chapter 13 is generally the path."),
        ("Which one hurts my credit less?",
         "Both appear on your credit report (Chapter 7 up to ten years, Chapter 13 up to seven), but many people rebuild within a year or two after discharge regardless of chapter."),
    ],
))

# 3. Sued by a debt collector
ARTICLES.append(Article(
    slug="sued-by-debt-collector-what-to-do",
    title="Sued by a Debt Collector? What to Do in the First 20 Days | Newark Law Offices",
    description="Being sued by a debt collector in Texas or Oklahoma? Don't ignore it. Here's what to do before the answer deadline turns into a default judgment.",
    h1="Sued by a debt collector? What to do first",
    dek="A collection lawsuit has a short deadline — and ignoring it is how a debt becomes a garnishment. Here's the move.",
    cta_practice=("Talk to us before your deadline — free consultation", "/debt-collection-defense.html"),
    knows_about=["debt collection lawsuit", "answer deadline", "default judgment"],
    related=[("Debt collection defense", "/debt-collection-defense.html"),
             ("Bankruptcy and lawsuits", "/bankruptcy-and-lawsuits.html"),
             ("Stop wage garnishment", "/stop-wage-garnishment.html")],
    body_html=f"""{a("What should I do if I'm sued by a debt collector?", "Don't ignore it. You have a short window — often a few weeks — to file a written answer with the court. Missing that deadline lets the collector take a default judgment, which can lead to bank levies and, in Oklahoma, wage garnishment. Responding preserves your defenses; filing bankruptcy can also stop the lawsuit entirely through the automatic stay.")}
        <h2>The clock is the first thing that matters</h2>
        <p>When you're served with a collection lawsuit, the citation states your deadline to respond — often a matter of weeks. If you do nothing, the collector wins automatically by <strong>default judgment</strong>, and then can pursue your bank account (both states) or wages (Oklahoma; Texas prohibits wage garnishment for most consumer debts).</p>
        <h2>Your options</h2>
        <ul>
          <li><strong>Answer and defend.</strong> Collectors that bought old debt often can't prove they own it or the amount. Old debts may be time-barred (four years in Texas).</li>
          <li><strong>Negotiate.</strong> Sometimes a lump-sum settlement makes sense — but get the terms in writing.</li>
          <li><strong>Bankruptcy.</strong> If several collectors are after you, a <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> filing stops all of them at once and discharges the underlying debt. See <a class="link" href="/bankruptcy-and-lawsuits.html">bankruptcy and lawsuits</a>.</li>
        </ul>
        <h2>What not to do</h2>
        <p>Don't ignore the suit, and don't make a partial payment on an old debt without advice — it can restart the statute of limitations. Talk to someone before the answer deadline.</p>""",
    faqs=[
        ("How long do I have to respond to a debt lawsuit?",
         "It's short — often a few weeks, and the exact date is on the citation you were served. Don't wait; a missed deadline becomes a default judgment."),
        ("Can they garnish my wages in Texas?",
         "Not for most consumer debts — Texas prohibits it. They can still levy a bank account. Oklahoma allows wage garnishment on a consumer judgment within federal limits."),
    ],
))

# 4. What is my car accident claim worth
ARTICLES.append(Article(
    slug="what-is-my-car-accident-claim-worth-texas",
    title="What Is My Car Accident Claim Worth in Texas or Oklahoma? | Newark Law Offices",
    description="How car accident claim value is actually calculated in Texas and Oklahoma — medical bills, lost income, coverage limits — and why the first offer is rarely the real number.",
    h1="What is my car accident claim worth?",
    dek="There's no calculator that spits out a number — but there is a method. Here's how claim value is actually built.",
    cta_practice=("Get a free case evaluation", "/personal-injury.html"),
    knows_about=["car accident claim value", "damages", "UM UIM"],
    related=[("Car accidents", "/car-accidents.html"), ("Insurance disputes", "/insurance-disputes.html"),
             ("Personal injury", "/personal-injury.html")],
    body_html=f"""{a("How is a car accident claim's value calculated?", "Claim value is built from the losses the crash caused: medical bills (past and future), lost income and lost earning capacity, property damage, and pain and suffering — measured against who was at fault and the available insurance coverage. There is no fixed formula or guaranteed number; the value depends entirely on the specific facts, and an early insurer offer often comes before the full medical picture is known.")}
        <h2>Why nobody can quote you a number up front</h2>
        <p>Anyone who promises a dollar figure before reviewing your facts is guessing. Real value comes from the pieces below — and from whether there's coverage to pay it.</p>
        <h2>The components</h2>
        <ul>
          <li><strong>Medical expenses</strong> — past treatment plus the cost of care you'll still need.</li>
          <li><strong>Lost income and earning capacity</strong> — time missed and any lasting effect on your ability to work.</li>
          <li><strong>Property damage</strong> — the vehicle and its contents.</li>
          <li><strong>Pain and suffering</strong> — the non-economic impact, which varies widely by facts.</li>
        </ul>
        <h2>Coverage is the ceiling</h2>
        <p>A claim is only worth what someone can pay. That's why we map every policy — the at-fault driver's liability, your own PIP/med-pay, and <a class="link" href="/car-accidents.html">uninsured/underinsured motorist coverage</a> — before talking value.</p>
        <h2>Fault reduces it</h2>
        <p>Texas and Oklahoma use comparative negligence: if you're found partly at fault, your recovery is reduced accordingly (and barred past a threshold). How fault is assigned matters as much as the injuries.</p>
        <h2>Why the first offer is low</h2>
        <p>Early offers usually arrive before future care and full coverage are known. Signing early can leave real losses uncovered — which is why a review before you sign matters.</p>""",
    faqs=[
        ("Do you pay a fee if there's no recovery?",
         "In appropriate cases these matters are handled on a contingent fee: the attorney fee is a percentage of any recovery, and no attorney fee is charged if there is no recovery. Expenses are separate and set out in a written agreement."),
        ("Should I take the insurer's first offer?",
         "Usually not before a review. Early offers often come before future care, lost earning capacity, and all coverage layers are known."),
    ],
))

# 5. Recorded statement trap
ARTICLES.append(Article(
    slug="recorded-statement-insurance-adjuster-trap",
    title="The Recorded-Statement Trap: What Not to Say to an Insurance Adjuster | Newark Law Offices",
    description="After a crash, the adjuster's recorded statement can be used to reduce your claim. Here's what to know before you talk to insurance in Texas or Oklahoma.",
    h1="What not to say to an insurance adjuster",
    dek="The friendly call asking for a 'quick recorded statement' is not there to help you. Here's why.",
    cta_practice=("Talk to us before you talk to the adjuster", "/personal-injury.html"),
    knows_about=["recorded statement", "insurance adjuster", "car accident claim"],
    related=[("Car accidents", "/car-accidents.html"),
             ("After a car crash (practice note)", "/insights/after-a-car-crash-texas-oklahoma.html"),
             ("Personal injury", "/personal-injury.html")],
    body_html=f"""{a("Do I have to give the insurance company a recorded statement after a car accident?", "Generally you are not required to give the at-fault driver's insurer a recorded statement, and doing so early can hurt your claim. Adjusters use recorded statements to lock in your words before the full injury picture is clear, then use inconsistencies to reduce or deny the claim. It's reasonable to decline and to have a claim reviewed first.")}
        <h2>Why they call so fast</h2>
        <p>The adjuster often calls within days — before you've finished treatment or understand your injuries. A recorded statement freezes your account at its least-informed moment. "I feel okay" said in shock becomes evidence you weren't hurt.</p>
        <h2>What to avoid</h2>
        <ul>
          <li>Don't speculate about fault or speed ("I think I was going about...").</li>
          <li>Don't minimize injuries ("I'm fine, just sore") — many injuries surface days later.</li>
          <li>Don't guess. "I don't recall" is an honest, safe answer.</li>
          <li>Don't agree to a recorded statement with the other driver's insurer without advice.</li>
        </ul>
        <h2>What you can do</h2>
        <p>You can politely decline a recorded statement with the at-fault insurer, provide basic facts in writing, and have your claim reviewed first. Your own insurer may require cooperation under your policy — that's different, and worth understanding before the call.</p>
        <h2>Before you sign anything</h2>
        <p>Don't sign a release or accept a check before you know what you're settling. See our <a class="link" href="/insights/after-a-car-crash-texas-oklahoma.html">post-crash practice note</a> and the <a class="link" href="/car-accidents.html">car accident page</a>.</p>""",
    faqs=[
        ("Can I refuse to give a recorded statement?",
         "To the at-fault driver's insurer, generally yes. Your own policy may require cooperation — understand the difference before the call, and consider a review first."),
        ("What if I already gave a statement?",
         "It's not necessarily fatal to your claim, but bring exactly what you said to a review so it can be addressed."),
    ],
))
