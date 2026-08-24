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
