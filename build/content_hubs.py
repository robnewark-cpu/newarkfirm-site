"""
Practice-hub landing pages (nav targets).

These are real, conversion-ready hub pages so the practice-first navigation has
no dead links from tranche one. Later tranches (PHASE 2/3/4/5) expand each into
a full spoke cluster. Content is process-only and makes no outcome promises.

Criminal defense and immigration are confirmed active service lines per the
firm's instruction; content describes representation the firm provides in
Texas and Oklahoma and coordinates with local counsel where required.
"""
from render_practice import PageSpec

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

PAGES = []

# Criminal Defense hub
PAGES.append(PageSpec(
    slug="criminal-defense-lawyer",
    title="Criminal Defense Lawyer | Texas & Oklahoma | Newark Law Offices",
    description="Criminal defense in Texas and Oklahoma — DUI/DWI, drug, assault, theft, domestic violence, expungement. Arrested? Call 866-230-7236 now. Free consultation.",
    h1="Criminal defense lawyer for Texas and Oklahoma",
    lede="If you or a loved one has been arrested or charged in Texas or Oklahoma, what you do in the first hours matters. Newark Law Offices defends misdemeanor and felony matters and protects your rights from the first call. Free, confidential consultation.",
    meta_tags=["Criminal defense", "DUI/DWI", "Arrested? Call now"],
    breadcrumb_name="Criminal Defense Lawyer",
    cluster="Criminal Defense", cluster_hub="/criminal-defense-lawyer.html",
    source="criminal-hub", matter="Criminal defense — general",
    rail_heading="Arrested? Get help now",
    rail_lede="If there is an arrest, a court date, or a police request to talk, call before you say anything. This is confidential.",
    chat_greeting="Arrested or charged in Texas or Oklahoma? Do not talk to police before counsel. Tell me what happened and I can point you to immediate help.",
    knows_about=["criminal defense", "DUI DWI defense", "drug charges", "assault charges",
                 "expungement", "record sealing"],
    related=[("DUI / DWI defense", "/dui-dwi-defense.html"),
             ("Drug charges", "/drug-charges.html"),
             ("Expungement", "/expungement.html"),
             ("Criminal defense FAQ", "/criminal-defense-faq.html")],
    body_html=f"""            <h2>The first 24 hours matter most</h2>
{ans("What should I do right after an arrest?", "Do not answer questions or explain your side to police without a lawyer — you have the right to remain silent and the right to counsel, and using them is not an admission of guilt. Do not consent to searches. Write down everything you remember. Contact a criminal defense lawyer as soon as possible, because early steps (bond, preserving evidence, contacting witnesses) shape the whole case.")}

            <h2>Matters we defend</h2>
            <ul>
              <li><a class="link" href="/dui-dwi-defense.html">DUI / DWI</a> and related license issues</li>
              <li><a class="link" href="/drug-charges.html">Drug possession and distribution charges</a></li>
              <li><a class="link" href="/assault-charges.html">Assault</a> and <a class="link" href="/domestic-violence-defense.html">domestic violence</a> matters</li>
              <li><a class="link" href="/theft-charges.html">Theft and property charges</a></li>
              <li><a class="link" href="/protective-orders.html">Protective orders</a> and <a class="link" href="/probation-violations.html">probation violations</a></li>
              <li><a class="link" href="/expungement.html">Expungement</a> and <a class="link" href="/record-sealing.html">record sealing</a></li>
            </ul>

            <h2>Where your case is handled</h2>
            <p>State charges are handled in the county where they are filed. The firm appears in Texas and Oklahoma courts and coordinates with licensed local counsel where the rules require it. Robert C. Newark, III is licensed in Texas and Oklahoma.</p>""",
    faqs=[
        ("Should I talk to the police to clear things up?",
         "No. You have the right to remain silent and to a lawyer. Politely decline to answer questions and ask for counsel. This protects you and is not an admission of guilt."),
        ("Do I need a lawyer for a first-time misdemeanor?",
         "Yes, it is worth a consultation. Even a first misdemeanor can carry a record, fines, and license or immigration consequences. Options like deferral or dismissal are often lost without early advice."),
        ("Can a charge be kept off my record?",
         "Sometimes, through diversion, deferred adjudication, expungement, or record sealing, depending on the charge, the outcome, and the state. See the expungement and record-sealing pages."),
    ],
))

# Immigration hub
PAGES.append(PageSpec(
    slug="immigration-lawyer",
    title="Immigration Lawyer | Removal & Deportation Defense | Newark Law Offices",
    description="Immigration and removal-defense help — immigration court, bond hearings, adjustment of status, family immigration, waivers, ICE detainers. Free consultation. Call 866-230-7236.",
    h1="Immigration and removal-defense lawyer",
    lede="Whether you are in removal proceedings, seeking a green card, or fighting an ICE detainer, deadlines are unforgiving. Newark Law Offices handles immigration matters and removal defense before the immigration courts. Free, confidential consultation.",
    meta_tags=["Immigration", "Removal defense", "Deportation defense"],
    breadcrumb_name="Immigration Lawyer",
    cluster="Immigration", cluster_hub="/immigration-lawyer.html",
    source="immigration-hub", matter="Immigration — general",
    rail_heading="Facing removal? Act now",
    rail_lede="If there is a court date, a detainer, or an ICE hold, tell us the date immediately. Immigration deadlines are strict.",
    chat_greeting="Facing removal, detention, or an immigration deadline? Tell me your situation and any court date and I can point you to help.",
    knows_about=["immigration lawyer", "removal defense", "deportation defense",
                 "adjustment of status", "bond hearings", "motions to reopen"],
    related=[("Removal defense", "/removal-defense.html"),
             ("Deportation defense", "/deportation-defense.html"),
             ("Adjustment of status", "/adjustment-of-status.html"),
             ("Immigration FAQ", "/immigration-faq.html")],
    body_html=f"""            <h2>Removal defense starts with the deadline</h2>
{ans("What happens in deportation (removal) proceedings?", "Removal proceedings take place in immigration court before an immigration judge. The government must prove the person is removable; the person can present defenses and apply for relief such as cancellation of removal, asylum, adjustment of status, or waivers. There are master calendar hearings (scheduling and pleadings) and an individual merits hearing. Missing a hearing usually results in an automatic removal order, so the court date controls everything.")}

            <h2>How we help</h2>
            <ul>
              <li><a class="link" href="/removal-defense.html">Removal</a> and <a class="link" href="/deportation-defense.html">deportation defense</a> in immigration court</li>
              <li><a class="link" href="/bond-hearings.html">Bond hearings</a> to seek release from detention</li>
              <li><a class="link" href="/adjustment-of-status.html">Adjustment of status</a> and <a class="link" href="/family-immigration.html">family immigration</a></li>
              <li><a class="link" href="/consular-processing.html">Consular processing</a>, <a class="link" href="/waivers.html">waivers</a>, and <a class="link" href="/motions-to-reopen.html">motions to reopen</a></li>
              <li><a class="link" href="/ice-detainers.html">ICE detainers</a> and holds</li>
            </ul>

            <h2>Immigration court and where it sits</h2>
            <p>Immigration courts are federal and operate nationwide; representation before them is not limited by state bar licensure. The firm coordinates with the immigration court and detention facility handling your matter and will tell you plainly what relief may be available.</p>""",
    faqs=[
        ("My family member was detained by ICE — what do I do?",
         "Act immediately. Find out where they are being held and whether there is a bond. A bond hearing can seek release while the case proceeds. Do not sign anything agreeing to removal without talking to a lawyer first."),
        ("Can I get a green card while in removal proceedings?",
         "Sometimes. Adjustment of status and other relief can be pursued before the immigration judge, depending on eligibility. This is exactly what a consultation evaluates."),
        ("What happens if I miss my immigration court date?",
         "Missing a hearing usually results in an in-absentia removal order. If that has happened, a motion to reopen may be possible on limited grounds and short deadlines — call right away."),
    ],
))

# Personal Injury hub is an EXISTING page (personal-injury.html). We add spokes
# in a later tranche; the nav points to the existing hub, so no stub needed here.

# Locations index
PAGES.append(PageSpec(
    slug="locations",
    title="Locations We Serve | Texas & Oklahoma | Newark Law Offices",
    description="Newark Law Offices serves clients across Texas and Oklahoma from Dallas and Edmond — bankruptcy, personal injury, criminal defense, and immigration. Find your city.",
    h1="Locations we serve in Texas and Oklahoma",
    lede="From offices in Dallas and Edmond, Newark Law Offices serves clients across Texas and Oklahoma. Choose your area for local court information and a direct line to a consultation.",
    meta_tags=["Locations", "Texas", "Oklahoma"],
    breadcrumb_name="Locations",
    cluster="Locations", cluster_hub="/locations.html",
    source="locations", matter="General — location inquiry",
    rail_heading="Talk to someone local",
    rail_lede="Tell us your city and matter and we will route you to the right office.",
    knows_about=["Dallas lawyer", "Oklahoma City lawyer", "Fort Worth lawyer"],
    related=[("Texas office", "/texas.html"), ("Oklahoma office", "/oklahoma.html"),
             ("Contact", "/contact.html")],
    body_html="""            <h2>Two offices, statewide reach</h2>
            <p>Our Dallas and Edmond offices anchor practices across both states. Choose your city or county for local court information and directions, or tell us your matter and we will connect you with the right office.</p>
            <div class="grid-2">
              <div class="office-card">
                <h3>Texas — Dallas</h3>
                <address>1341 W. Mockingbird Ln, Ste 600W<br>Dallas, TX 75247<br><a class="link" href="tel:+19723325733">972-332-5733</a></address>
                <p>Serving the Metroplex and statewide Texas.</p>
                <a class="link" href="/texas.html">Texas office</a>
              </div>
              <div class="office-card">
                <h3>Oklahoma — Edmond</h3>
                <address>1019 Waterwood Pkwy, Ste C<br>Edmond, OK 73034<br><a class="link" href="tel:+14057270269">405-727-0269</a></address>
                <p>Serving the OKC metro and statewide Oklahoma.</p>
                <a class="link" href="/oklahoma.html">Oklahoma office</a>
              </div>
            </div>

            <h2>Texas cities</h2>
            <ul class="loc-list">
              <li><a class="link" href="/dallas.html">Dallas</a></li>
              <li><a class="link" href="/fort-worth.html">Fort Worth</a></li>
              <li><a class="link" href="/arlington.html">Arlington</a></li>
              <li><a class="link" href="/plano.html">Plano</a></li>
              <li><a class="link" href="/irving.html">Irving</a></li>
              <li><a class="link" href="/garland.html">Garland</a></li>
              <li><a class="link" href="/denton.html">Denton</a></li>
              <li><a class="link" href="/houston.html">Houston</a></li>
              <li><a class="link" href="/san-antonio.html">San Antonio</a></li>
            </ul>
            <h2>Texas counties</h2>
            <ul class="loc-list">
              <li><a class="link" href="/dallas-county.html">Dallas County</a></li>
              <li><a class="link" href="/tarrant-county.html">Tarrant County</a></li>
              <li><a class="link" href="/collin-county.html">Collin County</a></li>
              <li><a class="link" href="/harris-county.html">Harris County</a></li>
              <li><a class="link" href="/bexar-county.html">Bexar County</a></li>
              <li><a class="link" href="/travis-county.html">Travis County</a></li>
            </ul>
            <h2>Oklahoma cities</h2>
            <ul class="loc-list">
              <li><a class="link" href="/oklahoma-city.html">Oklahoma City</a></li>
              <li><a class="link" href="/oklahoma.html">Edmond</a> <em>(our Oklahoma office)</em></li>
              <li><a class="link" href="/norman.html">Norman</a></li>
              <li><a class="link" href="/moore.html">Moore</a></li>
              <li><a class="link" href="/lawton.html">Lawton</a></li>
            </ul>
            <h2>Oklahoma counties</h2>
            <ul class="loc-list">
              <li><a class="link" href="/oklahoma-county.html">Oklahoma County</a></li>
              <li><a class="link" href="/cleveland-county.html">Cleveland County</a></li>
              <li><a class="link" href="/comanche-county.html">Comanche County</a></li>
            </ul>""",
    faqs=[
        ("Do you only take cases in Dallas and Edmond?",
         "No. Those are our offices, but we serve clients across Texas and Oklahoma. Many matters are handled by phone and video, and we appear in courts throughout both states."),
    ],
))
