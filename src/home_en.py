# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gfx import ladder_svg, layers_svg, share_svg
from parts import head, cico, ico, badges, phone, phone_skills, phone_decision, phone_exam, fan
REPO = os.path.expanduser('~/mnt/selm/selmapp.com')

def body(mock_html):
    """strip the .mock wrapper, keep only the <div class="phone">…</div>"""
    i = mock_html.index('<div class="phone">')
    j = mock_html.index('</div>\n  <p class="mock__cap">')
    return mock_html[i:j+6]

CENTRE = body(phone(dict(
    attempt='Practice attempt 3', test='IELTS General Training · speaking',
    skill='Speaking', range='Band 6 to 7', band=(6, 7), target=7,
    marks=[4, 5, 6, 7, 8, 9],
    sub='90&nbsp;% interval · target band 7', en='en',
    r1='Fluency and coherence', r2='Pronunciation', r3='Lexical resource',
    note='Whole bands only, as the Test Report Form reports them.',
    cap='')))

LEFT = phone_skills(dict(bar='Diagnostic', head='TCF Canada · where you stand', title='Four skills',
    rows=[('mic','Expression orale','Speaking','NCLC 6–8'),
          ('globe','Compréhension orale','Listening','NCLC 7'),
          ('book','Compréhension écrite','Reading','NCLC 6'),
          ('target','Expression écrite','Writing','NCLC 5–7')]))

RIGHT = phone_decision(dict(bar='Readiness', head='Ready to book?', verdict='Not yet',
    sub='Your lowest interval is NCLC 5 to 7. You need 7 in all four.',
    steps=[('book','Tâche 3 structure','Three sessions'),
           ('clock','Timed writing','Twice a week'),
           ('scales','Re-test','In three weeks')],
    note='A candidate told to wait has not spent CAD 390 on a sitting they were not ready for.'))

EXAM = phone_exam(dict(bar='Mock exam', head='TCF Canada · compréhension orale',
    title='Section 2', clock='04:12', progress='Question 14 of 39',
    r1='Audio plays once', r1s='No replay, exactly as in the exam',
    r2='Offline', r2s='The whole exam runs without a connection',
    note='The interface, the timings and the single playback match the official instrument.'))

LADDER = ladder_svg(dict(
    alt='What each accepted test asks for at CLB and NCLC levels 4 to 10, speaking',
    kicker='SPEAKING — WHAT EACH TEST ASKS FOR', lvl='CLB / NCLC', atleast='≥',
    foot='Transcribed from the IRCC equivalency charts. TCF Canada appears at NCLC 7 only.'))

LAYERS = layers_svg(dict(
    alt='The seven scoring layers, with the judge-disagreement branch',
    kicker='HOW ONE RESPONSE BECOMES ONE RANGE',
    sub='Blue is deterministic &#183; violet is judged &#183; amber is the disagreement branch',
    names=['Deterministic checks', 'Measurement', 'Evidence package',
           'Two independent judges', 'Disagreement handling', 'Calibration', 'Conformal interval'],
    branch='WHEN THE JUDGES DISAGREE',
    rules=['1 level apart → combine and narrow', '2 apart → widen, and say so',
           '3 or more → no number at all', 'a third judge, and a free review']))

SHARE = share_svg(dict(
    alt='Express Entry invitations by category, 1 January to 19 August 2026',
    kicker='EXPRESS ENTRY INVITATIONS, 1 JAN – 19 AUG 2026',
    sub='Total issued: 119,865',
    rows=[('French-language proficiency', 50500, '#2ec4b6', '42.1 % — the largest category'),
          ('Canadian Experience Class', 49250, '#4aa8ff', ''),
          ('Every other category combined', 20115, '#8b7cf6', '')],
    foot='Source: IRCC ministerial instructions, rounds of invitations.'))

SKILL_CARDS = [
    ('mic', 'teal', 'Speaking', 'Your own recording, replayed with word-level pronunciation, fluency and hesitation marks. Not a score and a sentence of advice.'),
    ('globe', 'sky', 'Listening', 'Quebec French audio, played once, at the real pace. Every accepted test scored on its own scale.'),
    ('book', 'violet', 'Reading', 'The exact question types the exam sets, including the ones candidates lose marks to for technique rather than comprehension.'),
    ('target', 'amber', 'Writing', 'Live checks against the five automatic-zero triggers while you write, then criterion-by-criterion feedback.'),
]

HTML = '''<main id="main">
<div class="wrap">

  <section class="hero">
    <div class="reveal">
      <span class="eyebrow">Live on iOS, Android and the web</span>
      <h1>Know your score <span class="hl">before you book the exam.</span></h1>
      <p class="lede">Four skills, scored the way the real examiner scores them — with an honest range, not a flattering number.</p>
      <p class="muted" style="max-width:56ch"><strong>Your score is produced by software, not by a human examiner.</strong> Speech is transcribed automatically, pronunciation and fluency are scored at the phoneme level, grammar and spelling are checked deterministically, and a language model applies the exam's published criteria. <a href="/scoring/">Exactly how, layer by layer →</a></p>
      <div class="cta-row">
        <a class="btn" href="/which-test/">Which test does Canada accept?</a>
        <a class="btn ghost" href="/calculator/">Work out my CLB / NCLC level</a>
      </div>
      <ul class="ticks">
        <li>Free tier at full scoring quality</li>
        <li>No card required</li>
        <li>English and français</li>
      </ul>
    </div>
    __FAN__
  </section>

  <section class="reveal" id="where">
    <div class="centered">
      <span class="kicker">Start here</span>
      <h2>Where are <span class="hl">you going?</span></h2>
      <p class="muted">Which test you need, and which score counts, follow from the destination. Pick yours.</p>
    </div>
    <div class="grid g4 dest">
      <a class="card card--teal" href="/which-test/">__D_PIN__<h3>Immigrating to Canada</h3><p class="muted">Express Entry and the provincial programmes. Five accepted tests, all read in CLB and NCLC.</p><span class="more">Which test Canada accepts &rarr;</span></a>
      <a class="card card--sky" href="/ielts/">__D_BOOK__<h3>Studying in the UK, Australia, New Zealand or Ireland</h3><p class="muted">University admission takes IELTS Academic — not the version Canada asks for.</p><span class="more">General Training or Academic? &rarr;</span></a>
      <a class="card card--violet" href="/ielts/">__D_GLOBE__<h3>Migrating to the UK, Australia or New Zealand</h3><p class="muted">The UK Skilled Worker route, the Australian points test and New Zealand residence.</p><span class="more">What each route asks for &rarr;</span></a>
      <a class="card card--amber" href="/which-test/#citizenship">__D_SHIELD__<h3>Canadian citizenship</h3><p class="muted">A different requirement from permanent residence, with a different list of accepted proofs.</p><span class="more">What counts for citizenship &rarr;</span></a>
    </div>
  </section>

  <div class="rule"></div>

  <section class="reveal">
    __H_SKILLS__
    <p class="muted" style="max-width:70ch">IELTS practice works today. TCF Canada and TEF Canada are in build — the site says which is which on every page, and the store listings will not describe either one before it ships.</p>
    <div class="grid g4">__SKILL_CARDS__</div>
  </section>

  <section class="feature reveal">
    <div class="mock">__EXAM__<p class="mock__cap"><b>A design of the exam screen — not a screenshot.</b> The French exams it refers to are in build.</p></div>
    <div>
      <span class="kicker">Exam conditions</span>
      <h2>The clock is real. <span class="hl">The audio plays once.</span></h2>
      <p>Readiness can only be observed under the conditions the exam actually imposes. That is a product-engineering problem rather than an intelligence problem, and it is the part a general assistant will never reproduce.</p>
      <ul class="checks">
        <li>Task timings taken from the published specification, not approximated</li>
        <li>Listening audio plays once — no replay, no pause</li>
        <li>The whole exam runs offline, with scoring queued for when you reconnect</li>
        <li>Quebec French voices, for an exam named TCF <em>Canada</em></li>
      </ul>
    </div>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">The method</span>
        <h2>How one response <span class="hl">becomes one range</span></h2>
        <p>Seven layers. The first three are deterministic and cost nothing. The fourth is where two independent judges score against the official criteria. The last three are what make the output honest.</p>
        <ul class="checks">
          <li>Neither judge can see the other's score</li>
          <li>Disagreement widens the range instead of being averaged away</li>
          <li>Calibrated against real graded samples, then published</li>
        </ul>
      </div>
      <figure class="figure">__LAYERS__</figure>
    </div></div>
  </section>

  <div class="rule"></div>

  <div class="rule"></div>

  <section class="reveal" id="whats-coming">
    __H_COMING__
    <div class="grid g2">
      <div class="card card--teal">
        <h3><span class="pill">Available now</span></h3>
        <ul>
          <li>IELTS-oriented practice across speaking, listening, reading and writing</li>
          <li>Real-time pronunciation, fluency and hesitation feedback on your own recording</li>
          <li>Band-criterion feedback in whole integers, as the real Test Report Form reports it</li>
          <li>The reference tools on this site — which test Canada accepts, and the score converter</li>
        </ul>
        <p class="muted">Free on iOS, Android and the web.</p>
      </div>
      <div class="card card--amber">
        <h3><span class="pill build">In build</span></h3>
        <ul>
          <li><strong>TCF Canada</strong> — all four épreuves, Quebec French audio, NCLC scoring, CRS calculator</li>
          <li><strong>TEF Canada</strong></li>
          <li>The full exam offline, with scoring queued for when you reconnect</li>
          <li>Published accuracy statistics and the first fairness audit</li>
        </ul>
        <p class="muted">We do not give a date. A date we could not keep would be worth less than silence.</p>
      </div>
    </div>
    __BADGES__
  </section>

  <div class="rule"></div>

  <section class="reveal" id="canada">
    <div class="centered">
      <span class="kicker">Canada only</span>
      <h2>If you are <span class="hl">going to Canada</span></h2>
      <p class="muted">Everything in this block is Canadian immigration and nothing else. If your destination is the UK, Australia, New Zealand or Ireland, these numbers are not yours &mdash; <a href="/ielts/">that route starts here</a>.</p>
    </div>
  </section>

  <section class="reveal">
    <div class="stats">
      <div class="card"><span class="stat">42.1&nbsp;%</span><div class="stat-lbl">of 2026 Express Entry invitations went to the French category</div></div>
      <div class="card"><span class="stat">141</span><div class="stat-lbl">CRS points between the French and CEC cut-offs</div></div>
      <div class="card"><span class="stat">$390</span><div class="stat-lbl">non-refundable, per sitting</div></div>
      <div class="card"><span class="stat">2027</span><div class="stat-lbl">before TCF re-marking returns</div></div>
    </div>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">One level, four scales</span>
        <h2>IRCC reads CLB and NCLC — <span class="hl">not your band score</span></h2>
        <p>Each accepted test reports on its own scale, and every one of them converts to a single number IRCC actually uses. Your governing level is the <strong>lowest</strong> of your four skills, which is where most candidates lose points they already had.</p>
        <ul class="pills"><li>4</li><li>5</li><li>6</li><li class="on">7</li><li>8</li><li>9</li><li>10</li></ul>
        <p class="muted" style="margin-top:14px">NCLC 7 across all four French skills is worth 50 CRS points if your English is CLB 5 or above.</p>
        <div class="cta-row" style="margin:16px 0 0"><a class="btn" href="/calculator/">Convert my scores</a><a class="btn ghost" href="/which-test/">Which test does Canada accept?</a></div>
      </div>
      <figure class="figure">__LADDER__<figcaption>Speaking, at each level. IELTS General Training and CELPIP-General report a minimum; TEF Canada reports a band. TCF Canada appears at NCLC 7 only — the rest of its chart is left out rather than guessed.</figcaption></figure>
    </div></div>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">Why French</span>
        <h2>The largest category, <span class="hl">by a wide margin</span></h2>
        <p>From 1 January to 19 August 2026, IRCC issued 119,865 Express Entry invitations. <strong>French-language proficiency accounted for 50,500 of them</strong> — more than the Canadian Experience Class, and more than every other category combined.</p>
        <ul class="checks">
          <li>The most recent French-category round cut off at <strong>CRS 382</strong>; the Canadian Experience Class round cut off at <strong>CRS 523</strong> — a 141-point gap</li>
          <li>The last general, no-category draw was 23 April 2024</li>
          <li>NCLC 7 in all four French skills is worth <strong>50 CRS points</strong> if your English is CLB 5 or above, and 25 points if it is CLB 4 or below</li>
        </ul>
        <div class="cta-row" style="margin:18px 0 0"><a class="btn" href="/calculator/">Work out what that gives you</a></div>
      </div>
      <figure class="figure">__SHARE__</figure>
    </div></div>
  </section>

  <section class="reveal">
    __H_TEACH__
    <p>We teach exam technique in full: what each task actually asks for, the hard constraints, the mistakes that score zero regardless of your language level, and where the minutes are worth points.</p>
    <p>We will give you structure — a skeleton you fill with your own content. We will not give you a script to reproduce. The exam scores memorised text at zero, and our own editor is built to flag it while you write.</p>
    <p class="quote">Every point your ability earns, plus the technique most candidates lose. Not a point beyond that.</p>
  </section>

  <div class="rule"></div>

  <section class="reveal">
    <div class="centered">
      <span class="kicker">Get in touch</span>
      <h2>Questions, or <span class="hl">something we got wrong</span></h2>
      <p class="muted">If a number on this site does not match a primary source, tell us and we will correct it.</p>
    </div>
    <div class="contact">
      <div class="card">__C_MAIL__<div class="lbl">Email</div><div class="val"><a href="mailto:admin@selmapp.com">admin@selmapp.com</a></div><div class="sub">We answer within one business day</div></div>
      <div class="card">__C_PHONE__<div class="lbl">Phone</div><div class="val"><a href="tel:+16047178543">+1 (604) 717-8543</a></div><div class="sub">Mon–Fri · 9am–5pm Pacific</div></div>
      <div class="card">__C_PIN__<div class="lbl">Office</div><div class="val">1188 West Pender Street</div><div class="sub">Vancouver, BC, Canada · V6E 0A2</div></div>
    </div>
  </section>

  <section class="reveal">
    <div class="cta-banner">
      <h2>Find out where you stand <span class="hl">before you pay the fee</span></h2>
      <p>The reference tools are free and open. The app is free to start, at full scoring quality.</p>
      <div class="cta-row">
        <a class="btn" href="/calculator/">Work out my CLB / NCLC level</a>
        <a class="btn ghost" href="/which-test/">Which test does Canada accept?</a>
      </div>
    </div>
  </section>

</div>
</main>'''

cards = ''.join(
    '<div class="card card--%s">%s<h3>%s</h3><p class="muted">%s</p></div>' % (tone, cico(i), t, d)
    for i, tone, t, d in SKILL_CARDS)

HTML = (HTML
    .replace('__FAN__', fan(LEFT, CENTRE, RIGHT,
             '<b>Designs of the result screens — not screenshots.</b> The IELTS card in the centre is the exam SELM practises today; the two French cards refer to exams that are in build.'))
    .replace('__EXAM__', EXAM)
    .replace('__LADDER__', LADDER).replace('__LAYERS__', LAYERS)
    .replace('__SKILL_CARDS__', cards).replace('__SHARE__', SHARE)
    .replace('__BADGES__', badges(dict(apple='Download on the', play='Get it on', web1='Or use it', web2='In your browser')))
    .replace('__H_SKILLS__', head('layers', '', 'Four skills, each scored on the exam’s own terms'))
    .replace('__H_COMING__', head('wrench', 'sky', 'What works today, and what is being built'))
    .replace('__H_FRENCH__', head('star', 'rose', 'Why French is worth the effort'))
    .replace('__H_TEACH__', head('book', 'violet', 'What we teach, and what we will not'))
    .replace('__D_PIN__', cico('pin')).replace('__D_BOOK__', cico('book')).replace('__D_GLOBE__', cico('globe')).replace('__D_SHIELD__', cico('shield'))
    .replace('__C_MAIL__', cico('mail')).replace('__C_PHONE__', cico('phone')).replace('__C_PIN__', cico('pin')))

p = os.path.join(REPO, 'index.html')
s = open(p, encoding='utf-8').read()
i, j = s.index('<main id="main">'), s.index('</main>') + 7
open(p, 'w', encoding='utf-8').write(s[:i] + HTML + s[j:])
print('index.html rebuilt —', len(HTML), 'bytes of main')
