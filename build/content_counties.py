"""
County location pages (PHASE 5, tranche 4).

Texas: Dallas, Tarrant, Collin, Harris, Bexar, Travis.
Oklahoma: Oklahoma, Cleveland, Comanche.

Each has unique county-level court/jurisdiction content, the district's
bankruptcy court, cities covered, and FAQs, with LocalBusiness+geo schema.
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

def county(slug, name, region, geo, seat, cities, courts_answer, bankruptcy_court,
           attorney_line):
    lede = (f"Newark Law Offices serves {name}, {region} — {cities} — across "
            f"bankruptcy, personal injury, criminal defense, and immigration. "
            f"Free, confidential consultation.")
    body = f"""            <h2>Serving {name}</h2>
            <p>{name} includes {cities}. The firm handles <a class="link" href="/bankruptcy-lawyer.html">bankruptcy</a>, <a class="link" href="/personal-injury.html">personal injury</a>, <a class="link" href="/criminal-defense-lawyer.html">criminal defense</a>, and <a class="link" href="/immigration-lawyer.html">immigration</a> matters throughout the county.</p>
{ans(f"Which courts serve {name}?", courts_answer)}
            <h2>Where cases are heard</h2>
            <p>The county seat is {seat}. {courts_answer}</p>
            <h2>Bankruptcy court</h2>
            <p>{bankruptcy_court}</p>
            <h2>Attorney</h2>
            <p>{attorney_line}</p>"""
    return LocationSpec(
        city=name, region=region, geo=geo, slug=slug,
        title=f"{name} Lawyer | Bankruptcy, Injury, Criminal, Immigration | Newark Law Offices",
        description=f"{name}, {region} attorneys for bankruptcy, personal injury, criminal defense, and immigration. Local court information. Free consultation. Call 866-230-7236.",
        h1=f"{name} attorneys — bankruptcy, personal injury, criminal defense, immigration",
        lede=lede, meta_tags=[name, region, "Local courts"],
        breadcrumb_name=name, cluster="Locations", cluster_hub="/locations.html",
        source=f"loc-{slug}", matter=f"General — {name}",
        rail_heading=f"Talk to us about a {name} matter",
        rail_lede="Tell us your matter and city. Phone and video consultations available.",
        knows_about=[f"{name} courts", f"{name} bankruptcy", f"{name} criminal defense"],
        related=RELATED, body_html=body,
        faqs=[
            (f"Do you handle cases in {name}?",
             f"Yes. The firm serves {name} across bankruptcy, personal injury, criminal defense, and immigration, with consultations by phone and video and court appearances as cases require."),
            ("Is the consultation free?",
             "Yes. The initial consultation is free and does not create an attorney-client relationship."),
        ])

PAGES = []

# --- Texas counties ---
PAGES.append(county(
    "dallas-county", "Dallas County", "TX", (32.7767, -96.7970), "Dallas",
    "Dallas, Irving, Garland, Mesquite, Richardson, and Grand Prairie",
    "Dallas County civil and family cases are heard at the George L. Allen Sr. Courts Building (600 Commerce St, Dallas); felony and misdemeanor criminal cases at the Frank Crowley Courts Building (133 N. Riverfront Blvd). Justice and small-claims matters are handled in the county's justice-of-the-peace precincts.",
    "Consumer bankruptcies for Dallas County are filed in the U.S. Bankruptcy Court for the Northern District of Texas, Dallas Division (Earle Cabell Federal Building, 1100 Commerce St).",
    "Handled from our Dallas office by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas."))
PAGES.append(county(
    "tarrant-county", "Tarrant County", "TX", (32.7717, -97.2919), "Fort Worth",
    "Fort Worth, Arlington, Grand Prairie, Mansfield, Euless, and Bedford",
    "Tarrant County civil cases are heard at the Tom Vandergriff Civil Courts Building and family matters at the Family Law Center; criminal cases at the Tim Curry Criminal Justice Center (401 W. Belknap St, Fort Worth).",
    "Consumer bankruptcies for Tarrant County are filed in the U.S. Bankruptcy Court for the Northern District of Texas, Fort Worth Division (501 W. 10th St).",
    "Handled from our Dallas office by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas."))
PAGES.append(county(
    "collin-county", "Collin County", "TX", (33.1795, -96.4930), "McKinney",
    "Plano, Frisco, McKinney, Allen, and Wylie",
    "Collin County civil, family, and criminal cases are heard at the Collin County Courthouse (2100 Bloomdale Rd, McKinney).",
    "Consumer bankruptcies for Collin County are filed in the U.S. Bankruptcy Court for the Eastern District of Texas, Plano Division (660 N. Central Expressway).",
    "Handled from our Dallas office by Robert C. Newark, III, licensed in Texas and admitted to the federal courts in Texas, including the Eastern District."))
PAGES.append(county(
    "harris-county", "Harris County", "TX", (29.7752, -95.3103), "Houston",
    "Houston, Pasadena, Baytown, and the greater Houston metro",
    "Harris County civil and family cases are heard at the Harris County Civil Courthouse (201 Caroline St, Houston); criminal cases at the Harris County Criminal Justice Center (1201 Franklin St).",
    "Consumer bankruptcies for Harris County are filed in the U.S. Bankruptcy Court for the Southern District of Texas, Houston Division (515 Rusk St).",
    "Served statewide by Robert C. Newark, III, licensed in Texas and admitted to the U.S. District Courts in Texas, including the Southern District, with phone/video consultations and Houston appearances as needed."))
PAGES.append(county(
    "bexar-county", "Bexar County", "TX", (29.4241, -98.4936), "San Antonio",
    "San Antonio and the surrounding metro",
    "Bexar County civil and family cases are heard at the Bexar County Courthouse and the Cadena-Reeves Justice Center (300 Dolorosa St, San Antonio); criminal cases at the Justice Center as well.",
    "Consumer bankruptcies for Bexar County are filed in the U.S. Bankruptcy Court for the Western District of Texas, San Antonio Division (615 E. Houston St).",
    "Served statewide by Robert C. Newark, III, licensed in Texas and admitted to the U.S. District Courts in Texas, including the Western District, with phone/video consultations and San Antonio appearances as needed."))
PAGES.append(county(
    "travis-county", "Travis County", "TX", (30.2672, -97.7431), "Austin",
    "Austin and the surrounding metro",
    "Travis County civil and family cases are heard at the Heman Marion Sweatt Travis County Courthouse (1000 Guadalupe St, Austin); criminal cases at the Blackwell-Thurman Criminal Justice Center (509 W. 11th St).",
    "Consumer bankruptcies for Travis County are filed in the U.S. Bankruptcy Court for the Western District of Texas, Austin Division (903 San Jacinto Blvd).",
    "Served statewide by Robert C. Newark, III, licensed in Texas and admitted to the U.S. District Courts in Texas, including the Western District, with phone/video consultations and Austin appearances as needed."))

# --- Oklahoma counties ---
PAGES.append(county(
    "oklahoma-county", "Oklahoma County", "OK", (35.4676, -97.5164), "Oklahoma City",
    "Oklahoma City, Edmond, Midwest City, and Del City",
    "Oklahoma County civil, family, and criminal cases are heard at the Oklahoma County Courthouse (321 Park Ave, Oklahoma City).",
    "Consumer bankruptcies for Oklahoma County are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma (215 Dean A. McGee Ave, Oklahoma City).",
    "Handled from our Edmond office by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma)."))
PAGES.append(county(
    "cleveland-county", "Cleveland County", "OK", (35.2226, -97.4395), "Norman",
    "Norman, Moore, and Noble",
    "Cleveland County civil, family, and criminal cases are heard at the Cleveland County Courthouse (200 S. Peters Ave, Norman).",
    "Consumer bankruptcies for Cleveland County are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma (215 Dean A. McGee Ave, Oklahoma City).",
    "Handled from our Edmond office by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma)."))
PAGES.append(county(
    "comanche-county", "Comanche County", "OK", (34.6087, -98.3903), "Lawton",
    "Lawton, Fort Sill, and Cache",
    "Comanche County civil, family, and criminal cases are heard at the Comanche County Courthouse (315 SW 5th St, Lawton).",
    "Consumer bankruptcies for Comanche County are filed in the U.S. Bankruptcy Court for the Western District of Oklahoma (215 Dean A. McGee Ave, Oklahoma City).",
    "Served by Robert C. Newark, III (licensed in Oklahoma and Texas) and Tyler Wilson (licensed in Oklahoma), with phone/video consultations and Comanche County appearances or local-counsel coordination as needed."))
