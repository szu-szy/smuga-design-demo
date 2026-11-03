// Smuga Design - demo v4: loader, megamenu, hero z przenikaniem, szuflada, wejścia, podgląd zdjęć, formularz.
const root = document.documentElement;
root.classList.add('js');
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;

// loader: raz na sesję, licznik 0-100, kurtyna z falą w górę i start hero
const loader = document.querySelector('.loader');
const start = () => root.classList.add('go');
if (root.classList.contains('ld') && loader && !still) {
  const num = loader.querySelector('.meta b');
  const t0 = performance.now();
  const tick = (t) => { const k = Math.min(1, (t - t0) / 1600); num.textContent = String(Math.round(k * 100)).padStart(3, '0'); if (k < 1) requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
  const done = () => {
    loader.classList.add('out');
    setTimeout(start, 300);
    loader.addEventListener('transitionend', (e) => { if (e.target !== loader) return; root.classList.remove('ld'); loader.remove(); });
    try { sessionStorage.setItem('smuga-ld', '1'); } catch (e) { /* tryb prywatny */ }
  };
  Promise.all([document.fonts ? document.fonts.ready : Promise.resolve(), new Promise((r) => setTimeout(r, 1700))]).then(done);
} else {
  root.classList.remove('ld');
  if (loader) loader.remove();
  start();
}

// megamenu Oferta: klik, najechanie, Esc, podgląd zdjęcia przy pozycji
const mmBtn = document.querySelector('.mm-btn');
const mm = document.querySelector('.mm');
if (mmBtn && mm) {
  let t = null;
  const set = (open) => { mm.classList.toggle('is-open', open); mmBtn.setAttribute('aria-expanded', String(open)); };
  const wrap = mmBtn.closest('.hdr');
  mmBtn.addEventListener('click', () => set(!mm.classList.contains('is-open')));
  mmBtn.addEventListener('mouseenter', () => { clearTimeout(t); set(true); });
  mm.addEventListener('mouseenter', () => clearTimeout(t));
  [mmBtn, mm].forEach((el) => el.addEventListener('mouseleave', () => { t = setTimeout(() => set(false), 200); }));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && mm.classList.contains('is-open')) { set(false); mmBtn.focus(); } });
  document.addEventListener('click', (e) => { if (!wrap.contains(e.target)) set(false); });
  wrap.addEventListener('focusout', (e) => { if (!wrap.contains(e.relatedTarget)) set(false); });
  const items = [...mm.querySelectorAll('.mm-list a')];
  const figs = [...mm.querySelectorAll('.mm-pre figure')];
  const pick = (i) => { items.forEach((a, j) => a.classList.toggle('on', i === j)); figs.forEach((f, j) => f.classList.toggle('on', i === j)); };
  items.forEach((a, i) => { a.addEventListener('mouseenter', () => pick(i)); a.addEventListener('focus', () => pick(i)); });
  pick(0);
}

// szuflada na telefonie
const burger = document.querySelector('.burger');
const drawer = document.querySelector('.drawer');
const setMenu = (open) => {
  drawer.classList.toggle('is-open', open);
  burger.setAttribute('aria-expanded', String(open));
  burger.querySelector('span').textContent = open ? 'Zamknij' : 'Menu';
  document.body.style.overflow = open ? 'hidden' : '';
};
burger.addEventListener('click', () => { setMenu(true); setTimeout(() => drawer.querySelector('.d-close').focus(), 60); });
drawer.querySelector('.d-close').addEventListener('click', () => { setMenu(false); burger.focus(); });
drawer.querySelectorAll('[data-modal]').forEach((a) => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', (e) => {
  if (!drawer.classList.contains('is-open')) return;
  if (e.key === 'Escape') { setMenu(false); burger.focus(); }
  if (e.key === 'Tab') { // fokus zostaje w szufladzie
    const f = [...drawer.querySelectorAll('a, button')];
    const i = f.indexOf(document.activeElement);
    e.preventDefault();
    f[(i + (e.shiftKey ? -1 : 1) + f.length) % f.length].focus();
  }
});

// hero: przenikające zdjęcia z paskiem postępu, pauza po najechaniu i poza ekranem
const hero = document.querySelector('.hero');
if (hero) {
  const slides = [...hero.querySelectorAll('.sl')];
  const bars = [...hero.querySelectorAll('.prog button')];
  const cap = hero.querySelector('.now .name');
  const num = hero.querySelector('.now .num');
  const dur = 6000;
  hero.style.setProperty('--dur', `${dur}ms`);
  let cur = 0; let timer = null; let left = dur; let t0 = 0; let paused = false;
  const show = (i) => {
    cur = (i + slides.length) % slides.length;
    slides.forEach((s, j) => s.classList.toggle('on', j === cur));
    bars.forEach((b, j) => { b.classList.toggle('on', j === cur); b.classList.toggle('done', j < cur); b.setAttribute('aria-current', j === cur ? 'true' : 'false'); });
    cap.style.opacity = 0;
    setTimeout(() => { cap.textContent = slides[cur].dataset.cap; num.textContent = `${String(cur + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`; cap.style.opacity = 1; }, 200);
    left = dur; run();
  };
  const run = () => { clearTimeout(timer); if (paused || still) return; t0 = Date.now(); timer = setTimeout(() => show(cur + 1), left); };
  const pause = () => { if (paused) return; paused = true; hero.classList.add('paused'); clearTimeout(timer); left -= Date.now() - t0; };
  const resume = () => { if (!paused) return; paused = false; hero.classList.remove('paused'); run(); };
  bars.forEach((b, i) => b.addEventListener('click', () => show(i)));
  hero.addEventListener('mouseenter', pause); hero.addEventListener('mouseleave', resume);
  hero.addEventListener('focusin', pause); hero.addEventListener('focusout', resume);
  new IntersectionObserver(([en]) => (en.isIntersecting ? resume() : pause())).observe(hero);
  const begin = () => show(0);
  if (root.classList.contains('go')) begin(); else new MutationObserver((m, o) => { if (root.classList.contains('go')) { o.disconnect(); begin(); } }).observe(root, { attributes: true });
}

// wejścia przy przewijaniu
const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
}, { rootMargin: '0px 0px -10% 0px' });
document.querySelectorAll('.rv, .mask, .stag').forEach((el) => io.observe(el));

// podgląd zdjęć
const lb = document.querySelector('.lb');
if (lb) {
  const shots = [...document.querySelectorAll('[data-shot]')];
  const img = lb.querySelector('img');
  const count = lb.querySelector('.lb-count');
  const cap = lb.querySelector('.lb-cap');
  let cur = 0; let opener = null;
  const show = (i) => {
    cur = (i + shots.length) % shots.length;
    img.src = shots[cur].dataset.shot; img.alt = shots[cur].dataset.alt;
    count.textContent = `${String(cur + 1).padStart(2, '0')} / ${String(shots.length).padStart(2, '0')}`;
    cap.textContent = shots[cur].dataset.alt;
  };
  const open = (i, btn) => { opener = btn; show(i); lb.classList.add('is-open'); document.body.style.overflow = 'hidden'; lb.querySelector('.close').focus(); };
  const close = () => { lb.classList.remove('is-open'); document.body.style.overflow = ''; if (opener) opener.focus(); };
  document.querySelectorAll('[data-open]').forEach((b) => b.addEventListener('click', () => open(Number(b.dataset.open), b)));
  lb.querySelector('.close').addEventListener('click', close);
  lb.querySelector('.prev').addEventListener('click', () => show(cur - 1));
  lb.querySelector('.nextb').addEventListener('click', () => show(cur + 1));
  document.addEventListener('keydown', (e) => {
    if (!lb.classList.contains('is-open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(cur - 1);
    if (e.key === 'ArrowRight') show(cur + 1);
    if (e.key === 'Tab') {
      const f = [...lb.querySelectorAll('button')].filter((b) => b.offsetParent);
      const i = f.indexOf(document.activeElement);
      e.preventDefault();
      f[(i + (e.shiftKey ? -1 : 1) + f.length) % f.length].focus();
    }
  });
  let x0 = null;
  lb.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', (e) => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 48) show(cur + (dx < 0 ? 1 : -1)); x0 = null; });
}

document.querySelectorAll('.form').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const ok = form.querySelector('.form-ok');
    ok.hidden = false; ok.focus();
  });
});

// modal "Umów rozmowę": natywny dialog (fokus w środku, Esc), zamykanie klikiem w tło
const dlg = document.querySelector('.dlg');
if (dlg) {
  let opener = null;
  document.querySelectorAll('[data-modal]').forEach((b) => b.addEventListener('click', (e) => { e.preventDefault(); opener = b; dlg.showModal(); }));
  dlg.querySelector('.x').addEventListener('click', () => dlg.close());
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener('close', () => { if (opener) opener.focus(); });
}

// przycisk telefonu na telefonie: pojawia się po zjechaniu w dół
const fab = document.querySelector('.fab');
if (fab) {
  const onFab = () => fab.classList.toggle('show', window.scrollY > 480);
  window.addEventListener('scroll', onFab, { passive: true });
  onFab();
}

// pole plików: przeciągnij i upuść, lista wybranych plików
document.querySelectorAll('.drop').forEach((drop) => {
  const input = drop.querySelector('input');
  const list = drop.parentElement.querySelector('.files');
  const show = () => { list.innerHTML = [...input.files].map((f) => `<li>${f.name.replace(/[<>&]/g, '')}</li>`).join(''); };
  input.addEventListener('change', show);
  ['dragenter', 'dragover'].forEach((ev) => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add('over'); }));
  ['dragleave', 'drop'].forEach((ev) => drop.addEventListener(ev, () => drop.classList.remove('over')));
  drop.addEventListener('drop', (e) => { e.preventDefault(); input.files = e.dataTransfer.files; show(); });
});

// indeks realizacji: podgląd zdjęcia przy najechaniu i fokusie
document.querySelectorAll('.wi').forEach((wi) => {
  const rows = [...wi.querySelectorAll('.wi-row')];
  const figs = [...wi.querySelectorAll('.wi-pre figure')];
  const pick = (i) => { rows.forEach((r, j) => r.classList.toggle('on', i === j)); figs.forEach((f, j) => f.classList.toggle('on', i === j)); };
  rows.forEach((r, i) => { r.addEventListener('mouseenter', () => pick(i)); r.addEventListener('focus', () => pick(i)); });
});

// karuzela: przyciski, pasek postępu, przewijanie palcem i klawiaturą
document.querySelectorAll('.car').forEach((car) => {
  const track = car.querySelector('.car-track');
  const prev = car.querySelector('.prev');
  const next = car.querySelector('.next');
  const bar = car.querySelector('.car-bar i');
  const step = () => track.querySelector('figure').getBoundingClientRect().width + 24;
  const update = () => {
    const max = track.scrollWidth - track.clientWidth;
    const k = max > 0 ? track.scrollLeft / max : 0;
    const vis = track.clientWidth / track.scrollWidth;
    bar.style.width = `${Math.round(vis * 100)}%`;
    bar.style.transform = `translateX(${Math.round(k * (1 / vis - 1) * 100)}%)`;
    prev.disabled = track.scrollLeft <= 2;
    next.disabled = track.scrollLeft >= max - 2;
  };
  prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: still ? 'auto' : 'smooth' }));
  next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: still ? 'auto' : 'smooth' }));
  track.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight') { e.preventDefault(); next.click(); } if (e.key === 'ArrowLeft') { e.preventDefault(); prev.click(); } });
  track.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
});

// oferta: podświetlenie aktywnej usługi w menu bocznym
const ofLinks = [...document.querySelectorAll('.of-nav a')];
if (ofLinks.length) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) ofLinks.forEach((a) => a.classList.toggle('on', a.getAttribute('href') === `#${en.target.id}`)); });
  }, { rootMargin: '-30% 0px -60% 0px' });
  document.querySelectorAll('.of-item').forEach((s) => spy.observe(s));
}
