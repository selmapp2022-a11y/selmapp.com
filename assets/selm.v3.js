/* Publishes the notice bar's real height so the fixed header, the main padding and
   the anchor scroll-offset all move down by exactly that much. Measured, not
   hard-coded, because the notice wraps to two lines on narrow viewports. */
(function () {
  function sync() {
    var n = document.querySelector('.notice');
    document.documentElement.style.setProperty('--notice-h', n ? n.offsetHeight + 'px' : '0px');
    /* The header is measured for the same reason the notice is: its height
       depends on how many destinations the navigation holds and how wide the
       viewport is, and a constant was wrong on a phone. */
    var h = document.querySelector('header.site');
    if (h) { document.documentElement.style.setProperty('--head-h', h.offsetHeight + 'px'); }
  }
  sync();
  window.addEventListener('resize', sync);
  window.addEventListener('load', sync);
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(sync); }
})();

/* Sections fade and rise as they enter the viewport. The hiding rule lives behind
   .reveal-on, which is only set here — if this script never runs, nothing is hidden.
   prefers-reduced-motion is honoured in the stylesheet and again below. */
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!els.length) return;
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (calm || !('IntersectionObserver' in window)) {
    for (var i = 0; i < els.length; i++) { els[i].classList.add('in'); }
    return;
  }
  document.documentElement.classList.add('reveal-on');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
  for (var j = 0; j < els.length; j++) { io.observe(els[j]); }
  /* Anything already on screen at load should not wait for a scroll. */
  window.addEventListener('load', function () {
    for (var k = 0; k < els.length; k++) {
      if (els[k].getBoundingClientRect().top < window.innerHeight) { els[k].classList.add('in'); }
    }
  });
})();

/* ---- v3 additions, 27 August 2026 ---------------------------------------
   Three small behaviours. Each one checks prefers-reduced-motion, each one
   leaves the page in its finished state if it never runs, and none of them
   is required for anything on the page to be readable.
   ----------------------------------------------------------------------- */

var CALM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* 0 — the fade at the right edge of the navigation is drawn only when there
       is actually something to scroll to. A gradient with nothing behind it
       reads as a smudge on the bar. */
(function () {
  var bar = document.querySelector('.hd');
  var nav = bar && bar.querySelector('nav.main');
  if (!nav) return;
  function check() {
    bar.classList.toggle('nav-over', nav.scrollWidth - nav.clientWidth > 4);
  }
  check();
  window.addEventListener('resize', check);
  window.addEventListener('load', check);
  nav.addEventListener('scroll', function () {
    bar.classList.toggle('nav-over', nav.scrollWidth - nav.clientWidth - nav.scrollLeft > 4);
  }, { passive: true });
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(check); }
})();

/* 1 — the header lifts once the page has moved. */
(function () {
  var head = document.querySelector('header.site');
  if (!head) return;
  var on = false;
  function check() {
    var should = window.scrollY > 8;
    if (should !== on) { on = should; head.classList.toggle('is-stuck', should); }
  }
  check();
  window.addEventListener('scroll', check, { passive: true });
})();

/* 2 — children of a .stagger arrive in sequence. The index is set here
       rather than written into the markup, so adding a card to a grid does
       not mean renumbering the ones after it. */
(function () {
  var groups = document.querySelectorAll('.stagger');
  for (var g = 0; g < groups.length; g++) {
    var kids = groups[g].children;
    for (var k = 0; k < kids.length; k++) {
      kids[k].style.setProperty('--i', k > 7 ? 7 : k);
    }
  }
})();

/* 3 — the statistics count up to the figure already written in the markup.
       The number is parsed out of the element's own text, so the animation can
       never disagree with what the page says: remove the script and the
       finished figure is what was there all along. The French page writes
       42,1 and the English page writes 42.1, so the separator is read from
       the text rather than assumed. */
(function () {
  var els = document.querySelectorAll('[data-count]');
  if (!els.length) return;
  if (CALM || !('IntersectionObserver' in window)) return;

  function shape(raw) {
    if (/^\d{1,3}([ ,\u00a0]\d{3})+$/.test(raw)) {
      return { value: parseFloat(raw.replace(/[ ,\u00a0]/g, '')), dec: 0, group: raw.match(/[ ,\u00a0]/)[0], dsep: '' };
    }
    if (/^\d+,\d+$/.test(raw)) {
      return { value: parseFloat(raw.replace(',', '.')), dec: raw.split(',')[1].length, group: '', dsep: ',' };
    }
    if (/^\d+\.\d+$/.test(raw)) {
      return { value: parseFloat(raw), dec: raw.split('.')[1].length, group: '', dsep: '.' };
    }
    return { value: parseFloat(raw), dec: 0, group: '', dsep: '' };
  }

  function render(n, sh) {
    var t = n.toFixed(sh.dec);
    var whole = sh.dec ? t.slice(0, t.length - sh.dec - 1) : t;
    var frac = sh.dec ? t.slice(t.length - sh.dec) : '';
    if (sh.group) { whole = whole.replace(/\B(?=(\d{3})+(?!\d))/g, sh.group); }
    return sh.dec ? whole + sh.dsep + frac : whole;
  }

  function run(el) {
    var text = el.textContent;
    var m = text.match(/\d[\d.,\u00a0 ]*\d|\d/);
    if (!m) return;
    var sh = shape(m[0]);
    if (!isFinite(sh.value)) return;
    var before = text.slice(0, m.index), after = text.slice(m.index + m[0].length);
    var start = null, DUR = 900;
    function frame(t) {
      if (start === null) start = t;
      var p = Math.min(1, (t - start) / DUR);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = before + render(sh.value * eased, sh) + after;
      if (p < 1) { requestAnimationFrame(frame); } else { el.textContent = text; }
    }
    requestAnimationFrame(frame);
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { io.unobserve(e.target); run(e.target); }
    });
  }, { threshold: 0.5 });
  for (var i = 0; i < els.length; i++) { io.observe(els[i]); }
})();
