"""Generator statycznego demo Smuga Design (GitHub Pages). Uruchom: python3 build.py"""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent
SITE = "Smuga Design"
STREAK = '<svg class="streak" viewBox="0 0 120 64" aria-hidden="true"><path d="M12 60C14 44 30 38 54 32C76 26 86 20 88 4H108C108 24 92 36 64 42C42 47 32 50 32 60Z"/></svg>'
EMAIL = "kontakt@smugadesign.pl"
PHONE = "+48 604 762 946"
PHONE_HREF = "+48604762946"
IG = "https://www.instagram.com/smuga_design/"
BEHANCE = "https://www.behance.net/smugadesign"

# Zdjęcia: (plik bez rozszerzenia, opis, proporcja szer./wys.)
IMG = {
    "mnc-kotara": ("Różowa kotara i stoliki przy wejściu, kawiarnia MNC Concept", (1400, 1960)),
    "mnc-sala": ("Sala z ławą wzdłuż ściany i okrągłymi kinkietami, kawiarnia MNC Concept", (1158, 1500)),
    "mnc-lada": ("Lada z frontem o wyrazistym rysunku drewna, kawiarnia MNC Concept", (1149, 1500)),
    "mnc-bar": ("Bar ze stali i kwiaty przy ekspresie, kawiarnia MNC Concept", (1062, 1400)),
    "mnc-loza": ("Strefa siedzisk przy jasnej kotarze, kawiarnia MNC Concept", (1320, 1731)),
    "mnc-wejscie": ("Logo MNC Concept na białej kotarze, kawiarnia MNC Concept", (808, 632)),
    "mnc-taras": ("Leżaki z logo na ogródku, kawiarnia MNC Concept", (1000, 1293)),
    "viz-apartament-wwa": ("Sypialnia z muralem i zabudową ze sklejki, mieszkanie w Warszawie, wizualizacja", (808, 632)),
    "viz-dom-001": ("Kuchnia z wyspą i ryflowaną zabudową, dom jednorodzinny, wizualizacja", (808, 632)),
    "viz-showroom": ("Jasny showroom z łukami i drewnianą zabudową, wizualizacja", (808, 632)),
    "smuga-wioleta": ("Arch. wn. Wioleta Siemieniuk, Smuga Design", (808, 632)),
}

PROJECTS = [
    {
        "slug": "mnc-concept", "code": "SD_MNC.CONCEPT_25", "status": "real",
        "title": "Kawiarnia MNC Concept", "short": "MNC Concept",
        "typ": "Wnętrze komercyjne", "lok": "Białystok", "rok": "2025",
        "cover": "mnc-kotara", "card": "mnc-sala",
        "lead": "Kawiarnia, w której wnętrze jest częścią marki: jasne kotary, stal i drewno tworzą spokojne tło, a kolor i kwiaty dają mu charakter.",
        "blocks": [
            ("Założenia", "Wnętrze miało pracować jak tło dla marki i ludzi: spokojne na co dzień, wyraziste na zdjęciach z Instagrama."),
            ("Materiały", "Miękkie kotary, szczotkowana stal baru, kamienne blaty stolików i front lady z mocnym rysunkiem drewna."),
            ("Efekt", "Przestrzeń, którą goście rozpoznają po jednym kadrze. Różowa kotara i kwiaty stały się znakiem miejsca."),
        ],
        "gallery": ["mnc-sala", "mnc-lada", "mnc-bar", "mnc-loza", "mnc-wejscie", "mnc-taras"],
    },
    {
        "slug": "mieszkanie-warszawa", "code": "SD_APARTMENT_002", "status": "viz",
        "title": "Mieszkanie w Warszawie", "short": "Mieszkanie WWA",
        "typ": "Mieszkanie", "lok": "Warszawa", "rok": "",
        "cover": "viz-apartament-wwa", "card": "viz-apartament-wwa",
        "lead": "Sypialnia, w której sztuka gra pierwsze skrzypce: mural na całą ścianę, ciepła sklejka i spokojne tkaniny.",
        "blocks": [
            ("Założenia", "Jedno odważne wydarzenie na ścianie i bardzo prosta reszta, żeby wnętrze nie męczyło na co dzień."),
            ("Materiały", "Sklejka w zabudowie i wezgłowiu, lniane tkaniny, toczone nóżki i grafiki w cienkich ramach."),
            ("Efekt", "Ciepła, osobista sypialnia z kolorem, który nie przytłacza."),
        ],
        "gallery": [],
    },
    {
        "slug": "dom-001", "code": "SD_HOUSE_001", "status": "viz",
        "title": "Dom z widokiem na ogród", "short": "Dom 001",
        "typ": "Dom jednorodzinny", "lok": "", "rok": "",
        "cover": "viz-dom-001", "card": "viz-dom-001",
        "lead": "Kuchnia otwarta na ogród: ryflowane drewno, kamień i dużo światła z okna od podłogi do sufitu.",
        "blocks": [
            ("Założenia", "Kuchnia jako spokojne centrum domu, z widokiem na zieleń z każdego miejsca przy wyspie."),
            ("Materiały", "Ryflowany front wyspy, zabudowa w jasnym drewnie, kamienne blaty i czarne, lekkie hokery."),
            ("Efekt", "Ciepły minimalizm, w którym rysunek drewna i kamienia zastępuje dekoracje."),
        ],
        "gallery": [],
    },
    {
        "slug": "showroom-spod-igly-i-nitki", "code": "SD_SHOWROOM", "status": "viz",
        "title": "Showroom Spod igły i nitki", "short": "Showroom",
        "typ": "Wnętrze komercyjne", "lok": "", "rok": "",
        "cover": "viz-showroom", "card": "viz-showroom",
        "lead": "Jasny showroom, w którym łuki, drewno i miękkie światło prowadzą klientkę od wejścia do przymierzalni.",
        "blocks": [
            ("Założenia", "Przestrzeń sprzedaży, która uspokaja i pozwala skupić się na produkcie."),
            ("Materiały", "Jasna posadzka, łukowe przejścia, drewniane regały i rzeźbiarskie meble jako akcenty."),
            ("Efekt", "Wnętrze z charakterem butiku, w którym produkt jest najważniejszy."),
        ],
        "gallery": [],
    },
]
BY = {p["slug"]: p for p in PROJECTS}
REAL = [p for p in PROJECTS if p["status"] == "real"]
VIZ = [p for p in PROJECTS if p["status"] == "viz"]
STATUS = {"real": ("Realizacja", "real"), "viz": ("Wizualizacja", "viz")}

NAV = [("realizacje.html", "Realizacje"), ("wizualizacje.html", "Wizualizacje"), ("oferta.html", "Oferta"), ("o-mnie.html", "O mnie")]


def pic(name, ratio="r-4-5", sizes="(max-width: 860px) 100vw, 33vw", eager=False):
    alt, (w, h) = IMG[name]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<div class="ph {ratio}"><img src="img/{name}-s.webp" srcset="img/{name}-s.webp 800w, img/{name}.webp {min(w, 1600)}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" {load} decoding="async"></div>')


def sub(p):
    return " · ".join(x for x in (p["typ"], p["lok"], p["rok"]) if x)


def tag(p):
    t, c = STATUS[p["status"]]
    return f'<span class="tag {c}">{t}</span>'


def card(p, ratio="r-4-5"):
    return (f'<a class="card rv" href="projekt-{p["slug"]}.html">{pic(p["card"], ratio)}'
            f'<div class="meta"><span class="t-code">{p["code"]}</span>{tag(p)}</div>'
            f'<h3>{escape(p["title"])}</h3><p class="sub">{escape(sub(p))}</p></a>')


def page(fname, title, desc, body, current=""):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    html = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="img/mnc-kotara.webp">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23FFC7C8'/%3E%3Ctext x='16' y='23' font-family='Arial' font-weight='700' font-size='20' text-anchor='middle' fill='%235C4741'%3ES%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112,600&family=Hanken+Grotesk:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Przejdź do treści</a>
<header class="hdr">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Smuga Design, strona główna">{STREAK}SMUGA<small>design</small></a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="nav"><span>Menu</span><i aria-hidden="true"></i></button>
    <nav class="nav" id="nav" aria-label="Główne">{links}<a class="cta" href="kontakt.html"{" aria-current=\"page\"" if current == "kontakt.html" else ""}>Kontakt</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="ftr">
  <div class="wrap">
    {STREAK}
    <div class="col"><b>Smuga Design</b><span>Projektowanie wnętrz</span><span>arch. wn. Wioleta Siemieniuk</span></div>
    <div class="col"><b>Kontakt</b><a href="tel:{PHONE_HREF}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="col"><b>Social media</b><a href="{IG}" rel="noopener">@smuga_design</a><a href="{BEHANCE}" rel="noopener">Behance</a></div>
    <p class="mark" aria-hidden="true">SMUGA DESIGN</p>
    <div class="bottom"><span>© 2026 Smuga Design · Białystok</span><span>{"  ·  ".join(f'<a href="{h}">{t}</a>' for h, t in NAV)}</span><span>Demo projektu strony · Impact Agencja</span></div>
  </div>
</footer>
<script src="assets/app.js" defer></script>
</body>
</html>
"""
    (OUT / fname).write_text(html, encoding="utf-8")


def contact_band():
    return f"""<section class="contact" aria-labelledby="c-h">
  <div class="wrap">
    <h2 class="big" id="c-h">Porozmawiajmy o Twoim wnętrzu</h2>
    <div class="lines">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="tel:{PHONE_HREF}">{PHONE}</a>
      <a href="kontakt.html">Formularz zapytania &#8594;</a>
    </div>
  </div>
</section>"""


def steps(label="Jak pracuję"):
    items = [
        ("Rozmowa", "Poznaję Ciebie, sposób życia i budżet. Ustalamy zakres i termin."),
        ("Pomiar i ankieta", "Mierzę wnętrze, robię zdjęcia, zbieram Twoje inspiracje."),
        ("Koncepcja", "Układ funkcjonalny i wizualizacje. Dopracowujemy je razem."),
        ("Projekt wykonawczy", "Rysunki dla ekip, dobór materiałów i kosztorys."),
        ("Realizacja", "Wspieram w wyborach na budowie, aż do sesji zdjęciowej."),
    ]
    lis = "".join(f"<li><b>{a}</b><p>{b}</p></li>" for a, b in items)
    return f"""<section class="sec"><div class="wrap steps">
  <div class="head rv"><p class="t-label muted">{label}</p><h2 class="t-h2">Pięć kroków od rozmowy do gotowego wnętrza</h2><a class="more" href="oferta.html">Zakres i pakiety</a></div>
  <ol class="rv">{lis}</ol>
</div></section>"""


# strona główna
mnc = BY["mnc-concept"]
home = f"""<section class="hero"><div class="wrap">
  <div class="hero-top">
    <h1 class="t-h1 rv">Wnętrza, które zostawiają ślad{STREAK}</h1>
    <div class="intro rv"><p class="t-lead">Pracownia projektowania wnętrz arch. wn. Wiolety Siemieniuk. Ciepły minimalizm z odwagą koloru, dla domów, mieszkań i marek.</p><p class="t-label muted">Białystok · Warszawa · zdalnie</p></div>
  </div>
  <div class="hero-grid">
    <figure class="rv"><a href="projekt-mnc-concept.html">{pic("mnc-kotara", "r-4-5", "(max-width: 860px) 100vw, 42vw", True)}<figcaption><span class="t-code">SD_MNC.CONCEPT_25</span><span class="tag real">Realizacja</span></figcaption></a></figure>
    <figure class="rv"><a href="projekt-mieszkanie-warszawa.html">{pic("viz-apartament-wwa", "r-3-4", "(max-width: 860px) 50vw, 33vw", True)}<figcaption><span class="t-code">SD_APARTMENT_002</span><span class="tag viz">Wizualizacja</span></figcaption></a></figure>
    <figure class="rv"><a href="projekt-dom-001.html">{pic("viz-dom-001", "r-1-1", "(max-width: 860px) 50vw, 25vw", True)}<figcaption><span class="t-code">SD_HOUSE_001</span><span class="tag viz">Wizualizacja</span></figcaption></a></figure>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><p class="t-label muted">Realizacje</p><h2 class="t-h2 rv">Wnętrza, które już żyją</h2><a class="more" href="realizacje.html">Wszystkie realizacje</a></div>
  <a class="feature rv" href="projekt-mnc-concept.html">
    {pic("mnc-sala", "r-5-4", "(max-width: 860px) 100vw, 58vw")}
    <div class="txt">
      <div><span class="t-code">{mnc["code"]}</span><h3>{mnc["title"]}</h3><p class="t-lead muted">{mnc["lead"]}</p></div>
      <dl class="facts"><div><dt>Typ</dt><dd>{mnc["typ"]}</dd></div><div><dt>Miasto</dt><dd>{mnc["lok"]}</dd></div><div><dt>Rok</dt><dd>{mnc["rok"]}</dd></div><div><dt>Status</dt><dd>Realizacja</dd></div></dl>
    </div>
  </a>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><p class="t-label muted">Wizualizacje</p><h2 class="t-h2 rv">Projekty, które czekają na realizację</h2><a class="more" href="wizualizacje.html">Wszystkie wizualizacje</a></div>
  <div class="grid">{"".join(card(p, "r-5-4") for p in VIZ)}</div>
</div></section>

<section class="sec"><div class="wrap about">
  <div class="rv">{pic("smuga-wioleta", "r-5-4", "(max-width: 860px) 100vw, 40vw")}</div>
  <div class="txt rv">
    <p class="t-label muted">O mnie</p>
    <h2 class="t-h2">Projektuję wnętrza jak światło, które wpada przez okno</h2>
    <p class="t-lead">Smuga to ślad: światła na podłodze, pędzla na ścianie, człowieka w przestrzeni. Spokojną bazę z naturalnych materiałów łączę z jednym odważnym gestem, kolorem albo sztuką.</p>
    <p class="muted">Prowadzę projekt od pierwszej rozmowy do sesji zdjęciowej gotowego wnętrza. Pracuję w Białymstoku, w Warszawie i zdalnie.</p>
    <div class="sign"><span>arch. wn. Wioleta Siemieniuk</span><a class="more" href="o-mnie.html">Więcej o mnie</a></div>
  </div>
</div></section>

{steps()}

<section class="band"><div class="wrap">
  <div class="txt rv"><p class="t-label">Dla biznesu</p><h2 class="t-h2">Wnętrza, które pracują na markę</h2><p class="t-lead">Kawiarnie, showroomy i lokale usługowe. Projektuję przestrzeń, którą klienci rozpoznają po jednym zdjęciu.</p><a class="more" href="oferta.html#biznes">Wnętrza komercyjne</a></div>
  <div class="pics rv">{pic("mnc-bar", "r-3-4", "(max-width: 860px) 60vw, 30vw")}{pic("mnc-lada", "r-3-4", "(max-width: 860px) 40vw, 20vw")}</div>
</div></section>

{contact_band()}"""
page("index.html", "Smuga Design · projektowanie wnętrz Białystok", "Pracownia projektowania wnętrz arch. wn. Wiolety Siemieniuk. Realizacje i wizualizacje domów, mieszkań i wnętrz komercyjnych. Białystok, Warszawa.", home)


# listy
def listing(fname, h1, lead, items, extra=""):
    sw = (f'<nav class="switch" aria-label="Rodzaj projektów"><a href="realizacje.html"{" aria-current=\"page\"" if fname == "realizacje.html" else ""}>Realizacje<sup>{len(REAL)}</sup></a>'
          f'<a href="wizualizacje.html"{" aria-current=\"page\"" if fname == "wizualizacje.html" else ""}>Wizualizacje<sup>{len(VIZ)}</sup></a></nav>')
    body = f"""<div class="wrap">
  <div class="page-head"><p class="crumbs"><a href="index.html">Start</a><span>/</span><span>{h1}</span></p><h1 class="t-h1">{h1}</h1><p class="t-lead muted">{lead}</p></div>
  {sw}
  <div class="grid">{"".join(card(p) for p in items)}{extra}</div>
</div>
<div style="height:128px"></div>
{contact_band()}"""
    page(fname, f"{h1} · Smuga Design", lead, body, fname)


soon = """<div class="soon rv"><span class="t-label muted">Wkrótce</span><div><h3 class="t-h3">Kolejne sesje zdjęciowe w przygotowaniu</h3><p>Gdy wizualizacja zostanie zrealizowana, projekt trafia tutaj ze zdjęciami z sesji, pod tym samym adresem.</p></div></div>"""
listing("realizacje.html", "Realizacje", "Wnętrza wykonane i sfotografowane po zakończeniu prac. Każdy projekt z pełną metryczką.", REAL, soon)
listing("wizualizacje.html", "Wizualizacje", "Projekty pokazane w wizualizacjach. Każde zdjęcie na tej stronie to wizualizacja, nie fotografia.", VIZ)


# strony projektów
order = [p["slug"] for p in PROJECTS]
for p in PROJECTS:
    nxt = BY[order[(order.index(p["slug"]) + 1) % len(order)]]
    facts = [("Kod", p["code"]), ("Typ", p["typ"]), ("Lokalizacja", p["lok"]), ("Rok", p["rok"]), ("Status", STATUS[p["status"]][0])]
    facts_html = "".join(f"<div><dt>{a}</dt><dd>{escape(b)}</dd></div>" for a, b in facts if b)
    blocks = "".join(f"<div><h2>{a}</h2><p>{b}</p></div>" for a, b in p["blocks"])
    shots = [p["cover"]] + p["gallery"]
    gal = ""
    if p["gallery"]:
        cells = []
        for i, name in enumerate(p["gallery"], start=1):
            full = i % 3 == 1
            ratio = "r-3-2" if full else "r-4-5"
            cells.append(f'<button type="button" class="rv{" full" if full else ""}" data-open="{i}" aria-label="Powiększ zdjęcie {i + 1} z {len(shots)}">{pic(name, ratio, "(max-width: 860px) 100vw, " + ("100vw" if full else "50vw"))}</button>')
        idx = "".join(f'<button type="button" data-open="{i}" aria-label="Zdjęcie {i + 1}">{pic(n, "r-1-1", "120px")}<span>{i + 1:02d}</span></button>' for i, n in enumerate(shots))
        gal = f'<div class="gal">{"".join(cells)}</div><div class="index"><p class="t-label muted">Indeks zdjęć ({len(shots)})</p>{idx}</div>'
    else:
        gal = '<p class="gal-note t-lead">Pełna galeria wizualizacji pojawi się tu po przekazaniu materiałów. W demo pokazujemy okładkę projektu.</p>'
    data = "".join(f'<span hidden data-shot="img/{n}.webp" data-alt="{escape(IMG[n][0])}"></span>' for n in shots)
    lb = f"""<div class="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęć">
  <div class="lb-top"><span class="lb-count t-code"></span><button type="button" class="close">Zamknij</button></div>
  <div class="lb-stage"><img src="" alt=""></div>
  <div class="lb-bot"><span class="lb-cap"></span></div>
  <button type="button" class="prev" aria-label="Poprzednie zdjęcie">&#8592;</button><button type="button" class="nextb" aria-label="Następne zdjęcie">&#8594;</button>
</div>""" if p["gallery"] else ""
    listpage = "realizacje.html" if p["status"] == "real" else "wizualizacje.html"
    body = f"""<div class="wrap">
  <div class="p-head">
    <div class="row"><p class="crumbs"><a href="index.html">Start</a><span>/</span><a href="{listpage}">{"Realizacje" if p["status"] == "real" else "Wizualizacje"}</a><span>/</span><span>{p["short"]}</span></p><div>{tag(p)}</div></div>
    <h1 class="p-title">{escape(p["title"])}</h1>
  </div>
  <div class="p-hero">{'<button type="button" data-open="0" aria-label="Powiększ zdjęcie główne" style="all:unset;display:block;cursor:zoom-in;width:100%">' if p["gallery"] else ''}{pic(p["cover"], "r-3-2", "100vw", True)}{'</button>' if p["gallery"] else ''}</div>
  <div class="p-info">
    <dl class="facts rv">{facts_html}</dl>
    <div class="desc rv"><p class="t-lead">{p["lead"]}</p><div class="blocks">{blocks}</div></div>
  </div>
  {gal}{data}
  <div style="height:128px"></div>
  <a class="next rv" href="projekt-{nxt["slug"]}.html"><div class="txt"><p class="t-label muted">Następny projekt</p><h2>{escape(nxt["title"])}</h2><p class="sub muted t-label" style="margin-top:12px">{escape(sub(nxt))}</p></div>{pic(nxt["card"], "r-3-2", "(max-width: 860px) 100vw, 58vw")}</a>
</div>
<div style="height:128px"></div>
{lb}
{contact_band()}"""
    page(f"projekt-{p['slug']}.html", f"{p['title']} · {STATUS[p['status']][0]} · Smuga Design", p["lead"], body, listpage)


# oferta
pk = [
    ("Konsultacja", "", ["spotkanie w Twoim wnętrzu", "kierunek kolorów i materiałów", "lista zmian do zrobienia samodzielnie"], "cena za spotkanie"),
    ("Projekt koncepcyjny", "", ["układ funkcjonalny", "wizualizacje kluczowych pomieszczeń", "paleta materiałów"], "cena za m²"),
    ("Projekt kompleksowy", "rec", ["koncepcja i wizualizacje", "projekt wykonawczy dla ekip", "dobór materiałów i kosztorys", "wsparcie podczas realizacji"], "cena za m²"),
]
pk_html = "".join(f'<article class="{c} rv"><p class="t-label muted">{"Najczęściej wybierany" if c else "Pakiet"}</p><h3>{n}</h3><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul><p class="price"><span class="t-label muted">Cena</span><br>od ... zł, {pr} <span class="muted">(do ustalenia)</span></p></article>' for n, c, li, pr in pk)
faq = [
    ("Ile kosztuje projekt wnętrz?", "Zależy od metrażu i zakresu. Projekt kompleksowy w Białymstoku to zwykle 180-380 zł za m². Dokładną wycenę przygotowuję po pierwszej rozmowie."),
    ("Ile trwa projekt?", "Koncepcja dla mieszkania to zwykle kilka tygodni, projekt kompleksowy kilka miesięcy. Termin ustalamy na starcie."),
    ("Czy pracujesz zdalnie?", "Tak. Pomiar i spotkania mogą odbywać się online, a materiały wysyłam w formie cyfrowej."),
    ("Co dostaję na koniec?", "Wizualizacje, rysunki wykonawcze dla ekip, listę materiałów z kosztorysem i wsparcie przy realizacji, zależnie od pakietu."),
    ("Czy projektujesz wnętrza komercyjne?", "Tak: kawiarnie, showroomy i lokale usługowe. Przykładem jest kawiarnia MNC Concept w Białymstoku."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
oferta = f"""<div class="wrap"><div class="page-head"><p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Oferta</span></p><h1 class="t-h1">Oferta</h1><p class="t-lead muted">Od jednej konsultacji po projekt kompleksowy z kosztorysem. Ceny "od" uzupełnimy po spotkaniu.</p></div></div>
<section class="sec" style="padding-top:48px"><div class="wrap"><div class="pk">{pk_html}</div></div></section>
{steps("Proces")}
<section class="sec" id="biznes"><div class="wrap about">
  <div class="rv">{pic("mnc-loza", "r-4-5", "(max-width: 860px) 100vw, 40vw")}</div>
  <div class="txt rv"><p class="t-label muted">Dla biznesu</p><h2 class="t-h2">Wnętrza komercyjne</h2><p class="t-lead">Kawiarnie, showroomy, lokale usługowe. Wnętrze, które buduje markę i dobrze wygląda na zdjęciach klientów.</p><p class="muted">Projekt uwzględnia identyfikację marki, przepływ gości i obsługi oraz budżet inwestycji.</p><div class="sign"><span>Realizacja: kawiarnia MNC Concept</span><a class="more" href="projekt-mnc-concept.html">Zobacz projekt</a></div></div>
</div></section>
<section class="sec"><div class="wrap steps"><div class="head rv"><p class="t-label muted">Pytania</p><h2 class="t-h2">Najczęstsze pytania</h2></div><div class="faq rv">{faq_html}</div></div></section>
{contact_band()}"""
page("oferta.html", "Oferta · projektowanie wnętrz · Smuga Design", "Konsultacja, projekt koncepcyjny i kompleksowy, wnętrza komercyjne. Proces, pakiety i najczęstsze pytania.", oferta, "oferta.html")


# o mnie
omnie = f"""<div class="wrap"><div class="page-head"><p class="crumbs"><a href="index.html">Start</a><span>/</span><span>O mnie</span></p><h1 class="t-h1">Wioleta Siemieniuk</h1><p class="t-lead muted">Architektka wnętrz, założycielka Smuga Design.</p></div></div>
<section class="sec" style="padding-top:48px"><div class="wrap about">
  <div class="rv">{pic("smuga-wioleta", "r-5-4", "(max-width: 860px) 100vw, 40vw", True)}</div>
  <div class="txt rv">
    <p class="t-label muted">Podejście</p>
    <h2 class="t-h2">Spokojna baza i jeden odważny gest</h2>
    <p class="t-lead">Lubię naturalne materiały: drewno, kamień, len. Na nich buduję wnętrza, w których jest miejsce na kolor i sztukę.</p>
    <p class="muted">Każdy projekt dostaje swój kod, jak w katalogu. Dzięki temu łatwo wrócić do decyzji, materiałów i zdjęć, także po latach. Tekst do uzupełnienia o wykształcenie, doświadczenie i publikacje.</p>
    <div class="sign"><a href="{IG}" rel="noopener">Instagram @smuga_design</a><a href="{BEHANCE}" rel="noopener">Behance</a></div>
  </div>
</div></section>
{steps()}
{contact_band()}"""
page("o-mnie.html", "O mnie · Wioleta Siemieniuk · Smuga Design", "Arch. wn. Wioleta Siemieniuk, Smuga Design. Ciepły minimalizm z odwagą koloru.", omnie, "o-mnie.html")


# kontakt
opts = lambda xs: "".join(f"<option>{x}</option>" for x in xs)
kontakt = f"""<div class="wrap"><div class="page-head"><p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Kontakt</span></p><h1 class="t-h1">Kontakt</h1><p class="t-lead muted">Opisz krótko wnętrze. Im więcej szczegółów, tym szybciej przygotuję wycenę.</p></div></div>
<section class="sec" style="padding-top:48px"><div class="wrap steps">
  <div class="head">
    <p class="t-label muted">Bezpośrednio</p>
    <h2 class="t-h2" style="margin:16px 0 24px">Napisz albo zadzwoń</h2>
    <dl class="facts"><div><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Telefon</dt><dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd></div><div><dt>Instagram</dt><dd><a href="{IG}" rel="noopener">@smuga_design</a></dd></div><div><dt>Obszar</dt><dd>Białystok, Warszawa, zdalnie</dd></div></dl>
  </div>
  <form class="form" novalidate>
    <label>Imię<input name="imie" autocomplete="given-name" required></label>
    <label>E-mail<input type="email" name="email" autocomplete="email" required></label>
    <label>Telefon<input type="tel" name="tel" autocomplete="tel"></label>
    <label>Rodzaj wnętrza<select name="typ" required><option value="">Wybierz</option>{opts(["Mieszkanie", "Dom", "Wnętrze komercyjne", "Inne"])}</select></label>
    <label>Lokalizacja<input name="miasto" placeholder="np. Białystok"></label>
    <label>Metraż (m²)<input name="metraz" inputmode="numeric" placeholder="np. 65"></label>
    <label>Zakres<select name="zakres"><option value="">Wybierz</option>{opts(["Konsultacja", "Projekt koncepcyjny", "Projekt kompleksowy", "Jeszcze nie wiem"])}</select></label>
    <label>Kiedy chcesz zacząć<select name="termin"><option value="">Wybierz</option>{opts(["Jak najszybciej", "W ciągu 3 miesięcy", "Za 3-6 miesięcy", "Później"])}</select></label>
    <label class="full">Budżet na projekt i wykończenie<select name="budzet"><option value="">Wybierz</option>{opts(["do 100 tys. zł", "100-250 tys. zł", "250-500 tys. zł", "powyżej 500 tys. zł", "Wolę omówić na rozmowie"])}</select></label>
    <label class="full">Wiadomość<textarea name="wiadomosc" placeholder="Co chcesz zmienić? Co lubisz, czego nie?"></textarea></label>
    <label class="full">Rzut lub zdjęcia (opcjonalnie)<input type="file" name="pliki" multiple accept=".pdf,.jpg,.jpeg,.png"></label>
    <label class="consent full"><input type="checkbox" required> Zgadzam się na kontakt w sprawie zapytania. Dane przetwarza Smuga Design zgodnie z polityką prywatności.</label>
    <button class="btn" type="submit">Wyślij zapytanie</button>
    <p class="form-ok" hidden tabindex="-1">To jest demo: formularz niczego nie wysyła. Na gotowej stronie wiadomość trafi na {EMAIL}.</p>
  </form>
</div></section>"""
page("kontakt.html", "Kontakt · Smuga Design", "Zapytanie o projekt wnętrza: mieszkanie, dom, wnętrze komercyjne. Białystok, Warszawa, zdalnie.", kontakt, "kontakt.html")

print("ok:", sorted(x.name for x in OUT.glob("*.html")))
