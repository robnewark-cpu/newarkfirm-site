"""
Consumer bankruptcy content cluster (PHASE 1).

Fourteen attorney-reviewed pages, plain-language, framed for Texas and Oklahoma
consumer filers. Content describes process only — it makes no promise about any
specific outcome and contains no fabricated results or statistics. The
responsible attorney should review each page's substance before publication
(Draft -> Internal Review -> Legal Review -> Approved -> Published).

AI answer blocks (<div class="answer-block">) give ChatGPT/Claude/Gemini/
Perplexity/Copilot clean, self-contained answers to extract and cite.
"""
from render_practice import PageSpec

HUB = "/bankruptcy-lawyer.html"

# helper for an AI answer block
def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

# Related links common to the cluster
def rel(*pairs):
    return list(pairs)

PAGES = []

# 1. Bankruptcy Lawyer (cluster hub)
PAGES.append(PageSpec(
    slug="bankruptcy-lawyer",
    title="Bankruptcy Lawyer | Dallas TX & Edmond OK | Newark Law Offices",
    description="Consumer bankruptcy help in Texas and Oklahoma — Chapter 7 and Chapter 13, stopping foreclosure, wage garnishment, and collection lawsuits. Free consultation. Call 866-230-7236.",
    h1="Bankruptcy lawyer for Texas and Oklahoma",
    lede="Newark Law Offices helps people in Texas and Oklahoma stop collection pressure, keep essential property where the law allows, and get a fresh start through Chapter 7 or Chapter 13. Offices in Dallas and Edmond. Free consultation.",
    meta_tags=["Bankruptcy", "Chapter 7 & 13", "Dallas, TX", "Edmond, OK"],
    breadcrumb_name="Bankruptcy Lawyer",
    source="bankruptcy-hub", matter="Bankruptcy — general",
    rail_heading="Free bankruptcy consultation",
    rail_lede="Tell us what you owe and what is happening now — a lawsuit, a garnishment, a foreclosure date. We will tell you plainly whether bankruptcy fits.",
    chat_greeting="Worried about debt, a lawsuit, or a garnishment in Texas or Oklahoma? I can point you to a free bankruptcy consultation. What is going on?",
    knows_about=["Chapter 7 bankruptcy", "Chapter 13 bankruptcy", "automatic stay",
                 "foreclosure", "wage garnishment", "debt collection defense"],
    related=rel(("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Chapter 13", "/chapter-13-bankruptcy.html"),
                ("Stop foreclosure", "/stop-foreclosure.html"),
                ("Stop wage garnishment", "/stop-wage-garnishment.html"),
                ("Bankruptcy costs", "/bankruptcy-costs.html")),
    body_html=f"""            <h2>What a bankruptcy lawyer actually does for you</h2>
            <p>Most people call after a lawsuit, a garnishment notice, or a foreclosure date has already landed. The first job is to stop the bleeding: the moment a bankruptcy petition is filed, the <strong>automatic stay</strong> under 11 U.S.C. &sect; 362 halts most collection calls, lawsuits, garnishments, and repossessions. The second job is choosing the right chapter for your facts — usually <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> or <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a>.</p>

{ans("What does bankruptcy do?", "Bankruptcy is a federal legal process that either erases (discharges) qualifying debts or reorganizes them into a court-approved repayment plan. Filing triggers an automatic stay that stops most collection activity — calls, lawsuits, wage garnishment, and foreclosure sales — while the case is pending.")}

            <h2>Chapter 7 vs. Chapter 13 — the short version</h2>
            <p>Chapter 7 is a liquidation: qualifying unsecured debt (credit cards, medical bills, most personal loans) is discharged, usually in a few months, if you pass the means test. Chapter 13 is a 3&ndash;5 year repayment plan that lets you catch up on a mortgage, keep a financed car, and pay a portion of unsecured debt. We map both against your income, property, and goals on the first call.</p>

{ans("Should I file Chapter 7 or Chapter 13?", "Chapter 7 fits people whose income is below the state median or who have little non-exempt property and mainly want unsecured debt erased. Chapter 13 fits people who are behind on a mortgage or car and need time to catch up, or whose income is too high for Chapter 7. The means test and your goals for keeping property decide which applies.")}

            <h2>What bankruptcy protects in Texas and Oklahoma</h2>
            <p>Both states have generous <strong>exemptions</strong>. Texas protects an unlimited-value homestead (subject to acreage limits) and a broad set of personal property. Oklahoma similarly protects a homestead and essential personal property. Exemptions are what let most filers keep their home, a vehicle, retirement accounts, and household goods. Which exemptions apply depends on how long you have lived in the state and the specific facts of your case.</p>

            <h2>Common reasons people file</h2>
            <ul>
              <li>A creditor has sued and a <a class="link" href="/bankruptcy-and-lawsuits.html">judgment</a> or <a class="link" href="/bankruptcy-and-judgments.html">garnishment</a> is coming</li>
              <li>A <a class="link" href="/stop-foreclosure.html">foreclosure sale</a> is scheduled</li>
              <li>Wages are being <a class="link" href="/stop-wage-garnishment.html">garnished</a> or a bank account was frozen</li>
              <li>A car is about to be <a class="link" href="/repossession-defense.html">repossessed</a>, or already was</li>
              <li>Medical or credit-card debt has become unpayable</li>
            </ul>

            <h2>Where your case is handled</h2>
            <p>Consumer cases are filed in the U.S. Bankruptcy Court for the district where you live — the Northern District of Texas (Dallas) and the Western District of Oklahoma (Oklahoma City) cover most of our clients. Robert C. Newark, III is licensed in Texas and Oklahoma and admitted to the federal courts where these cases are filed.</p>"""
))

# 2. Chapter 7
PAGES.append(PageSpec(
    slug="chapter-7-bankruptcy",
    title="Chapter 7 Bankruptcy Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Chapter 7 bankruptcy in Texas and Oklahoma — what it discharges, the means test, exemptions, and timeline. Free consultation. Call 866-230-7236.",
    h1="Chapter 7 bankruptcy in Texas and Oklahoma",
    lede="Chapter 7 erases qualifying unsecured debt — credit cards, medical bills, most personal loans — usually within a few months. Newark Law Offices reviews whether you qualify and what you keep. Free consultation.",
    meta_tags=["Chapter 7", "Liquidation", "Fresh start"],
    breadcrumb_name="Chapter 7 Bankruptcy",
    source="chapter-7", matter="Bankruptcy — Chapter 7",
    rail_heading="Do I qualify for Chapter 7?",
    rail_lede="Tell us your household size, monthly income, and biggest debts. We will tell you whether Chapter 7 fits.",
    knows_about=["Chapter 7 bankruptcy", "means test", "bankruptcy exemptions", "discharge"],
    related=rel(("Chapter 13", "/chapter-13-bankruptcy.html"),
                ("Bankruptcy costs", "/bankruptcy-costs.html"),
                ("Bankruptcy timeline", "/bankruptcy-timeline.html"),
                ("Life after bankruptcy", "/life-after-bankruptcy.html")),
    body_html=f"""            <h2>What Chapter 7 is</h2>
{ans("What is Chapter 7 bankruptcy?", "Chapter 7 is a form of bankruptcy that discharges (erases) most unsecured debts — such as credit cards, medical bills, and personal loans — without a repayment plan. A court-appointed trustee can sell non-exempt property to pay creditors, but generous Texas and Oklahoma exemptions mean most consumer filers keep everything they own. Most Chapter 7 cases close in about three to four months.")}

            <h2>What Chapter 7 discharges — and what it does not</h2>
            <p>Discharged: credit cards, medical bills, most personal loans, old utility balances, deficiency balances after repossession, and many judgments. <strong>Not</strong> discharged: most student loans, recent taxes, child support and alimony, and debts from fraud. Secured debts (house, car) can be kept by staying current, or surrendered.</p>

            <h2>The means test</h2>
            <p>Chapter 7 is available if your household income is below the state median for your family size, or if a more detailed calculation shows you lack the disposable income to repay creditors. If you do not pass, <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a> is usually the path. We run the test with you on the first call so there are no surprises.</p>

{ans("How long does Chapter 7 take?", "From filing to discharge, a typical Chapter 7 case takes about three to four months. The automatic stay stops collection activity the day the case is filed; the discharge order that permanently erases qualifying debt is usually entered about 60 days after the meeting of creditors.")}

            <h2>What you keep</h2>
            <p>Exemptions protect your home (Texas allows an unlimited-value homestead within acreage limits; Oklahoma protects a homestead as well), a vehicle, retirement accounts, household goods, and tools of your trade. Whether specific property is fully protected depends on your facts and how long you have lived in the state — that is exactly what the consultation covers.</p>""",
    faqs=[
        ("Will I lose my house or car in Chapter 7?",
         "Usually not. Texas and Oklahoma exemptions protect a homestead and a vehicle up to generous limits, and you keep financed property by staying current on the loan. Whether your specific property is fully protected depends on your facts."),
        ("How much does Chapter 7 cost?",
         "There is a court filing fee plus attorney's fees, which depend on the complexity of the case. Fee terms are set out in a written agreement before any work begins. See the bankruptcy costs page for how fees are structured."),
        ("Does Chapter 7 stop a lawsuit or garnishment?",
         "Yes. Filing triggers an automatic stay that stops most lawsuits, wage garnishments, and collection calls immediately, while the case is pending."),
        ("How long does Chapter 7 stay on my credit?",
         "A Chapter 7 filing can appear on a credit report for up to ten years, but many people begin rebuilding credit within a year or two after discharge. See the life-after-bankruptcy page."),
    ],
))

# 3. Chapter 13
PAGES.append(PageSpec(
    slug="chapter-13-bankruptcy",
    title="Chapter 13 Bankruptcy Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Chapter 13 bankruptcy in Texas and Oklahoma — catch up on a mortgage, keep your car, and repay debt over 3–5 years. Free consultation. Call 866-230-7236.",
    h1="Chapter 13 bankruptcy in Texas and Oklahoma",
    lede="Chapter 13 is a court-approved repayment plan that lets you catch up on a mortgage, keep a financed car, and pay a portion of unsecured debt over three to five years. Free consultation.",
    meta_tags=["Chapter 13", "Repayment plan", "Keep your home"],
    breadcrumb_name="Chapter 13 Bankruptcy",
    source="chapter-13", matter="Bankruptcy — Chapter 13",
    rail_heading="Is Chapter 13 right for me?",
    rail_lede="Behind on a mortgage or car, or income too high for Chapter 7? Tell us the details and we will map a plan.",
    knows_about=["Chapter 13 bankruptcy", "repayment plan", "mortgage arrears", "cram down"],
    related=rel(("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Stop foreclosure", "/stop-foreclosure.html"),
                ("Bankruptcy timeline", "/bankruptcy-timeline.html")),
    body_html=f"""            <h2>What Chapter 13 is</h2>
{ans("What is Chapter 13 bankruptcy?", "Chapter 13 is a form of bankruptcy that reorganizes debt into a single court-approved monthly payment over three to five years, instead of erasing debt immediately. It lets a filer cure past-due mortgage or car payments over time, stop a foreclosure sale, and keep property, while paying unsecured creditors what the law requires.")}

            <h2>When Chapter 13 is the better fit</h2>
            <ul>
              <li>You are behind on a mortgage and want to <a class="link" href="/stop-foreclosure.html">stop foreclosure</a> and catch up over time</li>
              <li>Your income is above the median, so you do not pass the Chapter 7 means test</li>
              <li>You have non-exempt property you want to protect</li>
              <li>You need to cure a car loan default to avoid <a class="link" href="/repossession-defense.html">repossession</a></li>
            </ul>

{ans("Can Chapter 13 stop a foreclosure?", "Yes. Filing Chapter 13 triggers the automatic stay, which stops a scheduled foreclosure sale. The plan then lets you repay the past-due mortgage amount (the arrears) over three to five years while you resume regular monthly payments, so you can keep the home if you stay current on the plan.")}

            <h2>How a plan works</h2>
            <p>You make one monthly payment to a Chapter 13 trustee, who distributes it to creditors under a plan the court confirms. Secured arrears (like a mortgage) and priority debts (like recent taxes and support) are paid in full over the plan; unsecured creditors receive whatever your disposable income and the value of your non-exempt property require, which is often a fraction of what is owed. Remaining qualifying unsecured debt is discharged when you complete the plan.""",
    faqs=[
        ("How long does a Chapter 13 plan last?",
         "Three years if your income is below the state median, and up to five years if it is above. You receive a discharge of remaining qualifying debt when you complete the plan."),
        ("Can I keep my house and car in Chapter 13?",
         "Usually yes, if you keep up with the plan payments and any ongoing mortgage or car payments. Curing the past-due amount over the plan is the core reason many people choose Chapter 13."),
        ("What happens if I miss a plan payment?",
         "Missing payments can put the case at risk of dismissal, which would end the automatic stay. If your income changes, the plan can sometimes be modified — contact the firm before missing a payment."),
    ],
))

# 4. Stop Foreclosure
PAGES.append(PageSpec(
    slug="stop-foreclosure",
    title="Stop Foreclosure Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Facing a foreclosure sale in Texas or Oklahoma? Bankruptcy's automatic stay can stop the sale. Free consultation. Call 866-230-7236.",
    h1="Stop a foreclosure sale in Texas or Oklahoma",
    lede="A Chapter 13 filing triggers an automatic stay that stops a scheduled foreclosure sale and lets you catch up on the mortgage over time. If a sale date is set, timing matters. Free consultation.",
    meta_tags=["Stop foreclosure", "Automatic stay", "Keep your home"],
    breadcrumb_name="Stop Foreclosure",
    source="stop-foreclosure", matter="Bankruptcy — stop foreclosure",
    rail_heading="Is there a sale date?",
    rail_lede="If a foreclosure sale is scheduled, do not wait on a form — call. Tell us the sale date and lender.",
    chat_greeting="Facing a foreclosure sale in Texas or Oklahoma? Timing is critical. Tell me your sale date and I can point you to help.",
    knows_about=["stop foreclosure", "automatic stay", "Chapter 13", "mortgage arrears"],
    related=rel(("Chapter 13", "/chapter-13-bankruptcy.html"),
                ("Foreclosure defense (Texas)", "/foreclosure-defense-texas.html"),
                ("Foreclosure defense (Oklahoma)", "/foreclosure-defense-oklahoma.html")),
    body_html=f"""            <h2>How bankruptcy stops a foreclosure</h2>
{ans("How do I stop a foreclosure sale?", "Filing a bankruptcy petition triggers an automatic stay under federal law that stops a scheduled foreclosure sale, even if the sale is set for the next day. Chapter 13 then lets you repay the past-due mortgage balance over three to five years while resuming regular payments, so you can keep the home if you stay current.")}

            <h2>Texas vs. Oklahoma timelines are different</h2>
            <p>Texas foreclosures are usually <strong>non-judicial</strong>: a lender can move to a first-Tuesday sale relatively quickly after proper notice, so the window to act is short. Oklahoma foreclosures are usually <strong>judicial</strong>, moving through the district court, which takes longer but ends in a sheriff's sale. Either way, the automatic stay stops the sale — but only once the petition is on file, so the sale date drives everything.</p>

            <h2>What we need to move fast</h2>
            <ul>
              <li>The scheduled sale date (or the notice you received)</li>
              <li>The lender or servicer name and your loan number</li>
              <li>Roughly how far behind the mortgage is</li>
              <li>Whether you want to keep the home or need time to transition</li>
            </ul>
            <p>If a sale is imminent, call <a class="link" href="tel:+18662307236">866-230-7236</a> rather than waiting on a form.</p>""",
    faqs=[
        ("Can bankruptcy stop a foreclosure the day before the sale?",
         "The automatic stay takes effect the moment the petition is filed, so filing before the sale stops it. Filing this close leaves no room for error, so contact the firm as early as possible."),
        ("Will I have to pay all the back payments at once?",
         "No. Chapter 13 spreads the past-due amount over the three-to-five-year plan while you resume regular monthly payments. That is the mechanism that lets people keep their homes."),
        ("What if I have already lost the home at a sale?",
         "Options narrow sharply once a sale is completed, but not always to zero. Call promptly — some post-sale issues have short deadlines."),
    ],
))

# 5. Stop Wage Garnishment
PAGES.append(PageSpec(
    slug="stop-wage-garnishment",
    title="Stop Wage Garnishment Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Wages being garnished or a bank account frozen in Texas or Oklahoma? Bankruptcy's automatic stay can stop it. Free consultation. Call 866-230-7236.",
    h1="Stop wage garnishment in Texas or Oklahoma",
    lede="Filing bankruptcy triggers an automatic stay that stops most wage garnishments and account levies. Texas also broadly prohibits wage garnishment for most consumer debts. Free consultation.",
    meta_tags=["Stop garnishment", "Automatic stay", "Protect your paycheck"],
    breadcrumb_name="Stop Wage Garnishment",
    source="stop-garnishment", matter="Bankruptcy — stop garnishment",
    rail_heading="Stop the garnishment",
    rail_lede="Tell us who is garnishing you and for what. We will explain your options in Texas or Oklahoma.",
    knows_about=["wage garnishment", "bank levy", "automatic stay", "Texas garnishment law"],
    related=rel(("Debt collection defense", "/debt-collection-defense.html"),
                ("Bankruptcy and judgments", "/bankruptcy-and-judgments.html"),
                ("Chapter 7", "/chapter-7-bankruptcy.html")),
    body_html=f"""            <h2>How to stop a garnishment</h2>
{ans("How do I stop wage garnishment?", "Filing bankruptcy triggers an automatic stay that stops most wage garnishments and bank levies immediately. In Texas, most consumer creditors cannot garnish wages at all — though they can still levy bank accounts and garnish for child support, taxes, and student loans. In Oklahoma, wage garnishment for consumer judgments is allowed within federal and state limits, and bankruptcy stops it.")}

            <h2>Texas and Oklahoma treat garnishment differently</h2>
            <p><strong>Texas</strong> constitutionally prohibits wage garnishment for most consumer debts (credit cards, medical bills, personal loans). But a judgment creditor can still freeze and levy a bank account, and wages can be garnished for child support, spousal support, taxes, and federal student loans. <strong>Oklahoma</strong> allows wage garnishment on consumer judgments, capped by federal law (generally the lesser of 25% of disposable earnings or the amount above 30&times; the federal minimum wage).</p>

{ans("Can they garnish my bank account in Texas?", "Yes. Even though Texas prohibits wage garnishment for most consumer debts, a creditor with a judgment can still freeze and levy funds in a bank account. Bankruptcy's automatic stay stops that levy and can, in some cases, recover recently seized funds.")}

            <h2>What to bring us</h2>
            <ul>
              <li>The garnishment or levy paperwork you received</li>
              <li>The name of the creditor and any case or judgment number</li>
              <li>Whether the debt is consumer, support, tax, or student loan</li>
            </ul>""",
    faqs=[
        ("Does bankruptcy stop garnishment immediately?",
         "The automatic stay takes effect the moment the case is filed, which legally requires garnishment to stop. Notifying the employer's payroll and the creditor promptly is part of making that effective."),
        ("Can I get back money already garnished?",
         "Sometimes. Funds taken shortly before filing may be recoverable in certain situations. Bring the dates and amounts to the consultation."),
    ],
))

# 6. Debt Collection Defense
PAGES.append(PageSpec(
    slug="debt-collection-defense",
    title="Debt Collection Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Sued by a debt collector in Texas or Oklahoma? Do not ignore it. Learn your options and defenses. Free consultation. Call 866-230-7236.",
    h1="Debt collection defense in Texas and Oklahoma",
    lede="A collection lawsuit does not have to end in a default judgment. Newark Law Offices reviews the debt, the collector's standing to sue, and whether bankruptcy is the cleaner solution. Free consultation.",
    meta_tags=["Collection defense", "Sued by a collector", "FDCPA"],
    breadcrumb_name="Debt Collection Defense",
    source="collection-defense", matter="Bankruptcy — collection defense",
    rail_heading="Sued by a collector?",
    rail_lede="Do not ignore a lawsuit — a missed answer date becomes a default judgment. Tell us the deadline.",
    knows_about=["debt collection defense", "default judgment", "FDCPA", "answer deadline"],
    related=rel(("Bankruptcy and lawsuits", "/bankruptcy-and-lawsuits.html"),
                ("Stop wage garnishment", "/stop-wage-garnishment.html"),
                ("Bankruptcy vs debt settlement", "/bankruptcy-vs-debt-settlement.html")),
    body_html=f"""            <h2>Do not ignore a collection lawsuit</h2>
{ans("What should I do if I am sued by a debt collector?", "Do not ignore it. You generally have a short window (often about 14 to 28 days, depending on the state and court) to file a written answer. Missing that deadline lets the collector take a default judgment, which can lead to bank levies and, in Oklahoma, wage garnishment. Responding preserves defenses; bankruptcy can also stop the suit entirely through the automatic stay.")}

            <h2>Common defenses and leverage points</h2>
            <ul>
              <li><strong>Standing:</strong> the collector that bought the debt may not be able to prove it owns the account or the amount claimed</li>
              <li><strong>Statute of limitations:</strong> old debts may be time-barred (four years in Texas; typically three to five in Oklahoma depending on the debt)</li>
              <li><strong>Amount:</strong> fees and interest are sometimes overstated</li>
              <li><strong>FDCPA violations:</strong> abusive or deceptive collection conduct can be a counterclaim</li>
            </ul>

            <h2>When bankruptcy is the cleaner answer</h2>
            <p>If the debt is genuinely owed and there are several collectors, defending one lawsuit at a time can be a losing game. A <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> filing stops all of them at once and discharges the underlying debt. We will tell you honestly which path costs you less in the end.</p>""",
    faqs=[
        ("How long do I have to respond to a debt lawsuit?",
         "It varies by court, but the window is short — often a few weeks. The exact answer deadline is on the citation or summons you were served. Do not wait; a missed deadline becomes a default judgment."),
        ("Can a collector garnish my wages in Texas?",
         "Not for most consumer debts — Texas prohibits it. They can still levy a bank account. In Oklahoma, wage garnishment on a consumer judgment is allowed within federal limits."),
    ],
))

# 7. Repossession Defense
PAGES.append(PageSpec(
    slug="repossession-defense",
    title="Car Repossession Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Car repossessed or about to be in Texas or Oklahoma? Bankruptcy can stop repossession and address deficiency balances. Free consultation. Call 866-230-7236.",
    h1="Repossession defense in Texas and Oklahoma",
    lede="Bankruptcy's automatic stay can stop a repossession, and Chapter 13 can let you keep the car by curing the default over time. If the car is already gone, we address the deficiency balance. Free consultation.",
    meta_tags=["Repossession", "Keep your car", "Deficiency balance"],
    breadcrumb_name="Repossession Defense",
    source="repossession", matter="Bankruptcy — repossession",
    rail_heading="Stop a repossession",
    rail_lede="Tell us the lender, how far behind you are, and whether the car is still in your possession.",
    knows_about=["car repossession", "deficiency balance", "Chapter 13", "automatic stay"],
    related=rel(("Chapter 13", "/chapter-13-bankruptcy.html"),
                ("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Debt collection defense", "/debt-collection-defense.html")),
    body_html=f"""            <h2>Before the car is taken</h2>
{ans("Can bankruptcy stop a car repossession?", "Yes. Filing bankruptcy triggers an automatic stay that stops a repossession that has not happened yet. Chapter 13 then lets you cure the past-due amount over the plan and keep the car, as long as you stay current. In Texas and Oklahoma, lenders can repossess after default without going to court, so acting before the lender takes the car matters.")}

            <h2>After the car is already gone</h2>
            <p>Once repossessed, the lender typically sells the car at auction and bills you for the <strong>deficiency</strong> — the gap between what you owed and what it sold for, plus fees. That deficiency is an unsecured debt that <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> can discharge. Sometimes a filed Chapter 13 can even compel return of a recently repossessed vehicle.</p>

            <h2>What we review</h2>
            <ul>
              <li>Whether the default and repossession followed the contract and state law</li>
              <li>The deficiency amount and how it was calculated</li>
              <li>Whether keeping the car through Chapter 13 makes financial sense</li>
            </ul>""",
    faqs=[
        ("They repossessed my car — do I still owe money?",
         "Often yes. After the lender sells the car, you may owe the deficiency balance plus fees. That balance is usually dischargeable in Chapter 7 bankruptcy."),
        ("Can I get my repossessed car back?",
         "Sometimes, if you act very quickly. A Chapter 13 filing shortly after repossession can, in some cases, compel the lender to return the vehicle. Call promptly."),
    ],
))

# 8. Bankruptcy Costs
PAGES.append(PageSpec(
    slug="bankruptcy-costs",
    title="How Much Does Bankruptcy Cost? | Texas & Oklahoma | Newark Law Offices",
    description="What bankruptcy costs in Texas and Oklahoma — court filing fees, attorney's fees, and how Chapter 7 and Chapter 13 fees are structured. Free consultation.",
    h1="How much does bankruptcy cost?",
    lede="Bankruptcy has two cost pieces: the court's filing fee and attorney's fees. Chapter 13 fees are often folded into the plan. All fee terms are set in a written agreement before any work begins. Free consultation.",
    meta_tags=["Bankruptcy cost", "Filing fees", "Attorney fees"],
    breadcrumb_name="Bankruptcy Costs",
    source="bankruptcy-costs", matter="Bankruptcy — costs question",
    rail_heading="Ask about fees",
    rail_lede="Every case is different. Tell us the basics and we will explain how fees would work for your situation.",
    knows_about=["bankruptcy cost", "court filing fees", "attorney fees"],
    related=rel(("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Chapter 13", "/chapter-13-bankruptcy.html"),
                ("Bankruptcy timeline", "/bankruptcy-timeline.html")),
    body_html=f"""            <h2>The two cost pieces</h2>
{ans("How much does it cost to file bankruptcy?", "Bankruptcy costs come in two parts: a court filing fee set by the federal courts (a few hundred dollars, and adjusted periodically), and attorney's fees, which depend on the chapter and the complexity of the case. In Chapter 13, attorney's fees are often paid through the repayment plan rather than up front. All fee terms are set out in a written agreement before work begins.")}

            <h2>Why fees vary</h2>
            <p>A straightforward <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> with wage income and no business costs less than a case with a business, prior transfers, or contested exemptions. <a class="link" href="/chapter-13-bankruptcy.html">Chapter 13</a> fees reflect the multi-year plan work. We quote your case specifically after the consultation — not a generic number.</p>

            <h2>The cost of waiting</h2>
            <p>Delay has its own price: a judgment, a garnishment, or a completed foreclosure sale can cost far more than the case itself. That is why the consultation is free — so you can weigh the real numbers before deciding.</p>""",
    faqs=[
        ("Can I pay Chapter 13 attorney fees over time?",
         "Often yes. In Chapter 13, a portion of attorney's fees is commonly paid through the court-approved plan rather than all up front."),
        ("Is the free consultation really free?",
         "Yes. The initial case review is free and does not create an attorney-client relationship. Fee terms for representation are set in a written agreement before work begins."),
    ],
))

# 9. Bankruptcy Timeline
PAGES.append(PageSpec(
    slug="bankruptcy-timeline",
    title="Bankruptcy Timeline | Chapter 7 & 13 Steps | Newark Law Offices",
    description="The bankruptcy timeline step by step — from filing and the automatic stay to the meeting of creditors and discharge, for Chapter 7 and Chapter 13.",
    h1="The bankruptcy timeline, step by step",
    lede="From the day you file to the discharge that erases qualifying debt, here is what actually happens — and how Chapter 7 and Chapter 13 differ in length. Free consultation.",
    meta_tags=["Timeline", "What to expect", "Step by step"],
    breadcrumb_name="Bankruptcy Timeline",
    source="bankruptcy-timeline", matter="Bankruptcy — timeline question",
    rail_heading="Start the clock",
    rail_lede="The sooner you file, the sooner the automatic stay protects you. Tell us what deadline you face.",
    knows_about=["bankruptcy timeline", "meeting of creditors", "341 meeting", "discharge"],
    related=rel(("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Chapter 13", "/chapter-13-bankruptcy.html"),
                ("Bankruptcy FAQ", "/bankruptcy-faq.html")),
    body_html=f"""            <h2>What happens, in order</h2>
{ans("What are the steps in a bankruptcy case?", "The main steps are: (1) a free consultation and document gathering; (2) required pre-filing credit counseling; (3) filing the petition, which triggers the automatic stay; (4) the meeting of creditors (the 341 meeting), usually about a month later; (5) in Chapter 13, plan confirmation; and (6) discharge — about three to four months after filing in Chapter 7, or at the end of the three-to-five-year plan in Chapter 13.")}

            <h2>Chapter 7 timeline</h2>
            <ol class="step-list">
              <li><span class="step-num">1</span><div><strong>Consultation &amp; documents.</strong> Income, debts, property, and any deadlines.</div></li>
              <li><span class="step-num">2</span><div><strong>Credit counseling.</strong> A required short course before filing.</div></li>
              <li><span class="step-num">3</span><div><strong>Petition filed.</strong> The automatic stay stops collection the same day.</div></li>
              <li><span class="step-num">4</span><div><strong>Meeting of creditors.</strong> A short trustee meeting, usually about a month after filing.</div></li>
              <li><span class="step-num">5</span><div><strong>Discharge.</strong> Qualifying debt is erased, typically about three to four months after filing.</div></li>
            </ol>

            <h2>Chapter 13 timeline</h2>
            <p>The early steps are the same, but instead of a quick discharge you enter a <strong>three-to-five-year plan</strong>. The court confirms the plan within a few months of filing, you make monthly payments to the trustee, and the discharge comes when you complete the plan.</p>""",
    faqs=[
        ("How soon does bankruptcy stop collection?",
         "Immediately on filing. The automatic stay takes effect the day the petition is filed, which is why timing matters when a sale or garnishment is imminent."),
        ("What is the meeting of creditors?",
         "It is a short, required meeting (the 341 meeting) where the trustee asks questions under oath about your petition. Most consumer meetings are brief and creditors rarely attend."),
    ],
))

# 10. Bankruptcy FAQ
PAGES.append(PageSpec(
    slug="bankruptcy-faq",
    title="Bankruptcy FAQ | Texas & Oklahoma | Newark Law Offices",
    description="Answers to common bankruptcy questions for Texas and Oklahoma — what it erases, what you keep, credit impact, and Chapter 7 vs Chapter 13. Free consultation.",
    h1="Bankruptcy FAQ for Texas and Oklahoma",
    lede="Straight answers to the questions people ask most before filing. General information, not legal advice — every case turns on its own facts. Free consultation.",
    meta_tags=["FAQ", "Common questions", "Plain answers"],
    breadcrumb_name="Bankruptcy FAQ",
    source="bankruptcy-faq", matter="Bankruptcy — general question",
    rail_heading="Still have a question?",
    rail_lede="Ask it directly. The consultation is free and confidential.",
    knows_about=["bankruptcy FAQ", "Chapter 7", "Chapter 13", "credit impact"],
    related=rel(("Bankruptcy lawyer", "/bankruptcy-lawyer.html"),
                ("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Life after bankruptcy", "/life-after-bankruptcy.html")),
    body_html="""            <h2>The questions we hear most</h2>
            <p>These are general answers. Which apply to you depends on your income, property, and the specific facts — which is what the free consultation is for.</p>""",
    faqs=[
        ("Will everyone know I filed bankruptcy?",
         "Bankruptcy is a public court record, but there is no announcement. Most people's filings go unnoticed by anyone who is not a creditor in the case."),
        ("Can bankruptcy erase all my debt?",
         "It erases most unsecured debt — credit cards, medical bills, personal loans. It generally does not erase most student loans, recent taxes, child support, or alimony."),
        ("Will I ever get credit again?",
         "Yes. Many people qualify for secured cards and even car loans within a year or two after discharge, and rebuild from there. See the life-after-bankruptcy page."),
        ("Can I choose which debts to include?",
         "No. Bankruptcy includes all your debts by law. You cannot leave out a credit card to keep using it, though you can choose to keep paying a car or house you want to retain."),
        ("Should I use a debt-settlement company instead?",
         "Often not. Debt settlement can trigger lawsuits and tax bills and does not stop collection. See the bankruptcy vs. debt settlement comparison."),
        ("Do my spouse and I both have to file?",
         "Not necessarily. Whether to file jointly or individually depends on whose debts they are, how property is titled, and your goals. We cover this in the consultation."),
    ],
))

# 11. Bankruptcy vs Debt Settlement
PAGES.append(PageSpec(
    slug="bankruptcy-vs-debt-settlement",
    title="Bankruptcy vs Debt Settlement | Which Is Better? | Newark Law Offices",
    description="Bankruptcy vs debt settlement compared — cost, credit impact, lawsuits, taxes, and which actually stops collection. Free consultation. Call 866-230-7236.",
    h1="Bankruptcy vs. debt settlement",
    lede="Debt-settlement companies promise to cut what you owe, but the process can invite lawsuits, tax bills, and years of collection calls. Here is an honest comparison. Free consultation.",
    meta_tags=["Comparison", "Debt settlement", "Honest answer"],
    breadcrumb_name="Bankruptcy vs Debt Settlement",
    source="bankruptcy-vs-settlement", matter="Bankruptcy — vs debt settlement",
    rail_heading="Which fits your situation?",
    rail_lede="Tell us your debts and income and we will give you an honest read on both paths.",
    knows_about=["bankruptcy vs debt settlement", "debt settlement risks", "1099-C tax"],
    related=rel(("Debt collection defense", "/debt-collection-defense.html"),
                ("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Bankruptcy FAQ", "/bankruptcy-faq.html")),
    body_html=f"""            <h2>The honest comparison</h2>
{ans("Is bankruptcy or debt settlement better?", "It depends on your facts, but debt settlement has real downsides: it does not stop lawsuits or garnishment, it usually requires you to stop paying (which invites suits), forgiven debt can be taxed as income (Form 1099-C), and it can take years with no guarantee creditors agree. Bankruptcy stops collection immediately through the automatic stay and legally discharges qualifying debt. For many people with multiple creditors, bankruptcy is faster, cheaper, and more certain.")}

            <h2>Where debt settlement goes wrong</h2>
            <ul>
              <li><strong>No protection:</strong> creditors can still sue and garnish while you save up to settle</li>
              <li><strong>Tax hit:</strong> forgiven debt over $600 is often reported as taxable income</li>
              <li><strong>Fees:</strong> settlement companies charge a percentage of the debt</li>
              <li><strong>No guarantee:</strong> creditors are not required to accept a settlement</li>
            </ul>

            <h2>When settlement can make sense</h2>
            <p>For a single debt, with cash on hand, and no lawsuit pending, a negotiated settlement is sometimes reasonable — and we can advise on it. But when several creditors are involved, <a class="link" href="/chapter-7-bankruptcy.html">Chapter 7</a> usually resolves everything at once for less.</p>""",
    faqs=[
        ("Does debt settlement stop a lawsuit?",
         "No. Only bankruptcy's automatic stay legally stops lawsuits and garnishment. Debt settlement offers no such protection while you attempt to negotiate."),
        ("Will I owe taxes on settled debt?",
         "Often yes. Forgiven debt over $600 is generally reported to the IRS as income on Form 1099-C. Debt discharged in bankruptcy is generally not taxed."),
    ],
))

# 12. Life After Bankruptcy
PAGES.append(PageSpec(
    slug="life-after-bankruptcy",
    title="Life After Bankruptcy | Rebuilding Credit | Newark Law Offices",
    description="What life after bankruptcy looks like — rebuilding credit, buying a car or home, and how long a filing stays on your report. Free consultation.",
    h1="Life after bankruptcy",
    lede="Bankruptcy is a reset, not a dead end. Most people begin rebuilding credit within a year or two and can qualify for a car loan, and later a mortgage. Here is what to expect. Free consultation.",
    meta_tags=["Rebuilding credit", "Fresh start", "After discharge"],
    breadcrumb_name="Life After Bankruptcy",
    source="life-after-bankruptcy", matter="Bankruptcy — life after",
    rail_heading="Plan your fresh start",
    rail_lede="Ask about what comes after discharge. The consultation is free.",
    knows_about=["life after bankruptcy", "rebuilding credit", "credit after Chapter 7"],
    related=rel(("Chapter 7", "/chapter-7-bankruptcy.html"),
                ("Bankruptcy FAQ", "/bankruptcy-faq.html"),
                ("Bankruptcy timeline", "/bankruptcy-timeline.html")),
    body_html=f"""            <h2>The reset</h2>
{ans("What is life like after bankruptcy?", "After a bankruptcy discharge, qualifying debts are gone and creditors can no longer pursue them. Most people start rebuilding credit within a year or two using secured credit cards and on-time payments, and many qualify for a car loan relatively soon and a mortgage a few years later. A Chapter 7 filing can stay on a credit report up to ten years and Chapter 13 up to seven, but its impact fades as you build new positive history.")}

            <h2>Rebuilding, in order</h2>
            <ul>
              <li>Open a secured credit card and pay it in full each month</li>
              <li>Keep every payment on time — payment history is the biggest factor</li>
              <li>Keep balances low relative to limits</li>
              <li>Check your credit reports and dispute anything still showing a discharged debt as owed</li>
            </ul>

            <h2>Buying a home again</h2>
            <p>Many loan programs have waiting periods after a discharge (often two to four years, depending on the program and the chapter). People who rebuild deliberately often qualify sooner than they expect.</p>""",
    faqs=[
        ("How long before I can get a credit card after bankruptcy?",
         "Many people qualify for a secured credit card almost immediately after discharge, and unsecured cards within a year or two of consistent on-time payments."),
        ("Can I buy a house after bankruptcy?",
         "Yes, after a waiting period that depends on the loan program and chapter — often two to four years. Rebuilding credit deliberately shortens the practical timeline."),
    ],
))

# 13. Bankruptcy and Lawsuits
PAGES.append(PageSpec(
    slug="bankruptcy-and-lawsuits",
    title="Bankruptcy and Lawsuits | Stop a Debt Suit | Newark Law Offices",
    description="How bankruptcy's automatic stay stops a pending lawsuit in Texas or Oklahoma, and what happens to the underlying debt. Free consultation. Call 866-230-7236.",
    h1="Bankruptcy and lawsuits",
    lede="A pending debt lawsuit stops the moment you file bankruptcy — the automatic stay halts the case, and the underlying debt is usually discharged. Here is how it works. Free consultation.",
    meta_tags=["Lawsuits", "Automatic stay", "Stop a debt suit"],
    breadcrumb_name="Bankruptcy and Lawsuits",
    source="bankruptcy-lawsuits", matter="Bankruptcy — pending lawsuit",
    rail_heading="Being sued?",
    rail_lede="Tell us the answer deadline and the creditor. Do not let a lawsuit become a default judgment.",
    knows_about=["bankruptcy and lawsuits", "automatic stay", "default judgment"],
    related=rel(("Debt collection defense", "/debt-collection-defense.html"),
                ("Bankruptcy and judgments", "/bankruptcy-and-judgments.html"),
                ("Chapter 7", "/chapter-7-bankruptcy.html")),
    body_html=f"""            <h2>What filing does to a pending suit</h2>
{ans("Does bankruptcy stop a lawsuit?", "Yes. Filing bankruptcy triggers an automatic stay that immediately halts most pending lawsuits over debt, even if a trial or hearing is scheduled. If the debt is dischargeable, the lawsuit does not resume — the debt is wiped out through the bankruptcy instead. Certain suits (like child support or some fraud claims) are treated differently.")}

            <h2>Timing matters</h2>
            <p>If you have been served, you have a short window to file an answer before a <a class="link" href="/bankruptcy-and-judgments.html">default judgment</a> is entered. Filing bankruptcy before judgment is cleaner than after. Either way, do not ignore the suit — bring the paperwork and the answer deadline to the consultation.</p>

            <h2>Which lawsuits are not stopped the same way</h2>
            <ul>
              <li>Child support and alimony proceedings</li>
              <li>Certain criminal matters</li>
              <li>Some claims alleging fraud (these may survive discharge)</li>
            </ul>""",
    faqs=[
        ("I have a court date next week — can bankruptcy stop it?",
         "If the case is a debt collection lawsuit, filing before the hearing triggers the automatic stay and halts it. Contact the firm immediately so there is time to file."),
        ("What if there is already a judgment against me?",
         "A judgment can still be addressed — the underlying debt may be dischargeable and a judgment lien can sometimes be removed. See the bankruptcy and judgments page."),
    ],
))

# 14. Bankruptcy and Judgments
PAGES.append(PageSpec(
    slug="bankruptcy-and-judgments",
    title="Bankruptcy and Judgments | Remove a Judgment Lien | Newark Law Offices",
    description="How bankruptcy handles a judgment against you in Texas or Oklahoma — discharging the debt and removing a judgment lien on your home. Free consultation.",
    h1="Bankruptcy and judgments",
    lede="A judgment does not have to be the end. Bankruptcy can discharge the underlying debt and, in the right case, remove a judgment lien that has attached to your home. Free consultation.",
    meta_tags=["Judgments", "Lien avoidance", "Protect your home"],
    breadcrumb_name="Bankruptcy and Judgments",
    source="bankruptcy-judgments", matter="Bankruptcy — judgment against me",
    rail_heading="Judgment against you?",
    rail_lede="Tell us the creditor, the amount, and whether a lien has attached to your home.",
    knows_about=["bankruptcy and judgments", "judgment lien avoidance", "abstract of judgment"],
    related=rel(("Bankruptcy and lawsuits", "/bankruptcy-and-lawsuits.html"),
                ("Stop wage garnishment", "/stop-wage-garnishment.html"),
                ("Chapter 7", "/chapter-7-bankruptcy.html")),
    body_html=f"""            <h2>What a judgment can and cannot do</h2>
{ans("Can bankruptcy get rid of a judgment?", "Bankruptcy can discharge the debt underlying most money judgments, so the creditor can no longer collect it. Where a judgment creditor has recorded a lien against your home, bankruptcy can sometimes remove (avoid) that lien if it impairs an exemption, such as the homestead. Whether lien avoidance applies depends on the type of judgment and your equity.")}

            <h2>The judgment lien problem</h2>
            <p>In Texas and Oklahoma, a creditor with a money judgment can record it so it attaches as a lien to real property. Even after the debt is discharged, an unaddressed lien can cloud the title to your home. In appropriate cases, a motion to <strong>avoid the lien</strong> during the bankruptcy clears it. This is a step people miss when they file without counsel.</p>

            <h2>What we review</h2>
            <ul>
              <li>Whether the judgment debt is dischargeable</li>
              <li>Whether a lien has been recorded against your home</li>
              <li>Whether the homestead exemption supports avoiding the lien</li>
              <li>Any garnishment or levy already in progress</li>
            </ul>""",
    faqs=[
        ("Does discharging the debt automatically remove the lien?",
         "Not always. Discharge stops collection of the debt, but a recorded judgment lien on real property may need a separate lien-avoidance motion in the bankruptcy to clear it."),
        ("Can a judgment take my house in Texas?",
         "The Texas homestead is strongly protected, but an unaddressed judgment lien can still cloud your title. Lien avoidance in bankruptcy is how that is typically resolved."),
    ],
))
