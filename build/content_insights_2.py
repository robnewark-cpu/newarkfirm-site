"""Insights articles batch 2 — criminal, immigration, crimigration, local.

'Arrested' is split into Texas and Oklahoma versions (booking/bond process and
some procedures differ, and it doubles local-SEO reach). Crimigration and ICE
articles are federal-law topics kept state-neutral with major cities named for
SEO. The Dallas County courts guide stays intentionally local. No fabricated
facts or outcomes; approval workflow first.
"""
from render_article import Article

def a(q, ans):
    return (f'        <div class="answer-block">\n'
            f'          <h3 class="answer-q">{q}</h3>\n'
            f'          <div class="answer-a">{ans}</div>\n'
            f'        </div>')

ARTICLES = []

# 7a. Arrested — TEXAS
ARTICLES.append(Article(
    slug="arrested-in-texas-your-rights-first-24-hours",
    title="Arrested in Texas? Your Rights in the First 24 Hours | Newark Law Offices",
    description="Just arrested in Texas — Dallas, Fort Worth, Houston, or anywhere in the state? Your rights, talking to police, bond, and the first 24 hours, in plain language.",
    h1="Arrested in Texas? Your rights in the first 24 hours",
    dek="The first day shapes the whole case. Here's what protects you across Texas — and what quietly hurts you.",
    cta_practice=("Talk to a Texas criminal defense lawyer — free & confidential", "/criminal-defense-lawyer.html"),
    knows_about=["arrested Texas", "right to remain silent", "Texas bond", "criminal defense"],
    related=[("Criminal defense lawyer", "/criminal-defense-lawyer.html"),
             ("Criminal defense FAQ", "/criminal-defense-faq.html"),
             ("Oklahoma version", "/insights/arrested-in-oklahoma-your-rights-first-24-hours.html")],
    body_html=f"""{a("What should I do in the first 24 hours after an arrest in Texas?", "Use your right to remain silent and your right to a lawyer — say you want an attorney and stop answering questions. Do not consent to searches, do not explain your side to police, and do not discuss the case on a recorded jail line. Write down what you remember, and contact a criminal defense lawyer as soon as possible. In Texas, a magistrate must promptly inform you of the charges and set conditions of release (bond); a lawyer can seek a bond or reduction.")}
        <h2>Silence is a right, not an admission</h2>
        <p>You have the constitutional right to remain silent and to counsel — using them can't be held against you. Say: "I want a lawyer, and I'm not answering questions." Then stop. This is true whether you were arrested in Dallas, Fort Worth, Arlington, Plano, Houston, San Antonio, or anywhere in Texas.</p>
        <h2>Don't consent to searches</h2>
        <p>You can decline to consent to a search of your car, phone, or home. If police search anyway, that's for your lawyer to challenge — but consenting waives the issue.</p>
        <h2>The jail phone is recorded</h2>
        <p>Calls from jail (except to your attorney) are recorded and used by prosecutors. Discuss the facts only with your lawyer.</p>
        <h2>Bond in Texas</h2>
        <p>A magistrate promptly informs you of the accusation and sets bail/conditions. A lawyer can request a bond or reduction so you're not held longer than necessary.</p>
        <h2>If you're not a U.S. citizen</h2>
        <p>A criminal charge can carry immigration consequences even before conviction — see <a class="link" href="/crimigration-immigration-consequences.html">crimigration</a>.</p>
        <p><em>Arrested in Oklahoma? See the <a class="link" href="/insights/arrested-in-oklahoma-your-rights-first-24-hours.html">Oklahoma version</a>.</em></p>""",
    faqs=[
        ("Should I explain my side to clear things up?",
         "No. Anything you say can be used against you. Ask for a lawyer and stay silent — you can tell your side later, through counsel, when it helps."),
        ("How does bond work in Texas?",
         "A magistrate sets bail and conditions of release shortly after arrest. A lawyer can seek a bond or a reduction based on the relevant factors."),
    ],
))

# 7b. Arrested — OKLAHOMA
ARTICLES.append(Article(
    slug="arrested-in-oklahoma-your-rights-first-24-hours",
    title="Arrested in Oklahoma? Your Rights in the First 24 Hours | Newark Law Offices",
    description="Just arrested in Oklahoma — Oklahoma City, Edmond, Norman, or anywhere in the state? Your rights, talking to police, bond, and the first 24 hours, in plain language.",
    h1="Arrested in Oklahoma? Your rights in the first 24 hours",
    dek="The first day shapes the whole case. Here's what protects you across Oklahoma — and what quietly hurts you.",
    cta_practice=("Talk to an Oklahoma criminal defense lawyer — free & confidential", "/criminal-defense-lawyer.html"),
    knows_about=["arrested Oklahoma", "right to remain silent", "Oklahoma bond", "criminal defense"],
    related=[("Criminal defense lawyer", "/criminal-defense-lawyer.html"),
             ("Criminal defense FAQ", "/criminal-defense-faq.html"),
             ("Texas version", "/insights/arrested-in-texas-your-rights-first-24-hours.html")],
    body_html=f"""{a("What should I do in the first 24 hours after an arrest in Oklahoma?", "Use your right to remain silent and your right to a lawyer — say you want an attorney and stop answering questions. Do not consent to searches, do not explain your side to police, and do not discuss the case on a recorded jail line. Write down what you remember, and contact a criminal defense lawyer as soon as possible. In Oklahoma, you are brought before a judge for an initial appearance where bond is addressed; a lawyer can seek a bond or reduction.")}
        <h2>Silence is a right, not an admission</h2>
        <p>You have the constitutional right to remain silent and to counsel — using them can't be held against you. Say: "I want a lawyer, and I'm not answering questions." Then stop. This is true whether you were arrested in Oklahoma City, Edmond, Norman, Moore, Lawton, or anywhere in Oklahoma.</p>
        <h2>Don't consent to searches</h2>
        <p>You can decline to consent to a search. If police search anyway, that's for your lawyer to challenge — consenting waives the issue.</p>
        <h2>The jail phone is recorded</h2>
        <p>Calls from jail (except to your attorney) are recorded and used by prosecutors. Discuss the facts only with your lawyer.</p>
        <h2>Bond in Oklahoma</h2>
        <p>You're brought before a judge for an initial appearance where bond is set. A lawyer can request a bond or reduction so you're not held longer than necessary.</p>
        <h2>If you're not a U.S. citizen</h2>
        <p>A criminal charge can carry immigration consequences even before conviction — see <a class="link" href="/crimigration-immigration-consequences.html">crimigration</a>.</p>
        <p><em>Arrested in Texas? See the <a class="link" href="/insights/arrested-in-texas-your-rights-first-24-hours.html">Texas version</a>.</em></p>""",
    faqs=[
        ("Should I explain my side to clear things up?",
         "No. Anything you say can be used against you. Ask for a lawyer and stay silent — you can tell your side later, through counsel, when it helps."),
        ("How does bond work in Oklahoma?",
         "You're brought before a judge for an initial appearance where bond is addressed. A lawyer can seek a bond or a reduction based on the relevant factors."),
    ],
))

# 8. Crimigration (federal, neutral, cities sprinkled)
ARTICLES.append(Article(
    slug="crimigration-guilty-plea-deportation",
    title="Crimigration: How a Guilty Plea Can Get a Non-Citizen Deported | Newark Law Offices",
    description="For non-citizens, a criminal plea can trigger deportation even when the penalty is minor. The crimigration trap and how to avoid it — for defendants across Texas and Oklahoma.",
    h1="Crimigration: how a guilty plea can trigger deportation",
    dek="A plea that looks like a win in criminal court can be a one-way ticket out of the country. Most people never see it coming.",
    cta_practice=("Talk to a firm that handles both — free consultation", "/crimigration-immigration-consequences.html"),
    knows_about=["crimigration", "immigration consequences of crimes", "deportable offense", "Padilla"],
    related=[("Crimigration", "/crimigration-immigration-consequences.html"),
             ("Criminal defense", "/criminal-defense-lawyer.html"),
             ("Immigration & removal defense", "/immigration-lawyer.html")],
    body_html=f"""{a("Can a guilty plea get a non-citizen deported?", "Yes. For a non-citizen, a criminal conviction — and sometimes just a plea — can trigger deportation, make you inadmissible, or bar relief like cancellation of removal or naturalization, even when the criminal penalty is minor. Certain offenses (aggravated felonies and crimes involving moral turpitude, including some drug and theft offenses) carry the harshest consequences. Immigration law is federal, so this applies the same way to defendants in Texas and Oklahoma. Padilla v. Kentucky requires defense counsel to advise a non-citizen of a plea's immigration consequences.")}
        <h2>The trap</h2>
        <p>A criminal defense lawyer's job is the best criminal outcome — probation, a reduced charge, deferred adjudication. But under immigration law, that "good" plea can be a <strong>deportable offense</strong>. The two systems don't talk to each other. This is a federal issue, identical for a non-citizen in Dallas, Houston, Oklahoma City, or anywhere else.</p>
        <h2>What triggers it</h2>
        <ul>
          <li><strong>Crimes involving moral turpitude</strong> — including some theft and fraud offenses.</li>
          <li><strong>Aggravated felonies</strong> — a broad immigration category.</li>
          <li><strong>Controlled-substance offenses</strong> — even minor drug charges.</li>
        </ul>
        <h2>Why "handle both" matters</h2>
        <p>Because Newark Law Offices handles <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a> and <a class="link" href="/immigration-lawyer.html">immigration</a> together, every criminal option is checked for its immigration effect <em>before</em> a plea.</p>
        <h2>The one rule</h2>
        <p>If you're not a U.S. citizen and facing any charge, get advice before you plead. See <a class="link" href="/crimigration-immigration-consequences.html">crimigration</a>.</p>""",
    faqs=[
        ("I have a green card — can a misdemeanor get me deported?",
         "Possibly. Some misdemeanors are crimes involving moral turpitude or controlled-substance offenses with immigration consequences even for lawful permanent residents. Get advice before pleading."),
        ("My criminal lawyer got me a good deal — am I safe?",
         "Not necessarily. A plea that's good under criminal law can still be a deportable offense under immigration law. Coordinating both is the point."),
    ],
))

# 9. ICE detention (federal, neutral, cities sprinkled)
ARTICLES.append(Article(
    slug="family-detained-by-ice-first-48-hours",
    title="My Family Member Was Detained by ICE — The First 48 Hours | Newark Law Offices",
    description="If a loved one is detained by ICE, the first 48 hours matter. What to do, what not to sign, and how a bond hearing can seek release — help across Texas and Oklahoma.",
    h1="My family member was detained by ICE — the first 48 hours",
    dek="It's frightening and fast-moving. Here are the steps that protect your loved one right now.",
    cta_practice=("Talk to us now — free consultation", "/immigration-lawyer.html"),
    knows_about=["ICE detention", "immigration bond", "detainer", "removal defense"],
    related=[("Bond hearings", "/bond-hearings.html"), ("ICE detainers", "/ice-detainers.html"),
             ("Removal defense", "/removal-defense.html")],
    body_html=f"""{a("What should I do if a family member is detained by ICE?", "Act immediately. Find out where they are held (the ICE online detainee locator can help) and whether there is a bond. Do not let them sign anything agreeing to removal or waiving rights. A bond hearing can seek release while the case proceeds. Immigration is federal, so this process is the same whether your family member was detained in Texas or Oklahoma. Early decisions — especially signing a voluntary-departure or removal document — are hard to undo.")}
        <h2>First, locate them</h2>
        <p>Use ICE's online detainee locator or contact the facility. Where they're held determines which immigration court applies. Families across Dallas, Houston, Oklahoma City, and both states face the same first steps.</p>
        <h2>Do NOT let them sign anything</h2>
        <p>Detained people are sometimes pressured to sign documents agreeing to removal or "voluntary departure," which can waive the right to a hearing and to relief. <strong>Sign nothing without a lawyer.</strong></p>
        <h2>Ask about bond</h2>
        <p>Many detained people not subject to mandatory detention can seek release at a <a class="link" href="/bond-hearings.html">bond hearing</a>. Evidence of family ties, employment, and stability helps.</p>
        <h2>Understand the detainer</h2>
        <p>If they were in local custody, an <a class="link" href="/ice-detainers.html">ICE detainer</a> may have triggered the transfer — a request, not a judicial warrant, with legal limits.</p>
        <h2>Get counsel fast</h2>
        <p>There's no government-appointed lawyer in immigration court. See <a class="link" href="/removal-defense.html">removal defense</a>.</p>""",
    faqs=[
        ("Can my detained relative be released?",
         "Possibly, through a bond hearing if they're bond-eligible (not subject to mandatory detention). A judge weighs flight risk and danger; evidence of ties helps."),
        ("Should they sign the papers ICE gives them?",
         "Not without talking to a lawyer. Signing can waive the right to a hearing and to relief, and is hard to undo."),
    ],
))

# 10. Dallas County courts guide (intentionally local)
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
    body_html=f"""{a("Which courts handle cases in Dallas County?", "Dallas County criminal cases (felony and misdemeanor) are heard at the Frank Crowley Courts Building (133 N. Riverfront Blvd). Civil and family matters are heard at the George L. Allen Sr. Courts Building (600 Commerce St). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Northern District of Texas, Dallas Division (Earle Cabell Federal Building, 1100 Commerce St). Which courthouse applies depends on the case type.")}
        <h2>Criminal — Frank Crowley Courts Building</h2>
        <p>133 N. Riverfront Blvd, Dallas. Felony and misdemeanor cases and criminal dockets. If you've been <a class="link" href="/insights/arrested-in-texas-your-rights-first-24-hours.html">arrested in Texas</a>, this is likely where a Dallas-area case proceeds.</p>
        <h2>Civil &amp; family — George L. Allen Sr. Courts Building</h2>
        <p>600 Commerce St, Dallas. Civil disputes, personal injury suits, and family matters. Federal civil matters are at the Earle Cabell Federal Building.</p>
        <h2>Bankruptcy — U.S. Bankruptcy Court, N.D. Tex. (Dallas Division)</h2>
        <p>1100 Commerce St (Earle Cabell Federal Building). Consumer Chapter 7 and 13 filings for Dallas-area residents. See <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>.</p>
        <h2>Immigration</h2>
        <p>Immigration matters are federal and heard at the Dallas Immigration Court, separate from the county system.</p>
        <h2>Getting help</h2>
        <p>Our Texas office is nearby at 1341 W. Mockingbird Ln. See the <a class="link" href="/dallas.html">Dallas page</a> for directions and a direct line.</p>""",
    faqs=[
        ("Where are criminal cases heard in Dallas County?",
         "At the Frank Crowley Courts Building, 133 N. Riverfront Blvd, Dallas — for both felonies and misdemeanors."),
        ("Where is a Dallas bankruptcy filed?",
         "In the U.S. Bankruptcy Court for the Northern District of Texas, Dallas Division, at the Earle Cabell Federal Building, 1100 Commerce St."),
    ],
))
