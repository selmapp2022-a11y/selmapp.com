# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _guard import confirm as _confirm
_confirm('build_home.py')
from gfx import interval_svg, ladder_svg
from parts import head, cico, badges, phone

REPO = os.path.expanduser('~/mnt/selm/selmapp.com')

# ---------------------------------------------------------------- English
EN_IV = interval_svg(dict(
    alt='A predicted level shown as a range that straddles the target',
    kicker='PREDICTED RANGE',
    target='target NCLC 7',
    range='NCLC 6 to 8',
    scale='Speaking &#183; 90&#160;% interval &#183; TEF Canada',
    note1='The range straddles the level this candidate needs.',
    note2='The honest reading is undecided — so that is the reading we show.'))
EN_LADDER = ladder_svg(dict(
    alt='What each accepted test asks for at CLB and NCLC levels 4 to 10, speaking',
    kicker='SPEAKING — WHAT EACH TEST ASKS FOR', lvl='CLB / NCLC', atleast='≥',
    foot='Transcribed from the IRCC equivalency charts. TCF Canada appears at NCLC 7 only.'))

EN_PHONE = phone(dict(
    attempt='Practice attempt 3', test='TEF Canada · speaking', to='to',
    sub='90&nbsp;% interval · target NCLC 7', en='en',
    r1='Fluency', r2='Pronunciation', r3='Range of structures',
    note='The two judges disagreed by one level, so this range is a level wider than usual.',
    cap='<b>A design of the result card — not a screenshot.</b> The French exams it refers to are in build.'))

EN = '''<main id="main">
<div class="wrap">

  <section class="hero">
    <div class="reveal">
      <span class="eyebrow">Live on iOS, Android and the web</span>
      <h1>Know your score before you book the exam.</h1>
      <p class="lede">Four skills, scored the way the real examiner scores them — with an honest range, not a flattering number.</p>
      <p class="muted" style="max-width:56ch"><strong>Your score is produced by software, not by a human examiner.</strong> Speech is transcribed automatically, pronunciation and fluency are scored at the phoneme level, grammar and spelling are checked deterministically, and a language model applies the exam's published criteria. <a href="/scoring/">Exactly how, layer by layer →</a></p>
      <div class="cta-row">
        <a class="btn" href="/which-test/">Which test does Canada accept?</a>
        <a class="btn ghost" href="/calculator/">Work out my CLB / NCLC level</a>
      </div>
    </div>
    __PHONE__
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
        <span class="kicker">The output</span>
        <h2>A range, not a single number</h2>
        <p>Every predicted score comes with its uncertainty attached. When our two independent judges disagree, the range widens and we say so. When they disagree badly, no number is shown at all until a third judge rules.</p>
        <p class="muted">The interval is the output. There is no single best guess hiding behind it — a point estimate nobody can stand behind is exactly what makes a scoring product sound confident and be wrong.</p>
        <div class="cta-row" style="margin:16px 0 0"><a class="btn ghost" href="/scoring/">How the score is built →</a></div>
      </div>
      <figure class="figure">__EN_IV__</figure>
    </div></div>
  </section>

  <section class="reveal">
    __H_EXAM__
    <p>You never see your written script. You never hear your recording back. From 1 September 2026, TCF candidates will not be able to request a re-mark at all until autumn 2027 — France Éducation international has announced the suspension for modernisation. You find out whether you were ready after you have paid, sat, and waited.</p>
    <p>SELM exists to answer one question before that happens: <strong>am I ready to sit this exam?</strong></p>
  </section>

  <section class="reveal">
    __H_BUILD__
    <div class="grid g3">
      <div class="card card--teal">
        __C_TARGET__
        <h3>A number, with its uncertainty attached</h3>
        <p class="muted">Every predicted score comes as a range with a stated confidence level, not a single digit. When the two judges disagree, the range widens. When they disagree badly, no number is shown until a third judge rules.</p>
      </div>
      <div class="card card--amber">
        __C_CLOCK__
        <h3>Real exam conditions</h3>
        <p class="muted">Audio plays once. The clock is real. The interface matches the official one. That is a product problem, not an intelligence problem — and it is the condition under which readiness can actually be observed.</p>
      </div>
      <div class="card card--violet">
        __C_SHIELD__
        <h3>Accuracy we publish</h3>
        <p class="muted">We measure our own error against real official score reports and publish the figure, including a fairness audit by candidate first language — including where we perform worse.</p>
      </div>
    </div>
    <p class="muted">We do not claim to predict your official result. We never write &ldquo;guaranteed&rdquo;, and we never claim to be 100&nbsp;% accurate — no one honestly can, and a product that says so is telling you something about itself. <a href="/scoring/">How the score is built →</a></p>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">One level, four scales</span>
        <h2>IRCC reads CLB and NCLC — not your band score</h2>
        <p>Each accepted test reports on its own scale, and every one of them converts to a single number IRCC actually uses. Your governing level is the <strong>lowest</strong> of your four skills, which is where most candidates lose points they already had.</p>
        <p class="muted">NCLC 7 across all four French skills is worth 50 CRS points if your English is CLB 5 or above.</p>
        <div class="cta-row" style="margin:16px 0 0"><a class="btn" href="/calculator/">Convert my scores</a><a class="btn ghost" href="/which-test/">Which test does Canada accept?</a></div>
      </div>
      <figure class="figure">__EN_LADDER__<figcaption>Speaking, at each level. IELTS General Training and CELPIP-General report a minimum; TEF Canada reports a band. TCF Canada appears at NCLC 7 only — the rest of its chart is left out rather than guessed.</figcaption></figure>
    </div></div>
  </section>

  <section class="reveal">
    __H_TEACH__
    <p>We teach exam technique in full: what each task actually asks for, the hard constraints, the mistakes that score zero regardless of your language level, and where the minutes are worth points.</p>
    <p>We will give you structure — a skeleton you fill with your own content. We will not give you a script to reproduce. The exam scores memorised text at zero, and our own editor is built to flag it while you write.</p>
    <p class="quote">Every point your ability earns, plus the technique most candidates lose. Not a point beyond that.</p>
  </section>

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

  <section class="reveal">
    __H_FRENCH__
    <p>From 1 January to 19 August 2026, IRCC issued 119,865 Express Entry invitations. <strong>French-language proficiency accounted for 50,500 of them — 42.1&nbsp;%</strong>, the single largest category, ahead of the Canadian Experience Class. The most recent French-category round cut off at <strong>CRS 382</strong>; the most recent Canadian Experience Class round cut off at <strong>CRS 523</strong>. The last general, no-category draw was 23 April 2024.</p>
    <p>Demonstrating NCLC 7 across all four French skills is worth <strong>50 CRS points</strong> if your English is CLB 5 or above, and <strong>25 points</strong> if your English is CLB 4 or below — or if you did not take an English test at all.</p>
    <div class="cta-row"><a class="btn" href="/calculator/">Work out what that gives you</a></div>
  </section>

</div>
</main>'''

EN = (EN.replace('__PHONE__', EN_PHONE)
        .replace('__EN_IV__', EN_IV)
        .replace('__EN_LADDER__', EN_LADDER)
        .replace('__BADGES__', badges(dict(apple='Download on the', play='Get it on', web1='Or use it', web2='In your browser')))
        .replace('__H_EXAM__', head('clock', 'amber', 'The exam tells you almost nothing'))
        .replace('__H_BUILD__', head('target', '', 'What we are building the company around'))
        .replace('__H_TEACH__', head('book', 'violet', 'What we teach, and what we will not'))
        .replace('__H_COMING__', head('wrench', 'sky', 'What works today, and what is being built'))
        .replace('__H_FRENCH__', head('star', 'rose', 'Why French is worth the effort'))
        .replace('__C_TARGET__', cico('target'))
        .replace('__C_CLOCK__', cico('clock'))
        .replace('__C_SHIELD__', cico('shield')))

def swap_main(path, new):
    p = os.path.join(REPO, path)
    s = open(p, encoding='utf-8').read()
    i, j = s.index('<main id="main">'), s.index('</main>') + 7
    s = s[:i] + new + s[j:]
    open(p, 'w', encoding='utf-8').write(s)
    print('rewrote', path, len(new), 'bytes of main')

swap_main('index.html', EN)
