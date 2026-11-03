"""Szablony stron demo Smuga Design v3. Dane w build_head.py. Uruchom: python3 build.py"""
from build_head import *  # noqa: F401,F403 - dane projektów, zdjęć i kontaktu

V = "10"
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


ICO = {
    "tel": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
    "mail": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
    "ig": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm5-9a1 1 0 1 0 0 2 1 1 0 0 0 0-2zM16 2H8a6 6 0 0 0-6 6v8a6 6 0 0 0 6 6h8a6 6 0 0 0 6-6V8a6 6 0 0 0-6-6zm4 14a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4z"/></svg>',
    "pin": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>',
    "up": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M11 16V7.8l-3.6 3.6L6 10l6-6 6 6-1.4 1.4L13 7.8V16zm-7 4v-2h16v2z"/></svg>',
}
WAVE = '<svg class="wave" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 44C360 44 480 4 720 24S1080 44 1440 4"/></svg>'


def wave_sec():
    return f'<div class="wave-sec rv"><div class="wrap">{WAVE}</div></div>'


def mark(cls="streak"):
    return f'<svg class="{cls}" viewBox="0 0 120 64" aria-hidden="true"><path d="{STREAK_PATH}"/></svg>'


def pic(name, ratio="r-4-5", sizes="(max-width: 860px) 100vw, 50vw", eager=False):
    alt, (w, h) = IMG[name]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<div class="ph {ratio}"><img src="img/{name}-s.webp" srcset="img/{name}-s.webp {min(w, 800)}w, img/{name}.webp {min(w, 1600)}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" {load} decoding="async"></div>')


def place(p):
    return "".join(f"<span>{escape(x)}</span>" for x in (p["typ"], p["lok"], p["rok"]) if x)


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
      <a href="kontakt.html"{ac("kontakt.html")}>Kontakt</a>
      <a class="tel" href="tel:{PHONE_HREF}" aria-label="Zadzwoń {PHONE}">{ICO["tel"]}<span>604 762 946</span></a>
      <a class="cta-s" href="kontakt.html" data-modal>Umów rozmowę</a>
    </nav>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer"><span>Menu</span><i aria-hidden="true"></i><b class="x" aria-hidden="true"></b></button>
  </div>
  <div class="mm" id="mm">
    <div class="wrap">
      <div class="mm-intro"><div><p class="lbl muted">Oferta</p><p class="d-s" style="margin-top:12px">Od jednej konsultacji po kompletny projekt wnętrza.</p></div><a class="lnk" href="oferta.html">Cała oferta</a></div>
      <nav class="mm-list" aria-label="Usługi">{mm_items}</nav>
      <div class="mm-pre">{mm_figs}</div>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Menu"><div class="d-top"><a class="logo" href="index.html">{mark()}SMUGA</a><button class="d-close" type="button" aria-label="Zamknij menu"><span></span></button></div><a href="realizacje.html">Realizacje</a><a href="oferta.html">Oferta</a><div class="sub">{sub}</div><a href="o-mnie.html">O mnie</a><a href="kontakt.html">Kontakt</a><div class="d-cta"><a class="btn" href="kontakt.html" data-modal>Umów rozmowę</a></div>{WAVE}<div class="small"><a href="tel:{PHONE_HREF}">{ICO["tel"]}{PHONE}</a><a href="mailto:{EMAIL}">{ICO["mail"]}{EMAIL}</a></div></div>"""


def footer():
    return f"""<footer class="ftr">
  <div class="wrap">
    <div class="top">
      <div class="intro"><p class="d-s">Projektuję wnętrza, które zostawiają ślad. Białystok, Warszawa i zdalnie.</p><a class="btn light" href="kontakt.html" data-modal>Umów rozmowę</a></div>
      <div class="col"><p class="lbl">Strona</p><a href="realizacje.html">Realizacje</a><a href="oferta.html">Oferta</a><a href="o-mnie.html">O mnie</a><a href="kontakt.html">Kontakt</a></div>
      <div class="col"><p class="lbl">Oferta</p>{"".join(f'<a href="oferta.html#{k}">{n}</a>' for k, n, _d, _i in SERVICES)}</div>
      <div class="col w3"><p class="lbl">Kontakt</p><a href="tel:{PHONE_HREF}">{ICO["tel"]}{PHONE}</a><a href="mailto:{EMAIL}">{ICO["mail"]}{EMAIL}</a><a href="{IG}" rel="noopener">{ICO["ig"]}@smuga_design</a><span style="display:inline-flex;gap:8px;align-items:center">{ICO["pin"]}Białystok</span></div>
    </div>
    <p class="mark" aria-hidden="true">SMUGA DESIGN</p>
    <div class="bottom"><span>© 2026 Smuga Design</span><span>arch. wn. Wioleta Siemieniuk</span><a href="{BEHANCE}" rel="noopener">Behance</a><span>Demo projektu strony: Impact Agencja</span></div>
  </div>
</footer>
<a class="fab" href="tel:{PHONE_HREF}" aria-label="Zadzwoń {PHONE}">{ICO["tel"]}</a>"""


LOADER = f"""<div class="loader" aria-hidden="true"><svg class="mk" viewBox="0 0 120 64"><path d="{DRAW_PATH}"/></svg><div class="word">{"".join(f'<span style="animation-delay:{500 + i * 50}ms">{"&nbsp;" if c == " " else c}</span>' for i, c in enumerate("SMUGA DESIGN"))}</div><div class="meta"><span>Projektowanie wnętrz</span><b>000</b></div></div>"""


def modal():
    pills = "".join(f'<label><input type="radio" name="typ" value="{t}"{" required" if i == 0 else ""}><span>{t}</span></label>' for i, t in enumerate(["Mieszkanie", "Dom", "Lokal"]))
    return f"""<dialog class="dlg" aria-labelledby="dlg-h">
  <button class="x" type="button" aria-label="Zamknij">&#10005;</button>
  <div class="in">
    <div class="l"><div><p class="lbl w">Umów rozmowę</p><h2 class="d-m" id="dlg-h" style="margin-top:16px">Porozmawiajmy o Twoim wnętrzu</h2></div><div style="display:grid;gap:8px;position:relative;z-index:1"><a href="tel:{PHONE_HREF}">{ICO["tel"]}{PHONE}</a><a href="mailto:{EMAIL}">{ICO["mail"]}{EMAIL}</a></div>{mark()}</div>
    <div class="r">
      <p class="lead">Zostaw kontakt, oddzwonię i umówimy pierwszą rozmowę.</p>
      <form class="form" novalidate>
        <label><span>Imię <span class="req" aria-hidden="true">*</span></span><input name="imie" autocomplete="given-name" required></label>
        <label><span>Telefon <span class="req" aria-hidden="true">*</span></span><input type="tel" name="tel" autocomplete="tel" required></label>
        <fieldset class="full"><legend><span>Rodzaj wnętrza <span class="req" aria-hidden="true">*</span></span></legend><div class="pills">{pills}</div></fieldset>
        <label class="full">Krótko o wnętrzu<textarea name="wiadomosc" placeholder="np. mieszkanie 60 m², chcę zmienić kuchnię i salon"></textarea></label>
        <label class="consent full"><input type="checkbox" required> Zgadzam się na kontakt w sprawie zapytania.</label>
        <div class="send full"><button class="btn" type="submit">Wyślij</button></div>
        <p class="form-ok" hidden tabindex="-1">{mark()}To jest demo: formularz niczego nie wysyła.</p>
      </form>
    </div>
  </div>
</dialog>"""


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
{modal()}
<script src="assets/app.js?v={V}" defer></script>
</body>
</html>
"""
    (OUT / fname).write_text(html, encoding="utf-8")


def cta():
    return f"""<section class="cta wtop pink" aria-labelledby="cta-h">
  <div class="wrap">
    <div class="top"><h2 class="d-xxl rv" id="cta-h">Porozmawiajmy</h2>{mark()}</div>
    <div class="row stag">
      <p class="lead">O mieszkaniu, domu albo lokalu. Pierwsza rozmowa niczego nie zobowiązuje, a po niej wiesz, jak mogłoby wyglądać Twoje wnętrze.</p>
      <div class="links"><a href="tel:{PHONE_HREF}">{ICO["tel"]}{PHONE}</a><a href="mailto:{EMAIL}">{ICO["mail"]}{EMAIL}</a></div>
      <a class="btn" href="kontakt.html" data-modal>Umów rozmowę</a>
    </div>
  </div>
</section>"""


def tile(p, ratio="r-4-5", sizes="(max-width: 860px) 50vw, 25vw", h="h3"):
    return (f'<a class="tile mask" href="projekt-{p["slug"]}.html">{pic(p["card"], ratio, sizes)}'
            f'<div class="row"><{h}>{escape(p["title"])}</{h}><span class="ar" aria-hidden="true">&#8594;</span></div>'
            f'<p class="meta-s muted">{place(p)}</p></a>')


def work_index():
    pre = "".join(f'<figure class="{"on" if i == 0 else ""}" aria-hidden="true">{pic(p["card"], "", "(max-width: 1080px) 40vw, 36vw")}</figure>' for i, p in enumerate(PROJECTS))
    rows = "".join(f'<li><a class="wi-row{" on" if i == 0 else ""}" href="projekt-{p["slug"]}.html"><span class="n">{i + 1:02d}</span><span class="thumb">{pic(p["card"], "r-1-1", "112px")}</span><h3>{escape(p["title"])}</h3><p class="meta-s">{place(p)}</p><span class="ar" aria-hidden="true">&#8594;</span></a></li>' for i, p in enumerate(PROJECTS))
    return f'<div class="wi"><div class="wi-pre">{pre}</div><ol class="wi-list stag">{rows}</ol></div>'


def carousel(label, h2, lead, imgs):
    figs = "".join(f'<figure><a href="projekt-{slug_of(n)}.html" tabindex="-1">{pic(n, "r-4-5", "(max-width: 860px) 72vw, 25vw")}</a><figcaption>{escape(IMG[n][0].split(",")[0])}</figcaption></figure>' for n in imgs)
    return f"""<div class="car">
  <div class="car-head"><div><p class="lbl w muted">{label}</p><h2 class="d-l rv">{h2}</h2><p class="lead muted">{lead}</p></div><div class="car-nav"><button type="button" class="prev" aria-label="Poprzednie zdjęcia">&#8592;</button><button type="button" class="next" aria-label="Następne zdjęcia">&#8594;</button></div></div>
  <div class="car-track" tabindex="0" role="region" aria-label="{label}: zdjęcia">{figs}</div>
  <div class="car-bar" aria-hidden="true"><i></i></div>
</div>"""


def slug_of(n):
    return "mnc-concept" if n.startswith("mnc") else {"wwa": "mieszkanie-warszawa", "dom": "dom-001", "sho": "showroom-spod-igly-i-nitki"}[n[:3]]


# STRONA GŁÓWNA
SLIDES = [("mnc-kotara", "MNC Concept, wejście"), ("mnc-sala", "MNC Concept, sala"), ("mnc-loza", "MNC Concept, strefa siedzisk"), ("mnc-lada", "MNC Concept, lada")]
slides = "".join(f'<div class="sl{" on" if i == 0 else ""}" data-cap="{escape(c)}"><img src="img/{n}.webp" width="{IMG[n][1][0]}" height="{IMG[n][1][1]}" alt="{escape(IMG[n][0])}"{" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\""}></div>' for i, (n, c) in enumerate(SLIDES))
bars = "".join(f'<button type="button" aria-label="Pokaż zdjęcie {i + 1}"><i></i></button>' for i in range(len(SLIDES)))
words = ["Projektowanie wnętrz", "Mieszkania", "Domy", "Wnętrza komercyjne", "Białystok", "Warszawa"]
grp = "".join(f"<span>{w}</span>{mark()}" for w in words)
mnc = BY["mnc-concept"]
det_imgs = ["mnc-bar", "dom-wyspa", "wwa-zabudowa", "show-luk", "mnc-lada", "show-regal", "dom-zabudowa", "wwa-mural"]
det = "".join(f'<a href="projekt-{slug_of(n)}.html">{pic(n, "r-1-1", "(max-width: 1080px) 50vw, 25vw")}<span>{escape(IMG[n][0].split(",")[0])}</span></a>' for n in det_imgs)

home = f"""<section class="hero" aria-labelledby="hero-h" style="--n:{len(SLIDES)}">
  <div class="hero-txt">
    {mark()}
    <div><p class="lbl w" style="margin-bottom:24px">Pracownia projektowania wnętrz</p><h1 class="d-xl" id="hero-h">Wnętrza, które zostawiają ślad</h1></div>
    <p class="lead">Ciepły minimalizm z odwagą koloru. Domy, mieszkania i lokale w Białymstoku, Warszawie i zdalnie.</p>
    <div class="hero-cap">
      <div class="now lbl"><span class="name">{SLIDES[0][1]}</span><span class="num">01 / {len(SLIDES):02d}</span></div>
      <div class="prog">{bars}</div>
      <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center"><a class="btn light" href="realizacje.html">Zobacz realizacje</a><a class="lnk" href="kontakt.html" data-modal style="color:var(--white)">Umów rozmowę</a></div>
    </div>
  </div>
  <div class="hero-img">{slides}<div class="sweep" aria-hidden="true"></div></div>
</section>

<div class="marq" aria-hidden="true"><div class="track"><div class="grp">{grp}</div><div class="grp">{grp}</div></div></div>

<section class="sec"><div class="wrap">
  <div class="sec-h"><div><span class="lbl w muted">Realizacje</span><h2 class="d-l rv">Wybrane projekty</h2></div><a class="lnk" href="realizacje.html">Wszystkie realizacje</a></div>
  <div class="ash stag">{"".join(f'<a class="mask" href="projekt-{p["slug"]}.html">{pic(p["card"], "r-3-4", "(max-width: 1080px) 50vw, 25vw")}<span class="cap"><b>{escape(p["title"])}</b><span>{escape(p["lok"] or p["typ"])}</span></span></a>' for p in PROJECTS)}</div>
</div></section>

<section class="feat wtop pink"><div class="wrap g12">
  <div class="txt stag">
    <p class="lbl w">Wyróżniona realizacja</p>
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
  {carousel("Detale", "Od detalu zaczyna się wnętrze", "Rysunek drewna, łuk przejścia, kolor kotary. Wybieram je tak, żeby wnętrze było rozpoznawalne po jednym kadrze.", det_imgs)}
</div></section>

<section class="me wtop soft"><div class="wrap g12">
  <figure class="pic mask">{pic("smuga-wioleta", "r-5-4", "(max-width: 860px) 100vw, 40vw")}</figure>
  <div class="txt stag">
    <p class="lbl w muted">O mnie</p>
    <h2 class="d-m">Smuga to ślad. Światła na podłodze, pędzla na ścianie, człowieka w przestrzeni.</h2>
    <p class="lead">Spokojną bazę z drewna, kamienia i lnu łączę z jednym odważnym gestem: kolorem albo sztuką. Prowadzę projekt od pierwszej rozmowy do sesji zdjęciowej gotowego wnętrza.</p>
    <div class="sig"><span>arch. wn. Wioleta Siemieniuk</span><a class="lnk" href="o-mnie.html">Poznaj pracownię</a></div>
  </div>
</div></section>

{cta()}"""
page("index.html", "Smuga Design | projektowanie wnętrz Białystok", "Pracownia projektowania wnętrz arch. wn. Wiolety Siemieniuk. Domy, mieszkania i wnętrza komercyjne. Białystok, Warszawa.", home)


# REALIZACJE
ROW_IMGS = {"mnc-concept": ["mnc-sala", "mnc-lada", "mnc-bar"], "mieszkanie-warszawa": ["viz-apartament-wwa", "wwa-zabudowa", "wwa-grafiki"], "dom-001": ["viz-dom-001", "dom-zabudowa", "dom-okno"], "showroom-spod-igly-i-nitki": ["viz-showroom", "show-regal", "show-fotel"]}


def kw_row(p):
    pics = ""
    for n in ROW_IMGS[p["slug"]]:
        w, h = IMG[n][1]
        r = round(w / h, 3)
        ph = pic(n, "", "(max-width: 860px) 70vw, 30vw").replace('class="ph "', f'class="ph" style="aspect-ratio:{w}/{h}"')
        pics += f'<a href="projekt-{p["slug"]}.html" tabindex="-1" aria-hidden="true" style="flex:{r} 1 0">{ph}</a>'
    return f'''<article class="kw-row"><div class="kw-name"><a href="projekt-{p["slug"]}.html">{escape(p["title"])}</a>{"".join(f"<span>{escape(x)}</span>" for x in (p["typ"], p["lok"], p["rok"]) if x)}</div><div class="kw-pics mask">{pics}</div></article>'''


works = "".join(kw_row(p) for p in PROJECTS)

real = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Realizacje</span></p>
  <div class="g12"><h1 class="d-xl">Realizacje</h1><p class="lead muted">Domy, mieszkania i wnętrza komercyjne. Każdy projekt z opisem i pełną galerią.</p></div>
</div></div>
<section><div class="wrap kw">{works}</div></section>
{cta()}"""
page("realizacje.html", "Realizacje | Smuga Design", "Realizacje pracowni Smuga Design: domy, mieszkania, wnętrza komercyjne.", real, "realizacje.html")


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
    nxt = BY[order[(order.index(p["slug"]) + 1) % len(order)]]
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
  <aside class="p-side"><p class="lead">{p["lead"]}</p><div class="blocks">{blocks}</div><a class="btn" href="kontakt.html" data-modal>Chcę podobne wnętrze</a></aside>
  {gal}
</div></section>
{data}
<a class="nx" href="projekt-{nxt["slug"]}.html">{pic(nxt["card"], "", "100vw")}<div class="txt"><p class="lbl w">Następna realizacja</p><p class="d-xl">{escape(nxt["title"])}</p><p class="meta-s">{place(nxt)}</p></div></a>
<div class="wrap nx-more"><div class="others">{"".join(f'<a class="lnk" href="projekt-{o["slug"]}.html">{escape(o["title"])}</a>' for o in others if o["slug"] != nxt["slug"])}</div><a class="btn" href="realizacje.html">Wszystkie realizacje</a></div>
{LB}
{cta()}"""
    page(f"projekt-{p['slug']}.html", f"{p['title']} | Realizacje | Smuga Design", p["lead"], body, "realizacje.html", og=p["cover"])


# OFERTA (bez cen)
SVC_DETAIL = {
    "mieszkania": ("Projekt, który porządkuje codzienność: gdzie stoi łóżko, jak pada światło, ile mieści szafa.", ["układ funkcjonalny i warianty", "wizualizacje pomieszczeń", "rysunki zabudów i elektryki", "dobór materiałów i zestawienie"]),
    "domy": ("Wnętrze domu projektowane razem z jego bryłą i ogrodem, najlepiej już na etapie budowy.", ["koncepcja dla całego domu", "wizualizacje kluczowych stref", "projekt wykonawczy dla ekip", "wsparcie podczas realizacji"]),
    "komercyjne": ("Przestrzeń, która buduje markę i dobrze wygląda na zdjęciach klientów. Przykład: kawiarnia MNC Concept.", ["identyfikacja marki we wnętrzu", "przepływ gości i obsługi", "dobór trwałych materiałów", "koordynacja z wykonawcami"]),
    "wizualizacje": ("Realistyczne obrazy wnętrza, które pomagają podjąć decyzje, zanim zaczną się wydatki.", ["wizualizacje projektów własnych", "warianty kolorów i materiałów", "obrazy do sprzedaży nieruchomości"]),
    "konsultacje": ("Jedno spotkanie w Twoim wnętrzu i konkretny kierunek zmian do zrobienia samodzielnie.", ["kierunek kolorów i materiałów", "lista zmian krok po kroku", "spotkanie na miejscu albo online"]),
}
of_nav = "".join(f'<li><a href="#{k}"><span>{i:02d}</span><span>{n}</span></a></li>' for i, (k, n, _d, _img) in enumerate(SERVICES, start=1))
svc = "".join(f'<section class="of-item" id="{k}"><div class="mask">{pic(img, "r-16-9", "(max-width: 860px) 100vw, 66vw")}</div><div class="top"><span class="n">{i:02d}</span><h2 class="d-l">{n}</h2></div><div class="cols"><p class="lead">{SVC_DETAIL[k][0]}</p><ul class="stag">{"".join(f"<li>{x}</li>" for x in SVC_DETAIL[k][1])}</ul></div></section>' for i, (k, n, _d, img) in enumerate(SERVICES, start=1))
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
<div class="wrap g12 of"><nav class="of-nav" aria-label="Usługi"><ol>{of_nav}</ol><a class="btn" href="kontakt.html" data-modal>Umów rozmowę</a></nav><div class="of-body">{svc}</div></div>
{wave_sec()}
<section class="proc wtop soft" style="margin-top:56px"><div class="wrap">
  <div class="head g12"><p class="lbl w">Jak pracuję</p><h2 class="d-m rv">Pięć kroków od pierwszej rozmowy do gotowego wnętrza</h2></div>
  <ol class="stag">{steps}</ol>
</div></section>
<section class="faq-w"><div class="wrap g12">
  <div class="head"><p class="lbl w muted">Pytania</p><h2 class="d-m rv" style="margin-top:16px">Najczęściej słyszę</h2></div>
  <div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)}</div>
</div></section>
{cta()}"""
page("oferta.html", "Oferta | projektowanie wnętrz | Smuga Design", "Mieszkania, domy, wnętrza komercyjne, wizualizacje i konsultacje. Proces współpracy i najczęstsze pytania.", oferta, "oferta.html")


# O MNIE
omnie = f"""<div class="ph-head"><div class="wrap">
  <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>O mnie</span></p>
  <div class="g12"><h1 class="d-xl">Wioleta Siemieniuk</h1><p class="lead muted">Architektka wnętrz, założycielka Smuga Design.</p></div>
</div></div>
<section class="me"><div class="wrap g12">
  <figure class="pic mask in">{pic("smuga-wioleta", "r-5-4", "(max-width: 860px) 100vw, 40vw", True)}</figure>
  <div class="txt stag">
    <p class="lbl w muted">Podejście</p>
    <h2 class="d-m">Spokojna baza i jeden odważny gest.</h2>
    <p class="lead">Lubię naturalne materiały: drewno, kamień, len. Na nich buduję wnętrza, w których jest miejsce na kolor i sztukę.</p>
    <p class="muted">Projektuję od okna: gdzie pada światło, tam zaczyna się wnętrze. Tekst do uzupełnienia o wykształcenie, doświadczenie i publikacje.</p>
    <div class="sig"><a href="{IG}" rel="noopener" style="display:inline-flex;gap:8px;align-items:center">{ICO["ig"]}@smuga_design</a><a class="btn" href="kontakt.html" data-modal>Umów rozmowę</a></div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  {carousel("Z pracowni", "Detale z moich projektów", "Materiały, kolory i formy, do których wracam.", ["dom-wyspa", "show-luk", "wwa-zabudowa", "mnc-bar", "show-regal", "dom-zabudowa", "wwa-mural", "mnc-lada"])}
</div></section>
{cta()}"""
page("o-mnie.html", "O mnie | Wioleta Siemieniuk | Smuga Design", "Arch. wn. Wioleta Siemieniuk, Smuga Design. Ciepły minimalizm z odwagą koloru.", omnie, "o-mnie.html", og="smuga-wioleta")


# KONTAKT (bez kwot)
def pills(name, items, req=False):
    return "".join(f'<label><input type="radio" name="{name}" value="{t}"{" required" if req and i == 0 else ""}><span>{t}</span></label>' for i, t in enumerate(items))


kontakt = f"""<section class="kt">
  <div class="kt-side">
    {mark()}
    <p class="crumbs"><a href="index.html">Start</a><span>/</span><span>Kontakt</span></p>
    <div><p class="lbl w">Kontakt</p><h1 class="d-l" style="margin-top:16px">Porozmawiajmy o Twoim wnętrzu</h1></div>
    <div class="kt-list">
      <a href="tel:{PHONE_HREF}"><span class="ic">{ICO["tel"]}</span><span><span class="lbl">Telefon</span><b>{PHONE}</b></span></a>
      <a href="mailto:{EMAIL}"><span class="ic">{ICO["mail"]}</span><span><span class="lbl">E-mail</span><b>{EMAIL}</b></span></a>
      <a href="{IG}" rel="noopener"><span class="ic">{ICO["ig"]}</span><span><span class="lbl">Instagram</span><b>@smuga_design</b></span></a>
      <div><span class="ic">{ICO["pin"]}</span><span><span class="lbl">Obszar</span><b>Białystok, Warszawa, zdalnie</b></span></div>
    </div>
    <ol class="kt-steps small"><li>Odpowiadam na wiadomość i umawiamy rozmowę.</li><li>Rozmawiamy o wnętrzu, potrzebach i terminie.</li><li>Przygotowuję zakres i wycenę na piśmie.</li></ol>
  </div>
  <div class="kt-form">
    <h2 class="d-l">Opisz swoje wnętrze</h2>
    <p class="lead muted">Im więcej szczegółów, tym lepiej przygotuję się do pierwszej rozmowy.</p>
    <form class="form" novalidate>
      <label><span>Imię <span class="req" aria-hidden="true">*</span></span><input name="imie" autocomplete="given-name" required></label>
      <label><span>E-mail <span class="req" aria-hidden="true">*</span></span><input type="email" name="email" autocomplete="email" required></label>
      <label>Telefon<input type="tel" name="tel" autocomplete="tel"></label>
      <label>Lokalizacja<input name="miasto" placeholder="np. Białystok"></label>
      <fieldset class="full"><legend><span>Rodzaj wnętrza <span class="req" aria-hidden="true">*</span></span></legend><div class="pills">{pills("typ", ["Mieszkanie", "Dom", "Wnętrze komercyjne", "Inne"], True)}</div></fieldset>
      <fieldset class="full"><legend>Zakres</legend><div class="pills">{pills("zakres", [n for _k, n, _d, _i in SERVICES] + ["Jeszcze nie wiem"])}</div></fieldset>
      <label>Metraż (m²)<input name="metraz" inputmode="numeric" placeholder="np. 65"></label>
      <fieldset><legend>Kiedy chcesz zacząć</legend><div class="pills">{pills("termin", ["Teraz", "Do 3 mies.", "Później"])}</div></fieldset>
      <label class="full">Wiadomość<textarea name="wiadomosc" placeholder="Co chcesz zmienić? Co lubisz, czego nie?"></textarea></label>
      <div class="full"><label class="drop"><input type="file" name="pliki" multiple accept=".pdf,.jpg,.jpeg,.png"><span class="ic">{ICO["up"]}</span><span><b>Dodaj rzut lub zdjęcia wnętrza</b><small>Przeciągnij pliki tutaj. PDF, JPG lub PNG.</small></span><span class="pick">Wybierz pliki</span></label><ul class="files"></ul></div>
      <label class="consent full"><input type="checkbox" required> Zgadzam się na kontakt w sprawie zapytania. Dane przetwarza Smuga Design zgodnie z polityką prywatności.</label>
      <div class="send full"><button class="btn" type="submit">Wyślij zapytanie</button><a class="lnk" href="tel:{PHONE_HREF}">albo zadzwoń: {PHONE}</a></div>
      <p class="form-ok" hidden tabindex="-1">{mark()}To jest demo: formularz niczego nie wysyła. Na gotowej stronie wiadomość trafi na {EMAIL}.</p>
    </form>
  </div>
</section>"""
page("kontakt.html", "Kontakt | Smuga Design", "Zapytanie o projekt wnętrza: mieszkanie, dom, wnętrze komercyjne. Białystok, Warszawa, zdalnie.", kontakt, "kontakt.html")

print("ok:", sorted(x.name for x in OUT.glob("*.html")))
