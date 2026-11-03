#!/usr/bin/env python3
"""Generates the static site into ./public. Two pages only: / and /personal-appearance-questionaire/."""
import os, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "public")
SITE = "https://www.tansaloninsurance.com"
NAME = "Tan Salon Insurance"
FORM_PATH = "/personal-appearance-questionaire/"
JOTFORM_SCRIPT = '<script type="text/javascript" src="https://form.jotform.com/jsform/241234750255047"></script>'

esc = lambda s: html.escape(s, quote=False)
attr = lambda s: html.escape(s, quote=True)

def write(rel, content):
    p = os.path.join(PUB, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

ICONS = {
 "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></svg>',
 "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V5l8-2v18M12 9h8v12M4 21h16M8 8h1M8 12h1M8 16h1M16 13h1M16 17h1"/></svg>',
 "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5M3 17.5l9 5 9-5"/></svg>',
 "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 16l1.5-5.5A2 2 0 018.4 9h7.2a2 2 0 011.9 1.5L19 16M3 16h18v3H3zM7 19v1.5M17 19v1.5"/><circle cx="7.5" cy="16" r=".6"/><circle cx="16.5" cy="16" r=".6"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
}
LOGO = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#1b3358"/>'
        '<circle cx="24" cy="24" r="8" fill="#e8923a"/><g stroke="#e8923a" stroke-width="2.6" stroke-linecap="round">'
        '<path d="M24 7v4M24 37v4M7 24h4M37 24h4M12 12l2.8 2.8M33.2 33.2L36 36M12 36l2.8-2.8M33.2 14.8L36 12"/></g></svg>')

SERVICES = ["Barbers", "Cosmetologists", "Estheticians", "Massage Therapists", "Booth Rentals",
            "Independent Contractors", "Beauty Schools", "Manicurists",
            "Tanning Salons, Including Spray-On and Airbrush Tanning"]

COVERAGES = [
 ("shield", "General & Professional Liability", "Protection if a client says they were injured at your business or by your services, including chemical burns, with no cancer exclusion."),
 ("building", "Property Coverage", "Replacement cost on your building and contents, plus business income loss, crime, signs and equipment breakdown."),
 ("layers", "Umbrella Liability", "Extra protection above your general liability or commercial auto limit if a catastrophic lawsuit hits, up to $10,000,000."),
 ("car", "Commercial Auto", "Commercial auto coverage is available for vehicles used in your business."),
]

FAQ = [
 ("General", [
  ("What payment plans are available?", "Premiums can be paid by automatic bank draft on a monthly, quarterly, semi-annual or annual basis."),
  ("What forms of payment do you accept?", "We accept Mastercard, Visa, Discover and American Express."),
  ("What is the difference between an additional insured and a loss payee?", "An additional insured, such as your landlord, is added to your liability policy so it is also protected if a claim involves the premises you lease. A loss payee, such as the company that leases you tanning-bed equipment, is named on your property coverage so it is paid for its interest in that equipment if it is damaged or destroyed."),
 ]),
 ("General and Professional Liability", [
  ("What liability limits do you recommend?", "We generally recommend limits starting at $300,000 and going up to an aggregate of $3 million, depending on your business. A quote request lets us match the limits to your situation."),
  ("Are booth renters and independent contractors covered?", "Booth renters and independent contractors are not your employees, but they can be insured as though they were. They are covered only for work performed at your business."),
  ("What is the difference between occurrence and aggregate limits?", "The occurrence limit is the most the policy pays for any single claim. The aggregate limit is the most it pays in total for all claims during the policy period."),
  ("What does professional liability mean?", "Professional liability covers claims that your services caused harm, such as a bad result from a treatment or service you provided to a client."),
  ("Is a chemical burn covered?", "Yes. A chemical burn from a service you perform is covered under professional liability."),
  ("Does a client waiver card protect me from being sued?", "No. A waiver card does not stop a client from suing you and does not prevent you from being found liable. Liability insurance is what protects you if that happens."),
  ("Are there cancer exclusions?", "No. Our tanning coverage has no cancer exclusions."),
 ]),
 ("Property", [
  ("What property coverage is available?", "Coverage is available on a replacement cost basis for your building and contents. Options include business income loss, crime, sign and equipment breakdown coverage."),
 ]),
 ("Umbrella", [
  ("What does an umbrella policy do?", "An umbrella policy protects you against a catastrophic lawsuit by paying above the limit of your general liability or commercial auto liability policy, with limits up to $10,000,000."),
 ]),
 ("Auto", [
  ("Is commercial auto available?", "Yes, commercial auto insurance is available for vehicles used in your business."),
 ]),
]

def faq_html():
    out = ['<div class="faq">']
    for grp, items in FAQ:
        out.append(f'<div class="faq-group"><h3>{esc(grp)}</h3>')
        for q, a in items:
            out.append(f'<details><summary>{esc(q)}</summary><div class="a"><p>{esc(a)}</p></div></details>')
        out.append('</div>')
    out.append('</div>')
    return "\n".join(out)

def faq_node():
    return {"@type": "FAQPage", "@id": SITE + "/#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for _, items in FAQ for q, a in items]}

def org_node():
    return {"@type": ["InsuranceAgency", "Organization"], "@id": SITE + "/#org", "name": NAME, "url": SITE + "/",
            "logo": SITE + "/assets/images/logo.png", "image": SITE + "/assets/images/og-image.jpg",
            "description": "Insurance for tanning salons, barbers, cosmetologists, estheticians, massage therapists, manicurists, booth renters and beauty schools. Insuring personal appearance services since 1973.",
            "slogan": "Not all tanning insurance is created equal.",
            "knowsAbout": ["Tanning salon insurance", "Salon liability insurance", "Professional liability insurance", "Booth renter insurance", "Beauty school insurance", "Umbrella liability", "Commercial auto"]}

def header(path):
    cur = lambda p: ' aria-current="page"' if p == path else ""
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="/" aria-label="{NAME} home">{LOGO}<span><b>Tan Salon Insurance</b><small>Personal appearance insurance since 1973</small></span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav" type="button">Menu</button>
<nav class="site-nav" id="primary-nav" aria-label="Primary"><ul>
<li><a href="/#coverage">Coverage</a></li><li><a href="/#who">Who We Insure</a></li><li><a href="/#faq">FAQ</a></li>
<li><a class="cta" href="{FORM_PATH}"{cur(FORM_PATH)}>Get a Free Quote</a></li></ul></nav></div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap"><div class="footer-grid">
<div><h2>{NAME}</h2><p>Insurance for tanning salons and personal appearance professionals. Insuring personal appearance services since 1973, with coverage backed by great carriers.</p></div>
<div><h2>Explore</h2><ul><li><a href="/#coverage">Coverage</a></li><li><a href="/#who">Who we insure</a></li><li><a href="/#faq">FAQ</a></li></ul></div>
<div><h2>Get started</h2><ul><li><a href="{FORM_PATH}">Request a free quote</a></li></ul></div>
</div><div class="legal">&copy; {NAME}. All rights reserved.</div></div></footer>'''

def layout(path, title, desc, body, kind, crumbs, faqs=False, extra_head=""):
    url = SITE + path
    graph = [org_node(),
             {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-US"},
             {"@type": kind, "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"},
              "about": {"@id": SITE + "/#org"}, "inLanguage": "en-US", "primaryImageOfPage": SITE + "/assets/images/og-image.jpg"},
             {"@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(crumbs)]}]
    if faqs: graph.append(faq_node())
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{attr(desc)}">
<link rel="canonical" href="{url}"><meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#1b3358">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{attr(title)}">
<meta property="og:description" content="{attr(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/images/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{attr(title)}"><meta name="twitter:description" content="{attr(desc)}">
<meta name="twitter:image" content="{SITE}/assets/images/og-image.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/css/styles.css">
<script type="application/ld+json">{ld}</script>{extra_head}</head>
<body>
{header(path)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/js/main.js" defer></script>
</body></html>
'''

def cta_band():
    return f'''<section class="cta-band"><div class="wrap"><h2>Ready for a quote built for your business?</h2>
<p>Tell us about your salon or personal appearance business and we will come back with coverage options. It is free and takes a few minutes.</p>
<div class="btn-row"><a class="btn" href="{FORM_PATH}">Get a Free Quote</a></div></div></section>'''

def page_home():
    cov = "".join(f'<div class="card"><div class="ico">{ICONS[i]}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, t, d in COVERAGES)
    chips = "".join(f"<li>{esc(s)}</li>" for s in SERVICES)
    body = f'''<section class="hero"><div class="wrap">
<span class="eyebrow">Insuring personal appearance services since 1973</span>
<h1>Not All Tanning Insurance Is Created Equal</h1>
<p class="lede">Coverage for tanning salons and personal appearance businesses from a team that has focused on these markets for decades, with great carriers behind every policy.</p>
<div class="btn-row"><a class="btn" href="{FORM_PATH}">Get a Free Quote</a><a class="btn alt" href="#coverage">See What We Cover</a></div>
<span class="badge">{ICONS["check"]} No cancer exclusions</span></div></section>
<section class="trust"><div class="wrap"><ul>
<li><strong>Since 1973</strong><span>Focused on personal appearance</span></li>
<li><strong>No Cancer Exclusions</strong><span>On tanning coverage</span></li>
<li><strong>Flexible Payments</strong><span>Monthly to annual bank draft</span></li>
<li><strong>Free Quotes</strong><span>Quick online request</span></li></ul></div></section>
<section class="section"><div class="wrap">
<div class="answer"><p><strong>Tan Salon Insurance provides liability, property, umbrella and commercial auto insurance for tanning salons, barbers, cosmetologists, estheticians, massage therapists, manicurists, booth renters and beauty schools.</strong> We have insured personal appearance services since 1973, and our tanning coverage has no cancer exclusions.</p></div>
<div class="section-head" id="coverage"><h2>Coverage built for personal appearance businesses</h2>
<p>Generic business policies often leave gaps in this industry. We focus on these markets so your coverage fits the way you actually work.</p></div>
<div class="grid g4">{cov}</div></div></section>
<section class="section alt" id="who"><div class="wrap"><div class="split"><div>
<h2>Who we insure</h2>
<p>If you provide personal appearance services, from a single booth to a full salon, we can help you find the right protection.</p>
<ul class="chips">{chips}</ul></div>
<div class="card"><h3>Why choose a specialist</h3><ul class="checks">
<li>Insuring personal appearance services since 1973</li>
<li>No cancer exclusions on tanning coverage</li>
<li>Booth renters and independent contractors can be insured</li>
<li>Coverage backed by great carriers</li>
<li>Pay by automatic bank draft, monthly to annual</li></ul>
<a class="btn navy" href="{FORM_PATH}">Request a Free Quote</a></div></div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><h2>How to get covered</h2><p>Three simple steps.</p></div>
<ol class="steps">
<li><h3>Fill out the questionnaire</h3><p>Tell us about your business using our short personal appearance questionnaire.</p></li>
<li><h3>Review your options</h3><p>We match you with coverage and limits that fit your business.</p></li>
<li><h3>Start your policy</h3><p>Choose a payment plan that suits you and get protected.</p></li></ol></div></section>
<section class="section alt" id="faq"><div class="wrap"><div class="section-head"><h2>Frequently asked questions</h2>
<p>Straight answers about payment, liability, property, umbrella and auto coverage.</p></div>
{faq_html()}</div></section>
{cta_band()}'''
    return layout("/", "Tanning Salon & Beauty Business Insurance Since 1973 | Tan Salon Insurance",
        "Insurance for tanning salons, barbers, cosmetologists, estheticians, massage therapists and booth renters. No cancer exclusions. Insuring personal appearance since 1973.",
        body, "WebPage", [("Home", "/")], faqs=True)

def page_form():
    body = f'''<section class="page-hero"><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Free Quote</li></ol></nav>
<h1>Personal Appearance Questionnaire</h1>
<p>Please fill out the information below to receive a free quote.</p></div></section>
<section class="section"><div class="wrap"><div class="split">
<div class="form-card">{JOTFORM_SCRIPT}</div>
<aside class="side card"><h2>What happens next</h2><ul class="checks">
<li>We review your answers</li><li>We match you with coverage and limits for your business</li><li>You choose a payment plan that fits</li></ul>
<p>Coverage is available for tanning salons, barbers, cosmetologists, estheticians, massage therapists, manicurists, booth renters, independent contractors and beauty schools.</p>
<p><a href="/#faq">Read the coverage FAQ</a></p></aside></div></div></section>'''
    return layout(FORM_PATH, "Free Quote Request | Personal Appearance Questionnaire | Tan Salon Insurance",
        "Fill out the personal appearance questionnaire to get a free insurance quote for your tanning salon, salon, spa or booth rental business.",
        body, "ContactPage", [("Home", "/"), ("Free Quote", FORM_PATH)])

def page_404():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Page not found</h1><p>That page does not exist. Head back home or request a quote.</p></div></section>
<section class="section"><div class="wrap"><div class="btn-row"><a class="btn navy" href="/">Go home</a><a class="btn" href="{FORM_PATH}">Get a Free Quote</a></div></div></section>'''
    return layout("/404.html", "Page Not Found | Tan Salon Insurance", "The page you requested could not be found.", body, "WebPage", [("Home", "/")]).replace('content="index,follow,max-image-preview:large"', 'content="noindex"')

def main():
    write("index.html", page_home())
    write(FORM_PATH.strip("/") + "/index.html", page_form())
    write("404.html", page_404())
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"<url><loc>{SITE}{p}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n" for p, pr in [("/", "1.0"), (FORM_PATH, "0.9")]) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("llms.txt", f"""# {NAME}

> Insurance for tanning salons and personal appearance businesses, insuring personal appearance services since 1973. Tanning coverage has no cancer exclusions.

## Pages
- [Home]({SITE}/): coverage overview, who we insure, FAQ
- [Free quote questionnaire]({SITE}{FORM_PATH}): request a free quote

## Key facts
- Insures: {', '.join(SERVICES)}
- Coverage: general and professional liability, property, umbrella (up to $10,000,000), commercial auto
- Payment: automatic bank draft monthly, quarterly, semi-annual or annual; Mastercard, Visa, Discover, American Express
""")
    write("favicon.svg", LOGO.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true"', ""))
    base = "default-src 'self'; img-src 'self' data:; style-src 'self'; font-src 'self'; connect-src 'self'; form-action 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'"
    jf = ("default-src 'self'; script-src 'self' https://*.jotform.com https://*.jotfor.ms; frame-src https://*.jotform.com https://*.jotfor.ms; "
          "img-src 'self' data: https://*.jotform.com https://*.jotfor.ms; style-src 'self' 'unsafe-inline' https://*.jotform.com https://*.jotfor.ms; "
          "font-src 'self' data: https://*.jotform.com https://*.jotfor.ms; connect-src 'self' https://*.jotform.com https://*.jotfor.ms; "
          "form-action 'self' https://*.jotform.com; base-uri 'self'; object-src 'none'; frame-ancestors 'none'")
    common = "  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n"
    write("_headers", f"/*\n{common}  Content-Security-Policy: {base}\n\n{FORM_PATH}\n  ! Content-Security-Policy\n  Content-Security-Policy: {jf}\n\n/assets/*\n  Cache-Control: public, max-age=604800\n")

if __name__ == "__main__":
    main()
    print("built")
