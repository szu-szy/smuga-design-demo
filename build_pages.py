"""Szablony stron demo Smuga Design v3. Dane w build_head.py. Uruchom: python3 build.py"""
from build_head import *  # noqa: F401,F403 - dane projektów, zdjęć i kontaktu

V = "4"
STREAK_PATH = "M12 60C14 44 30 38 54 32C76 26 86 20 88 4H108C108 24 92 36 64 42C42 47 32 50 32 60Z"
DRAW_PATH = "M22 58C24 46 36 40 58 35C80 30 96 22 98 6"
SERVICES = [
    ("mieszkania", "Mieszkania", "Od kawalerki po apartament: układ, zabudowy, światło i materiały.", "viz-apartament-wwa"),
    ("domy", "Domy", "Całe wnętrze domu jednorodzinnego, najlepiej już na etapie budowy.", "viz-dom-001"),
    ("komercyjne", "Wnętrza komercyjne", "Kawiarnie, showroomy i lokale, które pracują na markę.", "mnc-bar"),
    ("wizualizacje", "Wizualizacje", "Realistyczne obrazy wnętrza, zanim zapadną decyzje i wydatki.", "viz-showroom"),
    ("konsultacje", "Konsultacje", "Jedno spotkanie i konkretny kierunek zmian do zrobienia samodzielnie.", "mnc-loza"),
]
STEPS = [
    ("Rozmowa", "Poznaję Ciebie, sposób życia i potrzeby. Ustalamy zakres i termin."),
    ("Pomiar", "Mierzę wnętrze, robię zdjęcia, zbieram Twoje inspiracje."),
    ("Koncepcja", "Układ funkcjonalny i wizualizacje, które dopracowujemy razem."),
    ("Projekt wykonawczy", "Rysunki dla ekip, dobór materiałów i zestawienie."),
    ("Realizacja", "Jestem przy wyborach na budowie, aż do sesji zdjęciowej."),
]


def mark(cls="streak"):
    return f'<svg class="{cls}" viewBox="0 0 120 64" aria-hidden="true"><path d="{STREAK_PATH}"/></svg>'


def pic(name, ratio="r-4-5", sizes="(max-width: 860px) 100vw, 50vw", eager=False):
    alt, (w, h) = IMG[name]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<div class="ph {ratio}"><img src="img/{name}-s.webp" srcset="img/{name}-s.webp {min(w, 800)}w, img/{name}.webp {min(w, 1600)}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" {load} decoding="async"></div>')


def place(p):
    return " · ".join(x for x in (p["typ"], p["lok"], p["rok"]) if x)


def header(current):
    oferta_cur = current == "oferta.html"
    mm_items = "".join(f'<a href="oferta.html#{k}"><span class="lbl muted">{i:02d}</span><span class="d-s">{n}</span><span class="ar" aria-hidden="true">&#8594;</span></a>' for i, (k, n, _d, _img) in enumerate(SERVICES, start=1))
    mm_figs = "".join(f'<figure aria-hidden="true">{pic(img, "", "360px")}<figcaption class="small muted">{d}</figcaption></figure>' for _k, _n, d, img in SERVICES)
    sub = "".join(f'<a href="oferta.html#{k}">{n}</a>' for k, n, _d, _i in SERVICES)
    ac = lambda h: ' aria-current="page"' if h == current else ""
    return f"""<header class="hdr">
  <div class="wrap">
    <nav class="nav" aria-label="Główne">
      <a href="realizacje.html"{ac("realizacje.html")}>Realizacje</a>
      <button class="mm-btn{" cur" if oferta_cur else ""}" type="button" aria-expanded="false" aria-controls="mm">Oferta<i aria-hidden="true"></i></button>
    </nav>
    <a class="logo" href="index.html" aria-label="Smuga Design, strona główna">{mark()}SMUGA</a>
    <nav class="nav r" aria-label="Pracownia">
      <a href="o-mnie.html"{ac("o-mnie.html")}>O mnie</a>
      <a class="cta-s" href="kontakt.html"{ac("kontakt.html")}>Kontakt</a>
    </nav>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer"><span>Menu</span><i aria-hidden="true"></i></button>
  </div>
  <div class="mm" id="mm">
    <div class="wrap">
      <div class="mm-intro"><div><p class="lbl muted">Oferta</p><p class="d-s" style="margin-top:12px">Od jednej konsultacji po kompletny projekt wnętrza.</p></div><a class="lnk" href="oferta.html">Cała oferta</a></div>
      <nav class="mm-list" aria-label="Usługi">{mm_items}</nav>
      <div class="mm-pre">{mm_figs}</div>
    </div>
  </div>
</header>
<div class="drawer" id="drawer"><a href="realizacje.html">Realizacje</a><a href="oferta.html">Oferta</a><div class="sub">{sub}</div><a href="o-mnie.html">O mnie</a><a href="kontakt.html">Kontakt</a><div class="small"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_HREF}">{PHONE}</a></div></div>"""


def footer():
    links = [("realizacje.html", "Realizacje"), ("oferta.html", "Oferta"), ("o-mnie.html", "O mnie"), ("kontakt.html", "Kontakt")]
    return f"""<footer class="ftr">
  <div class="wrap g12">
    <div class="mk">{mark()}</div>
    <div class="col"><b>Smuga Design</b><span>Projektowanie wnętrz</span><span>arch. wn. Wioleta Siemieniuk</span></div>
    <div class="col"><b>Kontakt</b><a href="tel:{PHONE_HREF}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="col"><b>Social media</b><a href="{IG}" rel="noopener">@smuga_design</a><a href="{BEHANCE}" rel="noopener">Behance</a></div>
    <p class="mark" aria-hidden="true">SMUGA DESIGN</p>
    <div class="bottom"><span>© 2026 Smuga Design · Białystok</span><span>{" · ".join(f'<a href="{h}">{t}</a>' for h, t in links)}</span><span>Demo projektu strony · Impact Agencja</span></div>
  </div>
</footer>"""


LOADER = f"""<div class="loader" aria-hidden="true"><svg viewBox="0 0 120 64"><path d="{DRAW_PATH}"/></svg><div class="word">{"".join(f'<span style="animation-delay:{300 + i * 40}ms">{"&nbsp;" if c == " " else c}</span>' for i, c in enumerate("SMUGA DESIGN"))}</div><div class="bar"><i></i></div></div>"""


def page(fname, title, desc, body, current="", og="mnc-kotara"):
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
<script>try{{if(!sessionStorage.getItem('smuga-ld')&&!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('ld')}}catch(e){{}}</script>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 64'%3E%3Cpath fill='%23FFC7C8' d='{STREAK_PATH}'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..112,400..600&family=Hanken+Grotesk:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v={V}">
</head>
<body>
{LOADER}
<a class="skip" href="#main">Przejdź do treści</a>
{header(current)}
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


def tile(p, ratio="r-4-5", sizes="(max-width: 860px) 50vw, 25vw"):
    return (f'<a class="tile mask" href="projekt-{p["slug"]}.html">{pic(p["card"], ratio, sizes)}'
            f'<div class="row"><h3>{escape(p["title"])}</h3><span class="ar" aria-hidden="true">&#8594;</span></div>'
            f'<p class="lbl muted">{escape(place(p))}</p></a>')


# STRONA GŁÓWNA
SLIDES = [("mnc-kotara", "Kawiarnia MNC Concept · wejście"), ("mnc-sala", "Kawiarnia MNC Concept · sala"), ("mnc-loza", "Kawiarnia MNC Concept · strefa siedzisk"), ("mnc-lada", "Kawiarnia MNC Concept · lada")]
slides = "".join(f'<div class="sl{" on" if i == 0 else ""}" data-cap="{escape(c)}"><img src="img/{n}.webp" width="{IMG[n][1][0]}" height="{IMG[n][1][1]}" alt="{escape(IMG[n][0])}"{" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\""}></div>' for i, (n, c) in enumerate(SLIDES))
bars = "".join(f'<button type="button" aria-label="Pokaż zdjęcie {i + 1}"><i></i></button>' for i in range(len(SLIDES)))
words = ["Projektowanie wnętrz", "Mieszkania", "Domy", "Wnętrza komercyjne", "Białystok", "Warszawa"]
grp = "".join(f"<span>{w}</span>{mark()}" for w in words)
mnc = BY["mnc-concept"]
mos_imgs = [("mnc-bar", "r-4-5"), ("wwa-zabudowa", "r-3-4"), ("dom-wyspa", "r-5-4"), ("show-fotel", "r-2-3"), ("show-regal", "r-2-3"), ("mnc-taras", "r-4-5"), ("wwa-grafiki", "r-2-3"), ("mnc-wejscie", "r-5-4")]
slug_of = lambda n: "mnc-concept" if n.startswith("mnc") else {"wwa": "mieszkanie-warszawa", "dom": "dom-001", "sho": "showroom-spod-igly-i-nitki"}[n[:3]]
mos = "".join(f'<a href="projekt-{slug_of(n)}.html">{pic(n, r, "(max-width: 860px) 50vw, 25vw")}<span>{escape(IMG[n][0])}</span></a>' for n, r in mos_imgs)

home = f"""<section class="hero" aria-labelledby="hero-h" style="--n:{len(SLIDES)}">
  <div class="hero-txt">
    {mark()}
    <div><p class="lbl" style="margin-bottom:24px">Pracownia projektowania wnętrz</p><h1 class="d-xl" id="hero-h">Wnętrza, które zostawiają ślad</h1></div>
    <p class="lead">Ciepły minimalizm z odwagą koloru. Domy, mieszkania i lokale w Białymstoku, Warszawie i zdalnie.</p>
    <div class="hero-cap">
      <div class="now lbl"><span class="name">{SLIDES[0][1]}</span><span class="num">01 / {len(SLIDES):02d}</span></div>
      <div class="prog">{bars}</div>
      <div><a class="btn light" href="realizacje.html">Zobacz realizacje</a></div>
    </div>
  </div>
  <div class="hero-img">{slides}<div class="sweep" aria-hidden="true"></div></div>
</section>

<div class="marq" aria-hidden="true"><div class="track"><div class="grp">{grp}</div><div class="grp">{grp}</div></div></div>

<section class="sec"><div class="wrap">
  <div class="sec-h"><div><span class="lbl muted">Realizacje</span><h2 class="d-l rv">Wybrane projekty</h2></div><a class="lnk" href="realizacje.html">Wszystkie realizacje</a></div>
  <div class="strip stag">{"".join(tile(p) for p in PROJECTS)}</div>
</div></section>

<section class="feat"><div class="wrap g12">
  <div class="txt stag">
    <p class="lbl">Wyróżniona realizacja</p>
    <h2 class="d-l">{mnc["title"]}</h2>
    <p class="lead">{mnc["lead"]}</p>
    <dl class="facts"><div><dt class="lbl">Typ</dt><dd>{mnc["typ"]}</dd></div><div><dt class="lbl">Miasto</dt><dd>{mnc["lok"]}</dd></div><div><dt class="lbl">Rok</dt><dd>{mnc["rok"]}</dd></div></dl>
    <a class="btn" href="projekt-mnc-concept.html">Zobacz realizację</a>
  </div>
  <div class="col">
    <a class="a mask" href="projekt-mnc-concept.html" tabindex="-1" aria-hidden="true">{pic("mnc-lada", "r-4-5", "(max-width: 1080px) 60vw, 33vw")}</a>
    <a class="b mask" href="projekt-mnc-concept.html" tabindex="-1" aria-hidden="true">{pic("mnc-bar", "r-3-4", "(max-width: 1080px) 40vw, 25vw")}</a>
    <a class="c mask" href="projekt-mnc-concept.html" tabindex="-1" aria-hidden="true">{pic("mnc-wejscie", "r-5-4", "(max-width: 1080px) 50vw, 25vw")}</a>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="mos-h"><h2 class="d-l rv">Detale, od których zaczyna się wnętrze</h2><p class="lead muted">Rysunek drewna, łuk przejścia, kolor kotary. Wybieram je tak, żeby wnętrze było rozpoznawalne po jednym kadrze.</p></div>
  <div class="mos stag">{mos}</div>
</div></section>

<section class="me"><div class="wrap g12">
  <figure class="pic mask">{pic("smuga-wioleta", "r-5-4", "(max-width: 860px) 100vw, 40vw")}</figure>
  <div class="txt stag">
    <p class="lbl muted">O mnie</p>
    <h2 class="d-m">Smuga to ślad. Światła na podłodze, pędzla na ścianie, człowieka w przestrzeni.</h2>
    <p class="lead">Spokojną bazę z drewna, kamienia i lnu łączę z jednym odważnym gestem: kolorem albo sztuką. Prowadzę projekt od pierwszej rozmowy do sesji zdjęciowej gotowego wnętrza.</p>
    <div class="sig"><span>arch. wn. Wioleta Siemieniuk</span><a class="lnk" href="o-mnie.html">Poznaj pracownię</a></div>
  </div>
</div></section>

{cta()}"""
page("index.html", "Smuga Design · projektowanie wnętrz Białystok", "Pracownia projektowania wnętrz arch. wn. Wiolety Siemieniuk. Domy, mieszkania i wnętrza komercyjne. Białystok, Warszawa.", home)


# REALIZACJE
works = "".join(tile(p, "r-4-5" if i % 4 in (1, 2) else "r-5-4", "(max-width: 860px) 100vw, 58vw") for i, p in enumerate(PROJECTS))
real = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Realizacje</span></p>
  <div class="g12"><h1 class="d-xl">Realizacje</h1><p class="lead muted">Domy, mieszkania i wnętrza komercyjne. Każdy projekt z opisem i pełną galerią.</p></div>
</div></div>
<section><div class="wrap works">{works}</div></section>
{cta()}"""
page("realizacje.html", "Realizacje · Smuga Design", "Realizacje pracowni Smuga Design: domy, mieszkania, wnętrza komercyjne.", real, "realizacje.html")


# STRONY REALIZACJI
order = [p["slug"] for p in PROJECTS]
LB = """<div class="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęć">
  <div class="lb-top"><span class="lb-count lbl"></span><button type="button" class="close">Zamknij</button></div>
  <div class="lb-stage"><img src="" alt=""></div>
  <div class="lb-bot"><span class="lb-cap small"></span></div>
  <button type="button" class="prev" aria-label="Poprzednie zdjęcie">&#8592;</button><button type="button" class="nextb" aria-label="Następne zdjęcie">&#8594;</button>
</div>"""
for p in PROJECTS:
    others = [BY[s] for s in order if s != p["slug"]][:3]
    blocks = "".join(f"<div><h2>{a}</h2><p>{b}</p></div>" for a, b in p["blocks"])
    gal_imgs = p["gallery"] or p["details"]
    shots = [p["cover"]] + gal_imgs
    data = "".join(f'<span hidden data-shot="img/{n}.webp" data-alt="{escape(IMG[n][0])}"></span>' for n in shots)
    figs = []
    if p["gallery"]:
        layout = ["full", "", "off", "full", "", "off"]
        for i, name in enumerate(gal_imgs, start=1):
            cls = layout[(i - 1) % len(layout)]
            figs.append(f'<figure class="{cls} mask"><button type="button" data-open="{i}" aria-label="Powiększ zdjęcie {i + 1} z {len(shots)}">{pic(name, "r-3-2" if cls == "full" else "r-4-5", "(max-width: 1080px) 100vw, 60vw")}</button><figcaption>{escape(IMG[name][0].split(",")[0])}</figcaption></figure>')
            if i == 3:
                figs.append(f'<blockquote class="d-m rv">"{p["blocks"][2][1]}"</blockquote>')
        gal = f'<div class="p-gal">{"".join(figs)}</div>'
    else:
        for i, name in enumerate(gal_imgs, start=1):
            figs.append(f'<figure class="mask"><button type="button" data-open="{i}" aria-label="Powiększ zdjęcie {i + 1} z {len(shots)}">{pic(name, "r-3-4", "(max-width: 1080px) 100vw, 20vw")}</button><figcaption>{escape(IMG[name][0].split(",")[0])}</figcaption></figure>')
        gal = f'<div class="p-gal three">{"".join(figs)}<blockquote class="d-m rv">"{p["blocks"][2][1]}"</blockquote></div>'
    facts = "".join(f'<div><span class="lbl muted">{k}</span><span>{escape(v)}</span></div>' for k, v in (("Typ", p["typ"]), ("Lokalizacja", p["lok"]), ("Rok", p["rok"]), ("Zakres", "Projekt wnętrza")) if v)
    body = f"""<div class="p-top"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><a href="realizacje.html">Realizacje</a><span>/</span><span>{p["short"]}</span></p>
  <div class="g12"><h1 class="d-xl">{escape(p["title"])}</h1><div class="facts-top">{facts}</div></div>
</div></div>
<div class="p-hero"><div class="wrap"><button type="button" data-open="0" aria-label="Powiększ zdjęcie główne">{pic(p["cover"], "", "100vw", True)}</button></div></div>
<section class="p-body"><div class="wrap g12">
  <aside class="p-side"><p class="lead">{p["lead"]}</p><div class="blocks">{blocks}</div><a class="lnk" href="kontakt.html">Chcę podobne wnętrze</a></aside>
  {gal}
</div></section>
{data}
<section class="more-w"><div class="wrap">
  <div class="sec-h"><div><span class="lbl muted">Zobacz też</span><h2 class="d-m">Inne realizacje</h2></div><a class="lnk" href="realizacje.html">Wszystkie realizacje</a></div>
  <div class="strip stag" style="grid-template-columns:repeat(3,minmax(0,1fr))">{"".join(tile(o, "r-5-4", "(max-width: 860px) 50vw, 33vw") for o in others)}</div>
</div></section>
{LB}
{cta()}"""
    page(f"projekt-{p['slug']}.html", f"{p['title']} · Realizacje · Smuga Design", p["lead"], body, "realizacje.html", og=p["cover"])


# OFERTA (bez cen)
SVC_DETAIL = {
    "mieszkania": ("Projekt, który porządkuje codzienność: gdzie stoi łóżko, jak pada światło, ile mieści szafa.", ["układ funkcjonalny i warianty", "wizualizacje pomieszczeń", "rysunki zabudów i elektryki", "dobór materiałów i zestawienie"]),
    "domy": ("Wnętrze domu projektowane razem z jego bryłą i ogrodem, najlepiej już na etapie budowy.", ["koncepcja dla całego domu", "wizualizacje kluczowych stref", "projekt wykonawczy dla ekip", "wsparcie podczas realizacji"]),
    "komercyjne": ("Przestrzeń, która buduje markę i dobrze wygląda na zdjęciach klientów. Przykład: kawiarnia MNC Concept.", ["identyfikacja marki we wnętrzu", "przepływ gości i obsługi", "dobór trwałych materiałów", "koordynacja z wykonawcami"]),
    "wizualizacje": ("Realistyczne obrazy wnętrza, które pomagają podjąć decyzje, zanim zaczną się wydatki.", ["wizualizacje projektów własnych", "warianty kolorów i materiałów", "obrazy do sprzedaży nieruchomości"]),
    "konsultacje": ("Jedno spotkanie w Twoim wnętrzu i konkretny kierunek zmian do zrobienia samodzielnie.", ["kierunek kolorów i materiałów", "lista zmian krok po kroku", "spotkanie na miejscu albo online"]),
}
svc = "".join(f'<section class="svc" id="{k}"><span class="n">{i:02d}</span><div class="t rv"><h2 class="d-l">{n}</h2><p class="lead">{SVC_DETAIL[k][0]}</p></div><ul class="stag">{"".join(f"<li>{x}</li>" for x in SVC_DETAIL[k][1])}</ul><div class="mask">{pic(img, "r-4-5", "(max-width: 860px) 100vw, 25vw")}</div></section>' for i, (k, n, _d, img) in enumerate(SERVICES, start=1))
FAQ = [
    ("Od czego zaczynamy?", "Od rozmowy. Opowiadasz o wnętrzu i o tym, jak chcesz w nim żyć, a ja proponuję zakres i termin."),
    ("Jak wyceniasz projekt?", "Indywidualnie, po rozmowie i obejrzeniu wnętrza. Wycena zależy od metrażu i zakresu, a dostajesz ją na piśmie przed startem."),
    ("Ile trwa projekt?", "Koncepcja dla mieszkania to zwykle kilka tygodni, projekt kompleksowy kilka miesięcy. Termin ustalamy na starcie."),
    ("Czy pracujesz zdalnie?", "Tak. Pomiar i spotkania mogą odbywać się online, a materiały wysyłam w formie cyfrowej."),
    ("Co dostaję na koniec?", "Wizualizacje, rysunki wykonawcze dla ekip i listę materiałów, zależnie od zakresu. Przy realizacji jestem z Tobą do końca."),
]
steps = "".join(f"<li><b>{a}</b><p class=\"muted\">{b}</p></li>" for a, b in STEPS)
oferta = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Oferta</span></p>
  <div class="g12"><h1 class="d-xl">Oferta</h1><p class="lead muted">Od jednej konsultacji po kompletny projekt z wizualizacjami i wsparciem przy realizacji. Każdą współpracę wyceniam indywidualnie.</p></div>
</div></div>
<div class="wrap">{svc}</div>
<section class="proc" style="margin-top:96px"><div class="wrap">
  <div class="head g12"><p class="lbl">Jak pracuję</p><h2 class="d-m rv">Pięć kroków od pierwszej rozmowy do gotowego wnętrza</h2></div>
  <ol class="stag">{steps}</ol>
</div></section>
<section class="faq-w"><div class="wrap g12">
  <div class="head"><p class="lbl muted">Pytania</p><h2 class="d-m rv" style="margin-top:16px">Najczęściej słyszę</h2></div>
  <div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)}</div>
</div></section>
{cta()}"""
page("oferta.html", "Oferta · projektowanie wnętrz · Smuga Design", "Mieszkania, domy, wnętrza komercyjne, wizualizacje i konsultacje. Proces współpracy i najczęstsze pytania.", oferta, "oferta.html")


# O MNIE
omnie = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>O mnie</span></p>
  <div class="g12"><h1 class="d-xl">Wioleta Siemieniuk</h1><p class="lead muted">Architektka wnętrz, założycielka Smuga Design.</p></div>
</div></div>
<section class="me"><div class="wrap g12">
  <figure class="pic mask">{pic("smuga-wioleta", "r-5-4", "(max-width: 860px) 100vw, 40vw", True)}</figure>
  <div class="txt stag">
    <p class="lbl muted">Podejście</p>
    <h2 class="d-m">Spokojna baza i jeden odważny gest.</h2>
    <p class="lead">Lubię naturalne materiały: drewno, kamień, len. Na nich buduję wnętrza, w których jest miejsce na kolor i sztukę.</p>
    <p class="muted">Projektuję od okna: gdzie pada światło, tam zaczyna się wnętrze. Tekst do uzupełnienia o wykształcenie, doświadczenie i publikacje.</p>
    <div class="sig"><a href="{IG}" rel="noopener">Instagram @smuga_design</a><a href="{BEHANCE}" rel="noopener">Behance</a></div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="mos-h"><h2 class="d-l rv">Z pracowni</h2><p class="lead muted">Detale z projektów, nad którymi pracowałam.</p></div>
  <div class="mos stag">{mos}</div>
</div></section>
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
    <label>Zakres<select name="zakres"><option value="">Wybierz</option>{opts([n for _k, n, _d, _i in SERVICES] + ["Jeszcze nie wiem"])}</select></label>
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
