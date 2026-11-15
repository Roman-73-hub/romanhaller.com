# romanhaller.com, Fassung 2: bildgeführt, ohne Linien, Archivo
import os, json, html, re
from PIL import Image
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("OUT", "/home/claude/site")
BASE = "https://www.romanhaller.com"
DIARY = os.environ.get("DIARY", os.path.join(HERE, "tagebuch.json"))
if not os.path.exists(DIARY):
    DIARY = "/home/claude/diary/tagebuch.json"
CSS_V = "32"

def size(name, w):
    return Image.open(f"{OUT}/img/{name}-{w}.jpg").size

def img(name, alt, sizes="100vw", cls="", lazy=True, pos=None):
    avail = [w for w in (800, 1600, 2400) if os.path.exists(f"{OUT}/img/{name}-{w}.jpg")]
    srcset = ", ".join(f"/img/{name}-{w}.jpg {w}w" for w in avail)
    w, h = size(name, avail[0])
    la = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    st = f' style="object-position:{pos}"' if pos else ""
    return (f'<img{c} src="/img/{name}-{avail[min(1,len(avail)-1)]}.jpg" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{html.escape(alt)}"{la}{st}>')

LI = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'

T = {
"de": {
  "lang": "de-CH", "path": "/", "other": "/en/", "other_label": "EN", "other_name": "English", "navlabel": "Hauptnavigation",
  "title": "Roman Haller · Zermatt",
  "desc": "Roman Haller, Unternehmer in Zermatt. Seit über 25 Jahren in Hotellerie, Tourismus und Immobilien, heute mit ARM – Private Office.",
  "nav": [("#herkunft", "Herkunft"), ("#arbeiten", "Arbeiten"), ("#werdegang", "Werdegang"), ("#velo", "Velo"), ("#kontakt", "Kontakt")],
  "ids": ["herkunft", "arbeiten", "werdegang", "heute", "velo", "kontakt"],
  "hero_l": "Biglen", "hero_r": "Zermatt",
  "hero_alt_l": "Webstuhl in der Fabrik der Arm AG in Biglen, 2014",
  "hero_alt_r": "Steinmänner hoch über Zermatt",
  "statement": "Ich komme aus Biglen bei Bern, habe Schreiner gelernt und lebe seit Anfang der 1990er Jahre in Zermatt. Seit über 25 Jahren arbeite ich in Hotellerie, Tourismus und Immobilien.",
  "statement2": "Heute bringe ich mit meinem Private Office ARM Investoren, Entwickler, Betreiber und Gemeinden zusammen.",
  "portrait_alt": "Porträt Roman Haller",
  "h_origin": "Zwei Orte",
  "origin": [
    "1861 gründete Friedrich Arm in Biglen eine Blattmacherei. Über fünf Generationen wurde daraus ein Hersteller von Tritt- und Musterwebstühlen, bis in die 1980er Jahre. Die Arm AG ist unsere Familienfirma. Nach der Schreinerlehre habe ich dort in der Produktion, im Verkauf und in der Administration gearbeitet.",
    "Anfang der 1990er Jahre kam ich als Skilehrer nach Zermatt und gründete mit Kollegen die erste private Snowboardschule im Dorf. Geblieben bin ich wegen der Arbeit und der Berge, später wegen meiner Familie.",
    "2014 habe ich die Arm AG übernommen und das Fabrikareal bis 2020 zu Atelierwohnungen umgebaut. Heute ist die Firma mein Private Office in Zermatt. Der Name ist geblieben.",
  ],
  "cap_hobel": "Hobelbank in der Fabrik der Arm AG, 2014. Foto: Gaudenz Danuser",
  "h_work": "Arbeiten",
  "work": [
    {"y": "2015–2020", "t": "Fabrikareal Biglen",
     "d": "Umnutzung der früheren Webstuhlfabrik: 3'000 m³ zu Atelierwohnungen, Volumen CHF 8 Mio. Als Eigentümer war ich verantwortlich für Business- und Finanzplan, Architekturkonzept, Kosten, Termine und Qualität. Mit der Zeitschrift Hochparterre haben wir den Umbau mit Anlässen vor Ort begleitet. Die Liegenschaft ist verkauft.",
     "imgs": [("fabrikhalle", "Fabrikhalle vor dem Umbau, 2014"), ("biglen-2020", "Nach dem Umbau, 2020")], "layout": "pair"},
    {"y": "2008–2021", "t": "3100 Kulmhotel Gornergrat",
     "d": "Relaunch und Neupositionierung des höchstgelegenen Hotels der Schweizer Alpen: Marketing- und Verkaufsstrategie, Online-Vertrieb und Verkaufsreisen nach Europa, Nordamerika und Asien. Von 2014 bis 2020 sass ich zudem im Verwaltungsrat der Gornergrat Experience AG, dem Joint Venture von BVZ Gruppe und Matterhorn Group.",
     "imgs": [("kulm", "3100 Kulmhotel Gornergrat mit dem Matterhorn")], "layout": "wide"},
    {"y": "2008–2021", "t": "Grand Hotel Zermatterhof und Riffelhaus 1853",
     "d": "Repositionierung des Grand Hotel Zermatterhof und seiner Restaurants, Rebranding des Riffelhaus 1853. Für die Hotels der Matterhorn Group dazu ein zentrales Reservierungssystem und ein Reporting für die ganze Gruppe, mit 21 % mehr Umsatz in 18 Monaten.",
     "imgs": [("zermatterhof", "Grand Hotel Zermatterhof am Abend"), ("zermatterhof-lounge", "Lounge im Grand Hotel Zermatterhof"), ("riffelberg-winter", "Hotel am Riffelberg im Winter, im Hintergrund das Matterhorn")], "layout": "trio"},
    {"y": "2014–2015", "t": "150 Jahre Erstbesteigung des Matterhorns",
     "d": "Roadmap und Partnerschaftskonzept zum Jubiläum 2015. Für die Hörnlihütte, die in dieser Zeit erneuert wurde, die Kommunikation, die Partnerschaften und die Website. Während des Umbaus stand auf 2'880 m ein Basislager.",
     "imgs": [("hoernli-basislager", "Basislager beim Umbau der Hörnlihütte, 2014. Foto: Gaudenz Danuser")], "layout": "wide-r"},
  ],
  "more_h": "Weitere Arbeiten",
  "more": [
    ("2024–2026", "Gemeinden und Bauherren im Oberwallis", "Mit der Quant AG: Business- und Betriebsplanung für den Camping Täsch, Nutzungsevaluation für das Turbina-Areal in Zermatt, Roadmap mit Raumprogramm für das Rifugio by CERVO in Täsch."),
    ("2001–2002", "Expo.02", "Stellvertreter des Projektleiters Swisscom an der Landesausstellung, Mitarbeit im Projektcontrolling eines Engagements von CHF 74 Mio."),
  ],
  "h_cv": "Werdegang",
  "cv": [
    ("1989–1993", "Schreinerlehre", "Schreinerei Aeschlimann, Walkringen"),
    ("1993–1996", "Arm AG, Biglen", "Produktion, Verkauf und Administration im Familienbetrieb"),
    ("1993–1997", "Snowboardschule Stoked, Zermatt", "Mitgründer der ersten privaten Snowboardschule im Dorf"),
    ("2000", "Tourismusfachmann HF", "Schweizerische Tourismusfachschule, Siders"),
    ("2001–2007", "Swisscom AG", "Expo.02, Aufbau Marketing Swisscom Eurospot in Genf, Marketing Manager"),
    ("2008–2021", "Matterhorn Group, Zermatt", "Director Revenue, Marketing & Sales, Mitglied der Geschäftsleitung"),
    ("2014–2020", "Gornergrat Experience AG", "Mitglied des Verwaltungsrats"),
    ("seit 2014", "Arm AG", "Inhaber und VR-Präsident"),
    ("2020", "IMD Lausanne", "Executive MBA"),
    ("seit 2024", "Quant AG, Flims", "Business Associate auf Mandatsbasis"),
  ],
  "h_today": "ARM – Private Office",
  "today": [
    "Mit ARM (Arm AG, Zermatt) verbinde ich Investoren, Entwickler, Betreiber und öffentliche Institutionen, in der Schweiz und international. Im Zentrum stehen bewirtschaftete Immobilien: Hotels und Resorts, Serviced Apartments und bewirtschaftete Wohnungen, Branded Residences, Workation und gemischt genutzte Areale. Dazu kommen Standort- und Destinationsentwicklung.",
    "Die Arbeit beginnt mit Recherche. Wem gehört ein Haus, wer entscheidet, wo bewegt sich etwas? Danach spreche ich die Leute direkt an.",
  ],
  "today_cta": "arm.swiss besuchen",
  "h_velo": "Velo und Berg",
  "velo_lead": "Im August 2023 bin ich von Zermatt nach Bern gefahren, über alle damals 124 offiziellen Schweizer Strassenpässe.",
  "stats": [("124", "Pässe"), ("21", "Tage"), ("1'916", "Kilometer"), ("54'310", "Höhenmeter")],
  "diary": "Das Tagebuch der 21 Tage lesen",
  "rides_h": "Klassiker",
  "rides": [
    ("2023", "Tour de Suisse Challenge", "1'131 km, 18'790 Höhenmeter"),
    ("2023", "Paris-Roubaix Challenge", "170 km über die Pavés"),
    ("2024", "Strade Bianche Gran Fondo", "144 km auf Schotter, Ziel in Siena"),
    ("2025", "Ronde van Vlaanderen", "229 km"),
    ("2025", "Liège-Bastogne-Liège", "253 km"),
    ("2025", "Il Lombardia Gran Fondo", "über 110 km, Ghisallo und Sormano"),
  ],
  "mountain": "Am Berg: 21 Viertausender und die Patrouille des Glaciers. In Zermatt bin ich Coach im MTB Youth Team.",
  "velo_imgs": [
    ("gletsch", "Passstrasse über Gletsch, August 2023"),
    ("lombardia", "Il Lombardia Gran Fondo am Comersee, 2025"),
    ("umbrail", "Auf dem Umbrailpass, August 2023"),
    ("strade", "Strade Bianche Gran Fondo, 2024"),
    ("ronde", "Ronde van Vlaanderen, 2025"),
    ("roubaix-feld", "Pavés bei Paris-Roubaix, 2023"),
    ("scheidegg", "Grosse Scheidegg mit dem Wetterhorn, August 2023"),
    ("lombardia-kurve", "Il Lombardia Gran Fondo, 2025"),
  ],
  "h_contact": "Kontakt",
  "contact_lead": "Am einfachsten per E-Mail.",
  "imprint": "Impressum und Datenschutz",
  "imprint_title": "Impressum und Datenschutz · Roman Haller",
  "imprint_body": [
    ("Impressum", "Roman Haller<br>3920 Zermatt<br>Schweiz<br><a href=\"mailto:rh@arm.swiss\">rh@arm.swiss</a>"),
    ("Datenschutz", "Diese Website setzt keine Cookies, verwendet keine Analysewerkzeuge und lädt keine Schriften oder Inhalte von Dritten. Sie wird bei GitHub Pages (GitHub Inc., USA) betrieben. Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie die IP-Adresse, um die Seite auszuliefern. Wer mir eine E-Mail schreibt, dessen Angaben verwende ich nur, um zu antworten."),
    ("Bilder", "Fotos Fabrik Biglen 2014, Hörnlihütte und Grand Hotel Zermatterhof: Gaudenz Danuser. Übrige Fotos: Roman Haller, Matterhorn Group und Veranstalter der genannten Anlässe."),
  ],
  "back": "Zur Startseite",
  "notfound": "Diese Seite gibt es nicht mehr.",
},
"en": {
  "lang": "en", "path": "/en/", "other": "/", "other_label": "DE", "other_name": "Deutsch", "navlabel": "Main navigation",
  "title": "Roman Haller · Zermatt",
  "desc": "Roman Haller, entrepreneur in Zermatt. More than 25 years in hospitality, tourism and real estate, today with ARM – Private Office.",
  "nav": [("#origins", "Origins"), ("#work", "Work"), ("#career", "Career"), ("#cycling", "Cycling"), ("#contact", "Contact")],
  "ids": ["origins", "work", "career", "today", "cycling", "contact"],
  "hero_l": "Biglen", "hero_r": "Zermatt",
  "hero_alt_l": "Loom in the Arm AG factory in Biglen, 2014",
  "hero_alt_r": "Cairns high above Zermatt",
  "statement": "I come from Biglen near Bern, trained as a cabinetmaker and have lived in Zermatt since the early 1990s. For more than 25 years I have worked in hospitality, tourism and real estate.",
  "statement2": "Today, through my private office ARM, I bring together investors, developers, operators and communes.",
  "portrait_alt": "Portrait of Roman Haller",
  "h_origin": "Two places",
  "origin": [
    "In 1861 Friedrich Arm founded a reed-making workshop in Biglen. Over five generations it became a maker of treadle and pattern looms, until the 1980s. Arm AG is our family company. After my apprenticeship as a cabinetmaker I worked there in production, sales and administration.",
    "In the early 1990s I came to Zermatt as a ski instructor and, with friends, founded the first private snowboard school in the village. I stayed for the work and the mountains, and later for my family.",
    "In 2014 I took over Arm AG and by 2020 had converted the factory site into studio apartments. Today the company is my private office in Zermatt. The name has stayed.",
  ],
  "cap_hobel": "Workbench in the Arm AG factory, 2014. Photo: Gaudenz Danuser",
  "h_work": "Work",
  "work": [
    {"y": "2015–2020", "t": "Biglen factory site",
     "d": "Conversion of the former loom factory: 3,000 m³ into studio apartments, volume CHF 8m. As owner I was responsible for the business and financial plan, the architectural concept, cost, schedule and quality. Together with the architecture magazine Hochparterre we accompanied the conversion with events on site. The property has been sold.",
     "imgs": [("fabrikhalle", "Factory hall before the conversion, 2014"), ("biglen-2020", "After the conversion, 2020")], "layout": "pair"},
    {"y": "2008–2021", "t": "3100 Kulmhotel Gornergrat",
     "d": "Relaunch and repositioning of the highest hotel in the Swiss Alps: marketing and sales strategy, online distribution and sales trips to Europe, North America and Asia. From 2014 to 2020 I also sat on the board of Gornergrat Experience AG, the joint venture of BVZ Group and Matterhorn Group.",
     "imgs": [("kulm", "3100 Kulmhotel Gornergrat with the Matterhorn")], "layout": "wide"},
    {"y": "2008–2021", "t": "Grand Hotel Zermatterhof and Riffelhaus 1853",
     "d": "Repositioning of the Grand Hotel Zermatterhof and its restaurants, rebranding of the Riffelhaus 1853. For the Matterhorn Group hotels also a central reservation system and group-wide reporting, with 21% more revenue in 18 months.",
     "imgs": [("zermatterhof", "Grand Hotel Zermatterhof in the evening"), ("zermatterhof-lounge", "Lounge at the Grand Hotel Zermatterhof"), ("riffelberg-winter", "Hotel on the Riffelberg in winter, with the Matterhorn")], "layout": "trio"},
    {"y": "2014–2015", "t": "150 years since the first ascent of the Matterhorn",
     "d": "Roadmap and partnership concept for the 2015 anniversary. For the Hörnli hut, rebuilt at the time, the communication, the partnerships and the website. During the rebuild a base camp stood at 2,880 m.",
     "imgs": [("hoernli-basislager", "Base camp during the rebuild of the Hörnli hut, 2014. Photo: Gaudenz Danuser")], "layout": "wide-r"},
  ],
  "more_h": "More work",
  "more": [
    ("2024–2026", "Communes and developers in the Upper Valais", "With Quant AG: business and operating plan for Camping Täsch, use evaluation for the Turbina site in Zermatt, roadmap and space programme for Rifugio by CERVO in Täsch."),
    ("2001–2002", "Expo.02", "Deputy project manager for Swisscom at the Swiss national exhibition, project controlling of a CHF 74m engagement."),
  ],
  "h_cv": "Career",
  "cv": [
    ("1989–1993", "Apprenticeship as a cabinetmaker", "Schreinerei Aeschlimann, Walkringen"),
    ("1993–1996", "Arm AG, Biglen", "Production, sales and administration in the family business"),
    ("1993–1997", "Stoked snowboard school, Zermatt", "Co-founder of the first private snowboard school in the village"),
    ("2000", "Tourism Specialist HF", "Swiss School of Tourism, Sierre"),
    ("2001–2007", "Swisscom AG", "Expo.02, European marketing at Swisscom Eurospot in Geneva, marketing manager"),
    ("2008–2021", "Matterhorn Group, Zermatt", "Director Revenue, Marketing & Sales, member of the executive board"),
    ("2014–2020", "Gornergrat Experience AG", "Member of the board of directors"),
    ("since 2014", "Arm AG", "Owner and chairman of the board"),
    ("2020", "IMD Lausanne", "Executive MBA"),
    ("since 2024", "Quant AG, Flims", "Business associate on a mandate basis"),
  ],
  "h_today": "ARM – Private Office",
  "today": [
    "With ARM (Arm AG, Zermatt) I bring together investors, developers, operators and public institutions, in Switzerland and internationally. The focus is on managed real estate: hotels and resorts, serviced apartments and managed residences, branded residences, workation and mixed-use sites, as well as location and destination development.",
    "The work starts with research. Who owns a property, who decides, where is something moving? Then I approach the people directly.",
  ],
  "today_cta": "Visit arm.swiss",
  "h_velo": "Cycling and mountains",
  "velo_lead": "In August 2023 I rode from Zermatt to Bern over all 124 official Swiss road passes of the time.",
  "stats": [("124", "passes"), ("21", "days"), ("1,916", "kilometres"), ("54,310", "metres climbed")],
  "diary": "Read the 21-day diary (in German)",
  "rides_h": "Classics",
  "rides": [
    ("2023", "Tour de Suisse Challenge", "1,131 km, 18,790 m of climbing"),
    ("2023", "Paris-Roubaix Challenge", "170 km over the cobbles"),
    ("2024", "Strade Bianche Gran Fondo", "144 km on gravel, finish in Siena"),
    ("2025", "Ronde van Vlaanderen", "229 km"),
    ("2025", "Liège-Bastogne-Liège", "253 km"),
    ("2025", "Il Lombardia Gran Fondo", "more than 110 km, Ghisallo and Sormano"),
  ],
  "mountain": "In the mountains: 21 four-thousanders and the Patrouille des Glaciers. In Zermatt I coach the MTB youth team.",
  "velo_imgs": [
    ("gletsch", "Pass road above Gletsch, August 2023"),
    ("lombardia", "Il Lombardia Gran Fondo on Lake Como, 2025"),
    ("umbrail", "On the Umbrail Pass, August 2023"),
    ("strade", "Strade Bianche Gran Fondo, 2024"),
    ("ronde", "Ronde van Vlaanderen, 2025"),
    ("roubaix-feld", "Cobbles at Paris-Roubaix, 2023"),
    ("scheidegg", "Grosse Scheidegg with the Wetterhorn, August 2023"),
    ("lombardia-kurve", "Il Lombardia Gran Fondo, 2025"),
  ],
  "h_contact": "Contact",
  "contact_lead": "E-mail is the easiest way.",
  "imprint": "Legal notice and privacy",
  "imprint_title": "Legal notice and privacy · Roman Haller",
  "imprint_body": [
    ("Legal notice", "Roman Haller<br>3920 Zermatt<br>Switzerland<br><a href=\"mailto:rh@arm.swiss\">rh@arm.swiss</a>"),
    ("Privacy", "This website sets no cookies, uses no analytics and loads no fonts or content from third parties. It is hosted on GitHub Pages (GitHub Inc., USA). When the site is accessed, GitHub processes technically necessary data such as the IP address in order to deliver it. If you write to me by e-mail, I use your details only to reply."),
    ("Images", "Photos of the Biglen factory 2014, the Hörnli hut and the Grand Hotel Zermatterhof: Gaudenz Danuser. Other photos: Roman Haller, Matterhorn Group and the organisers of the events mentioned."),
  ],
  "back": "Back to the homepage",
  "notfound": "This page no longer exists.",
},
}

def head(t, title, desc, path, alt_path, extra=""):
    de = path if t["lang"] != "en" else alt_path
    en = path if t["lang"] == "en" else alt_path
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}{path}">
<link rel="alternate" hreflang="de-CH" href="{BASE}{de}">
<link rel="alternate" hreflang="en" href="{BASE}{en}">
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
    pre = "" if home else t["path"]
    nav = "".join(f'<a href="{pre}{h}">{l}</a>' for h, l in t["nav"])
    other_lang = "en" if t["lang"] != "en" else "de-CH"
    cls = "top on-image" if home else "top"
    return f"""<header class="{cls}">
  <a class="brand" href="{t['path']}">Roman Haller</a>
  <nav class="nav" aria-label="{t['navlabel']}">{nav}</nav>
  <details class="menu">
    <summary><span class="m-open">{'Menu' if t['lang']=='en' else 'Menü'}</span><span class="m-close">{'Close' if t['lang']=='en' else 'Schliessen'}</span></summary>
    <nav class="menu-panel" aria-label="{t['navlabel']}">{nav}<span class="menu-meta"><a href="https://www.linkedin.com/in/romanhaller/" rel="noopener">LinkedIn</a><a href="{t['other']}" hreflang="{other_lang}">{t['other_name']}</a></span></nav>
  </details>
  <div class="tools">
    <a class="social" href="https://www.linkedin.com/in/romanhaller/" rel="noopener" aria-label="LinkedIn" title="LinkedIn">{LI}</a>
    <a class="lang" href="{t['other']}" hreflang="{other_lang}" lang="{other_lang}" title="{t['other_name']}">{t['other_label']}</a>
  </div>
</header>
"""

def footer(t):
    imp = "/impressum/" if t["lang"] != "en" else "/en/legal/"
    return f"""<footer class="foot">
  <span>© 2026 Roman Haller, Zermatt</span>
  <span class="foot-links"><a href="https://www.linkedin.com/in/romanhaller/" rel="noopener">LinkedIn</a><a href="https://www.strava.com/athletes/22958186" rel="noopener">Strava</a><a href="https://www.arm.swiss" rel="noopener">arm.swiss</a><a href="{imp}">{t['imprint']}</a></span>
</footer>
<script>document.querySelectorAll('.menu-panel a').forEach(function(a){{a.addEventListener('click',function(){{var d=a.closest('details');if(d)d.removeAttribute('open')}})}})</script>
"""

def fig(name, alt, sizes, cls="", cap=True, pos=None):
    c = f' class="{cls}"' if cls else ""
    fc = f"<figcaption>{html.escape(alt)}</figcaption>" if cap else ""
    return f"<figure{c}>{img(name, alt, sizes, pos=pos)}{fc}</figure>"

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
    s = head(t, t["title"], t["desc"], t["path"], t["other"], f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>\n')
    s += '<body class="home">\n' + header(t) + "<main>\n"
    # Einstieg: zwei Orte, ein Name
    s += f"""<section class="hero" aria-label="Roman Haller">
  <div class="hero-half">{img('webstuhl', t['hero_alt_l'], '50vw', lazy=False, pos='50% 55%')}<span class="place">{t['hero_l']}</span></div>
  <div class="hero-half">{img('steinmann', t['hero_alt_r'], '50vw', lazy=False, pos='60% 50%')}<span class="place">{t['hero_r']}</span></div>
  <h1 class="hero-name"><span>Roman</span> <span>Haller</span></h1>
</section>
<section class="intro">
  <p class="statement">{t['statement']}</p>
  <p class="statement2">{t['statement2']}</p>
  <figure class="intro-portrait">{img('portrait', t['portrait_alt'], '(min-width: 900px) 55vw, 100vw')}</figure>
</section>
"""
    # Herkunft
    paras = "".join(f"<p>{p}</p>" for p in t["origin"])
    s += f"""<section id="{i[0]}" class="origin">
  <figure class="origin-img">{img('hobelbank', t['cap_hobel'], '(min-width: 900px) 55vw, 100vw')}<figcaption>{t['cap_hobel']}</figcaption></figure>
  <div class="origin-text"><h2>{t['h_origin']}</h2>{paras}</div>
</section>
"""
    # Arbeiten
    items = ""
    for n, w in enumerate(t["work"]):
        text = f'<div class="work-text"><p class="year">{w["y"]}</p><h3>{w["t"]}</h3><p>{w["d"]}</p></div>'
        if w["layout"] == "pair":
            pics = '<div class="work-pics pair">' + "".join(fig(a, b, "(min-width: 900px) 34vw, 100vw") for a, b in w["imgs"]) + "</div>"
        elif w["layout"] == "trio":
            a = w["imgs"]
            pics = ('<div class="work-pics trio">' + fig(a[0][0], a[0][1], "(min-width: 900px) 40vw, 100vw", "t-a")
                    + fig(a[1][0], a[1][1], "(min-width: 900px) 28vw, 50vw", "t-b") + fig(a[2][0], a[2][1], "(min-width: 900px) 28vw, 50vw", "t-c") + "</div>")
        else:
            pics = '<div class="work-pics single">' + fig(w["imgs"][0][0], w["imgs"][0][1], "(min-width: 900px) 62vw, 100vw") + "</div>"
        items += f'<article class="work work-{w["layout"]}">{pics}{text}</article>\n'
    more = "".join(f'<div class="more-item"><p class="year">{y}</p><h3>{n}</h3><p>{d}</p></div>' for y, n, d in t["more"])
    s += f"""<section id="{i[1]}" class="works">
  <h2 class="sec-h">{t['h_work']}</h2>
  {items}
  <div class="more"><h3 class="more-h">{t['more_h']}</h3><div class="more-grid">{more}</div></div>
</section>
"""
    # Werdegang
    rows = "".join(f'<li><span class="year">{y}</span><span class="cv-what"><strong>{w}</strong>{d}</span></li>' for y, w, d in t["cv"])
    s += f"""<section id="{i[2]}" class="cv-sec">
  <h2 class="sec-h">{t['h_cv']}</h2>
  <ol class="cv">{rows}</ol>
</section>
"""
    # ARM
    tp = "".join(f"<p>{p}</p>" for p in t["today"])
    s += f"""<section id="{i[3]}" class="arm">
  <h2>{t['h_today']}</h2>
  <div class="arm-text">{tp}<p><a class="btn" href="https://www.arm.swiss" rel="noopener">{t['today_cta']}</a></p></div>
</section>
"""
    # Velo
    stats = "".join(f'<div class="stat"><span class="num">{a}</span><span class="lbl">{b}</span></div>' for a, b in t["stats"])
    rides = "".join(f'<li><span class="year">{y}</span><strong>{n}</strong><span>{d}</span></li>' for y, n, d in t["rides"])
    mos = "".join(fig(a, b, "(min-width: 900px) 33vw, 50vw") for a, b in t["velo_imgs"])
    s += f"""<section id="{i[4]}" class="velo">
  <div class="velo-head">
    <h2 class="sec-h">{t['h_velo']}</h2>
    <p class="velo-lead">{t['velo_lead']}</p>
  </div>
  <div class="stats">{stats}</div>
  <p class="velo-cta"><a class="btn btn-ink" href="/124-paesse/">{t['diary']}</a></p>
  <div class="mosaic">{mos}</div>
  <div class="velo-foot">
    <div><h3 class="more-h">{t['rides_h']}</h3><ul class="rides">{rides}</ul></div>
    <div><p class="mountain">{t['mountain']}</p><p class="links"><a href="https://www.strava.com/athletes/22958186" rel="noopener">Strava</a><a href="https://open.spotify.com/playlist/7xD3Vn8n3mYziDWH4mLomV" rel="noopener">R-Works Playlist</a></p></div>
  </div>
</section>
"""
    # Kontakt
    s += f"""<section id="{i[5]}" class="contact">
  <h2 class="sec-h">{t['h_contact']}</h2>
  <p class="contact-lead">{t['contact_lead']}</p>
  <p class="mail"><a href="mailto:rh@arm.swiss">rh@arm.swiss</a></p>
  <p class="links"><a href="https://www.linkedin.com/in/romanhaller/" rel="noopener">LinkedIn</a><a href="https://www.arm.swiss" rel="noopener">arm.swiss</a></p>
</section>
"""
    s += "</main>\n" + footer(t) + "</body>\n</html>\n"
    return s

def imprint(t):
    path = "/impressum/" if t["lang"] != "en" else "/en/legal/"
    other = "/en/legal/" if t["lang"] != "en" else "/impressum/"
    s = head(t, t["imprint_title"], t["imprint_title"], path, other).replace("<head>", "<head>\n<meta name=\"robots\" content=\"noindex\">", 1)
    tt = dict(t); tt["other"] = other
    s += "<body>\n" + header(tt, False) + '<main class="legal">\n' + f"<h1>{t['imprint']}</h1>\n"
    for h, b in t["imprint_body"]:
        s += f"<h2>{h}</h2><p>{b}</p>\n"
    s += f'<p><a href="{t["path"]}">{t["back"]}</a></p>\n</main>\n' + footer(t) + "</body>\n</html>\n"
    return s, path

def redirect(target, depth=1):
    up = "../" * depth
    return f"""<!DOCTYPE html><html lang="de-CH"><head><meta charset="utf-8"><title>Roman Haller</title>
<meta http-equiv="refresh" content="0; url={up}{target.lstrip('/')}"><link rel="canonical" href="{BASE}{target.split('#')[0]}"><meta name="robots" content="noindex"></head>
<body><p><a href="{up}{target.lstrip('/')}">Roman Haller</a></p></body></html>
"""

def relativize(content, path):
    depth = path.strip("/").count("/") + (1 if path.strip("/") else 0)
    p = "../" * depth
    content = re.sub(r'(href|src|content)="/(?!/)', lambda m: f'{m.group(1)}="{p}', content)
    content = re.sub(r'(srcset="[^"]*")', lambda m: m.group(1).replace("/img/", p + "img/"), content)
    content = content.replace('href=""', 'href="./"')
    return content

def write(path, content, rel=True):
    if rel:
        content = relativize(content, path)
    full = OUT + path + ("index.html" if path.endswith("/") else "")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

write("/", page(T["de"]))
write("/en/", page(T["en"]))
for k in ("de", "en"):
    c, p = imprint(T[k]); write(p, c)

for p, tgt in {"/about/": "/#werdegang", "/work/": "/#arbeiten", "/tour-de-suisse-challenge/": "/#velo", "/paris-roubaix/": "/#velo",
               "/strade-bianche/": "/#velo", "/ronde-van-vlaanderen/": "/#velo", "/lige-bastogne-lige/": "/#velo", "/il-lombardia/": "/#velo",
               "/124-psse/": "/124-paesse/", "/124-passes/": "/124-paesse/"}.items():
    write(p, redirect(tgt, 1), rel=False)

# ---------- Tagebuch ----------
D = json.load(open(DIARY))
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
            out.append(f"<{el.name}>" + "".join(f"<li>{html.escape(li.get_text(' ', strip=True))}</li>" for li in el.find_all("li")) + f"</{el.name}>")
            continue
        txt = el.get_text(" ", strip=True)
        if txt:
            tag = "h3" if el.name.startswith("h") else ("blockquote" if el.name == "blockquote" else "p")
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
    cards += f'<a class="day-card" href="/124-paesse/tag-{n:02d}/">{img(f"tag-{n:02d}", a, "(min-width: 900px) 24vw, 46vw")}<span class="day-no">{a}</span><span class="day-t">{html.escape(b)}</span></a>\n'
stats = "".join(f'<div class="stat"><span class="num">{a}</span><span class="lbl">{b}</span></div>' for a, b in td["stats"])
s = head(td, "124 Schweizer Pässe in 21 Tagen · Roman Haller", "Tagebuch einer Velofahrt von Zermatt nach Bern über alle 124 offiziellen Schweizer Strassenpässe, August 2023.", "/124-paesse/", "/en/")
s += "<body>\n" + header(td, False) + '<main class="diary">\n'
s += f'<section class="diary-hero"><p class="back"><a href="/#velo">Velo und Berg</a></p><h1>124 Schweizer Pässe in 21 Tagen</h1>'
s += "".join(f'<p class="velo-lead">{p}</p>' for p in intro)
s += f'<div class="stats">{stats}</div>'
s += '<p class="links"><a href="https://www.strava.com/athletes/22958186" rel="noopener">Die Strecke auf Strava</a></p>'
s += '<p class="note">Als ich die Routen im Winter und Frühjahr 2023 plante, waren es offiziell 124 Pässe. Heute sind es 120: Tüfletehöchi, Buuseregg, Wintersingenegg und Rumpelhöchi stehen nicht mehr im Verzeichnis.</p></section>\n'
s += f'<section class="days-sec"><h2 class="sec-h">Das Tagebuch</h2><div class="days">{cards}</div></section>\n'
s += "</main>\n" + footer(td) + "</body>\n</html>\n"
write("/124-paesse/", s)

for n, x in enumerate(D, 1):
    a, b = clean_title(x["title"])
    prev = f'<a href="/124-paesse/tag-{n-1:02d}/">Tag {n-1}</a>' if n > 1 else "<span></span>"
    nxt = f'<a href="/124-paesse/tag-{n+1:02d}/">Tag {n+1}</a>' if n < len(D) else "<span></span>"
    title = f"{a}: {b}" if b else a
    s = head(td, f"{title} · 124 Pässe · Roman Haller", f"124 Schweizer Pässe in 21 Tagen. {title}.", f"/124-paesse/tag-{n:02d}/", "/en/")
    s += "<body>\n" + header(td, False) + '<main class="day">\n'
    s += f'<figure class="day-img">{img(f"tag-{n:02d}", title, "(min-width: 900px) 42vw, 100vw", lazy=False)}</figure>\n'
    s += f'<article class="day-text"><p class="back"><a href="/124-paesse/">124 Pässe in 21 Tagen</a>, {a}</p><h1>{html.escape(b or a)}</h1>\n<div class="prose">{body_html(x["body"])}</div>\n'
    s += f'<nav class="day-nav">{prev}<a href="/124-paesse/">Übersicht</a>{nxt}</nav></article>\n</main>\n' + footer(td) + "</body>\n</html>\n"
    write(f"/124-paesse/tag-{n:02d}/", s)
    write(f"/124-psse/{x['urlId']}/", redirect(f"/124-paesse/tag-{n:02d}/", 2), rel=False)

# 404
nf = head(td, "Roman Haller", td["notfound"], "/404.html", "/en/").replace("<head>", "<head>\n<meta name=\"robots\" content=\"noindex\">", 1)
nf += "<body>\n" + header(td, False) + f'<main class="legal"><h1>404</h1><p>{td["notfound"]} This page no longer exists.</p><p><a href="/">{td["back"]}</a>, <a href="/en/">Homepage in English</a></p></main>\n' + footer(td) + "</body></html>\n"
open(OUT + "/404.html", "w").write(nf)

open(OUT + "/CNAME", "w").write("www.romanhaller.com\n")
open(OUT + "/.nojekyll", "w").write("")
open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(OUT + "/sitemap.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>{BASE}/</loc></url>
<url><loc>{BASE}/en/</loc></url>
<url><loc>{BASE}/124-paesse/</loc></url>
</urlset>
""")
print("ok")
