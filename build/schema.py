"""
JSON-LD schema builders for Newark Law Offices.

Mirrors the schema already present on the live site (LegalService, Attorney,
FAQPage, HowTo, BreadcrumbList) so structured data stays consistent. Adds
LocalBusiness (with geo) for location pages.

No AggregateRating / Review objects are emitted here. Ratings and reviews are
only rendered from a human-approved data file (see reviews approval workflow);
fabricated ratings are prohibited and would be an attorney-advertising problem.
"""
import json

SITE = "https://newarkfirm.com"

DALLAS_ADDR = {
    "@type": "PostalAddress",
    "streetAddress": "1341 W. Mockingbird Ln, Ste 600W",
    "addressLocality": "Dallas", "addressRegion": "TX",
    "postalCode": "75247", "addressCountry": "US",
}
EDMOND_ADDR = {
    "@type": "PostalAddress",
    "streetAddress": "1019 Waterwood Pkwy, Ste C",
    "addressLocality": "Edmond", "addressRegion": "OK",
    "postalCode": "73034", "addressCountry": "US",
}
PHONES = ["+1-866-230-7236", "+1-972-332-5733", "+1-405-727-0269"]


def _dump(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)


def legal_service(name, url, description, *, area_served=None, knows_about=None,
                  service_type=None):
    obj = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "name": name,
        "url": url,
        "description": description,
        "telephone": PHONES,
        "email": "potentialclient@newarkfirm.com",
        "image": f"{SITE}/rob-headshot.jpg",
        "priceRange": "$$",
        "areaServed": area_served or ["Texas", "Oklahoma"],
        "address": [DALLAS_ADDR, EDMOND_ADDR],
        "provider": {"@type": "Person", "name": "Robert C. Newark, III"},
    }
    if service_type:
        obj["serviceType"] = service_type
    if knows_about:
        obj["knowsAbout"] = knows_about
    return _dump(obj)


def faq_page(qa_pairs):
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in qa_pairs
        ],
    }
    return _dump(obj)


def breadcrumbs(trail):
    """trail: list of (name, url)."""
    obj = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(trail)
        ],
    }
    return _dump(obj)


def local_business(name, url, city, region, description, *, geo=None,
                   address=None, phone=None):
    obj = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "name": name,
        "url": url,
        "description": description,
        "telephone": phone or "+1-866-230-7236",
        "email": "potentialclient@newarkfirm.com",
        "image": f"{SITE}/rob-headshot.jpg",
        "priceRange": "$$",
        "areaServed": {"@type": "City", "name": city},
        "address": address or (DALLAS_ADDR if region == "TX" else EDMOND_ADDR),
        "provider": {"@type": "Person", "name": "Robert C. Newark, III"},
    }
    if geo:
        obj["geo"] = {"@type": "GeoCoordinates",
                      "latitude": geo[0], "longitude": geo[1]}
    return _dump(obj)
