/* Publishes the notice bar's real height so the fixed header, the main padding and
   the anchor scroll-offset all move down by exactly that much. Measured, not
   hard-coded, because the notice wraps to two lines on narrow viewports. */
(function () {
  function sync() {
    var n = document.querySelector('.notice');
    document.documentElement.style.setProperty('--notice-h', n ? n.offsetHeight + 'px' : '0px');
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
