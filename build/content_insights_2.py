"""Insights articles batch 2 — criminal, immigration, crimigration, local (6-10).

Publish-ready, plain-language, TX/OK-framed. General legal information only —
no fabricated facts, statistics, or outcomes. Approval workflow before publish.
"""
from render_article import Article

def a(q, ans):
    return (f'        <div class="answer-block">\n'
            f'          <h3 class="answer-q">{q}</h3>\n'
            f'          <div class="answer-a">{ans}</div>\n'
            f'        </div>')

ARTICLES = []

# 6. Arrested in Dallas
ARTICLES.append(Article(
    slug="arrested-in-dallas-your-rights-first-24-hours",
    title="Arrested in Dallas? Your Rights in the First 24 Hours | Newark Law Offices",
    description="Just arrested in Dallas or the Metroplex? What you do in the first 24 hours matters. Your rights, talking to police, and bond — plain language.",
    h1="Arrested in Dallas? Your rights in the first 24 hours",
    dek="The first day shapes the whole case. Here's what protects you — and what quietly hurts you.",
    cta_practice=("Talk to a criminal defense lawyer — free & confidential", "/criminal-defense-lawyer.html"),
    knows_about=["arrested Dallas", "right to remain silent", "bond", "criminal defense"],
    related=[("Criminal defense lawyer", "/criminal-defense-lawyer.html"),
             ("Criminal defense FAQ", "/criminal-defense-faq.html"), ("Dallas", "/dallas.html")],
    body_html=f"""{a("What should I do in the first 24 hours after an arrest?", "Use your right to remain silent and your right to a lawyer — say you want an attorney and stop answering questions. Do not consent to searches, do not explain your side to police, and do not discuss the case on a recorded jail phone line. Write down everything you remember. Contact a criminal defense lawyer as soon as possible, because early steps — bond, preserving evidence, contacting witnesses — shape the entire case.")}
        <h2>Silence is a right, not an admission</h2>
        <p>Police are trained to get statements. You have the constitutional right to remain silent and to counsel — and using them cannot be held against you. Politely say: "I want a lawyer, and I'm not answering questions." Then stop.</p>
        <h2>Don't consent to searches</h2>
        <p>You can decline to consent to a search of your car, phone, or home. If police search anyway, that's for your lawyer to challenge later — but consenting waives the issue.</p>
        <h2>The jail phone is recorded</h2>
        <p>Calls from jail (except to your attorney) are recorded and routinely used by prosecutors. Don't discuss the facts of your case with anyone but your lawyer.</p>
        <h2>Bond</h2>
        <p>In Dallas County, criminal cases run through the Frank Crowley Courts Building. A lawyer can request a bond or bond reduction and argue the relevant factors so you're not sitting longer than necessary.</p>
        <h2>Why early matters</h2>
        <p>Evidence disappears, witnesses forget, and early decisions (what to say, whether to consent) are hard to undo. The first call to a lawyer is the highest-leverage thing you can do. If you're not a U.S. citizen, this is doubly true — see <a class="link" href="/crimigration-immigration-consequences.html">crimigration</a>.</p>""",
    faqs=[
        ("Should I explain my side to clear things up?",
         "No. Anything you say can be used against you. Ask for a lawyer and stay silent — you can always tell your side later, through counsel, when it helps you."),
        ("Do I need a lawyer for a misdemeanor?",
         "Yes, it's worth a consultation. Even a misdemeanor can carry a record, fines, and license or immigration consequences, and early options can be lost without advice."),
    ],
))

# 7. Expungement vs sealing
ARTICLES.append(Article(
    slug="expungement-vs-sealing-texas-oklahoma",
    title="Can I Get a Charge Off My Record? Expungement vs. Sealing | Newark Law Offices",
    description="Expungement vs. record sealing (nondisclosure) in Texas and Oklahoma — what each does, who qualifies, and how to clear an old charge from background checks.",
    h1="Can I get a charge off my record? Expungement vs. sealing",
    dek="An old arrest can follow you into every job application. Two different tools can clear it — here's which is which.",
    cta_practice=("See if you qualify — free consultation", "/expungement.html"),
    knows_about=["expungement", "record sealing", "nondisclosure", "clear criminal record"],
    related=[("Expungement", "/expungement.html"), ("Record sealing", "/record-sealing.html"),
             ("Criminal defense lawyer", "/criminal-defense-lawyer.html")],
    body_html=f"""{a("What's the difference between expungement and record sealing?", "Expungement (called expunction in Texas) removes or destroys the record so it no longer appears on most background checks. Record sealing — an order of nondisclosure in Texas — hides the record from most public background checks but still lets certain government and licensing agencies see it. Eligibility for each depends on the outcome of the case, the offense, and waiting periods under Texas or Oklahoma law.")}
        <h2>Why it matters</h2>
        <p>Employers, landlords, and licensing boards run background checks. A dismissed charge or old arrest can still surface and cost you a job — even if you were never convicted. Clearing it lets you honestly answer "no."</p>
        <h2>Expungement (expunction in Texas)</h2>
        <p>Generally destroys or removes the record. In Texas, expunction is typically available for arrests that did <em>not</em> lead to conviction — dismissals, acquittals, no-bills — after applicable waiting periods. Oklahoma has its own expungement categories.</p>
        <h2>Sealing / nondisclosure</h2>
        <p>Hides the record from most public view but not from all government/licensing access. In Texas this is an <strong>order of nondisclosure</strong>, often available after successfully completing deferred adjudication and a waiting period.</p>
        <h2>Which applies to you</h2>
        <p>It turns on how your case ended (dismissal vs. deferred vs. conviction), the specific offense, and time elapsed. A record review is the only way to know for sure — and it's what the free consultation covers. See <a class="link" href="/expungement.html">expungement</a> and <a class="link" href="/record-sealing.html">record sealing</a>.</p>""",
    faqs=[
        ("Can I expunge a dismissed charge in Texas?",
         "Often yes. Texas expunction is generally available for arrests that didn't result in conviction, subject to waiting periods. A record review confirms eligibility."),
        ("Who can still see a sealed record?",
         "Sealing hides a record from most public background checks, but certain law-enforcement, government, and licensing agencies may still access it."),
    ],
))

# 8. Crimigration
ARTICLES.append(Article(
    slug="crimigration-guilty-plea-deportation",
    title="Crimigration: How a Guilty Plea Can Get a Non-Citizen Deported | Newark Law Offices",
    description="For non-citizens, a criminal plea can trigger deportation even when the criminal penalty is minor. Here's the crimigration trap and how to avoid it.",
    h1="Crimigration: how a guilty plea can trigger deportation",
    dek="A plea that looks like a win in criminal court can be a one-way ticket out of the country. Most people never see it coming.",
    cta_practice=("Talk to a firm that handles both — free consultation", "/crimigration-immigration-consequences.html"),
    knows_about=["crimigration", "immigration consequences of crimes", "deportable offense", "Padilla"],
    related=[("Crimigration", "/crimigration-immigration-consequences.html"),
             ("Criminal defense", "/criminal-defense-lawyer.html"),
             ("Immigration & removal defense", "/immigration-lawyer.html")],
    body_html=f"""{a("Can a guilty plea get a non-citizen deported?", "Yes. For a non-citizen, a criminal conviction — and sometimes just a plea — can trigger deportation, make you inadmissible, or bar relief like cancellation of removal or naturalization, even when the criminal penalty itself is minor. Certain offenses (aggravated felonies and crimes involving moral turpitude, including some drug and theft offenses) carry the harshest immigration consequences. The U.S. Supreme Court held in Padilla v. Kentucky that defense counsel must advise a non-citizen of a plea's immigration consequences.")}
        <h2>The trap</h2>
        <p>A criminal defense lawyer's job is the best criminal outcome — probation, a reduced charge, deferred adjudication. But under immigration law, that "good" plea can be a <strong>deportable offense</strong>. The two systems don't talk to each other, and a lawyer who handles only the criminal side may not see the immigration cliff.</p>
        <h2>What triggers it</h2>
        <ul>
          <li><strong>Crimes involving moral turpitude</strong> — including some theft and fraud offenses.</li>
          <li><strong>Aggravated felonies</strong> — a broad immigration category that can include offenses that aren't "aggravated" or "felonies" in ordinary terms.</li>
          <li><strong>Controlled-substance offenses</strong> — even minor drug charges can carry severe immigration consequences.</li>
        </ul>
        <h2>Why "handle both" matters</h2>
        <p>Because Newark Law Offices handles <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a> and <a class="link" href="/immigration-lawyer.html">immigration</a> together, every criminal option is evaluated for its immigration effect <em>before</em> a plea — whether an alternative charge avoids the trigger, and how a disposition affects future relief.</p>
        <h2>The one rule</h2>
        <p>If you're not a U.S. citizen and facing any charge, get advice before you plead. A conviction is very hard to undo for immigration purposes afterward. Tell your lawyer your status early — see <a class="link" href="/crimigration-immigration-consequences.html">crimigration</a>.</p>""",
    faqs=[
        ("I have a green card — can a misdemeanor get me deported?",
         "Possibly. Some misdemeanors are crimes involving moral turpitude or controlled-substance offenses with immigration consequences even for lawful permanent residents. The specific charge and disposition matter — get advice before pleading."),
        ("My criminal lawyer got me a good deal — am I safe?",
         "Not necessarily. A plea that's good under criminal law can still be a deportable offense under immigration law. Coordinating both is the point."),
    ],
))

# 9. ICE detention first 48 hours
ARTICLES.append(Article(
    slug="family-detained-by-ice-first-48-hours",
    title="My Family Member Was Detained by ICE — The First 48 Hours | Newark Law Offices",
    description="If a loved one is detained by ICE, the first 48 hours matter. What to do, what not to sign, and how a bond hearing can seek their release.",
    h1="My family member was detained by ICE — the first 48 hours",
    dek="It's frightening and fast-moving. Here are the steps that protect your loved one right now.",
    cta_practice=("Talk to us now — free consultation", "/immigration-lawyer.html"),
    knows_about=["ICE detention", "immigration bond", "detainer", "removal defense"],
    related=[("Bond hearings", "/bond-hearings.html"), ("ICE detainers", "/ice-detainers.html"),
             ("Removal defense", "/removal-defense.html")],
    body_html=f"""{a("What should I do if a family member is detained by ICE?", "Act immediately. Find out where they are being held (the ICE online detainee locator can help), and whether there is a bond. Do not let them sign anything agreeing to removal or waiving rights. A bond hearing can seek their release while the case proceeds, and an attorney can identify defenses and relief. The first 48 hours matter because decisions made early — especially signing a voluntary-departure or removal document — are hard to undo.")}
        <h2>First, locate them</h2>
        <p>Use ICE's online detainee locator or contact the facility. Knowing where they are held determines which immigration court and which steps apply.</p>
        <h2>Do NOT let them sign anything</h2>
        <p>Detained people are sometimes pressured to sign documents agreeing to removal or "voluntary departure." Signing can waive the right to a hearing and to relief. The safest instruction: <strong>sign nothing without talking to a lawyer.</strong></p>
        <h2>Ask about bond</h2>
        <p>Many detained people who aren't subject to mandatory detention can seek release at a <a class="link" href="/bond-hearings.html">bond hearing</a>, where a judge weighs flight risk and danger. Gathering evidence of family ties, employment, and stability helps.</p>
        <h2>Understand the detainer</h2>
        <p>If the person was in local custody, an <a class="link" href="/ice-detainers.html">ICE detainer</a> may have triggered the transfer. A detainer is a request, not a judicial warrant, with legal limits.</p>
        <h2>Get counsel fast</h2>
        <p>There's no government-appointed lawyer in immigration court. Early representation shapes bond, defenses, and relief. See <a class="link" href="/removal-defense.html">removal defense</a>.</p>""",
    faqs=[
        ("Can my detained relative be released?",
         "Possibly, through a bond hearing if they're bond-eligible (not subject to mandatory detention). A judge weighs flight risk and danger; evidence of ties and stability helps."),
        ("Should they sign the papers ICE gives them?",
         "Not without talking to a lawyer. Signing can waive the right to a hearing and to relief, and is hard to undo."),
    ],
))

# 10. Dallas County courts guide
ARTICLES.append(Article(
    slug="dallas-county-courts-guide",
    title="A Guide to the Dallas County Courts | Newark Law Offices",
    description="Where your case is heard in Dallas County — criminal, civil, family, and bankruptcy courts, with addresses. A plain-language orientation.",
    h1="A guide to the Dallas County courts",
    dek="If you have a case in Dallas County, here's where it's actually heard — and who handles what.",
    cta_practice=("Talk to a Dallas attorney — free consultation", "/dallas.html"),
    knows_about=["Dallas County courts", "Frank Crowley", "George Allen courts building"],
    related=[("Dallas", "/dallas.html"), ("Dallas County", "/dallas-county.html"),
             ("Locations", "/locations.html")],
    body_html=f"""{a("Which courts handle cases in Dallas County?", "Dallas County criminal cases (felony and misdemeanor) are heard at the Frank Crowley Courts Building (133 N. Riverfront Blvd). Civil and family matters are heard at the George L. Allen Sr. Courts Building (600 Commerce St). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Northern District of Texas, Dallas Division (Earle Cabell Federal Building, 1100 Commerce St). Which courthouse applies depends on the type of case.")}
        <h2>Criminal — Frank Crowley Courts Building</h2>
        <p>133 N. Riverfront Blvd, Dallas. Felony and misdemeanor cases, arraignments, and criminal dockets. If you've been <a class="link" href="/insights/arrested-in-dallas-your-rights-first-24-hours.html">arrested in Dallas</a>, this is likely where the case proceeds.</p>
        <h2>Civil &amp; family — George L. Allen Sr. Courts Building</h2>
        <p>600 Commerce St, Dallas. Civil disputes, personal injury suits, and family matters. Federal civil matters are heard at the Earle Cabell Federal Building.</p>
        <h2>Bankruptcy — U.S. Bankruptcy Court, N.D. Tex. (Dallas Division)</h2>
        <p>1100 Commerce St (Earle Cabell Federal Building). Consumer Chapter 7 and Chapter 13 filings for Dallas-area residents. See <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>.</p>
        <h2>Immigration</h2>
        <p>Immigration matters are federal and heard at the Dallas Immigration Court, separate from the county system.</p>
        <h2>Getting help</h2>
        <p>Our Texas office is nearby at 1341 W. Mockingbird Ln. Whatever court your matter sits in, the <a class="link" href="/dallas.html">Dallas page</a> has directions and a direct line.</p>""",
    faqs=[
        ("Where are criminal cases heard in Dallas County?",
         "At the Frank Crowley Courts Building, 133 N. Riverfront Blvd, Dallas — for both felonies and misdemeanors."),
        ("Where is a Dallas bankruptcy filed?",
         "In the U.S. Bankruptcy Court for the Northern District of Texas, Dallas Division, at the Earle Cabell Federal Building, 1100 Commerce St."),
    ],
))
