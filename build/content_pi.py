"""
Personal injury spoke cluster (PHASE 2).

The PI hub already exists at /personal-injury.html; these are spoke pages that
link back to it. TX/OK-framed, process-only, contingent-fee language matching
the existing PI page. No fabricated results, settlements, or statistics.
"""
from render_practice import PageSpec

HUB = "/personal-injury.html"

def ans(q, a):
    return (f'            <div class="answer-block">\n'
            f'              <h3 class="answer-q">{q}</h3>\n'
            f'              <div class="answer-a">{a}</div>\n'
            f'            </div>')

CONTINGENT = ("In appropriate cases these matters are handled on a contingent "
              "fee: the attorney fee is a percentage of any recovery, and no "
              "attorney fee is charged if there is no recovery. Case expenses "
              "are separate and are addressed in a written fee agreement.")

def pi(slug, title, desc, h1, lede, tags, bc, body, faqs, source, matter,
       related, knows):
    return PageSpec(
        slug=slug, title=title, description=desc, h1=h1, lede=lede,
        meta_tags=tags, breadcrumb_name=bc, cluster="Personal Injury",
        cluster_hub=HUB, source=source, matter=matter,
        rail_heading="Free case evaluation",
        rail_lede="Tell us the date, the state, injuries, and what the insurer has said. No fee unless you recover, in appropriate cases.",
        chat_greeting="Hurt in an accident in Texas or Oklahoma? Tell me what happened and I can point you to a free case evaluation.",
        knows_about=knows, related=related, body_html=body, faqs=faqs)

PAGES = []

PAGES.append(pi(
    "personal-injury-lawyer",
    "Personal Injury Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Personal injury lawyer for Texas and Oklahoma — car, truck, motorcycle, wrongful death, premises liability. Free case evaluation. Call 866-230-7236.",
    "Personal injury lawyer for Texas and Oklahoma",
    "From car and truck wrecks to premises liability and wrongful death, Newark Law Offices reviews how a claim actually works, what coverage applies, and whether an insurer's offer matches the loss. Offices in Dallas and Edmond. Free case evaluation.",
    ["Personal injury", "Dallas & Edmond", "No fee unless you recover"],
    "Personal Injury Lawyer",
    f"""            <h2>How a personal injury claim works</h2>
{ans("How does a personal injury claim work?", "A personal injury claim seeks compensation from the at-fault party (usually through their insurer) for losses caused by negligence — medical bills, lost income, and pain and suffering. The steps are: get medical treatment and document it, identify every applicable insurance policy, establish liability, and value the full loss before settling. Both Texas and Oklahoma follow at-fault rules and comparative negligence, and most injury suits have a two-year limitations window that specific facts can change.")}
            <h2>Matters we handle</h2>
            <ul>
              <li><a class="link" href="/car-accidents.html">Car accidents</a>, <a class="link" href="/truck-accidents.html">truck accidents</a>, and <a class="link" href="/motorcycle-accidents.html">motorcycle accidents</a></li>
              <li><a class="link" href="/wrongful-death.html">Wrongful death</a> and <a class="link" href="/catastrophic-injury.html">catastrophic injury</a></li>
              <li><a class="link" href="/premises-liability.html">Premises liability</a>, <a class="link" href="/slip-and-fall.html">slip and fall</a>, and <a class="link" href="/negligent-security.html">negligent security</a></li>
              <li><a class="link" href="/commercial-vehicle-accidents.html">Commercial vehicle accidents</a> and <a class="link" href="/insurance-disputes.html">insurance disputes</a></li>
            </ul>
            <h2>Why the insurer's first call is not the finish line</h2>
            <p>Early offers often arrive before the medical picture is clear and rarely include future care, lost earning capacity, or every available coverage layer. We map the coverage and value the full loss before anyone signs.</p>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("How long do I have to file an injury claim?",
      "Many Texas and Oklahoma injury claims run on a two-year limitations clock, but notice rules, minors, and government defendants can change the date. Calendar the incident and call early."),
     ("Should I sign the insurer's first offer?",
      "Usually not before a review. Early offers often come before future care and full coverage are known.")],
    "pi-hub-lawyer", "Personal injury — general",
    [("Car accidents", "/car-accidents.html"), ("Truck accidents", "/truck-accidents.html"),
     ("Wrongful death", "/wrongful-death.html"), ("Personal injury hub", HUB)],
    ["personal injury", "car accidents", "truck accidents", "wrongful death"]))

PAGES.append(pi(
    "car-accidents",
    "Car Accident Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Car accident claim review in Texas and Oklahoma — liability, UM/UIM coverage, and settlement offers. Free case evaluation. Call 866-230-7236.",
    "Car accident claims in Texas and Oklahoma",
    "Injured in a crash? We review liability, every insurance layer including uninsured/underinsured motorist coverage, and whether an offer reflects the real loss. Free case evaluation.",
    ["Car accidents", "UM/UIM", "Texas & Oklahoma"], "Car Accidents",
    f"""            <h2>What we review after a crash</h2>
{ans("What should I do after a car accident?", "Get medical care and keep every record; photograph the vehicles, scene, and injuries; identify every policy (at-fault driver, your own liability, PIP/med-pay, and UM/UIM); and do not give a recorded statement or sign a release before a review. In Texas and Oklahoma the at-fault driver's insurer is the starting point, comparative negligence can reduce recovery, and most claims run on a two-year clock.")}
            <h2>Coverage we map on every file</h2>
            <ul>
              <li>At-fault driver's liability limits</li>
              <li>Your own liability, PIP, or med-pay</li>
              <li>Uninsured/underinsured motorist coverage on household policies</li>
              <li>Rideshare or commercial layers when applicable</li>
              <li>Health-insurance liens that come out of a settlement</li>
            </ul>
            <p>See the firm's <a class="link" href="/insights/after-a-car-crash-texas-oklahoma.html">72-hour post-crash practice note</a>.</p>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("What if the other driver had no insurance?",
      "Your own uninsured/underinsured motorist (UM/UIM) coverage may apply. Identifying every policy is the first thing we do."),
     ("How long do I have to file?",
      "Often about two years in Texas and Oklahoma, but the real date depends on the facts. Call if a crash is approaching a year old.")],
    "pi-car-accidents", "Personal injury — car accident",
    [("Truck accidents", "/truck-accidents.html"), ("Motorcycle accidents", "/motorcycle-accidents.html"),
     ("Insurance disputes", "/insurance-disputes.html"), ("Personal injury hub", HUB)],
    ["car accidents", "UM UIM claims", "comparative negligence"]))

PAGES.append(pi(
    "truck-accidents",
    "Truck Accident Lawyer | Texas & Oklahoma | Newark Law Offices",
    "18-wheeler and commercial truck accident claims in Texas and Oklahoma — federal safety rules, multiple defendants, and evidence preservation. Free case evaluation.",
    "Truck accident claims in Texas and Oklahoma",
    "Commercial truck wrecks involve federal safety rules, multiple potentially liable parties, and evidence that can disappear fast. We move to preserve it and identify every source of coverage. Free case evaluation.",
    ["Truck accidents", "18-wheelers", "FMCSA rules"], "Truck Accidents",
    f"""            <h2>Why truck cases are different</h2>
{ans("Why are truck accident claims different from car accidents?", "Commercial trucks are governed by Federal Motor Carrier Safety Administration (FMCSA) rules, and liability can extend beyond the driver to the motor carrier, the truck's owner, a maintenance provider, or a shipper. Key evidence — logbooks, electronic logging data, maintenance records, and dashcam footage — can be lost if not preserved quickly, so a prompt spoliation/preservation demand matters. Coverage limits on commercial policies are usually far higher than on personal auto.")}
            <h2>What we pursue early</h2>
            <ul>
              <li>Preservation of driver logs, ELD data, and maintenance records</li>
              <li>The carrier's and driver's commercial coverage layers</li>
              <li>Whether hours-of-service or maintenance rules were violated</li>
              <li>All potentially liable parties, not just the driver</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Who can be responsible in a truck accident?",
      "Beyond the driver, the motor carrier, truck owner, maintenance provider, or shipper may share liability depending on the facts."),
     ("Why act quickly after a truck wreck?",
      "Critical evidence like logs and ELD data can be lost. A prompt preservation demand helps protect the claim.")],
    "pi-truck-accidents", "Personal injury — truck accident",
    [("Commercial vehicle accidents", "/commercial-vehicle-accidents.html"),
     ("Car accidents", "/car-accidents.html"), ("Catastrophic injury", "/catastrophic-injury.html"),
     ("Personal injury hub", HUB)],
    ["truck accidents", "FMCSA", "commercial trucking liability"]))

PAGES.append(pi(
    "motorcycle-accidents",
    "Motorcycle Accident Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Motorcycle accident claims in Texas and Oklahoma — bias, serious injuries, and coverage. Free case evaluation. Call 866-230-7236.",
    "Motorcycle accident claims in Texas and Oklahoma",
    "Motorcyclists face serious injuries and unfair bias from insurers. We build the liability picture on facts, not stereotypes, and pursue every coverage layer. Free case evaluation.",
    ["Motorcycle accidents", "Serious injury", "Anti-bias"], "Motorcycle Accidents",
    f"""            <h2>Fighting the bias</h2>
{ans("Are motorcycle accident claims harder because of rider bias?", "Insurers sometimes assume a motorcyclist was at fault or riding recklessly. A claim is decided on evidence — scene photos, witness accounts, the other driver's actions, and physical evidence — not on stereotypes. Motorcycle injuries tend to be severe, so valuing future medical care and lost earning capacity accurately is essential before any settlement.")}
            <h2>What we document</h2>
            <ul>
              <li>The other driver's conduct (left turns, lane changes, failure to yield)</li>
              <li>Scene and vehicle evidence, and any available video</li>
              <li>The full medical picture, including future care</li>
              <li>Every applicable policy, including UM/UIM</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Does not wearing a helmet hurt my claim?",
      "It can become an argument, but it does not automatically bar recovery. Liability still turns on who caused the crash. Bring the facts to a review.")],
    "pi-motorcycle", "Personal injury — motorcycle accident",
    [("Car accidents", "/car-accidents.html"), ("Catastrophic injury", "/catastrophic-injury.html"),
     ("Personal injury hub", HUB)],
    ["motorcycle accidents", "rider bias", "UM UIM"]))

PAGES.append(pi(
    "wrongful-death",
    "Wrongful Death Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Wrongful death claims in Texas and Oklahoma — who can file, what is recoverable, and deadlines. Compassionate, free case evaluation. Call 866-230-7236.",
    "Wrongful death claims in Texas and Oklahoma",
    "When negligence takes a family member, a wrongful death claim can hold the responsible party accountable and provide for those left behind. We handle these matters with care. Free case evaluation.",
    ["Wrongful death", "Surviving family", "Compassionate"], "Wrongful Death",
    f"""            <h2>What a wrongful death claim covers</h2>
{ans("Who can file a wrongful death claim and what is recoverable?", "A wrongful death claim is brought by statutorily authorized family members — typically a spouse, children, or parents — and, in some cases, the estate. Recoverable losses can include lost financial support and services, loss of companionship, funeral and medical expenses, and (through a survival claim) the decedent's own pre-death losses. Texas and Oklahoma each set who may recover and the deadlines, which are usually two years but fact-dependent.")}
            <h2>How we approach these cases</h2>
            <p>We investigate liability thoroughly, coordinate with the estate where needed, and value the loss with the seriousness it deserves — while keeping the family informed at every step.</p>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Who can bring a wrongful death case?",
      "Usually a surviving spouse, children, or parents, and sometimes the estate. The specific rules differ in Texas and Oklahoma."),
     ("How long do we have to file?",
      "Often about two years, but the date depends on the facts. Contact the firm early so nothing is lost.")],
    "pi-wrongful-death", "Personal injury — wrongful death",
    [("Catastrophic injury", "/catastrophic-injury.html"), ("Truck accidents", "/truck-accidents.html"),
     ("Personal injury hub", HUB)],
    ["wrongful death", "survival claim", "surviving family recovery"]))

PAGES.append(pi(
    "premises-liability",
    "Premises Liability Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Premises liability claims in Texas and Oklahoma — unsafe property, duty owed, and proving notice. Free case evaluation. Call 866-230-7236.",
    "Premises liability in Texas and Oklahoma",
    "Property owners must keep their premises reasonably safe. When they do not and someone is hurt, a premises liability claim can follow. We evaluate duty, notice, and the loss. Free case evaluation.",
    ["Premises liability", "Unsafe property", "Notice"], "Premises Liability",
    f"""            <h2>What a premises case requires</h2>
{ans("What do I have to prove in a premises liability case?", "You generally must show the property owner or occupier owed you a duty of care, that a dangerous condition existed, that the owner knew or should have known about it (notice), that the owner failed to fix or warn of it, and that this caused your injury. The duty owed depends on why you were on the property (invitee, licensee, or trespasser), which Texas and Oklahoma define. Proving notice — that the hazard existed long enough that the owner should have addressed it — is often the key issue.")}
            <h2>Common premises claims</h2>
            <ul>
              <li><a class="link" href="/slip-and-fall.html">Slip and fall</a> on unsafe floors or walkways</li>
              <li><a class="link" href="/negligent-security.html">Negligent security</a> leading to assault or harm</li>
              <li>Falling merchandise, unsafe stairs, or inadequate lighting</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Is a business automatically liable if I fall?",
      "No. You generally must show the owner knew or should have known about the hazard and failed to address it. That notice question is often the heart of the case.")],
    "pi-premises", "Personal injury — premises liability",
    [("Slip and fall", "/slip-and-fall.html"), ("Negligent security", "/negligent-security.html"),
     ("Personal injury hub", HUB)],
    ["premises liability", "duty of care", "notice", "invitee licensee"]))

PAGES.append(pi(
    "slip-and-fall",
    "Slip and Fall Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Slip and fall claims in Texas and Oklahoma — proving the hazard and notice, and documenting injuries. Free case evaluation. Call 866-230-7236.",
    "Slip and fall claims in Texas and Oklahoma",
    "A fall on someone else's property can cause lasting injury. The claim turns on the hazard, whether the owner should have known, and prompt documentation. Free case evaluation.",
    ["Slip and fall", "Documentation", "Notice"], "Slip and Fall",
    f"""            <h2>What makes a slip-and-fall claim work</h2>
{ans("What should I do after a slip and fall?", "Report the fall to the property owner or manager and ask for an incident report; photograph the hazard (spill, ice, uneven surface) before it is cleaned up; get names of witnesses; and seek medical care promptly. A slip-and-fall claim depends on showing the owner knew or should have known about the hazard and failed to fix or warn of it, so evidence captured right away is often decisive.")}
            <h2>What we gather</h2>
            <ul>
              <li>Photos of the hazard and the scene</li>
              <li>Incident reports and any surveillance video</li>
              <li>Witness statements</li>
              <li>Medical records tying the injury to the fall</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("What if I did not report the fall right away?",
      "It can complicate the claim but does not always end it. Prompt medical care and any photos or witnesses still help. Bring what you have to a review.")],
    "pi-slip-fall", "Personal injury — slip and fall",
    [("Premises liability", "/premises-liability.html"), ("Negligent security", "/negligent-security.html"),
     ("Personal injury hub", HUB)],
    ["slip and fall", "hazard notice", "incident report"]))

PAGES.append(pi(
    "negligent-security",
    "Negligent Security Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Negligent security claims in Texas and Oklahoma — when a property owner's failure to provide security leads to assault or harm. Free case evaluation.",
    "Negligent security in Texas and Oklahoma",
    "When a foreseeable crime happens because a property owner failed to provide reasonable security, the owner may share responsibility. We evaluate foreseeability and the security that was — or was not — in place. Free case evaluation.",
    ["Negligent security", "Foreseeability", "Premises"], "Negligent Security",
    f"""            <h2>The foreseeability question</h2>
{ans("What is a negligent security claim?", "Negligent security is a type of premises liability claim: when a property owner should have foreseen a risk of crime (based on prior incidents or the area) and failed to provide reasonable security — lighting, locks, cameras, or personnel — and that failure allowed a foreseeable assault or harm, the owner may be liable. The central issues are whether the harm was foreseeable and whether the security in place was reasonable.")}
            <h2>What we investigate</h2>
            <ul>
              <li>Prior crimes at or near the property</li>
              <li>Lighting, locks, cameras, and security staffing</li>
              <li>Whether warnings or measures were reasonable for the risk</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Can a property owner be liable for someone else's crime?",
      "In some cases, yes — where the crime was foreseeable and the owner failed to provide reasonable security. Foreseeability is the key issue.")],
    "pi-negligent-security", "Personal injury — negligent security",
    [("Premises liability", "/premises-liability.html"), ("Slip and fall", "/slip-and-fall.html"),
     ("Personal injury hub", HUB)],
    ["negligent security", "foreseeable crime", "premises liability"]))

PAGES.append(pi(
    "commercial-vehicle-accidents",
    "Commercial Vehicle Accident Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Commercial vehicle accident claims in Texas and Oklahoma — delivery vans, work trucks, and company fleets. Higher coverage, multiple defendants. Free case evaluation.",
    "Commercial vehicle accident claims",
    "Crashes with delivery vans, work trucks, and company fleets bring employer liability and higher coverage into play. We identify every responsible party and coverage layer. Free case evaluation.",
    ["Commercial vehicles", "Employer liability", "Fleet coverage"], "Commercial Vehicle Accidents",
    f"""            <h2>When a company vehicle is involved</h2>
{ans("Who is liable in a commercial vehicle accident?", "When a driver was working at the time of the crash, the employer can be liable for the employee's negligence (respondeat superior), and separate claims like negligent hiring or maintenance may apply. Commercial policies usually carry higher limits than personal auto, and there may be multiple defendants — the driver, the employer, and a vehicle owner or maintenance provider.")}
            <h2>What we pursue</h2>
            <ul>
              <li>Whether the driver was on the job at the time</li>
              <li>The employer's commercial coverage</li>
              <li>Maintenance and hiring records where relevant</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Is the company liable if their employee hit me?",
      "Often yes, if the employee was working at the time. The employer's higher commercial coverage frequently applies.")],
    "pi-commercial-vehicle", "Personal injury — commercial vehicle",
    [("Truck accidents", "/truck-accidents.html"), ("Car accidents", "/car-accidents.html"),
     ("Personal injury hub", HUB)],
    ["commercial vehicle accidents", "employer liability", "respondeat superior"]))

PAGES.append(pi(
    "insurance-disputes",
    "Insurance Dispute Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Insurance disputes in Texas and Oklahoma — underpaid, delayed, or denied claims, and bad-faith conduct. Free case evaluation. Call 866-230-7236.",
    "Insurance disputes in Texas and Oklahoma",
    "When an insurer underpays, delays, or denies a valid claim, you have options. We evaluate the policy, the denial, and whether the carrier's conduct crossed into bad faith. Free case evaluation.",
    ["Insurance disputes", "Denied claims", "Bad faith"], "Insurance Disputes",
    f"""            <h2>When the carrier will not pay fairly</h2>
{ans("What can I do if my insurance claim was denied or underpaid?", "Start by getting the denial in writing and the policy language it relies on. Insurers in Texas and Oklahoma owe duties to handle claims reasonably and promptly; an unreasonable denial, delay, or lowball can support a dispute and, in some cases, a bad-faith or statutory claim. Deadlines in the policy and by statute apply, so a prompt review of the denial and the policy is important.")}
            <h2>What we review</h2>
            <ul>
              <li>The policy language and the stated reason for denial</li>
              <li>Whether the carrier investigated and paid reasonably</li>
              <li>Deadlines in the policy and under state law</li>
            </ul>
            <p>Related storm-claim pages: <a class="link" href="/wind-hail-damage-claim-texas.html">Wind &amp; hail (Texas)</a> &middot; <a class="link" href="/wind-hail-damage-claim-oklahoma.html">Wind &amp; hail (Oklahoma)</a>.</p>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("What is insurance bad faith?",
      "Broadly, it is an insurer's unreasonable handling of a valid claim — denying, delaying, or underpaying without a reasonable basis. Whether conduct rises to bad faith depends on the facts and state law.")],
    "pi-insurance-disputes", "Personal injury — insurance dispute",
    [("Car accidents", "/car-accidents.html"), ("Wind & hail (Texas)", "/wind-hail-damage-claim-texas.html"),
     ("Personal injury hub", HUB)],
    ["insurance disputes", "bad faith", "denied claim"]))

PAGES.append(pi(
    "catastrophic-injury",
    "Catastrophic Injury Lawyer | Texas & Oklahoma | Newark Law Offices",
    "Catastrophic injury claims in Texas and Oklahoma — brain and spinal injuries, burns, amputations, and lifetime care. Free case evaluation. Call 866-230-7236.",
    "Catastrophic injury claims in Texas and Oklahoma",
    "Life-altering injuries demand a claim built around lifetime care and lost earning capacity, not just current bills. We work with the right experts to value the full future loss. Free case evaluation.",
    ["Catastrophic injury", "Lifetime care", "Future loss"], "Catastrophic Injury",
    f"""            <h2>Valuing a lifetime, not a moment</h2>
{ans("What makes an injury 'catastrophic' in a legal claim?", "A catastrophic injury is one with long-term or permanent effects — traumatic brain injury, spinal cord injury, serious burns, amputation, or injuries requiring lifelong care. Valuing such a claim requires more than current medical bills: it means projecting future medical care, assistive needs, home modifications, and lost earning capacity, often with medical and economic experts. Settling before that full picture is established risks leaving the future uncovered.")}
            <h2>What we build into the claim</h2>
            <ul>
              <li>Life-care plans and future medical projections</li>
              <li>Lost earning capacity and vocational impact</li>
              <li>Every available coverage layer</li>
            </ul>""",
    [("Do I pay a fee if there is no recovery?", CONTINGENT),
     ("Why not settle a serious injury quickly?",
      "Because future care and lost earning capacity may far exceed current bills. Settling before the full picture is known can leave the future uncovered.")],
    "pi-catastrophic", "Personal injury — catastrophic injury",
    [("Wrongful death", "/wrongful-death.html"), ("Truck accidents", "/truck-accidents.html"),
     ("Personal injury hub", HUB)],
    ["catastrophic injury", "life care plan", "lost earning capacity"]))
