# -*- coding: utf-8 -*-
ICO = {
 'clock':'<circle cx="12" cy="13" r="8.2"/><path d="M12 8.6v4.6l3 1.9"/><path d="M4.8 3.4 2.4 6M19.2 3.4 21.6 6"/>',
 'target':'<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1.2"/>',
 'layers':'<path d="M12 3.2 3.4 8 12 12.8 20.6 8 12 3.2Z"/><path d="M3.4 12.4 12 17.2l8.6-4.8"/><path d="M3.4 16.6 12 21.4l8.6-4.8"/>',
 'book':'<path d="M4.2 5.6A2.6 2.6 0 0 1 6.8 3H20v15.2H6.8a2.6 2.6 0 0 0-2.6 2.6Z"/><path d="M8 7.6h8M8 11.2h5.6"/>',
 'wrench':'<path d="M15.4 3.6a5.1 5.1 0 0 0-6.4 6.4l-6 6V21h4.8l6-6a5.1 5.1 0 0 0 6.4-6.4l-3.1 3.1-2.8-.7-.7-2.8 3.1-3.1Z"/>',
 'bars':'<path d="M3 20.4h18"/><path d="M6.4 20.4v-6.2M11.4 20.4V7.6M16.4 20.4v-9.4M21 20.4V4.4"/>',
 'scales':'<path d="M12 4.2v16M6.4 7.6h11.2M8 20.2h8"/><path d="M6.4 7.6 3.2 14h6.4L6.4 7.6ZM17.6 7.6 14.4 14h6.4l-3.2-6.4Z"/>',
 'shield':'<path d="M12 3.2 19 6v6.1c0 4.3-2.9 7.5-7 8.9-4.1-1.4-7-4.6-7-8.9V6l7-2.8Z"/><path d="M8.8 12.1l2.3 2.3 4.3-4.4"/>',
 'star':'<path d="m12 3.4 1.7 3.8 3.6-1-1 3.6 3.6-.6-2.5 2.7 3.1 1.9-3.5 1.1 1 3.4-3.5-1.3L12 20.6l-2.5-2.6-3.5 1.3 1-3.4-3.5-1.1 3.1-1.9-2.5-2.7 3.6.6-1-3.6 3.6 1L12 3.4Z"/>',
 'mic':'<rect x="9" y="2.8" width="6" height="11" rx="3"/><path d="M5.2 11.6a6.8 6.8 0 0 0 13.6 0M12 18.4V21.2M8.6 21.2h6.8"/>',
 'globe':'<circle cx="12" cy="12" r="8.8"/><path d="M3.2 12h17.6M12 3.2c2.4 2.5 3.6 5.5 3.6 8.8s-1.2 6.3-3.6 8.8c-2.4-2.5-3.6-5.5-3.6-8.8S9.6 5.7 12 3.2Z"/>',
 'mail':'<rect x="2.8" y="5" width="18.4" height="14" rx="3"/><path d="m3.6 6.6 8.4 6 8.4-6"/>',
 'phone':'<path d="M7.4 3.4h2.2l1.6 4-2 1.4a12.5 12.5 0 0 0 5.9 5.9l1.4-2 4 1.6v2.2a2.4 2.4 0 0 1-2.6 2.4C10.6 18.4 5.6 13.4 5 6.1A2.4 2.4 0 0 1 7.4 3.4Z"/>',
 'pin':'<path d="M12 21.2s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z"/><circle cx="12" cy="10.2" r="2.7"/>',
}
def ico(name, tone=''):
    return ('<span class="sec-ico %s"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>' % (tone, ICO[name])).replace('  ',' ')
def cico(name):
    return '<span class="card__ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>' % ICO[name]
def head(name, tone, title):
    return '<div class="sec-head">%s<h2>%s</h2></div>' % (ico(name, tone), title)

APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M17.05 12.54c-.03-2.6 2.12-3.85 2.22-3.91-1.21-1.77-3.1-2.01-3.77-2.04-1.6-.16-3.13.94-3.94.94-.81 0-2.07-.92-3.4-.9-1.75.03-3.36 1.02-4.26 2.58-1.82 3.15-.47 7.81 1.3 10.36.87 1.25 1.9 2.65 3.26 2.6 1.31-.05 1.8-.84 3.38-.84 1.58 0 2.02.84 3.4.81 1.4-.02 2.29-1.27 3.15-2.53.99-1.45 1.4-2.86 1.42-2.93-.03-.01-2.73-1.05-2.76-4.14ZM14.6 4.9c.72-.87 1.2-2.08 1.07-3.29-1.03.04-2.28.69-3.02 1.56-.66.77-1.24 2-1.09 3.18 1.15.09 2.32-.58 3.04-1.45Z"/></svg>')
PLAY = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
 '<path fill="#00C3FF" d="M3.6 1.93c-.3.32-.48.81-.48 1.45v17.24c0 .64.18 1.13.48 1.45l.06.06 9.66-9.66v-.23L3.66 1.87l-.06.06Z"/>'
 '<path fill="#FFCE00" d="m16.6 15.4-3.28-3.29v-.23l3.29-3.29.07.05 3.9 2.21c1.11.63 1.11 1.66 0 2.3l-3.9 2.21-.08.04Z"/>'
 '<path fill="#FF3A44" d="m16.68 15.36-3.36-3.36-9.72 9.72c.37.39.97.43 1.65.05l11.43-6.41Z"/>'
 '<path fill="#00C853" d="M16.68 8.64 5.25 2.23c-.68-.38-1.28-.34-1.65.05l9.72 9.72 3.36-3.36Z"/></svg>')
GLOBE = '<svg viewBox="0 0 24 24" aria-hidden="true" style="fill:none;stroke:currentColor;stroke-width:1.7">%s</svg>' % ICO['globe']

def badges(L):
    return ('<div class="badges">'
      '<a class="badge" href="https://apps.apple.com/app/id6764625502">%s<span><span class="b1">%s</span><span class="b2">App Store</span></span></a>'
      '<a class="badge" href="https://play.google.com/store/apps/details?id=com.selmapp.app">%s<span><span class="b1">%s</span><span class="b2">Google Play</span></span></a>'
      '<a class="badge badge--web" href="https://selmapp.com">%s<span><span class="b1">%s</span><span class="b2">%s</span></span></a>'
      '</div>') % (APPLE, L['apple'], PLAY, L['play'], GLOBE, L['web1'], L['web2'])

def phone(L):
    """Result card. The scale, the band and the target are all parameters —
    the card used to hard-code an NCLC 4-10 axis, which meant it could only
    ever show a French exam."""
    marks = L.get('marks', [4, 5, 6, 7, 8, 9, 10])
    lo, hi = marks[0], marks[-1]
    span = float(hi - lo)
    pos = lambda v: (v - lo) / span * 100.0
    band_lo, band_hi = L['band']
    scale = ''.join('<span>%s</span>' % m for m in marks)
    L = dict(L,
             _scale=scale,
             _bl='%.4g' % pos(band_lo),
             _br='%.4g' % (100.0 - pos(band_hi)),
             _tgt='%.4g' % pos(L['target']))
    return '''<div class="mock reveal">
  <div class="phone">
    <div class="phone__scr">
      <span class="phone__notch"></span>
      <div class="phone__bar"><b>SELM</b><span>%(attempt)s</span></div>
      <div class="rcard">
        <div class="rcard__test">%(test)s</div>
        <div class="rcard__skill">%(skill)s</div>
        <div class="rcard__range">%(range)s</div>
        <div class="rcard__sub">%(sub)s</div>
        <div class="gauge">
          <span class="gauge__track"></span>
          <span class="gauge__band" style="left:%(_bl)s%%;right:%(_br)s%%"></span>
          <span class="gauge__tgt %(en)s" style="left:%(_tgt)s%%"></span>
          <span class="gauge__scale">%(_scale)s</span>
        </div>
        <div class="rrow"><span>%(r1)s</span><span class="mini"><i style="width:72%%"></i></span></div>
        <div class="rrow"><span>%(r2)s</span><span class="mini amber"><i style="width:54%%"></i></span></div>
        <div class="rrow"><span>%(r3)s</span><span class="mini violet"><i style="width:63%%"></i></span></div>
        <p class="rnote">%(note)s</p>
      </div>
    </div>
  </div>
  <p class="mock__cap">%(cap)s</p>
</div>''' % L


def phone_skills(L):
    rows = ''.join(
        '<div class="mrow"><span class="mrow__ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>'
        '<span><b>%s</b><span>%s</span></span><em>%s</em></div>' % (ICO[i], n, s, v)
        for i, n, s, v in L['rows'])
    return ('<div class="phone"><div class="phone__scr"><span class="phone__notch"></span>'
            '<div class="phone__bar"><b>SELM</b><span>%s</span></div>'
            '<div class="mhead">%s</div><div class="mtitle">%s</div>%s</div></div>'
            % (L['bar'], L['head'], L['title'], rows))


def phone_decision(L):
    steps = ''.join('<div class="mrow"><span class="mrow__ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>'
                    '<span><b>%s</b><span>%s</span></span></div>' % (ICO[i], n, s)
                    for i, n, s in L['steps'])
    return ('<div class="phone"><div class="phone__scr"><span class="phone__notch"></span>'
            '<div class="phone__bar"><b>SELM</b><span>%s</span></div>'
            '<div class="mhead">%s</div>'
            '<div class="rcard__range" style="font-size:27px;margin:2px 0 0">%s</div>'
            '<p class="rcard__sub" style="margin:4px 0 12px">%s</p>%s'
            '<p class="rnote">%s</p></div></div>'
            % (L['bar'], L['head'], L['verdict'], L['sub'], steps, L['note']))


def phone_exam(L):
    return ('<div class="phone"><div class="phone__scr"><span class="phone__notch"></span>'
            '<div class="phone__bar"><b>SELM</b><span>%s</span></div>'
            '<div class="mhead">%s</div><div class="mtitle">%s</div>'
            '<div class="rcard__range" style="font-size:30px;letter-spacing:0;margin:10px 0 0">%s</div>'
            '<div class="mbar"><i style="width:38%%"></i></div>'
            '<p class="rcard__sub" style="margin:2px 0 12px">%s</p>'
            '<div class="mrow"><span class="mrow__ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>'
            '<span><b>%s</b><span>%s</span></span></div>'
            '<div class="mrow"><span class="mrow__ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>'
            '<span><b>%s</b><span>%s</span></span></div>'
            '<p class="rnote">%s</p></div></div>'
            % (L['bar'], L['head'], L['title'], L['clock'], L['progress'],
               ICO['mic'], L['r1'], L['r1s'], ICO['globe'], L['r2'], L['r2s'], L['note']))


def fan(left, centre, right, cap):
    return ('<div class="mock reveal"><div class="fan">%s%s%s</div>'
            '<p class="mock__cap">%s</p></div>' % (left, right, centre, cap))
