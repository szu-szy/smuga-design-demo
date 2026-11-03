// Smuga Design - demo: nagłówek, menu mobilne, pojawianie się sekcji, podgląd zdjęć, formularz.
document.documentElement.classList.add('js');

const hdr = document.querySelector('.hdr');
const onScroll = () => hdr.classList.toggle('is-scrolled', window.scrollY > 60);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav');
const setMenu = (open) => {
  nav.classList.toggle('is-open', open);
  burger.setAttribute('aria-expanded', String(open));
  burger.querySelector('span').textContent = open ? 'Zamknij' : 'Menu';
  document.body.style.overflow = open ? 'hidden' : '';
};
burger.addEventListener('click', () => setMenu(!nav.classList.contains('is-open')));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && nav.classList.contains('is-open')) { setMenu(false); burger.focus(); } });

const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
}, { rootMargin: '0px 0px -10% 0px' });
document.querySelectorAll('.rv').forEach((el) => io.observe(el));

// podgląd zdjęć: licznik, strzałki, Esc, przesuwanie palcem
const lb = document.querySelector('.lb');
if (lb) {
  const shots = [...document.querySelectorAll('[data-shot]')];
  const img = lb.querySelector('img');
  const count = lb.querySelector('.lb-count');
  const cap = lb.querySelector('.lb-cap');
  let cur = 0;
  let opener = null;
  const show = (i) => {
    cur = (i + shots.length) % shots.length;
    const s = shots[cur];
    img.src = s.dataset.shot;
    img.alt = s.dataset.alt;
    count.textContent = `${cur + 1} / ${shots.length}`;
    cap.textContent = s.dataset.alt;
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
    if (e.key === 'Tab') { // fokus zostaje w podglądzie
      const f = [...lb.querySelectorAll('button')].filter((b) => b.offsetParent);
      const i = f.indexOf(document.activeElement);
      e.preventDefault();
      f[(i + (e.shiftKey ? -1 : 1) + f.length) % f.length].focus();
    }
  });
  let x0 = null;
  lb.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 48) show(cur + (dx < 0 ? 1 : -1));
    x0 = null;
  });
}

const form = document.querySelector('.form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const ok = form.querySelector('.form-ok');
    ok.hidden = false;
    ok.focus();
  });
}
