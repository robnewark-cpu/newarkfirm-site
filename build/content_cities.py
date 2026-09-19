"""
Remaining Texas & Oklahoma city location pages (PHASE 5, tranche 4).

Each has unique local content: county, courts, directions/reach, attorney note,
and FAQs, with LocalBusiness+geo schema. Cities near an office reference that
office; farther cities are served statewide by phone/video with appearances as
needed. No fabricated results or rankings.
"""
from content_locations import LocationSpec

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

RELATED = [("Bankruptcy", "/bankruptcy-lawyer.html"),
           ("Personal injury", "/personal-injury.html"),
           ("Criminal defense", "/criminal-defense-lawyer.html"),
           ("Locations", "/locations.html")]

def city(slug, name, county, region, geo, county_slug, courts_html, reach_html,
         office_line, attorney_line, near_office):
    lede = (f"Newark Law Offices serves {name} and {county} across bankruptcy, "
            f"personal injury, criminal defense, and immigration. {office_line} "
            f"Free, confidential consultation.")
    body = f"""            <h2>Serving {name} and {county}</h2>
            <p>{reach_html} We handle <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>, <a class="link" href="/personal-injury.html">personal injury</a>, <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a>, and <a class="link" href="/immigration-lawyer.html">immigration</a> matters for {name}-area clients.</p>
{ans(f"Where are {name} cases heard?", courts_html)}
            <h2>Local courts</h2>
            <p>{name} sits in {county} (<a class="link" href="/{county_slug}.html">{county} court information</a>). {courts_html}</p>
            <h2>How we serve {name} clients</h2>
            <p>{reach_html} Consultations are available by phone and video, with in-person appearances as a case requires. Call <a class="link" href="tel:+18662307236">866-230-7236</a>.</p>
            <h2>Attorney</h2>
            <p>{attorney_line}</p>"""
    return LocationSpec(
        city=name, region=region, geo=geo, slug=slug,
        title=f"{name} Lawyer | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
        description=f"{name} attorneys for bankruptcy, personal injury, criminal defense, and immigration. {county}. Free consultation. Call 866-230-7236.",
        h1=f"{name} attorneys — bankruptcy, personal injury, criminal defense, immigration",
        lede=lede, meta_tags=[f"{name}, {region}", county, "Free consultation"],
        breadcrumb_name=name, cluster="Locations", cluster_hub="/locations.html",
        source=f"loc-{slug}", matter=f"General — {name}",
        rail_heading=f"Talk to us about a {name} matter",
        rail_lede="Tell us your matter and city. Phone and video consultations available.",
        knows_about=[f"{name} bankruptcy lawyer", f"{name} personal injury lawyer",
                     f"{name} criminal defense lawyer", f"{name} immigration lawyer"],
        related=RELATED, body_html=body,
        faqs=[
            (f"Do you serve clients in {name}?",
             f"Yes. The firm serves {name} and {county} across bankruptcy, personal injury, criminal defense, and immigration, with phone and video consultations and court appearances as cases require."),
            ("Is the consultation free?",
             "Yes. The initial consultation is free and does not create an attorney-client relationship."),
        ])

PAGES = []

# --- Texas cities (DFW metro, near Dallas office) ---
PAGES.append(city(
    "fort-worth", "Fort Worth", "Tarrant County", "TX", (32.7555, -97.3308),
    "tarrant-county",
    "Tarrant County civil and family cases are heard at the Tom Vandergriff Civil Courts Building and the Tarrant County Family Law Center; criminal cases at the Tim Curry Criminal Justice Center (401 W. Belknap St, Fort Worth). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Northern District of Texas, Fort Worth Division (501 W. 10th St).",
    "Fort Worth is about 35 miles west of our Dallas office, well within our core Metroplex service area.",
    "Our Dallas office at 1341 W. Mockingbird Ln is a short drive east via I-30.",
    "Texas matters are directed by Robert C. Newark, III, licensed in Texas and Oklahoma and admitted to the federal courts in Texas.",
    True))
PAGES.append(city(
    "arlington", "Arlington", "Tarrant County", "TX", (32.7357, -97.1081),
    "tarrant-county",
    "Arlington is in Tarrant County; civil and criminal matters are heard in the Tarrant County courts in Fort Worth (Tom Vandergriff Civil Courts Building and Tim Curry Criminal Justice Center). Consumer bankruptcies are filed in the U.S. Bankruptcy Court, Northern District of Texas (Fort Worth or Dallas Division).",
    "Arlington sits between Dallas and Fort Worth, minutes from our Dallas office via I-30.",
    "Our Dallas office at 1341 W. Mockingbird Ln is a short drive northeast.",
    "Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas.",
    True))
PAGES.append(city(
    "plano", "Plano", "Collin County", "TX", (33.0198, -96.6989),
    "collin-county",
    "Plano is in Collin County; civil, family, and criminal cases are heard at the Collin County Courthouse (2100 Bloomdale Rd, McKinney). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Eastern District of Texas (Plano Division), 660 N. Central Expressway, Plano.",
    "Plano is just north of Dallas along US-75, within our core Metroplex service area.",
    "Our Dallas office at 1341 W. Mockingbird Ln is a short drive south via US-75.",
    "Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas, including the Eastern District.",
    True))
PAGES.append(city(
    "irving", "Irving", "Dallas County", "TX", (32.8140, -96.9489),
    "dallas-county",
    "Irving is in Dallas County; civil and family matters are heard at the George L. Allen Sr. Courts Building and criminal cases at the Frank Crowley Courts Building in Dallas. Consumer bankruptcies are filed in the U.S. Bankruptcy Court, Northern District of Texas (Dallas Division).",
    "Irving borders our Dallas office neighborhood — it is one of the closest cities we serve.",
    "Our Dallas office at 1341 W. Mockingbird Ln is minutes away.",
    "Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas.",
    True))
PAGES.append(city(
    "garland", "Garland", "Dallas County", "TX", (32.9126, -96.6389),
    "dallas-county",
    "Garland is in Dallas County; civil and criminal matters are heard at the George L. Allen Sr. Courts Building and the Frank Crowley Courts Building in Dallas. Consumer bankruptcies are filed in the U.S. Bankruptcy Court, Northern District of Texas (Dallas Division).",
    "Garland is northeast of downtown Dallas, within our core Metroplex service area.",
    "Our Dallas office at 1341 W. Mockingbird Ln is a short drive southwest.",
    "Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas.",
    True))
PAGES.append(city(
    "denton", "Denton", "Denton County", "TX", (33.2148, -97.1331),
    "collin-county",
    "Denton is the seat of Denton County; civil, family, and criminal cases are heard at the Denton County Courts Building and the Denton County Courthouse-on-the-Square. Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Eastern District of Texas (Sherman/Plano Division).",
    "Denton is on the northern edge of the Metroplex, served from our Dallas office.",
    "Our Dallas office at 1341 W. Mockingbird Ln is south via I-35E.",
    "Texas matters are directed by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas.",
    True))

# --- Oklahoma cities (OKC metro, near Edmond office) ---
PAGES.append(city(
    "norman", "Norman", "Cleveland County", "TX".replace("TX", "OK"), (35.2226, -97.4395),
    "cleveland-county",
    "Norman is the seat of Cleveland County; civil, family, and criminal cases are heard at the Cleveland County Courthouse (200 S. Peters Ave, Norman). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma in Oklahoma City.",
    "Norman is just south of Oklahoma City, served from our Edmond office.",
    "Our Edmond office at 1019 Waterwood Pkwy is a straightforward drive north of Norman via I-35.",
    "Oklahoma matters are handled by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma).",
    False))
PAGES.append(city(
    "moore", "Moore", "Cleveland County", "OK", (35.3395, -97.4867),
    "cleveland-county",
    "Moore is in Cleveland County; civil and criminal cases are heard at the Cleveland County Courthouse in Norman (200 S. Peters Ave). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma in Oklahoma City.",
    "Moore sits between Oklahoma City and Norman along I-35, served from our Edmond office.",
    "Our Edmond office at 1019 Waterwood Pkwy is north via I-35.",
    "Oklahoma matters are handled by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma).",
    False))
PAGES.append(city(
    "lawton", "Lawton", "Comanche County", "OK", (34.6087, -98.3903),
    "comanche-county",
    "Lawton is the seat of Comanche County; civil, family, and criminal cases are heard at the Comanche County Courthouse (315 SW 5th St, Lawton). Consumer bankruptcies are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma in Oklahoma City.",
    "Lawton is in southwest Oklahoma; the firm serves it statewide with phone and video consultations and appearances as needed.",
    "Consultations are by phone or video, with appearances in Comanche County or local-counsel coordination as required.",
    "Oklahoma matters are handled by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma).",
    False))
