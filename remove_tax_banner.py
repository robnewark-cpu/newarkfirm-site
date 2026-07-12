import re

files = ["about.html", "contact.html", "disclaimer.html", "experience.html",
         "index.html", "insights.html", "people.html"]

for fname in files:
    with open(fname, 'r') as f:
        content = f.read()
    original = content

    # Remove the nav "Pandemic Tax Relief" link
    content = re.sub(
        r'\s*<li class="irs-conditional">.*?</li>\n?',
        '\n', content, flags=re.DOTALL
    )

    # Remove the urgency banner section
    content = re.sub(
        r'\s*<section class="urgency-banner irs-conditional">.*?</section>\n?',
        '\n', content, flags=re.DOTALL
    )

    # Remove ONLY the specific script block that references irs-conditional
    content = re.sub(
        r'\s*<script>\s*document\.addEventListener\("DOMContentLoaded".*?irs-conditional.*?</script>\n?',
        '\n', content, flags=re.DOTALL
    )

    if content != original:
        with open(fname, 'w') as f:
            f.write(content)
        print(f"{fname}: CHANGED")
    else:
        print(f"{fname}: no match found (needs manual check)")

print("\nDone.")
