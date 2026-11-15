# Baut romanhaller.com als statische Seite in DE und EN
import os, json, html

OUT = "/home/claude/site"
BASE = "https://www.romanhaller.com"

def img(name, alt, sizes="100vw", cls="", widths=(800, 1600, 2400), lazy=True):
    avail = [w for w in widths if os.path.exists(f"{OUT}/img/{name}-{w}.jpg")]
    srcset = ", ".join(f"/img/{name}-{w}.jpg {w}w" for w in avail)
    from PIL import Image
    im = Image.open(f"{OUT}/img/{name}-{avail[0]}.jpg")
    w, h = im.size
    la = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="/img/{name}-{avail[-1] if len(avail)>1 else avail[0]}.jpg" '
            f'srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(alt)}"{la}>')

T = {
"de": {
  "lang": "de-CH", "path": "/", "other": "/en/", "other_label": "EN", "other_name": "English",
  "title": "Roman Haller · Zermatt",
  "desc": "Roman Haller, Unternehmer in Zermatt. Seit über 25 Jahren in Hotellerie, Tourismus und Immobilien, heute mit ARM – Private Office.",
  "nav": [("#herkunft", "Herkunft"), ("#werdegang", "Werdegang"), ("#arbeiten", "Arbeiten"), ("#velo", "Velo"), ("#kontakt", "Kontakt")],
  "ids": ["herkunft", "werdegang", "arbeiten", "heute", "velo", "kontakt"],
  "kicker": "Biglen · Zermatt",
  "lead": "Ich komme aus Biglen bei Bern, habe Schreiner gelernt und lebe seit Anfang der 1990er Jahre in Zermatt. Seit über 25 Jahren arbeite ich in Hotellerie, Tourismus und Immobilien.",
  "lead2": "Heute bringe ich mit meinem Private Office ARM Investoren, Entwickler, Betreiber und Gemeinden zusammen.",
  "cta1": "Werdegang", "cta2": "arm.swiss",
  "portrait_alt": "Porträt Roman Haller",
  "h_origin": "Biglen und Zermatt",
  "origin": [
    "1861 gründete Friedrich Arm in Biglen eine Blattmacherei. Über fünf Generationen wurde daraus ein Hersteller von Tritt- und Musterwebstühlen, bis in die 1980er Jahre. Die Arm AG ist unsere Familienfirma. Nach der Schreinerlehre habe ich dort in der Produktion, im Verkauf und in der Administration gearbeitet.",
    "Anfang der 1990er Jahre kam ich als Skilehrer nach Zermatt und gründete mit Kollegen die erste private Snowboardschule im Dorf. Geblieben bin ich wegen der Arbeit und der Berge, später wegen meiner Familie.",
    "2014 habe ich die Arm AG übernommen und das Fabrikareal bis 2020 zu Atelierwohnungen umgebaut. Heute ist die Firma mein Private Office in Zermatt. Der Name ist geblieben.",
  ],
  "cap_webstuhl": "Fabrikareal der Arm AG in Biglen vor dem Umbau, März 2014. Foto: Gaudenz Danuser",
  "h_cv": "Werdegang",
  "cv": [
    ("1989–1993", "Schreinerlehre", "Schreinerei Aeschlimann, Walkringen. Eidgenössisches Fähigkeitszeugnis."),
    ("1993–1996", "Arm AG, Biglen", "Produktion, Marketing, Verkauf und Administration im Familienbetrieb."),
    ("1993–1997", "Snowboardschule Stoked, Zermatt", "Mitgründer der ersten privaten Snowboardschule im Dorf."),
    ("2000", "Tourismusfachmann HF", "Schweizerische Tourismusfachschule, Siders."),
    ("2001–2007", "Swisscom AG, Bern, Genf, Biel", "Stellvertreter des Projektleiters Swisscom an der Expo.02. Aufbau des europäischen Marketings bei Swisscom Eurospot in Genf. Marketing Manager bei Swisscom Mobile und Solutions."),
    ("2008–2021", "Matterhorn Group, Zermatt", "Heute Zermatt Hospitality Group der Burgergemeinde Zermatt: fünf Hotels, 14 Restaurants und Detailhandel. Director Revenue, Marketing & Sales, Mitglied der Geschäftsleitung."),
    ("2014–2020", "Gornergrat Experience AG", "Mitglied des Verwaltungsrats. Joint Venture der BVZ Gruppe und der Matterhorn Group."),
    ("seit 2014", "Arm AG", "Inhaber und VR-Präsident. Umnutzung des Fabrikareals Biglen 2015–2020."),
    ("2020", "Executive MBA, IMD Lausanne", ""),
    ("seit 2024", "Quant AG, Flims", "Business Associate auf Mandatsbasis. Projekte für Gemeinden und Bauherren im Oberwallis."),
    ("heute", "ARM – Private Office, Zermatt", "Investoren, Entwickler, Betreiber und öffentliche Institutionen zusammenbringen."),
  ],
  "h_work": "Ausgewählte Arbeiten",
  "work": [
    ("2015–2020", "Fabrikareal Biglen", "Umnutzung der früheren Webstuhlfabrik: 3'000 m³ zu Atelierwohnungen, Volumen CHF 8 Mio. Als Eigentümer war ich verantwortlich für Business- und Finanzplan, Architekturkonzept, Kosten, Termine und Qualität. Mit der Zeitschrift Hochparterre haben wir den Umbau mit Anlässen vor Ort begleitet. Die Liegenschaft ist verkauft.", True),
    ("2008–2021", "Hotels der Matterhorn Group, Zermatt", "Relaunch des 3100 Kulmhotel Gornergrat, Rebranding des Riffelhaus 1853, Repositionierung des Grand Hotel Zermatterhof und seiner Restaurants. Dazu ein zentrales Reservierungssystem, ein Reporting für die ganze Gruppe mit 21 % mehr Umsatz in 18 Monaten und Verkaufsreisen nach Europa, Nordamerika und Asien.", False),
    ("2015", "150 Jahre Erstbesteigung des Matterhorns", "Roadmap und Partnerschaftskonzept zum Jubiläum. Für die Hörnlihütte, die in dieser Zeit erneuert wurde, die Kommunikation, die Partnerschaften und die Website.", False),
    ("2014–2020", "Gornergrat Experience AG", "Im Verwaltungsrat des Joint Ventures von BVZ Gruppe und Matterhorn Group. Weiterentwicklung des Gornergrats mit Investitions- und Erlebnisprojekten entlang der Bahn und auf dem Gipfel.", False),
    ("2024–2026", "Gemeinden und Bauherren im Oberwallis", "Mit der Quant AG: Business- und Betriebsplanung für den Camping Täsch, Nutzungsevaluation für das Turbina-Areal in Zermatt, Roadmap mit Raumprogramm für das Rifugio by CERVO in Täsch.", False),
    ("2001–2002", "Expo.02", "Stellvertreter des Projektleiters Swisscom an der Landesausstellung, Mitarbeit im Projektcontrolling eines Engagements von CHF 74 Mio.", False),
  ],
  "cap_before": "Fabrikhalle, 2014", "cap_after": "Nach dem Umbau, 2020",
  "h_today": "Heute",
  "today": [
    "Mit ARM – Private Office (Arm AG, Zermatt) verbinde ich Investoren, Entwickler, Betreiber und öffentliche Institutionen, in der Schweiz und international. Im Zentrum stehen bewirtschaftete Immobilien: Hotels und Resorts, Serviced Apartments und bewirtschaftete Wohnungen, Branded Residences, Workation und gemischt genutzte Areale. Dazu kommen Standort- und Destinationsentwicklung.",
    "Die Arbeit beginnt mit Recherche. Wem gehört ein Haus, wer entscheidet, wo bewegt sich etwas? Danach spreche ich die Leute direkt an.",
  ],
  "today_cta": "Mehr auf arm.swiss",
  "h_velo": "Velo und Berg",
  "velo_lead": "Im August 2023 bin ich von Zermatt nach Bern gefahren, über alle damals 124 offiziellen Schweizer Strassenpässe.",
  "stats": [("124", "Pässe"), ("21", "Tage"), ("1'916", "Kilometer"), ("54'310", "Höhenmeter")],
  "rides": [
    ("2023", "Tour de Suisse Challenge", "Acht Etappen auf der Originalstrecke der Tour de Suisse, 1'131 km und 18'790 Höhenmeter."),
    ("2023", "Paris-Roubaix Challenge", "170 km über die Pavés bis ins Velodrom von Roubaix."),
    ("2024", "Strade Bianche Gran Fondo", "144 km auf den weissen Schotterstrassen der Toskana, Ziel auf der Piazza del Campo in Siena."),
    ("2025", "Ronde van Vlaanderen", "229 km über die Hellingen und Kopfsteinpflaster Flanderns."),
    ("2025", "Liège-Bastogne-Liège", "253 km, La Doyenne, mit La Redoute und der Roche-aux-Faucons."),
    ("2025", "Il Lombardia Gran Fondo", "Über 110 km mit Ghisallo und Sormano, hoch über dem Comersee."),
  ],
  "mountain": "Am Berg: 21 Viertausender und die Patrouille des Glaciers. In Zermatt bin ich Coach im MTB Youth Team.",
  "alt_lombardia": "Roman Haller am Il Lombardia Gran Fondo am Comersee, 2025",
  "alt_ronde": "Roman Haller auf dem Kopfsteinpflaster der Ronde van Vlaanderen, 2025",
  "alt_strade": "Roman Haller am Strade Bianche Gran Fondo, 2024",
  "alt_ghisallo": "Roman Haller bei der Kapelle Madonna del Ghisallo, 2025",
  "strava": "Strava", "playlist": "R-Works Playlist auf Spotify", "diary": "Das Tagebuch der 21 Tage →",
  "h_contact": "Kontakt",
  "contact_lead": "Am einfachsten per E-Mail.",
  "imprint": "Impressum und Datenschutz",
  "imprint_title": "Impressum und Datenschutz · Roman Haller",
  "imprint_body": [
    ("Impressum", "Roman Haller<br>3920 Zermatt<br>Schweiz<br><a href=\"mailto:rh@arm.swiss\">rh@arm.swiss</a>"),
    ("Datenschutz", "Diese Website setzt keine Cookies, verwendet keine Analysewerkzeuge und lädt keine Schriften oder Inhalte von Dritten. Sie wird bei GitHub Pages (GitHub Inc., USA) betrieben. Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie die IP-Adresse, um die Seite auszuliefern. Wer mir eine E-Mail schreibt, dessen Angaben verwende ich nur, um zu antworten."),
    ("Bilder", "Fotos Fabrikareal Biglen 2014: Gaudenz Danuser. Übrige Fotos: Roman Haller und Veranstalter der genannten Anlässe."),
  ],
  "back": "Zur Startseite",
  "notfound": "Diese Seite gibt es nicht mehr.",
},
"en": {
  "lang": "en", "path": "/en/", "other": "/", "other_label": "DE", "other_name": "Deutsch",
  "title": "Roman Haller · Zermatt",
  "desc": "Roman Haller, entrepreneur in Zermatt. More than 25 years in hospitality, tourism and real estate, today with ARM – Private Office.",
  "nav": [("#origins", "Origins"), ("#career", "Career"), ("#work", "Work"), ("#cycling", "Cycling"), ("#contact", "Contact")],
  "ids": ["origins", "career", "work", "today", "cycling", "contact"],
  "kicker": "Biglen · Zermatt",
  "lead": "I come from Biglen near Bern, trained as a cabinetmaker and have lived in Zermatt since the early 1990s. For more than 25 years I have worked in hospitality, tourism and real estate.",
  "lead2": "Today, through my private office ARM, I bring together investors, developers, operators and communes.",
  "cta1": "Career", "cta2": "arm.swiss",
  "portrait_alt": "Portrait of Roman Haller",
  "h_origin": "Biglen and Zermatt",
  "origin": [
    "In 1861 Friedrich Arm founded a reed-making workshop in Biglen. Over five generations it became a maker of treadle and pattern looms, until the 1980s. Arm AG is our family company. After my apprenticeship as a cabinetmaker I worked there in production, sales and administration.",
    "In the early 1990s I came to Zermatt as a ski instructor and, with friends, founded the first private snowboard school in the village. I stayed for the work and the mountains, and later for my family.",
    "In 2014 I took over Arm AG and by 2020 had converted the factory site into studio apartments. Today the company is my private office in Zermatt. The name has stayed.",
  ],
  "cap_webstuhl": "The Arm AG factory in Biglen before the conversion, March 2014. Photo: Gaudenz Danuser",
  "h_cv": "Career",
  "cv": [
    ("1989–1993", "Apprenticeship as a cabinetmaker", "Schreinerei Aeschlimann, Walkringen. Federal certificate of proficiency."),
    ("1993–1996", "Arm AG, Biglen", "Production, marketing, sales and administration in the family business."),
    ("1993–1997", "Stoked snowboard school, Zermatt", "Co-founder of the first private snowboard school in the village."),
    ("2000", "Tourism Specialist HF", "Swiss School of Tourism, Sierre."),
    ("2001–2007", "Swisscom AG, Bern, Geneva, Biel", "Deputy project manager for Swisscom at Expo.02. Set up European marketing at Swisscom Eurospot in Geneva. Marketing manager at Swisscom Mobile and Solutions."),
    ("2008–2021", "Matterhorn Group, Zermatt", "Today Zermatt Hospitality Group, owned by the Burgergemeinde Zermatt: five hotels, 14 restaurants and retail. Director Revenue, Marketing & Sales, member of the executive board."),
    ("2014–2020", "Gornergrat Experience AG", "Member of the board of directors. Joint venture of BVZ Group and Matterhorn Group."),
    ("since 2014", "Arm AG", "Owner and chairman of the board. Conversion of the Biglen factory site 2015–2020."),
    ("2020", "Executive MBA, IMD Lausanne", ""),
    ("since 2024", "Quant AG, Flims", "Business associate on a mandate basis. Projects for communes and developers in the Upper Valais."),
    ("today", "ARM – Private Office, Zermatt", "Bringing together investors, developers, operators and public institutions."),
  ],
  "h_work": "Selected work",
  "work": [
    ("2015–2020", "Biglen factory site", "Conversion of the former loom factory: 3,000 m³ into studio apartments, volume CHF 8m. As owner I was responsible for the business and financial plan, the architectural concept, cost, schedule and quality. Together with the architecture magazine Hochparterre we accompanied the conversion with events on site. The property has been sold.", True),
    ("2008–2021", "Matterhorn Group hotels, Zermatt", "Relaunch of the 3100 Kulmhotel Gornergrat, rebranding of the Riffelhaus 1853, repositioning of the Grand Hotel Zermatterhof and its restaurants. Also a central reservation system, group-wide reporting with 21% more revenue in 18 months, and sales trips to Europe, North America and Asia.", False),
    ("2015", "150 years since the first ascent of the Matterhorn", "Roadmap and partnership concept for the anniversary. For the Hörnli hut, rebuilt at the time, the communication, the partnerships and the website.", False),
    ("2014–2020", "Gornergrat Experience AG", "On the board of the joint venture of BVZ Group and Matterhorn Group. Development of the Gornergrat with investment and visitor projects along the railway and on the summit.", False),
    ("2024–2026", "Communes and developers in the Upper Valais", "With Quant AG: business and operating plan for Camping Täsch, use evaluation for the Turbina site in Zermatt, roadmap and space programme for Rifugio by CERVO in Täsch.", False),
    ("2001–2002", "Expo.02", "Deputy project manager for Swisscom at the Swiss national exhibition, project controlling of a CHF 74m engagement.", False),
  ],
  "cap_before": "Factory hall, 2014", "cap_after": "After the conversion, 2020",
  "h_today": "Today",
  "today": [
    "With ARM – Private Office (Arm AG, Zermatt) I bring together investors, developers, operators and public institutions, in Switzerland and internationally. The focus is on managed real estate: hotels and resorts, serviced apartments and managed residences, branded residences, workation and mixed-use sites, as well as location and destination development.",
    "The work starts with research. Who owns a property, who decides, where is something moving? Then I approach the people directly.",
  ],
  "today_cta": "More at arm.swiss",
  "h_velo": "Cycling and mountains",
  "velo_lead": "In August 2023 I rode from Zermatt to Bern over all 124 official Swiss road passes of the time.",
  "stats": [("124", "passes"), ("21", "days"), ("1,916", "kilometres"), ("54,310", "metres climbed")],
  "rides": [
    ("2023", "Tour de Suisse Challenge", "Eight stages on the original Tour de Suisse route, 1,131 km and 18,790 m of climbing."),
    ("2023", "Paris-Roubaix Challenge", "170 km over the cobbles to the velodrome in Roubaix."),
    ("2024", "Strade Bianche Gran Fondo", "144 km on the white gravel roads of Tuscany, finishing on the Piazza del Campo in Siena."),
    ("2025", "Ronde van Vlaanderen", "229 km over the hellingen and cobbles of Flanders."),
    ("2025", "Liège-Bastogne-Liège", "253 km of La Doyenne, with La Redoute and the Roche-aux-Faucons."),
    ("2025", "Il Lombardia Gran Fondo", "More than 110 km with the Ghisallo and Sormano, high above Lake Como."),
  ],
  "mountain": "In the mountains: 21 four-thousanders and the Patrouille des Glaciers. In Zermatt I coach the MTB youth team.",
  "alt_lombardia": "Roman Haller at the Il Lombardia Gran Fondo on Lake Como, 2025",
  "alt_ronde": "Roman Haller on the cobbles of the Ronde van Vlaanderen, 2025",
  "alt_strade": "Roman Haller at the Strade Bianche Gran Fondo, 2024",
  "alt_ghisallo": "Roman Haller at the Madonna del Ghisallo chapel, 2025",
  "strava": "Strava", "playlist": "R-Works playlist on Spotify", "diary": "The 21-day diary (in German) →",
  "h_contact": "Contact",
  "contact_lead": "E-mail is the easiest way.",
  "imprint": "Legal notice and privacy",
  "imprint_title": "Legal notice and privacy · Roman Haller",
  "imprint_body": [
    ("Legal notice", "Roman Haller<br>3920 Zermatt<br>Switzerland<br><a href=\"mailto:rh@arm.swiss\">rh@arm.swiss</a>"),
    ("Privacy", "This website sets no cookies, uses no analytics and loads no fonts or content from third parties. It is hosted on GitHub Pages (GitHub Inc., USA). When the site is accessed, GitHub processes technically necessary data such as the IP address in order to deliver it. If you write to me by e-mail, I use your details only to reply."),
    ("Images", "Photos of the Biglen factory 2014: Gaudenz Danuser. Other photos: Roman Haller and the organisers of the events mentioned."),
  ],
  "back": "Back to the homepage",
  "notfound": "This page no longer exists.",
},
}

CSS_V = "6"

def head(t, title, desc, path, alt_path, extra=""):
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}{path}">
<link rel="alternate" hreflang="de-CH" href="{BASE}{path if t['lang']!='en' else alt_path}">
<link rel="alternate" hreflang="en" href="{BASE}{path if t['lang']=='en' else alt_path}">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<meta property="og:type" content="profile">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#231F20">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css?v={CSS_V}">
{extra}</head>
"""

def header(t, home=True):
    nav = "".join(f'<a href="{"" if home else t["path"]}{h}">{l}</a>' for h, l in t["nav"])
    return f"""<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="{t['path']}">Roman Haller</a>
    <nav class="nav" aria-label="{"Hauptnavigation" if t["lang"]!="en" else "Main navigation"}">{nav}</nav>
    <a class="lang" href="{t['other']}" hreflang="{'en' if t['lang']!='en' else 'de-CH'}" lang="{'en' if t['lang']!='en' else 'de-CH'}" title="{t['other_name']}">{t['other_label']}</a>
  </div>
</header>
"""

def footer(t):
    imp = "/impressum/" if t["lang"] != "en" else "/en/legal/"
    return f"""<footer class="foot">
  <div class="wrap foot-in">
    <span>© 2026 Roman Haller, Zermatt</span>
    <a href="{imp}">{t['imprint']}</a>
  </div>
</footer>
"""

def page(t):
    i = t["ids"]
    jsonld = {
        "@context": "https://schema.org", "@type": "Person", "name": "Roman Haller",
        "url": BASE + t["path"], "image": BASE + "/img/portrait-800.jpg",
        "jobTitle": "Inhaber, Arm AG" if t["lang"] != "en" else "Owner, Arm AG",
        "worksFor": {"@type": "Organization", "name": "ARM – Private Office (Arm AG)", "url": "https://www.arm.swiss"},
        "homeLocation": {"@type": "Place", "name": "Zermatt, Switzerland"},
        "alumniOf": [{"@type": "CollegeOrUniversity", "name": "IMD Lausanne"}],
        "sameAs": ["https://www.linkedin.com/in/romanhaller/", "https://www.strava.com/athletes/22958186"],
    }
    extra = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>\n'
    s = head(t, t["title"], t["desc"], t["path"], t["other"], extra)
    s += "<body>\n" + header(t) + "<main>\n"
    # Hero
    s += f"""<section class="hero wrap">
  <div class="hero-text">
    <p class="kicker">{t['kicker']}</p>
    <h1>Roman Haller</h1>
    <p class="lead">{t['lead']}</p>
    <p class="lead lead2">{t['lead2']}</p>
    <p class="ctas"><a class="btn" href="#{i[1]}">{t['cta1']}</a><a class="btn btn-line" href="https://www.arm.swiss" rel="noopener">{t['cta2']} <span aria-hidden="true">↗</span></a></p>
  </div>
  <figure class="hero-img">{img('portrait', t['portrait_alt'], '(min-width: 900px) 360px, 70vw', widths=(800,), lazy=False)}</figure>
</section>
"""
    # Herkunft
    paras = "".join(f"<p>{p}</p>" for p in t["origin"])
    s += f"""<section id="{i[0]}" class="sec">
  <div class="wrap grid">
    <h2 class="col-h">{t['h_origin']}</h2>
    <div class="col-b prose">{paras}</div>
  </div>
  <figure class="bleed">{img('webstuhl', t['cap_webstuhl'])}<figcaption class="wrap">{t['cap_webstuhl']}</figcaption></figure>
</section>
"""
    # Werdegang
    rows = "".join(f'<li><span class="yr">{y}</span><div><strong>{w}</strong>{f"<p>{d}</p>" if d else ""}</div></li>' for y, w, d in t["cv"])
    s += f"""<section id="{i[1]}" class="sec">
  <div class="wrap grid">
    <h2 class="col-h">{t['h_cv']}</h2>
    <ol class="cv col-b">{rows}</ol>
  </div>
</section>
"""
    # Arbeiten
    items = ""
    for n, (y, ttl, d, pics) in enumerate(t["work"], 1):
        pic = ""
        if pics:
            pic = f"""<div class="pair">
  <figure>{img('fabrik-2014', t['cap_before'], '(min-width: 900px) 30vw, 50vw', widths=(800,1600))}<figcaption>{t['cap_before']}</figcaption></figure>
  <figure>{img('biglen-2020', t['cap_after'], '(min-width: 900px) 30vw, 50vw', widths=(800,1600))}<figcaption>{t['cap_after']}</figcaption></figure>
</div>"""
        items += f'<article class="work-item"><p class="yr">{y}</p><div><h3>{ttl}</h3><p>{d}</p>{pic}</div></article>\n'
    s += f"""<section id="{i[2]}" class="sec">
  <div class="wrap grid">
    <h2 class="col-h">{t['h_work']}</h2>
    <div class="col-b works">{items}</div>
  </div>
</section>
"""
    # Heute ARM
    tp = "".join(f"<p>{p}</p>" for p in t["today"])
    s += f"""<section id="{i[3]}" class="sec dark">
  <div class="wrap grid">
    <h2 class="col-h">{t['h_today']}</h2>
    <div class="col-b prose">{tp}<p><a class="btn btn-inv" href="https://www.arm.swiss" rel="noopener">{t['today_cta']} <span aria-hidden="true">↗</span></a></p></div>
  </div>
</section>
"""
    # Velo
    stats = "".join(f'<div class="stat"><span class="num">{a}</span><span class="lbl">{b}</span></div>' for a, b in t["stats"])
    rides = "".join(f'<li><span class="yr">{y}</span><div><strong>{n}</strong><p>{d}</p></div></li>' for y, n, d in t["rides"])
    s += f"""<section id="{i[4]}" class="sec">
  <div class="wrap grid">
    <h2 class="col-h">{t['h_velo']}</h2>
    <div class="col-b"><p class="lead">{t['velo_lead']}</p><div class="stats">{stats}</div></div>
  </div>
  <figure class="bleed">{img('lombardia', t['alt_lombardia'])}</figure>
  <div class="wrap grid">
    <div class="col-h"></div>
    <div class="col-b">
      <ol class="cv rides">{rides}</ol>
      <div class="trio">
        <figure>{img('strade', t['alt_strade'], '(min-width: 900px) 22vw, 33vw', widths=(800,))}</figure>
        <figure>{img('ronde', t['alt_ronde'], '(min-width: 900px) 22vw, 33vw', widths=(800,))}</figure>
        <figure>{img('ghisallo', t['alt_ghisallo'], '(min-width: 900px) 22vw, 33vw', widths=(800,))}</figure>
      </div>
      <p class="mountain">{t['mountain']}</p>
      <p class="links"><a href="/124-paesse/">{t['diary']}</a><a href="https://www.strava.com/athletes/22958186" rel="noopener">{t['strava']} ↗</a><a href="https://open.spotify.com/playlist/7xD3Vn8n3mYziDWH4mLomV" rel="noopener">{t['playlist']} ↗</a></p>
    </div>
  </div>
</section>
"""
    # Kontakt
    s += f"""<section id="{i[5]}" class="sec contact">
  <div class="wrap grid">
    <h2 class="col-h">{t['h_contact']}</h2>
    <div class="col-b">
      <p class="lead">{t['contact_lead']}</p>
      <p class="mail"><a href="mailto:rh@arm.swiss">rh@arm.swiss</a></p>
      <p class="links"><a href="https://www.linkedin.com/in/romanhaller/" rel="noopener">LinkedIn ↗</a><a href="https://www.arm.swiss" rel="noopener">arm.swiss ↗</a></p>
    </div>
  </div>
</section>
"""
    s += "</main>\n" + footer(t) + "</body>\n</html>\n"
    return s

def imprint(t):
    path = "/impressum/" if t["lang"] != "en" else "/en/legal/"
    other = "/en/legal/" if t["lang"] != "en" else "/impressum/"
    s = head(t, t["imprint_title"], t["imprint_title"], path, other).replace("<head>", "<head>\n<meta name=\"robots\" content=\"noindex\">", 1)
    tt = dict(t); tt["other"] = other
    s += "<body>\n" + header(tt, False) + '<main class="wrap legal">\n'
    s += f"<h1>{t['imprint']}</h1>\n"
    for h, b in t["imprint_body"]:
        s += f"<h2>{h}</h2><p>{b}</p>\n"
    s += f'<p><a href="{t["path"]}">{t["back"]}</a></p>\n</main>\n' + footer(t) + "</body>\n</html>\n"
    return s, path

def redirect(target):
    return f"""<!DOCTYPE html><html lang="de-CH"><head><meta charset="utf-8"><title>Roman Haller</title>
<meta http-equiv="refresh" content="0; url=..{target}"><link rel="canonical" href="{BASE}{target.split('#')[0]}"><meta name="robots" content="noindex"></head>
<body><p><a href="..{target}">Roman Haller</a></p></body></html>
"""

import re
def relativize(content, path):
    depth = path.strip("/").count("/") + (1 if path.strip("/") else 0)
    p = "../" * depth
    content = re.sub(r'(href|src|content)="/(?!/)', lambda m: f'{m.group(1)}="{p}', content)
    content = re.sub(r'(srcset="[^"]*")', lambda m: m.group(1).replace("/img/", p + "img/"), content)
    content = content.replace('href=""', 'href="./"').replace('url=""', 'url=./')
    return content

def write(path, content):
    if not path.endswith(".html"):
        content = relativize(content, path)
    full = OUT + path + ("index.html" if path.endswith("/") else "")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

write("/", page(T["de"]))
write("/en/", page(T["en"]))
for k in ("de", "en"):
    c, p = imprint(T[k]); write(p, c)

# Alte Squarespace-Adressen weiterleiten
old = {"/about/": "/#werdegang", "/work/": "/#arbeiten",
       "/tour-de-suisse-challenge/": "/#velo", "/paris-roubaix/": "/#velo", "/strade-bianche/": "/#velo",
       "/ronde-van-vlaanderen/": "/#velo", "/lige-bastogne-lige/": "/#velo", "/il-lombardia/": "/#velo"}
for p, tgt in old.items():
    write(p, redirect(tgt))

t = T["de"]
nf = head(t, "Roman Haller", t["notfound"], "/404.html", "/en/").replace("<head>", "<head>\n<meta name=\"robots\" content=\"noindex\">", 1)
nf += "<body>\n" + header(t, False) + f'<main class="wrap legal"><h1>404</h1><p>{t["notfound"]} This page no longer exists.</p><p><a href="/">{t["back"]}</a> · <a href="/en/">Homepage in English</a></p></main>\n' + footer(t) + "</body></html>\n"
open(OUT + "/404.html", "w").write(nf)

open(OUT + "/CNAME", "w").write("www.romanhaller.com\n")
open(OUT + "/.nojekyll", "w").write("")
open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(OUT + "/sitemap.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>{BASE}/</loc></url>
<url><loc>{BASE}/en/</loc></url>\n<url><loc>{BASE}/124-paesse/</loc></url>
</urlset>
""")
open(OUT + "/favicon.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#231F20"/><text x="32" y="42" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-size="26" font-weight="700" fill="#F7F5F0" text-anchor="middle" letter-spacing="-1">RH</text></svg>\n')
print("ok")

# ---------- Tagebuch 124 Pässe ----------
from bs4 import BeautifulSoup
D = json.load(open(os.path.join(os.path.dirname(__file__), "tagebuch.json")))
def clean_title(t):
    t = t.replace("ß", "ss")
    if " - " in t:
        a, b = t.split(" - ", 1)
        return a.strip(), b.strip()
    return t, ""
def body_html(b):
    s = BeautifulSoup(b, "html.parser")
    out = []
    for el in s.find_all(["h1", "h2", "h3", "h4", "p", "ul", "ol", "blockquote"]):
        if el.find_parent(["ul", "ol", "blockquote"]) and el.name == "p":
            continue
        if el.name in ("ul", "ol"):
            items = "".join(f"<li>{html.escape(li.get_text(' ', strip=True))}</li>" for li in el.find_all("li"))
            out.append(f"<{el.name}>{items}</{el.name}>")
            continue
        txt = el.get_text(" ", strip=True)
        if not txt:
            continue
        tag = "h3" if el.name in ("h1", "h2", "h3", "h4") else ("blockquote" if el.name == "blockquote" else "p")
        out.append(f"<{tag}>{html.escape(txt)}</{tag}>")
    return "\n".join(out).replace("ß", "ss")

td = T["de"]
intro = [
    "Ich habe mir ein Ziel gesetzt, das über das Gewöhnliche hinausgeht: eine Reise von meinem Zuhause in Zermatt bis zu meinen Wurzeln in Bern, über alle 124 offiziellen Schweizer Strassenpässe.",
    "Mit durchschnittlich 88 Kilometern und 2'600 Höhenmetern pro Tag und fast fünf Stunden im Sattel war die Reise auch eine körperliche Herausforderung. Vor allem aber wollte ich die Schweiz, meine Heimat, auf eine neue Weise kennenlernen. Unterwegs habe ich jeden Tag aufgeschrieben, was ich erlebt habe.",
]
cards = ""
for n, x in enumerate(D, 1):
    a, b = clean_title(x["title"])
    cards += f'<a class="day-card" href="/124-paesse/tag-{n:02d}/">{img(f"tag-{n:02d}", a, "(min-width: 900px) 25vw, 45vw", widths=(800,))}<span class="day-no">{a}</span><span class="day-t">{html.escape(b)}</span></a>\n'
stats = "".join(f'<div class="stat"><span class="num">{a}</span><span class="lbl">{b}</span></div>' for a, b in td["stats"])
s = head(td, "124 Schweizer Pässe in 21 Tagen · Roman Haller", "Tagebuch einer Velofahrt von Zermatt nach Bern über alle 124 offiziellen Schweizer Strassenpässe, August 2023.", "/124-paesse/", "/en/")
s += "<body>\n" + header(td, False) + '<main>\n<section class="hero-sm wrap">\n'
s += f'<p class="kicker"><a href="/#velo">Velo und Berg</a></p><h1>124 Schweizer Pässe in 21 Tagen</h1>'
s += "".join(f'<p class="lead">{p}</p>' for p in intro)
s += f'<div class="stats">{stats}</div>'
s += '<p class="links"><a href="https://www.strava.com/athletes/22958186" rel="noopener">Die Strecke auf Strava ↗</a></p>'
s += '<p class="note">Als ich die Routen im Winter und Frühjahr 2023 plante, waren es offiziell 124 Pässe. Heute sind es 120: Tüfletehöchi, Buuseregg, Wintersingenegg und Rumpelhöchi stehen nicht mehr im Verzeichnis.</p>\n</section>\n'
s += f'<section class="sec"><div class="wrap"><h2 class="col-h">Das Tagebuch</h2><div class="days">{cards}</div></div></section>\n'
s += "</main>\n" + footer(td) + "</body>\n</html>\n"
write("/124-paesse/", s)

for n, x in enumerate(D, 1):
    a, b = clean_title(x["title"])
    prev = f'<a href="/124-paesse/tag-{n-1:02d}/">← Tag {n-1}</a>' if n > 1 else "<span></span>"
    nxt = f'<a href="/124-paesse/tag-{n+1:02d}/">Tag {n+1} →</a>' if n < len(D) else "<span></span>"
    title = f"{a}: {b}" if b else a
    s = head(td, f"{title} · 124 Pässe · Roman Haller", f"124 Schweizer Pässe in 21 Tagen. {title}.", f"/124-paesse/tag-{n:02d}/", "/en/")
    s += "<body>\n" + header(td, False) + '<main class="wrap day">\n'
    s += f'<figure class="day-img">{img(f"tag-{n:02d}", title, "(min-width: 900px) 40vw, 100vw", widths=(800,1600), lazy=False)}</figure>\n'
    s += f'<article class="day-text"><p class="kicker"><a href="/124-paesse/">124 Pässe in 21 Tagen</a> · {a}</p><h1>{html.escape(b or a)}</h1>\n<div class="prose">{body_html(x["body"])}</div>\n'
    s += f'<nav class="day-nav">{prev}<a href="/124-paesse/">Übersicht</a>{nxt}</nav></article>\n</main>\n' + footer(td) + "</body>\n</html>\n"
    write(f"/124-paesse/tag-{n:02d}/", s)
    # alte Squarespace-Adresse des Eintrags
    write(f"/124-psse/{x['urlId']}/", redirect(f"/124-paesse/tag-{n:02d}/").replace("url=..", "url=../..").replace('href="..', 'href="../..'))
write("/124-psse/", redirect("/124-paesse/"))
write("/124-passes/", redirect("/124-paesse/"))
print("diary ok")
