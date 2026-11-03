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
    "viz-apartament-wwa": ("Sypialnia z muralem i zabudową ze sklejki, mieszkanie w Warszawie", (808, 632)),
    "viz-dom-001": ("Kuchnia z wyspą i ryflowaną zabudową, dom jednorodzinny", (808, 632)),
    "viz-showroom": ("Jasny showroom z łukami i drewnianą zabudową, showroom Spod igły i nitki", (808, 632)),
    "smuga-wioleta": ("Arch. wn. Wioleta Siemieniuk, Smuga Design", (808, 632)),
    "wwa-mural": ("Mural nad łóżkiem, mieszkanie w Warszawie", (450, 360)),
    "wwa-zabudowa": ("Zabudowa ze sklejki, mieszkanie w Warszawie", (300, 420)),
    "wwa-grafiki": ("Grafiki na ścianie sypialni, mieszkanie w Warszawie", (208, 400)),
    "dom-wyspa": ("Ryflowana wyspa kuchenna, dom jednorodzinny", (480, 382)),
    "dom-zabudowa": ("Zabudowa kuchni w jasnym drewnie, dom jednorodzinny", (378, 450)),
    "dom-okno": ("Okno na ogród z kuchni, dom jednorodzinny", (300, 420)),
    "show-regal": ("Drewniany regał z podświetleniem, showroom Spod igły i nitki", (328, 500)),
    "show-luk": ("Łukowe przejście do przymierzalni, showroom Spod igły i nitki", (400, 400)),
    "show-fotel": ("Rzeźbiarski fotel, showroom Spod igły i nitki", (248, 382)),
}

PROJECTS = [
    {
        "slug": "mnc-concept", "code": "SD_MNC.CONCEPT_25", "status": "real", "field": "pink",
        "title": "Kawiarnia MNC Concept", "short": "MNC Concept",
        "typ": "Wnętrze komercyjne", "lok": "Białystok", "rok": "2025",
        "cover": "mnc-kotara", "card": "mnc-sala", "details": [],
        "lead": "Kawiarnia, w której wnętrze jest częścią marki: jasne kotary, stal i drewno tworzą spokojne tło, a kolor i kwiaty dają mu charakter.",
        "blocks": [
            ("Założenia", "Wnętrze miało pracować jak tło dla marki i ludzi: spokojne na co dzień, wyraziste na zdjęciach z Instagrama."),
            ("Materiały", "Miękkie kotary, szczotkowana stal baru, kamienne blaty stolików i front lady z mocnym rysunkiem drewna."),
            ("Efekt", "Przestrzeń, którą goście rozpoznają po jednym kadrze. Różowa kotara i kwiaty stały się znakiem miejsca."),
        ],
        "gallery": ["mnc-sala", "mnc-lada", "mnc-bar", "mnc-loza", "mnc-wejscie", "mnc-taras"],
    },
    {
        "slug": "mieszkanie-warszawa", "code": "SD_APARTMENT_002", "status": "viz", "field": "dark",
        "title": "Mieszkanie w Warszawie", "short": "Mieszkanie WWA",
        "typ": "Mieszkanie", "lok": "Warszawa", "rok": "",
        "cover": "viz-apartament-wwa", "card": "viz-apartament-wwa", "details": ["wwa-mural", "wwa-zabudowa", "wwa-grafiki"],
        "lead": "Sypialnia, w której sztuka gra pierwsze skrzypce: mural na całą ścianę, ciepła sklejka i spokojne tkaniny.",
        "blocks": [
            ("Założenia", "Jedno odważne wydarzenie na ścianie i bardzo prosta reszta, żeby wnętrze nie męczyło na co dzień."),
            ("Materiały", "Sklejka w zabudowie i wezgłowiu, lniane tkaniny, toczone nóżki i grafiki w cienkich ramach."),
            ("Efekt", "Ciepła, osobista sypialnia z kolorem, który nie przytłacza."),
        ],
        "gallery": [],
    },
    {
        "slug": "dom-001", "code": "SD_HOUSE_001", "status": "viz", "field": "soft",
        "title": "Dom z widokiem na ogród", "short": "Dom 001",
        "typ": "Dom jednorodzinny", "lok": "", "rok": "",
        "cover": "viz-dom-001", "card": "viz-dom-001", "details": ["dom-wyspa", "dom-zabudowa", "dom-okno"],
        "lead": "Kuchnia otwarta na ogród: ryflowane drewno, kamień i dużo światła z okna od podłogi do sufitu.",
        "blocks": [
            ("Założenia", "Kuchnia jako spokojne centrum domu, z widokiem na zieleń z każdego miejsca przy wyspie."),
            ("Materiały", "Ryflowany front wyspy, zabudowa w jasnym drewnie, kamienne blaty i czarne, lekkie hokery."),
            ("Efekt", "Ciepły minimalizm, w którym rysunek drewna i kamienia zastępuje dekoracje."),
        ],
        "gallery": [],
    },
    {
        "slug": "showroom-spod-igly-i-nitki", "code": "SD_SHOWROOM", "status": "viz", "field": "",
        "title": "Showroom Spod igły i nitki", "short": "Showroom",
        "typ": "Wnętrze komercyjne", "lok": "", "rok": "",
        "cover": "viz-showroom", "card": "viz-showroom", "details": ["show-regal", "show-luk", "show-fotel"],
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

