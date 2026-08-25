# -*- coding: utf-8 -*-
"""Diagram builders for selmapp.ca. Every number here is transcribed from the
IRCC equivalency charts already used by assets/calc.js."""

def interval_svg(L):
    """The published output is an interval, not a point estimate — so the figure
    shows a band and a threshold, and no single-value marker."""
    x0, x1 = 62, 486                      # NCLC / CLB 4 .. 10
    def X(v): return x0 + (x1 - x0) * (v - 4) / 6.0
    lo, hi, tgt = 6, 8, 7
    ticks = ''.join(
        '<line x1="%.1f" y1="182" x2="%.1f" y2="190" stroke="rgba(255,255,255,.25)"/>'
        '<text x="%.1f" y="211" text-anchor="middle">%d</text>' % (X(v), X(v), X(v), v)
        for v in range(4, 11))
    return '''<svg viewBox="0 0 520 300" role="img" aria-label="%(alt)s">
  <defs>
    <linearGradient id="ivBand" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%%" stop-color="#2ec4b6" stop-opacity=".35"/>
      <stop offset="50%%" stop-color="#2ec4b6" stop-opacity=".9"/>
      <stop offset="100%%" stop-color="#2ec4b6" stop-opacity=".35"/>
    </linearGradient>
    <filter id="ivBlur" x="-40%%" y="-80%%" width="180%%" height="300%%">
      <feGaussianBlur stdDeviation="13"/>
    </filter>
  </defs>
  <text x="14" y="30" fill="#8ba3b8" font-size="15" font-weight="700" letter-spacing="1.5">%(kicker)s</text>
  <text x="14" y="66" fill="#ffffff" font-size="30" font-weight="800" letter-spacing="-.8">%(range)s</text>
  <text x="14" y="90" fill="#8ba3b8" font-size="14.5">%(scale)s</text>
  <rect x="%(bx).1f" y="108" width="%(bw).1f" height="62" rx="16" fill="#2ec4b6" opacity=".45" filter="url(#ivBlur)"/>
  <rect x="%(bx).1f" y="112" width="%(bw).1f" height="54" rx="14" fill="url(#ivBand)" stroke="#2ec4b6" stroke-opacity=".85" stroke-width="1.5"/>
  <line x1="%(tx).1f" y1="98" x2="%(tx).1f" y2="182" stroke="#f0b429" stroke-width="2.5" stroke-dasharray="7 6"/>
  <circle cx="%(tx).1f" cy="98" r="5" fill="#f0b429"/>
  <text x="%(tx2).1f" y="103" fill="#f0b429" font-size="16" font-weight="700">%(target)s</text>
  <line x1="%(x0)d" y1="182" x2="%(x1)d" y2="182" stroke="rgba(255,255,255,.25)" stroke-width="1.5"/>
  <g fill="#8ba3b8" font-size="15">%(ticks)s</g>
  <text x="14" y="252" fill="#b9cbdb" font-size="14.5">%(note1)s</text>
  <text x="14" y="276" fill="#b9cbdb" font-size="14.5">%(note2)s</text>
</svg>''' % dict(alt=L['alt'], kicker=L['kicker'], target=L['target'], range=L['range'],
                 scale=L['scale'], ticks=ticks, x0=x0, x1=x1, note1=L['note1'], note2=L['note2'],
                 bx=X(lo), bw=X(hi) - X(lo), tx=X(tgt), tx2=X(tgt) + 11)


LADDER = [
    # level, IELTS GT speaking minimum, CELPIP speaking, TEF speaking band, TCF speaking band
    (10, '7.5', '10', '556-699', None),
    (9,  '7.0', '9',  '518-555', None),
    (8,  '6.5', '8',  '494-517', None),
    (7,  '6.0', '7',  '456-493', '10-11'),
    (6,  '5.5', '6',  '422-455', None),
    (5,  '5.0', '5',  '387-421', None),
    (4,  '4.0', '4',  '328-386', None),
]
COLS = [('IELTS GT', '#4aa8ff'), ('CELPIP-G', '#8b7cf6'), ('TEF Canada', '#2ec4b6'), ('TCF Canada', '#f0b429')]


def ladder_svg(L):
    rowh, top, lx, cw, gap = 48, 76, 128, 122, 14
    out = ['<svg viewBox="0 0 720 %d" role="img" aria-label="%s">' % (top + rowh * 7 + 34, L['alt'])]
    out.append('<text x="8" y="26" fill="#8ba3b8" font-size="13" font-weight="700" letter-spacing="1.4">%s</text>' % L['kicker'])
    for i, (name, col) in enumerate(COLS):
        cx = lx + i * (cw + gap) + cw / 2.0
        out.append('<text x="%.1f" y="58" fill="%s" font-size="13.5" font-weight="800" text-anchor="middle" letter-spacing=".3">%s</text>' % (cx, col, name))
    for r, row in enumerate(LADDER):
        y = top + r * rowh
        lvl = row[0]
        hi = lvl == 7
        if r % 2 == 0:
            out.append('<rect x="0" y="%.1f" width="720" height="%d" rx="9" fill="rgba(255,255,255,.028)"/>' % (y - 6, rowh - 6))
        if hi:
            out.append('<rect x="0" y="%.1f" width="720" height="%d" rx="9" fill="rgba(240,180,41,.10)" stroke="rgba(240,180,41,.34)"/>' % (y - 6, rowh - 6))
        out.append('<text x="10" y="%.1f" fill="%s" font-size="14" font-weight="%s">%s %d</text>'
                   % (y + 14, '#ffffff' if hi else '#b9cbdb', '800' if hi else '600', L['lvl'], lvl))
        for i, (name, col) in enumerate(COLS):
            v = row[i + 1]
            x = lx + i * (cw + gap)
            if v is None:
                out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="rgba(255,255,255,.13)" stroke-width="2" stroke-linecap="round"/>'
                           % (x + cw / 2 - 9, y + 9, x + cw / 2 + 9, y + 9))
                continue
            txt = v.replace('-', '–')
            pre = L['atleast'] + ' ' if i < 2 else ''
            out.append('<rect x="%.1f" y="%.1f" width="%d" height="30" rx="8" fill="%s22" stroke="%s%s"/>'
                       % (x, y - 4, cw, col, col, '' if hi else '55'))
            out.append('<text x="%.1f" y="%.1f" fill="%s" font-size="%s" font-weight="700" text-anchor="middle">%s%s</text>'
                       % (x + cw / 2, y + 16, '#e8f0f7', '13.5' if len(txt) < 8 else '12.5', pre, txt))
    y = top + rowh * 7 + 12
    out.append('<text x="10" y="%.1f" fill="#8ba3b8" font-size="12">%s</text>' % (y, L['foot']))
    out.append('</svg>')
    return '\n'.join(out)


LAYER_TONE = ['#4aa8ff', '#4aa8ff', '#4aa8ff', '#8b7cf6', '#f0b429', '#2ec4b6', '#2ec4b6']

def layers_svg(L):
    """Seven layers, coloured by what they are: deterministic (blue), judged
    (violet), disagreement (amber), calibrated output (teal)."""
    W, bx, bw, h, gap, top = 820, 24, 400, 52, 16, 96
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (W, top + 7 * (h + gap) + 26, L['alt'])]
    o.append('<defs><marker id="arw" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="7" markerHeight="7" orient="auto">'
             '<path d="M0 0 L8 4 L0 8 z" fill="#7f97ab"/></marker>'
             '<linearGradient id="spine" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0%" stop-color="#4aa8ff"/><stop offset="45%" stop-color="#8b7cf6"/>'
             '<stop offset="70%" stop-color="#f0b429"/><stop offset="100%" stop-color="#2ec4b6"/>'
             '</linearGradient></defs>')
    o.append('<text x="%d" y="34" fill="#8ba3b8" font-size="16" font-weight="700" letter-spacing="1.5">%s</text>' % (bx, L['kicker']))
    o.append('<text x="%d" y="66" fill="#e8f0f7" font-size="17">%s</text>' % (bx, L['sub']))
    o.append('<rect x="%d" y="%d" width="4" height="%d" rx="2" fill="url(#spine)" opacity=".55"/>'
             % (bx + 26, top + 22, 7 * (h + gap) - gap - 44))
    for i, name in enumerate(L['names']):
        y = top + i * (h + gap)
        c = LAYER_TONE[i]
        o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="13" fill="%s16" stroke="%s%s" stroke-width="%s"/>'
                 % (bx, y, bw, h, c, c, '' if i in (3, 4) else '66', '1.8' if i in (3, 4) else '1.2'))
        o.append('<circle cx="%d" cy="%d" r="15" fill="%s2e" stroke="%s"/>' % (bx + 28, y + h / 2, c, c))
        o.append('<text x="%d" y="%d" fill="%s" font-size="15" font-weight="800" text-anchor="middle">%d</text>'
                 % (bx + 28, y + h / 2 + 5, c, i + 1))
        o.append('<text x="%d" y="%d" fill="#e8f0f7" font-size="16.5">%s</text>' % (bx + 56, y + h / 2 + 6, name))
        if i < 6:
            o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#7f97ab" stroke-opacity=".7" stroke-width="1.6" marker-end="url(#arw)"/>'
                     % (bx + 28, y + h + 1, bx + 28, y + h + gap - 5))
    # the disagreement branch, pulled out to the right of layer 5
    by = top + 4 * (h + gap)
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#f0b429" stroke-opacity=".8" stroke-width="1.8" marker-end="url(#arw)"/>'
             % (bx + bw, by + h / 2, bx + bw + 34, by + h / 2))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="rgba(240,180,41,.10)" stroke="#f0b429" stroke-opacity=".55"/>'
             % (bx + bw + 38, by - 54, 330, 172))
    o.append('<text x="%d" y="%d" fill="#f0b429" font-size="13.5" font-weight="800" letter-spacing=".8">%s</text>'
             % (bx + bw + 58, by - 24, L['branch']))
    for k, line in enumerate(L['rules']):
        o.append('<text x="%d" y="%d" fill="%s" font-size="15" font-weight="%s">%s</text>'
                 % (bx + bw + 58, by + 8 + k * 32, '#e8f0f7' if k == 2 else '#b9cbdb', '700' if k == 2 else '400', line))
    o.append('</svg>')
    return '\n'.join(o)


def share_svg(L):
    """Express Entry invitations by category, 1 January to 19 August 2026.
    Figures from the IRCC rounds-of-invitations feed."""
    rows = L['rows']          # (label, value, colour, note)
    total = max(v for _, v, _, _ in rows)
    x0, w, top, h, gap = 20, 660, 96, 54, 40
    o = ['<svg viewBox="0 0 720 %d" role="img" aria-label="%s">' % (top + len(rows) * (h + gap) + 46, L['alt'])]
    o.append('<text x="20" y="30" fill="#8ba3b8" font-size="17" font-weight="700" letter-spacing="1.4">%s</text>' % L['kicker'])
    o.append('<text x="20" y="60" fill="#e8f0f7" font-size="19">%s</text>' % L['sub'])
    for i, (lab, val, col, note) in enumerate(rows):
        y = top + i * (h + gap)
        bw = w * val / float(total)
        o.append('<text x="20" y="%d" fill="#e8f0f7" font-size="18" font-weight="700">%s</text>' % (y - 12, lab))
        o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="rgba(255,255,255,.05)"/>' % (x0, y, w, h))
        o.append('<rect x="%d" y="%d" width="%.1f" height="%d" rx="9" fill="%s33" stroke="%s"/>' % (x0, y, bw, h, col, col))
        o.append('<text x="%.1f" y="%d" fill="%s" font-size="22" font-weight="800">%s</text>'
                 % (x0 + bw + 12 if bw < w - 150 else x0 + 16, y + h / 2 + 6, col, '{:,}'.format(val)))
        if note:
            o.append('<text x="%.1f" y="%d" fill="#b9cbdb" font-size="16">%s</text>'
                     % ((x0 + bw + 130) if bw < w - 150 else (x0 + 130), y + h / 2 + 6, note))
    y = top + len(rows) * (h + gap) + 16
    o.append('<text x="20" y="%d" fill="#8ba3b8" font-size="15">%s</text>' % (y, L['foot']))
    o.append('</svg>')
    return '\n'.join(o)
