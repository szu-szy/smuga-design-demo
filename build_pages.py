"""Szablony stron demo Smuga Design v2. Dane w build_head.py. Uruchom: python3 build.py"""
from build_head import *  # noqa: F401,F403 - dane projektów, zdjęć i kontaktu

V = "3"
NAV_L = [("realizacje.html", "Realizacje"), ("wizualizacje.html", "Wizualizacje")]
NAV_R = [("oferta.html", "Oferta"), ("o-mnie.html", "O mnie"), ("kontakt.html", "Kontakt")]
STREAK_PATH = "M12 60C14 44 30 38 54 32C76 26 86 20 88 4H108C108 24 92 36 64 42C42 47 32 50 32 60Z"
DRAW_PATH = "M22 58C24 46 36 40 58 35C80 30 96 22 98 6"


def mark(cls="streak"):
    return f'<svg class="{cls}" viewBox="0 0 120 64" aria-hidden="true"><path d="{STREAK_PATH}"/></svg>'


def mark_draw():
    return f'<svg class="streak-draw" viewBox="0 0 120 64" aria-hidden="true"><path d="{DRAW_PATH}"/></svg>'


def pic(name, ratio="r-4-5", sizes="(max-width: 860px) 100vw, 50vw", eager=False):
    alt, (w, h) = IMG[name]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<div class="ph {ratio}"><img src="img/{name}-s.webp" srcset="img/{name}-s.webp 800w, img/{name}.webp {min(w, 1600)}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" {load} decoding="async"></div>')


def status_name(p):
    return STATUS[p["status"]][0]


def tag(p):
    return f'<span class="tag{" real" if p["status"] == "real" else ""}">{status_name(p)}</span>'


def facts(p, keys=("Typ", "Lokalizacja", "Rok", "Status")):
    vals = {"Kod": p["code"], "Typ": p["typ"], "Lokalizacja": p["lok"], "Rok": p["rok"], "Status": status_name(p)}
    return "".join(f"<div><dt>{k}</dt><dd>{escape(vals[k])}</dd></div>" for k in keys if vals[k])


def header(current, over):
    left = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV_L)
    right = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV_R)
    drawer = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV_L + NAV_R)
    return f"""<header class="hdr{" over" if over else ""}">
  <div class="wrap">
    <nav class="nav" aria-label="Projekty">{left}</nav>
    <a class="logo" href="index.html" aria-label="Smuga Design, strona główna">{mark_draw()}SMUGA</a>
    <nav class="nav r" aria-label="Pracownia">{right}</nav>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer"><span>Menu</span><i aria-hidden="true"></i></button>
  </div>
</header>
<div class="drawer" id="drawer">{drawer}<div class="small"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_HREF}">{PHONE}</a></div></div>"""


def footer():
    return f"""<footer class="ftr">
  <div class="wrap g12">
    <div class="mk">{mark()}</div>
    <div class="col"><b>Smuga Design</b><span>Projektowanie wnętrz</span><span>arch. wn. Wioleta Siemieniuk</span></div>
    <div class="col"><b>Kontakt</b><a href="tel:{PHONE_HREF}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="col"><b>Social media</b><a href="{IG}" rel="noopener">@smuga_design</a><a href="{BEHANCE}" rel="noopener">Behance</a></div>
    <p class="mark" aria-hidden="true">SMUGA DESIGN</p>
    <div class="bottom"><span>© 2026 Smuga Design · Białystok</span><span>{" · ".join(f'<a href="{h}">{t}</a>' for h, t in NAV_L + NAV_R)}</span><span>Demo projektu strony · Impact Agencja</span></div>
  </div>
</footer>"""


def page(fname, title, desc, body, current="", over=False, og="mnc-kotara"):
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
<meta property="og:image" content="img/{og}.webp">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 64'%3E%3Cpath fill='%23FFC7C8' d='{STREAK_PATH}'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..112,400..600&family=Hanken+Grotesk:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v={V}">
</head>
<body>
<a class="skip" href="#main">Przejdź do treści</a>
{header(current, over)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/app.js?v={V}" defer></script>
</body>
</html>
"""
    (OUT / fname).write_text(html, encoding="utf-8")


def cta():
    return f"""<section class="cta" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 class="d-xxl rv" id="cta-h">Porozmawiajmy</h2>
    <div class="row stag">
      <p class="lead">O mieszkaniu, domu albo lokalu. Pierwsza rozmowa niczego nie zobowiązuje, a po niej wiesz, jak mogłoby wyglądać Twoje wnętrze.</p>
      <div class="links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_HREF}">{PHONE}</a></div>
      <a class="btn" href="kontakt.html">Opisz swoje wnętrze</a>
    </div>
  </div>
</section>"""


STEPS = [
    ("Rozmowa", "Poznaję Ciebie, sposób życia i potrzeby. Ustalamy zakres i termin."),
    ("Pomiar", "Mierzę wnętrze, robię zdjęcia, zbieram Twoje inspiracje."),
    ("Koncepcja", "Układ funkcjonalny i wizualizacje, które dopracowujemy razem."),
    ("Projekt wykonawczy", "Rysunki dla ekip, dobór materiałów i zestawienie kosztów."),
    ("Realizacja", "Jestem przy wyborach na budowie, aż do sesji zdjęciowej."),
]


def process(title="Pięć kroków od pierwszej rozmowy do gotowego wnętrza"):
    lis = "".join(f"<li><b>{a}</b><p class=\"muted\">{b}</p></li>" for a, b in STEPS)
    return f"""<section class="proc"><div class="wrap">
  <div class="head g12"><p class="lbl">Jak pracuję</p><h2 class="d-m rv">{title}</h2></div>
  <ol class="stag">{lis}</ol>
</div></section>"""


SERVICES = [
    ("mieszkania", "Mieszkania", "Od kawalerki po apartament. Układ, zabudowy, światło, materiały."),
    ("domy", "Domy", "Całe wnętrze domu jednorodzinnego, także na etapie budowy."),
    ("komercyjne", "Wnętrza komercyjne", "Kawiarnie, showroomy, lokale usługowe, które pracują na markę."),
    ("wizualizacje", "Wizualizacje", "Realistyczne obrazy wnętrza, zanim zapadną decyzje i wydatki."),
    ("konsultacje", "Konsultacje", "Jedno spotkanie, konkretny kierunek kolorów, materiałów i zmian."),
]


# STRONA GŁÓWNA
chapters = []
for i, p in enumerate(PROJECTS, start=1):
    flip = " flip" if i % 2 == 0 else ""
    ratio = "r-5-4"
    img = p["card"] if p["status"] == "real" else p["cover"]
    chapters.append(f"""<section class="chap {p["field"]}{flip}" aria-labelledby="ch{i}">
  <div class="wrap">
    <div class="chap-top"><span class="num">{i:02d} / {len(PROJECTS):02d}</span><span class="code">{p["code"]}</span>{tag(p)}</div>
    <div class="g12">
      <a class="media mask" href="projekt-{p["slug"]}.html" tabindex="-1" aria-hidden="true">{pic(img, ratio, "(max-width: 1080px) 100vw, 66vw")}</a>
      <div class="txt stag">
        <h2 class="d-m" id="ch{i}">{escape(p["title"])}</h2>
        <p>{p["lead"]}</p>
        <dl class="meta">{facts(p)}</dl>
        <a class="lnk" href="projekt-{p["slug"]}.html">Zobacz projekt</a>
      </div>
    </div>
  </div>
</section>""")

svc_rows = "".join(f'<li><a href="oferta.html#{k}"><span class="code muted">{i:02d}</span><span class="d-l"><span class="hl">{n}</span></span><p class="muted">{d}</p><span class="ar" aria-hidden="true">&#8594;</span></a></li>' for i, (k, n, d) in enumerate(SERVICES, start=1))

home = f"""<section class="hero" aria-labelledby="hero-h">
  <img src="img/mnc-kotara.webp" srcset="img/mnc-kotara-s.webp 800w, img/mnc-kotara.webp 1400w" sizes="100vw" width="1400" height="1960" alt="{escape(IMG["mnc-kotara"][0])}" fetchpriority="high">
  <div class="sweep" aria-hidden="true"></div>
  <div class="wrap">
    <h1 class="d-xl" id="hero-h">Wnętrza, które zostawiają ślad{mark()}</h1>
    <div class="hero-bar">
      <p class="lead">Pracownia projektowania wnętrz arch. wn. Wiolety Siemieniuk. Ciepły minimalizm z odwagą koloru.</p>
      <span class="lbl">Białystok · Warszawa · zdalnie</span>
      <a class="lnk" href="#projekty">Zobacz projekty</a>
    </div>
  </div>
</section>

<section class="intro" id="projekty"><div class="wrap g12">
  <p class="lbl muted">Wybrane projekty</p>
  <h2 class="d-l rv">Spokojna baza, naturalne materiały i jeden <em>odważny gest</em>: kolor, sztuka albo światło.</h2>
</div></section>

{"".join(chapters)}

<section class="studio"><div class="wrap g12">
  <figure class="pic mask">{pic("smuga-wioleta", "r-4-5", "(max-width: 1080px) 100vw, 40vw")}<figcaption class="small muted"><span>arch. wn. Wioleta Siemieniuk</span><span>Założycielka</span></figcaption></figure>
  <div class="txt">
    <p class="lbl muted">Pracownia</p>
    <h2 class="d-m rv">Smuga to ślad. Światła na podłodze, pędzla na ścianie, człowieka w przestrzeni.</h2>
    <ul class="means stag">
      <li><b>Światło</b><span class="muted">Projektuję od okna: gdzie pada słońce, tam zaczyna się wnętrze.</span></li>
      <li><b>Kolor</b><span class="muted">Jeden odważny akcent zamiast dziesięciu bezpiecznych.</span></li>
      <li><b>Materiał</b><span class="muted">Drewno, kamień, len i stal, które ładnie się starzeją.</span></li>
      <li><b>Porządek</b><span class="muted">Każdy projekt ma swój kod i pełny opis, jak w katalogu.</span></li>
    </ul>
    <p style="margin-top:32px"><a class="lnk" href="o-mnie.html">Poznaj pracownię</a></p>
  </div>
</div></section>

<section class="svc"><div class="wrap">
  <div class="svc-head g12"><p class="lbl muted">Co projektuję</p><p class="lead">Od jednej konsultacji po kompletny projekt z nadzorem nad realizacją.</p></div>
  <ul class="svc-list">{svc_rows}</ul>
</div></section>

{process()}
{cta()}"""
page("index.html", "Smuga Design · projektowanie wnętrz Białystok", "Pracownia projektowania wnętrz arch. wn. Wiolety Siemieniuk. Realizacje i wizualizacje domów, mieszkań i wnętrz komercyjnych. Białystok, Warszawa.", home, over=True)


# LISTY
def idx_row(p, i):
    return (f'<a class="idx-row stag" href="projekt-{p["slug"]}.html"><span class="code muted num-c">{i:02d}</span>{pic(p["card"], "", "280px")}'
            f'<span><span class="d-m">{escape(p["title"])}</span><span class="code muted" style="display:block;margin-top:8px">{p["code"]}</span></span>'
            f'<span class="hide-t muted">{escape(p["typ"])}</span><span class="hide-t hide-m muted">{escape(p["lok"] or "")}</span><span class="end hide-m">{tag(p)}</span></a>')


def listing(fname, h1, lead, items, soon=""):
    sw = (f'<nav class="switch" aria-label="Rodzaj projektów"><a href="realizacje.html"{" aria-current=\"page\"" if fname == "realizacje.html" else ""}>Realizacje<sup>{len(REAL):02d}</sup></a>'
          f'<a href="wizualizacje.html"{" aria-current=\"page\"" if fname == "wizualizacje.html" else ""}>Wizualizacje<sup>{len(VIZ):02d}</sup></a></nav>')
    first = items[0]
    big = f'<div class="idx-big"><a class="mask" href="projekt-{first["slug"]}.html" aria-label="{escape(first["title"])}">{pic(first["cover"] if first["status"] == "viz" else first["card"], "r-16-9", "100vw", True)}</a></div>'
    rows = "".join(idx_row(p, i) for i, p in enumerate(items, start=1)) + soon
    body = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>{h1}</span></p>
  <div class="g12"><h1 class="d-xl">{h1}</h1><p class="lead muted">{lead}</p></div>
</div></div>
<div class="wrap">{sw}{big}</div>
<section class="idx"><div class="wrap">{rows}</div></section>
{cta()}"""
    page(fname, f"{h1} · Smuga Design", lead, body, fname)


soon_row = f'<div class="idx-row soon"><span class="code num-c">+</span><div class="ph">{mark()}</div><span><span class="d-m">Kolejne sesje w przygotowaniu</span><span class="small" style="display:block;margin-top:8px">Zrealizowane wizualizacje trafią tutaj ze zdjęciami z sesji, pod tym samym adresem.</span></span></div>'
listing("realizacje.html", "Realizacje", "Wnętrza wykonane i sfotografowane po zakończeniu prac. Każdy projekt z pełną metryczką.", REAL, soon_row)
listing("wizualizacje.html", "Wizualizacje", "Projekty pokazane w wizualizacjach. Każde zdjęcie w tej zakładce to wizualizacja, nie fotografia.", VIZ)


# STRONY PROJEKTÓW
order = [p["slug"] for p in PROJECTS]
for p in PROJECTS:
    nxt = BY[order[(order.index(p["slug"]) + 1) % len(order)]]
    blocks = "".join(f"<div><h2>{a}</h2><p>{b}</p></div>" for a, b in p["blocks"])
    shots = [p["cover"]] + p["gallery"]
    data = "".join(f'<span hidden data-shot="img/{n}.webp" data-alt="{escape(IMG[n][0])}"></span>' for n in shots)
    has_gal = bool(p["gallery"])
    if has_gal:
        figs = []
        layout = ["full", "", "off", "full", "", "off"]
        for i, name in enumerate(p["gallery"], start=1):
            cls = layout[(i - 1) % len(layout)]
            ratio = "r-3-2" if cls == "full" else "r-4-5"
            figs.append(f'<figure class="{cls} mask"><button type="button" data-open="{i}" aria-label="Powiększ zdjęcie {i + 1} z {len(shots)}">{pic(name, ratio, "(max-width: 1080px) 100vw, 60vw")}</button><figcaption><b>{i + 1:02d}</b><span>{escape(IMG[name][0].split(",")[0])}</span></figcaption></figure>')
            if i == 3:
                figs.append(f'<blockquote class="d-m rv">"{p["blocks"][2][1]}"</blockquote>')
        right = f'<div class="p-gal">{"".join(figs)}</div>'
    else:
        right = f'<div class="p-note"><p class="lbl muted">Galeria</p><p class="d-s">Pełna galeria wizualizacji pojawi się tutaj po przekazaniu materiałów.</p><p class="muted">W demo pokazujemy okładkę projektu z Behance. Gdy wnętrze zostanie wykonane, nad galerią pojawi się przełącznik „Zdjęcia z realizacji | Wizualizacje”.</p></div>'
    hero = pic(p["cover"], "", "100vw", True)
    hero = f'<button type="button" data-open="0" aria-label="Powiększ zdjęcie główne">{hero}</button>' if has_gal else hero
    lb = """<div class="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęć">
  <div class="lb-top"><span class="lb-count code"></span><button type="button" class="close">Zamknij</button></div>
  <div class="lb-stage"><img src="" alt=""></div>
  <div class="lb-bot"><span class="lb-cap small"></span></div>
  <button type="button" class="prev" aria-label="Poprzednie zdjęcie">&#8592;</button><button type="button" class="nextb" aria-label="Następne zdjęcie">&#8594;</button>
</div>""" if has_gal else ""
    listpage = "realizacje.html" if p["status"] == "real" else "wizualizacje.html"
    body = f"""<div class="p-top"><div class="wrap">
  <div class="row"><p class="crumbs"><a href="index.html">Start</a><span>/</span><a href="{listpage}">{"Realizacje" if p["status"] == "real" else "Wizualizacje"}</a><span>/</span><span>{p["short"]}</span></p><span class="code">{p["code"]}</span></div>
  <h1 class="d-xl">{escape(p["title"])}</h1>
</div></div>
<div class="p-hero"><div class="wrap mask in">{hero}</div></div>
<section class="p-body"><div class="wrap g12">
  <aside class="p-side">
    <div>{tag(p)}</div>
    <p class="lead">{p["lead"]}</p>
    <dl class="facts">{facts(p, ("Kod", "Typ", "Lokalizacja", "Rok", "Status"))}</dl>
    <div class="blocks">{blocks}</div>
  </aside>
  {right}
</div></section>
{data}
<a class="next-chap{" chap " + nxt["field"] if nxt["field"] else ""}" href="projekt-{nxt["slug"]}.html"><div class="wrap g12">
  <div class="txt"><p class="lbl">Następny projekt</p><h2 class="d-l">{escape(nxt["title"])}</h2><span class="code">{nxt["code"]} · {status_name(nxt)}</span></div>
  {pic(nxt["card"], "r-3-2", "(max-width: 860px) 100vw, 58vw")}
</div></a>
{lb}
{cta()}"""
    page(f"projekt-{p['slug']}.html", f"{p['title']} · {status_name(p)} · Smuga Design", p["lead"], body, listpage, og=p["cover"])


# OFERTA (bez cen)
SVC_DETAIL = {
    "mieszkania": ("Projekt, który porządkuje codzienność: gdzie stoi łóżko, jak pada światło, ile mieści szafa.", ["układ funkcjonalny i warianty", "wizualizacje pomieszczeń", "rysunki zabudów i elektryki", "dobór materiałów i zestawienie"]),
    "domy": ("Wnętrze domu projektowane razem z jego bryłą i ogrodem, najlepiej już na etapie budowy.", ["koncepcja dla całego domu", "wizualizacje kluczowych stref", "projekt wykonawczy dla ekip", "wsparcie podczas realizacji"]),
    "komercyjne": ("Przestrzeń, która buduje markę i dobrze wygląda na zdjęciach klientów. Przykład: kawiarnia MNC Concept.", ["identyfikacja marki we wnętrzu", "przepływ gości i obsługi", "dobór trwałych materiałów", "koordynacja z wykonawcami"]),
    "wizualizacje": ("Realistyczne obrazy wnętrza, które pomagają podjąć decyzje, zanim zaczną się wydatki.", ["wizualizacje projektów własnych", "warianty kolorów i materiałów", "obrazy do sprzedaży nieruchomości"]),
    "konsultacje": ("Jedno spotkanie w Twoim wnętrzu i konkretny kierunek zmian do zrobienia samodzielnie.", ["kierunek kolorów i materiałów", "lista zmian krok po kroku", "spotkanie na miejscu albo online"]),
}
det = "".join(f'<details id="{k}"{" open" if i == 1 else ""}><summary><span class="code muted">{i:02d}</span><span class="d-l">{n}</span></summary><div class="body"><p class="lead">{SVC_DETAIL[k][0]}</p><ul>{"".join(f"<li>{x}</li>" for x in SVC_DETAIL[k][1])}</ul></div></details>' for i, (k, n, _d) in enumerate(SERVICES, start=1))
FAQ = [
    ("Od czego zaczynamy?", "Od rozmowy. Opowiadasz o wnętrzu i o tym, jak chcesz w nim żyć, a ja proponuję zakres i termin."),
    ("Jak wyceniasz projekt?", "Indywidualnie, po rozmowie i obejrzeniu wnętrza. Wycena zależy od metrażu i zakresu, a otrzymujesz ją na piśmie przed startem."),
    ("Ile trwa projekt?", "Koncepcja dla mieszkania to zwykle kilka tygodni, projekt kompleksowy kilka miesięcy. Termin ustalamy na starcie."),
    ("Czy pracujesz zdalnie?", "Tak. Pomiar i spotkania mogą odbywać się online, a materiały wysyłam w formie cyfrowej."),
    ("Co dostaję na koniec?", "Wizualizacje, rysunki wykonawcze dla ekip i listę materiałów, zależnie od zakresu. Przy realizacji jestem z Tobą do końca."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
oferta = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Oferta</span></p>
  <div class="g12"><h1 class="d-xl">Co projektuję</h1><p class="lead muted">Od jednej konsultacji po kompletny projekt z wizualizacjami i wsparciem przy realizacji. Każdą współpracę wyceniam indywidualnie.</p></div>
</div></div>
<section class="svc-detail"><div class="wrap">{det}</div></section>
{process()}
<section class="svc"><div class="wrap g12">
  <div style="grid-column:1/5"><p class="lbl muted">Pytania</p><h2 class="d-m rv" style="margin-top:16px">Najczęściej słyszę</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>
{cta()}"""
page("oferta.html", "Oferta · projektowanie wnętrz · Smuga Design", "Mieszkania, domy, wnętrza komercyjne, wizualizacje i konsultacje. Proces współpracy i najczęstsze pytania.", oferta, "oferta.html")


# O MNIE
omnie = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>O mnie</span></p>
  <div class="g12"><h1 class="d-xl">Wioleta Siemieniuk</h1><p class="lead muted">Architektka wnętrz, założycielka Smuga Design.</p></div>
</div></div>
<section class="studio" style="padding-top:32px"><div class="wrap g12">
  <figure class="pic mask in">{pic("smuga-wioleta", "r-4-5", "(max-width: 1080px) 100vw, 40vw", True)}<figcaption class="small muted"><span>Białystok · Warszawa</span><span>@smuga_design</span></figcaption></figure>
  <div class="txt">
    <p class="lbl muted">Podejście</p>
    <h2 class="d-m rv">Spokojna baza i jeden odważny gest.</h2>
    <p class="lead" style="margin-bottom:24px">Lubię naturalne materiały: drewno, kamień, len. Na nich buduję wnętrza, w których jest miejsce na kolor i sztukę.</p>
    <p class="muted">Każdy projekt dostaje swój kod, jak w katalogu. Dzięki temu łatwo wrócić do decyzji, materiałów i zdjęć, także po latach. Tekst do uzupełnienia o wykształcenie, doświadczenie i publikacje.</p>
    <ul class="means stag" style="margin-top:40px">
      <li><b>Światło</b><span class="muted">Projektuję od okna.</span></li>
      <li><b>Kolor</b><span class="muted">Jeden akcent zamiast dziesięciu.</span></li>
      <li><b>Materiał</b><span class="muted">Takie, które ładnie się starzeją.</span></li>
      <li><b>Porządek</b><span class="muted">Kod i opis każdego projektu.</span></li>
    </ul>
  </div>
</div></section>
{process()}
{cta()}"""
page("o-mnie.html", "O mnie · Wioleta Siemieniuk · Smuga Design", "Arch. wn. Wioleta Siemieniuk, Smuga Design. Ciepły minimalizm z odwagą koloru.", omnie, "o-mnie.html", og="smuga-wioleta")


# KONTAKT (bez kwot)
def opts(xs):
    return "".join(f"<option>{x}</option>" for x in xs)


kontakt = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Kontakt</span></p>
  <div class="g12"><h1 class="d-xl">Opisz swoje wnętrze</h1><p class="lead muted">Im więcej szczegółów, tym lepiej przygotuję się do pierwszej rozmowy.</p></div>
</div></div>
<section class="contact-body"><div class="wrap g12">
  <div class="side">
    <dl class="facts"><div><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Telefon</dt><dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd></div><div><dt>Instagram</dt><dd><a href="{IG}" rel="noopener">@smuga_design</a></dd></div><div><dt>Obszar</dt><dd>Białystok, Warszawa, zdalnie</dd></div></dl>
    {mark()}
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
    <label class="full">Wiadomość<textarea name="wiadomosc" placeholder="Co chcesz zmienić? Co lubisz, czego nie?"></textarea></label>
    <label class="full">Rzut lub zdjęcia (opcjonalnie)<input type="file" name="pliki" multiple accept=".pdf,.jpg,.jpeg,.png"></label>
    <label class="consent full"><input type="checkbox" required> Zgadzam się na kontakt w sprawie zapytania. Dane przetwarza Smuga Design zgodnie z polityką prywatności.</label>
    <button class="btn" type="submit">Wyślij zapytanie</button>
    <p class="form-ok" hidden tabindex="-1">To jest demo: formularz niczego nie wysyła. Na gotowej stronie wiadomość trafi na {EMAIL}.</p>
  </form>
</div></section>"""
page("kontakt.html", "Kontakt · Smuga Design", "Zapytanie o projekt wnętrza: mieszkanie, dom, wnętrze komercyjne. Białystok, Warszawa, zdalnie.", kontakt, "kontakt.html")

print("ok:", sorted(x.name for x in OUT.glob("*.html")))
