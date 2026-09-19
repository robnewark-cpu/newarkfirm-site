"""
Priority location pages (PHASE 5, tranche 2): Dallas, Houston, Oklahoma City,
San Antonio.

Each page has UNIQUE local content — not a templated find/replace — with local
court information, directions, attorney note, FAQs, and LocalBusiness (geo)
schema. Content is process/geography only; no fabricated results or rankings.
"""
from render_practice import PageSpec
import schema as S

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')


class LocationSpec(PageSpec):
    """PageSpec plus geo/city fields for LocalBusiness schema."""
    def __init__(self, *, city, region, geo, **kw):
        self.city = city
        self.region = region
        self.geo = geo
        super().__init__(**kw)


PAGES = []

# ---- Dallas, TX ----
PAGES.append(LocationSpec(
    city="Dallas", region="TX", geo=(32.8115, -96.8807),
    slug="dallas",
    title="Dallas Lawyer | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
    description="Dallas attorneys for bankruptcy, personal injury, criminal defense, and immigration. Office at 1341 W. Mockingbird Ln. Free consultation. Call 866-230-7236.",
    h1="Dallas attorneys — bankruptcy, injury, criminal defense, immigration",
    lede="Newark Law Offices' Texas office sits in Dallas at 1341 W. Mockingbird Ln, serving Dallas County and the wider Metroplex. Whether it is debt, a crash, an arrest, or a removal notice, help starts with a free consultation.",
    meta_tags=["Dallas, TX", "Dallas County", "Metroplex"],
    breadcrumb_name="Dallas", cluster="Locations", cluster_hub="/locations.html",
    source="loc-dallas", matter="General — Dallas",
    rail_heading="Talk to the Dallas office",
    rail_lede="Tell us your matter and we will route you to the Dallas team. Free consultation.",
    knows_about=["Dallas bankruptcy lawyer", "Dallas personal injury lawyer",
                 "Dallas criminal defense lawyer", "Dallas immigration lawyer"],
    related=[("Bankruptcy", "/bankruptcy-lawyer.html"), ("Personal injury", "/personal-injury.html"),
             ("Criminal defense", "/criminal-defense-lawyer.html"), ("Locations", "/locations.html")],
    body_html=f"""            <h2>Serving Dallas and Dallas County</h2>
            <p>Our Texas office is in the Mockingbird/Stemmons corridor, minutes from downtown Dallas and I-35E. From here we handle <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>, <a class="link" href="/personal-injury.html">personal injury</a>, <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a>, and <a class="link" href="/immigration-lawyer.html">immigration</a> matters for clients across Dallas County and the surrounding metro.</p>
{ans("Where are the courts for a Dallas case?", "Civil and family matters in Dallas County are heard at the George L. Allen Sr. Courts Building (600 Commerce St) and the Renaissance Tower civil courts; felony and misdemeanor criminal cases run through the Frank Crowley Courts Building (133 N. Riverfront Blvd). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Northern District of Texas, Earle Cabell Federal Building (1100 Commerce St). Which courthouse applies depends on the type of case.")}
            <h2>Local courts</h2>
            <ul>
              <li><strong>Bankruptcy:</strong> U.S. Bankruptcy Court, Northern District of Texas (Dallas Division), 1100 Commerce St</li>
              <li><strong>Criminal:</strong> Frank Crowley Courts Building, 133 N. Riverfront Blvd</li>
              <li><strong>Civil/injury:</strong> George L. Allen Sr. Courts Building, 600 Commerce St; federal civil at the Earle Cabell Federal Building</li>
              <li><strong>Immigration:</strong> Dallas Immigration Court (federal)</li>
            </ul>
            <h2>Office &amp; directions</h2>
            <p>1341 W. Mockingbird Ln, Ste 600W, Dallas, TX 75247. Just off I-35E (Stemmons) at Mockingbird, near the Medical District/Market Center DART station. In-office visits by appointment; phone and video consultations available. Call <a class="link" href="tel:+19723325733">972-332-5733</a> or toll-free <a class="link" href="tel:+18662307236">866-230-7236</a>.</p>
            <h2>Attorney</h2>
            <p>Dallas matters are directed by Robert C. Newark, III, licensed in Texas and Oklahoma and admitted to the federal courts in Texas.</p>""",
    faqs=[
        ("Do you have an office in Dallas?",
         "Yes. Our Texas office is at 1341 W. Mockingbird Ln, Ste 600W, Dallas, TX 75247, just off I-35E at Mockingbird. In-office visits are by appointment; phone and video consultations are available."),
        ("What kinds of cases do you handle in Dallas?",
         "Bankruptcy (Chapter 7 and 13), personal injury, criminal defense, and immigration and removal defense, plus select corporate and litigation matters."),
        ("Is the consultation free?",
         "Yes. The initial consultation is free and does not create an attorney-client relationship."),
    ],
))

# ---- Houston, TX ----
PAGES.append(LocationSpec(
    city="Houston", region="TX", geo=(29.7604, -95.3698),
    slug="houston",
    title="Houston Lawyer | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
    description="Houston-area attorneys for bankruptcy, personal injury, criminal defense, and immigration. Statewide Texas practice. Free consultation. Call 866-230-7236.",
    h1="Houston attorneys — bankruptcy, injury, criminal defense, immigration",
    lede="Newark Law Offices serves Houston and Harris County clients across bankruptcy, personal injury, criminal defense, and immigration. Many matters are handled by phone and video, with appearances in Houston's courts as needed. Free consultation.",
    meta_tags=["Houston, TX", "Harris County", "Statewide Texas"],
    breadcrumb_name="Houston", cluster="Locations", cluster_hub="/locations.html",
    source="loc-houston", matter="General — Houston",
    rail_heading="Talk to us about a Houston matter",
    rail_lede="Tell us your matter and city. Phone and video consultations available statewide.",
    knows_about=["Houston bankruptcy lawyer", "Houston personal injury lawyer",
                 "Houston criminal defense lawyer", "Houston immigration lawyer"],
    related=[("Bankruptcy", "/bankruptcy-lawyer.html"), ("Personal injury", "/personal-injury.html"),
             ("Immigration", "/immigration-lawyer.html"), ("Locations", "/locations.html")],
    body_html=f"""            <h2>Serving Houston and Harris County</h2>
            <p>Houston is the largest legal market in Texas, and the firm serves clients here statewide — handling <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>, <a class="link" href="/personal-injury.html">injury</a>, <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a>, and <a class="link" href="/immigration-lawyer.html">immigration</a> matters. Much of the work is handled by phone and video, with in-person appearances in Houston courts when a case requires it.</p>
{ans("Where are Houston cases heard?", "Harris County civil and family cases are heard at the Harris County Civil Courthouse (201 Caroline St); criminal cases at the Harris County Criminal Justice Center (1201 Franklin St). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Southern District of Texas (Houston Division), 515 Rusk St. Houston also has a federal immigration court. The right courthouse depends on the case type.")}
            <h2>Local courts</h2>
            <ul>
              <li><strong>Bankruptcy:</strong> U.S. Bankruptcy Court, Southern District of Texas (Houston Division), 515 Rusk St</li>
              <li><strong>Criminal:</strong> Harris County Criminal Justice Center, 1201 Franklin St</li>
              <li><strong>Civil/injury:</strong> Harris County Civil Courthouse, 201 Caroline St</li>
              <li><strong>Immigration:</strong> Houston Immigration Court (federal)</li>
            </ul>
            <h2>How we serve Houston clients</h2>
            <p>Consultations are by phone or video, and documents are handled securely online. When a hearing or filing calls for a Houston appearance, we appear or coordinate with local counsel as the rules require. Call <a class="link" href="tel:+18662307236">866-230-7236</a>.</p>
            <h2>Attorney</h2>
            <p>Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the U.S. District Courts in Texas, including the Southern District.</p>""",
    faqs=[
        ("Do you serve clients in Houston?",
         "Yes. The firm serves Houston and Harris County statewide, with phone and video consultations and court appearances in Houston as cases require."),
        ("Do I have to come to Dallas for a Houston case?",
         "No. Most consultations are by phone or video, and documents are handled securely online. We appear in Houston courts or coordinate with local counsel when needed."),
    ],
))

# ---- Oklahoma City, OK ----
PAGES.append(LocationSpec(
    city="Oklahoma City", region="OK", geo=(35.4676, -97.5164),
    slug="oklahoma-city",
    title="Oklahoma City Lawyer | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
    description="Oklahoma City attorneys for bankruptcy, personal injury, criminal defense, and immigration. Edmond office nearby. Free consultation. Call 866-230-7236.",
    h1="Oklahoma City attorneys — bankruptcy, injury, criminal defense, immigration",
    lede="Newark Law Offices serves Oklahoma City and Oklahoma County from its Edmond office just north of the metro. From debt relief to injury, criminal, and immigration matters, help starts with a free consultation.",
    meta_tags=["Oklahoma City, OK", "Oklahoma County", "Metro OKC"],
    breadcrumb_name="Oklahoma City", cluster="Locations", cluster_hub="/locations.html",
    source="loc-okc", matter="General — Oklahoma City",
    rail_heading="Talk to the Oklahoma office",
    rail_lede="Tell us your matter and we will route you to the Edmond/OKC team. Free consultation.",
    knows_about=["Oklahoma City bankruptcy lawyer", "OKC personal injury lawyer",
                 "OKC criminal defense lawyer", "OKC immigration lawyer"],
    related=[("Bankruptcy", "/bankruptcy-lawyer.html"), ("Personal injury", "/personal-injury.html"),
             ("Criminal defense", "/criminal-defense-lawyer.html"), ("Oklahoma office", "/oklahoma.html")],
    body_html=f"""            <h2>Serving Oklahoma City and Oklahoma County</h2>
            <p>Our Oklahoma office is in Edmond, minutes north of Oklahoma City via I-35 and the Broadway Extension, serving the whole OKC metro. We handle <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>, <a class="link" href="/personal-injury.html">injury</a>, <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a>, and <a class="link" href="/immigration-lawyer.html">immigration</a> matters for OKC-area clients.</p>
{ans("Where are Oklahoma City cases heard?", "Oklahoma County civil, family, and criminal cases are heard at the Oklahoma County Courthouse (321 Park Ave, Oklahoma City). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma (215 Dean A. McGee Ave). Oklahoma foreclosures are judicial and proceed through the district court. Which court applies depends on the type of case.")}
            <h2>Local courts</h2>
            <ul>
              <li><strong>Bankruptcy:</strong> U.S. Bankruptcy Court, Western District of Oklahoma, 215 Dean A. McGee Ave</li>
              <li><strong>Criminal/civil:</strong> Oklahoma County Courthouse, 321 Park Ave</li>
              <li><strong>Foreclosure:</strong> Oklahoma County District Court (judicial foreclosure)</li>
              <li><strong>Immigration:</strong> matters proceed before the federal immigration courts</li>
            </ul>
            <h2>Office &amp; directions</h2>
            <p>1019 Waterwood Pkwy, Ste C, Edmond, OK 73034 — just off I-35 north of OKC. In-office visits by appointment; phone and video consultations available. Call <a class="link" href="tel:+14057270269">405-727-0269</a> or toll-free <a class="link" href="tel:+18662307236">866-230-7236</a>.</p>
            <h2>Attorneys</h2>
            <p>Oklahoma matters are handled by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma), from the Edmond office.</p>""",
    faqs=[
        ("Do you have an office near Oklahoma City?",
         "Yes. Our Oklahoma office is at 1019 Waterwood Pkwy, Ste C, Edmond, OK 73034, just north of OKC off I-35. In-office visits are by appointment; phone and video consultations are available."),
        ("Where is my Oklahoma City bankruptcy filed?",
         "Consumer bankruptcies for the OKC area are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma at 215 Dean A. McGee Ave."),
        ("Is the consultation free?",
         "Yes. The initial consultation is free and does not create an attorney-client relationship."),
    ],
))

# ---- San Antonio, TX ----
PAGES.append(LocationSpec(
    city="San Antonio", region="TX", geo=(29.4241, -98.4936),
    slug="san-antonio",
    title="San Antonio Lawyer | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
    description="San Antonio-area attorneys for bankruptcy, personal injury, criminal defense, and immigration. Statewide Texas practice. Free consultation. Call 866-230-7236.",
    h1="San Antonio attorneys — bankruptcy, injury, criminal defense, immigration",
    lede="Newark Law Offices serves San Antonio and Bexar County clients across bankruptcy, personal injury, criminal defense, and immigration, with phone and video consultations and appearances in San Antonio courts as needed. Free consultation.",
    meta_tags=["San Antonio, TX", "Bexar County", "Statewide Texas"],
    breadcrumb_name="San Antonio", cluster="Locations", cluster_hub="/locations.html",
    source="loc-san-antonio", matter="General — San Antonio",
    rail_heading="Talk to us about a San Antonio matter",
    rail_lede="Tell us your matter and city. Phone and video consultations available statewide.",
    knows_about=["San Antonio bankruptcy lawyer", "San Antonio personal injury lawyer",
                 "San Antonio criminal defense lawyer", "San Antonio immigration lawyer"],
    related=[("Bankruptcy", "/bankruptcy-lawyer.html"), ("Personal injury", "/personal-injury.html"),
             ("Immigration", "/immigration-lawyer.html"), ("Locations", "/locations.html")],
    body_html=f"""            <h2>Serving San Antonio and Bexar County</h2>
            <p>The firm serves San Antonio and Bexar County across <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>, <a class="link" href="/personal-injury.html">injury</a>, <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a>, and <a class="link" href="/immigration-lawyer.html">immigration</a> matters. Consultations are by phone and video, with in-person appearances in San Antonio courts when a case requires it.</p>
{ans("Where are San Antonio cases heard?", "Bexar County civil and family cases are heard at the Bexar County Courthouse and the Cadena-Reeves Justice Center (300 Dolorosa St); criminal cases at the Justice Center as well. Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Western District of Texas (San Antonio Division), 615 E. Houston St. San Antonio has a federal immigration court. The right court depends on the case type.")}
            <h2>Local courts</h2>
            <ul>
              <li><strong>Bankruptcy:</strong> U.S. Bankruptcy Court, Western District of Texas (San Antonio Division), 615 E. Houston St</li>
              <li><strong>Criminal/civil:</strong> Cadena-Reeves Justice Center &amp; Bexar County Courthouse, 300 Dolorosa St</li>
              <li><strong>Immigration:</strong> San Antonio Immigration Court (federal)</li>
            </ul>
            <h2>How we serve San Antonio clients</h2>
            <p>Consultations are by phone or video and documents are handled securely online, with appearances in San Antonio courts or local-counsel coordination as the rules require. Call <a class="link" href="tel:+18662307236">866-230-7236</a>.</p>
            <h2>Attorney</h2>
            <p>Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the U.S. District Courts in Texas, including the Western District.</p>""",
    faqs=[
        ("Do you serve clients in San Antonio?",
         "Yes. The firm serves San Antonio and Bexar County statewide, with phone and video consultations and appearances in San Antonio courts as cases require."),
        ("Where is a San Antonio bankruptcy filed?",
         "Consumer bankruptcies for the San Antonio area are filed in the U.S. Bankruptcy Court for the Western District of Texas (San Antonio Division), 615 E. Houston St."),
    ],
))
