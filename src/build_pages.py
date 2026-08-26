# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _guard import confirm as _confirm
_confirm('build_pages.py')
from gfx import layers_svg
REPO = os.path.expanduser('~/mnt/selm/selmapp.com')

EN = layers_svg(dict(
    alt='The seven scoring layers, with the judge-disagreement branch',
    kicker='HOW ONE RESPONSE BECOMES ONE RANGE',
    sub='Blue is deterministic &#183; violet is judged &#183; amber is the disagreement branch',
    names=['Deterministic checks', 'Measurement', 'Evidence package',
           'Two independent judges', 'Disagreement handling', 'Calibration', 'Conformal interval'],
    branch='WHEN THE JUDGES DISAGREE',
    rules=['1 level apart → combine and narrow', '2 apart → widen, and say so',
           '3 or more → no number at all', 'a third judge, and a free review']))

FR = layers_svg(dict(
    alt='Les sept couches de notation, avec la branche du désaccord entre correcteurs',
    kicker='D’UNE RÉPONSE À UN INTERVALLE',
    sub='Bleu&#160;: déterministe &#183; violet&#160;: jugé &#183; ambre&#160;: la branche du désaccord',
    names=['Vérifications déterministes', 'Mesure', 'Dossier de preuves',
           'Deux correcteurs indépendants', 'Gestion du désaccord', 'Calibrage', 'Intervalle conforme'],
    branch='EN CAS DE DÉSACCORD',
    rules=['1 niveau d’écart → combiner', '2 d’écart → élargir, et le dire',
           '3 ou plus → aucun chiffre', 'un 3e correcteur, révision offerte']))

def replace_figure(path, svg):
    p = os.path.join(REPO, path)
    s = open(p, encoding='utf-8').read()
    i = s.index('<figure class="figure figure--tight">')
    j = s.index('</figure>', i) + 9
    cap = re.search(r'<figcaption>(.*?)</figcaption>', s[i:j], re.S).group(1)
    new = ('<div class="band"><figure class="figure">%s<figcaption>%s</figcaption></figure></div>' % (svg, cap))
    s = s[:i] + new + s[j:]
    open(p, 'w', encoding='utf-8').write(s)
    print('figure replaced in', path)

replace_figure('scoring/index.html', EN)
replace_figure('fr/notation/index.html', FR)

# every page: sections fade in, and the reveal class is harmless without JS
for path in ['index.html', 'fr/index.html', 'scoring/index.html', 'fr/notation/index.html',
             'which-test/index.html', 'fr/quel-test/index.html', 'calculator/index.html',
             'fr/calculateur/index.html', 'ielts/index.html', 'legal/index.html']:
    p = os.path.join(REPO, path)
    s = open(p, encoding='utf-8').read()
    n = s.count('<section>')
    s = s.replace('<section>', '<section class="reveal">')
    s = re.sub(r'<section id="([^"]+)">', r'<section id="\1" class="reveal">', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('%-30s sections armed: %d' % (path, n))
