# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gfx import ladder_svg, layers_svg, share_svg
from parts import head, cico, badges, phone, phone_skills, phone_decision, phone_exam, fan
REPO = os.path.expanduser('~/mnt/selm/selmapp.com')

def body(m):
    i = m.index('<div class="phone">'); j = m.index('</div>\n  <p class="mock__cap">')
    return m[i:j+6]

CENTRE = body(phone(dict(
    attempt='Tentative d’entraînement 3', test='IELTS General Training · expression orale',
    skill='Expression orale', range='Bande 6 à 7', band=(6, 7), target=7,
    marks=[4, 5, 6, 7, 8, 9],
    sub='intervalle à 90&nbsp;% · cible bande 7', en='',
    r1='Aisance et cohérence', r2='Prononciation', r3='Étendue lexicale',
    note='Bandes entières uniquement, comme le Test Report Form les rapporte.',
    cap='')))

LEFT = phone_skills(dict(bar='Diagnostic', head='TCF Canada · où vous en êtes', title='Quatre compétences',
    rows=[('mic','Expression orale','Production orale','NCLC 6–8'),
          ('globe','Compréhension orale','Écoute','NCLC 7'),
          ('book','Compréhension écrite','Lecture','NCLC 6'),
          ('target','Expression écrite','Production écrite','NCLC 5–7')]))

RIGHT = phone_decision(dict(bar='État de préparation', head='Prêt à réserver&nbsp;?', verdict='Pas encore',
    sub='Votre intervalle le plus bas est NCLC 5 à 7. Il vous faut 7 dans les quatre.',
    steps=[('book','Structure de la tâche 3','Trois séances'),
           ('clock','Écriture chronométrée','Deux fois par semaine'),
           ('scales','Nouveau test','Dans trois semaines')],
    note='Une candidate à qui l’on dit d’attendre n’a pas dépensé 390&nbsp;$ pour une session à laquelle elle n’était pas prête.'))

EXAM = phone_exam(dict(bar='Examen blanc', head='TCF Canada · compréhension orale',
    title='Section 2', clock='04:12', progress='Question 14 sur 39',
    r1='L’audio passe une seule fois', r1s='Aucune réécoute, exactement comme à l’examen',
    r2='Hors ligne', r2s='L’examen complet fonctionne sans connexion',
    note='L’interface, les minutages et l’écoute unique correspondent à l’instrument officiel.'))

LADDER = ladder_svg(dict(
    alt='Ce que chaque test accepté exige aux niveaux NCLC et CLB 4 à 10, expression orale',
    kicker='EXPRESSION ORALE — CE QUE CHAQUE TEST EXIGE', lvl='NCLC / CLB', atleast='≥',
    foot='Transcrit des tables d’équivalence d’IRCC. Le TCF Canada ne figure qu’au NCLC 7.'))

LAYERS = layers_svg(dict(
    alt='Les sept couches de notation, avec la branche du désaccord entre correcteurs',
    kicker='D’UNE RÉPONSE À UN INTERVALLE',
    sub='Bleu&#160;: déterministe &#183; violet&#160;: jugé &#183; ambre&#160;: la branche du désaccord',
    names=['Vérifications déterministes', 'Mesure', 'Dossier de preuves',
           'Deux correcteurs indépendants', 'Gestion du désaccord', 'Calibrage', 'Intervalle conforme'],
    branch='EN CAS DE DÉSACCORD',
    rules=['1 niveau d’écart → combiner', '2 d’écart → élargir, et le dire',
           '3 ou plus → aucun chiffre', 'un 3e correcteur, révision offerte']))

SHARE = share_svg(dict(
    alt='Invitations d’Entrée express par catégorie, 1er janvier au 19 août 2026',
    kicker='INVITATIONS D’ENTRÉE EXPRESS, 1ER JANV. – 19 AOÛT 2026',
    sub='Total émis&#160;: 119 865',
    rows=[('Compétence en français', 50500, '#2ec4b6', '42,1 % — la plus grande catégorie'),
          ('Catégorie de l’expérience canadienne', 49250, '#4aa8ff', ''),
          ('Toutes les autres catégories réunies', 20115, '#8b7cf6', '')],
    foot='Source&#160;: instructions ministérielles d’IRCC, rondes d’invitations.'))

SKILLS = [
    ('mic', 'teal', 'Expression orale', 'Votre propre enregistrement, réécouté avec la prononciation, l’aisance et les hésitations annotées mot à mot. Pas un score suivi d’une phrase de conseil.'),
    ('globe', 'sky', 'Compréhension orale', 'Audio en français québécois, passé une seule fois, au rythme réel. Chaque test accepté noté sur sa propre échelle.'),
    ('book', 'violet', 'Compréhension écrite', 'Exactement les types de questions posés par l’examen, y compris ceux où les points se perdent par technique plutôt que par compréhension.'),
    ('target', 'amber', 'Expression écrite', 'Vérification en direct des cinq déclencheurs de note zéro pendant que vous écrivez, puis un retour critère par critère.'),
]

HTML = '''<main id="main">
<div class="wrap">

  <section class="hero">
    <div class="reveal">
      <span class="eyebrow">Sur iOS, Android et le Web</span>
      <h1>Connaissez votre score <span class="hl">avant de réserver l'examen.</span></h1>
      <p class="lede">Quatre compétences, corrigées comme un vrai examinateur les corrige — avec un intervalle honnête, pas un chiffre flatteur.</p>
      <p class="muted" style="max-width:56ch"><strong>Votre score est produit par un logiciel, et non par un examinateur humain.</strong> La parole est transcrite automatiquement, la prononciation et la fluidité sont notées au niveau du phonème, la grammaire et l'orthographe sont vérifiées de façon déterministe, et un modèle de langue applique les critères publiés de l'examen. <a href="/fr/notation/">Exactement comment, couche par couche →</a></p>
      <div class="cta-row">
        <a class="btn" href="/fr/quel-test/">Quel test le Canada accepte-t-il&nbsp;?</a>
        <a class="btn ghost" href="/fr/calculateur/">Calculer mon niveau</a>
      </div>
      <ul class="ticks">
        <li>Version gratuite, qualité de notation complète</li>
        <li>Sans carte bancaire</li>
        <li>English et français</li>
      </ul>
    </div>
    __FAN__
  </section>

  <section class="reveal" id="destination">
    <div class="centered">
      <span class="kicker">Commencez ici</span>
      <h2>Où <span class="hl">allez-vous&nbsp;?</span></h2>
      <p class="muted">Le test dont vous avez besoin, et la note qui compte, découlent de la destination. Choisissez la vôtre.</p>
    </div>
    <div class="grid g4 dest">
      <a class="card card--teal" href="/fr/quel-test/">__D_PIN__<h3>Immigrer au Canada</h3><p class="muted">Entrée express et programmes provinciaux. Cinq tests acceptés, tous lus en NCLC et CLB.</p><span class="more">Quel test le Canada accepte &rarr;</span></a>
      <a class="card card--sky" href="/ielts/">__D_BOOK__<h3>Étudier au Royaume-Uni, en Australie, en Nouvelle-Zélande ou en Irlande</h3><p class="muted">L’admission universitaire exige l’IELTS Academic, pas la version canadienne. <em>Page en anglais.</em></p><span class="more">General Training ou Academic&nbsp;? &rarr;</span></a>
      <a class="card card--violet" href="/ielts/">__D_GLOBE__<h3>Immigrer au Royaume-Uni, en Australie ou en Nouvelle-Zélande</h3><p class="muted">Skilled Worker britannique, test à points australien, résidence néo-zélandaise. <em>Page en anglais.</em></p><span class="more">Ce que chaque voie demande &rarr;</span></a>
      <a class="card card--amber" href="/fr/quel-test/">__D_SHIELD__<h3>Citoyenneté canadienne</h3><p class="muted">Une exigence différente de la résidence permanente, avec une autre liste de preuves acceptées.</p><span class="more">Ce qui compte pour la citoyenneté &rarr;</span></a>
    </div>
  </section>

  <section class="reveal" id="etat">
    __H_ETAT__
    <div class="callout warn">
      <p><strong>Le simulateur TCF Canada n'est pas encore disponible, et l'application est actuellement en anglais.</strong></p>
      <p class="muted" style="margin-bottom:0">Nous le disons ici plutôt que de vous laisser le découvrir après l'installation.</p>
    </div>
    <div class="tbl-scroll">
      <table>
        <thead><tr><th>État</th><th>Ce que cela couvre</th></tr></thead>
        <tbody>
          <tr><td><span class="pill">Disponible</span></td><td>Les outils de référence de ce site, en français&nbsp;: quel test le Canada accepte, et le calculateur d'équivalence NCLC / CLB. L'application d'entraînement, dont l'interface est en anglais.</td></tr>
          <tr><td><span class="pill build">En construction</span></td><td>Le TCF Canada complet&nbsp;: les quatre épreuves, l'audio en français québécois, la notation NCLC et le calculateur CRS. Puis le TEF Canada.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted">Nous ne donnons pas de date. Une date que nous ne pourrions pas tenir vaudrait moins que le silence.</p>
    __BADGES__
  </section>

  <div class="rule"></div>

  <section class="reveal">
    __H_SKILLS__
    <div class="grid g4">__SKILLS__</div>
  </section>

  <section class="feature reveal">
    <div class="mock">__EXAM__<p class="mock__cap"><b>Une maquette de l'écran d'examen, pas une capture d'écran.</b> Les examens français concernés sont en construction.</p></div>
    <div>
      <span class="kicker">Conditions d'examen</span>
      <h2>Le chrono est réel. <span class="hl">L'audio passe une fois.</span></h2>
      <p>On ne peut observer l'état de préparation que dans les conditions que l'examen impose réellement. C'est un problème d'ingénierie produit, pas un problème d'intelligence — et c'est la partie qu'un assistant généraliste ne reproduira jamais.</p>
      <ul class="checks">
        <li>Minutages repris de la spécification publiée, non approximés</li>
        <li>L'audio de compréhension passe une seule fois — aucune réécoute, aucune pause</li>
        <li>L'examen complet fonctionne hors ligne, la notation étant mise en file d'attente</li>
        <li>Voix en français québécois, pour un examen qui s'appelle TCF <em>Canada</em></li>
      </ul>
    </div>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">La méthode</span>
        <h2>D'une réponse <span class="hl">à un intervalle</span></h2>
        <p>Sept couches. Les trois premières sont déterministes et ne coûtent rien. La quatrième est celle où deux correcteurs indépendants évaluent selon les critères officiels. Les trois dernières sont celles qui rendent le résultat honnête.</p>
        <ul class="checks">
          <li>Aucun correcteur ne voit la note de l'autre</li>
          <li>Le désaccord élargit l'intervalle au lieu d'être noyé dans une moyenne</li>
          <li>Calibré sur des copies réellement notées, puis publié</li>
        </ul>
      </div>
      <figure class="figure">__LAYERS__</figure>
    </div></div>
  </section>

  <div class="rule"></div>

  <section class="reveal" id="canada">
    <div class="centered">
      <span class="kicker">Canada uniquement</span>
      <h2>Si vous allez <span class="hl">au Canada</span></h2>
      <p class="muted">Tout ce bloc porte sur l’immigration canadienne et sur rien d’autre. Si votre destination est le Royaume-Uni, l’Australie, la Nouvelle-Zélande ou l’Irlande, ces chiffres ne sont pas les vôtres &mdash; <a href="/ielts/">cette voie commence ici</a>.</p>
    </div>
  </section>

  <section class="reveal">
    <div class="stats">
      <div class="card"><span class="stat">42,1&nbsp;%</span><div class="stat-lbl">des invitations d'Entrée express 2026 sont allées à la catégorie francophone</div></div>
      <div class="card"><span class="stat">141</span><div class="stat-lbl">points CRS d'écart entre le seuil francophone et celui de l'expérience canadienne</div></div>
      <div class="card"><span class="stat">390&nbsp;$</span><div class="stat-lbl">non remboursables, par session</div></div>
      <div class="card"><span class="stat">2027</span><div class="stat-lbl">avant le retour de la révision de note du TCF</div></div>
    </div>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">Un niveau, quatre échelles</span>
        <h2>IRCC lit le NCLC et le CLB, <span class="hl">pas votre note brute</span></h2>
        <p>Chaque test accepté rend ses résultats sur sa propre échelle, et toutes se convertissent vers le seul chiffre qu'IRCC utilise. Votre niveau retenu est le <strong>plus faible</strong> de vos quatre compétences&nbsp;: c'est là que la plupart des candidats perdent des points qu'ils avaient déjà.</p>
        <ul class="pills"><li>4</li><li>5</li><li>6</li><li class="on">7</li><li>8</li><li>9</li><li>10</li></ul>
        <p class="muted" style="margin-top:14px">Le NCLC 7 dans les quatre compétences vaut 50 points CRS si votre anglais atteint le CLB 5.</p>
        <div class="cta-row" style="margin:16px 0 0"><a class="btn" href="/fr/calculateur/">Calculer mon niveau</a><a class="btn ghost" href="/fr/quel-test/">Quel test le Canada accepte-t-il&nbsp;?</a></div>
      </div>
      <figure class="figure">__LADDER__<figcaption>L'expression orale, à chaque niveau. L'IELTS General Training et le CELPIP-général indiquent un minimum&nbsp;; le TEF Canada indique une plage. Le TCF Canada ne figure qu'au NCLC 7 — le reste de sa table est omis plutôt que deviné.</figcaption></figure>
    </div></div>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">Pourquoi le français</span>
        <h2>La plus grande catégorie, <span class="hl">de loin</span></h2>
        <p>Du 1<sup>er</sup> janvier au 19 août 2026, IRCC a émis 119&nbsp;865 invitations dans Entrée express. <strong>La catégorie « compétence en français » en représente 50&nbsp;500</strong> — plus que la catégorie de l'expérience canadienne, et plus que toutes les autres catégories réunies.</p>
        <ul class="checks">
          <li>La ronde francophone la plus récente s'est arrêtée à <strong>382 points</strong>; celle de l'expérience canadienne, à <strong>523</strong> — un écart de 141 points</li>
          <li>La dernière ronde générale, sans catégorie, remonte au 23 avril 2024</li>
          <li>Le NCLC 7 dans les quatre compétences vaut <strong>50 points CRS</strong> si votre anglais atteint le CLB 5, et 25 points s'il se situe au CLB 4 ou moins</li>
        </ul>
        <div class="cta-row" style="margin:18px 0 0"><a class="btn" href="/fr/calculateur/">Calculer mon niveau</a></div>
      </div>
      <figure class="figure">__SHARE__</figure>
    </div></div>
  </section>

  <div class="rule"></div>

  <section class="reveal">
    __H_TEACH__
    <p>Nous enseignons la technique d'examen sans réserve&nbsp;: ce que chaque épreuve demande vraiment, les contraintes strictes, les erreurs qui valent zéro quel que soit votre niveau, et où les minutes rapportent des points.</p>
    <p>Nous vous donnerons une structure à remplir avec vos propres idées. Nous ne vous donnerons pas un texte à réciter&nbsp;: l'examen attribue la note la plus basse au texte appris par cœur.</p>
    <p class="quote">Chaque point que votre niveau mérite, plus la technique que la plupart des candidats perdent. Pas un point de plus.</p>
  </section>

  <div class="rule"></div>

  <section class="reveal">
    <div class="centered">
      <span class="kicker">Nous joindre</span>
      <h2>Une question, ou <span class="hl">une erreur à signaler</span></h2>
      <p class="muted">Si un chiffre de ce site ne correspond pas à une source primaire, dites-le-nous et nous le corrigerons.</p>
    </div>
    <div class="contact">
      <div class="card">__C_MAIL__<div class="lbl">Courriel</div><div class="val"><a href="mailto:admin@selmapp.com">admin@selmapp.com</a></div><div class="sub">Réponse sous un jour ouvrable</div></div>
      <div class="card">__C_PHONE__<div class="lbl">Téléphone</div><div class="val"><a href="tel:+16047178543">+1 (604) 717-8543</a></div><div class="sub">Lun–ven · 9h–17h, heure du Pacifique</div></div>
      <div class="card">__C_PIN__<div class="lbl">Bureau</div><div class="val">1188 West Pender Street</div><div class="sub">Vancouver, C.-B., Canada · V6E 0A2</div></div>
    </div>
  </section>

  <section class="reveal">
    <div class="cta-banner">
      <h2>Sachez où vous en êtes <span class="hl">avant de payer les frais</span></h2>
      <p>Les outils de référence sont gratuits et ouverts. L'application est gratuite au départ, à pleine qualité de notation.</p>
      <div class="cta-row">
        <a class="btn" href="/fr/calculateur/">Calculer mon niveau</a>
        <a class="btn ghost" href="/fr/quel-test/">Quel test le Canada accepte-t-il&nbsp;?</a>
      </div>
    </div>
  </section>

</div>
</main>'''

cards = ''.join('<div class="card card--%s">%s<h3>%s</h3><p class="muted">%s</p></div>' % (tone, cico(i), t, d)
                for i, tone, t, d in SKILLS)

HTML = (HTML
    .replace('__FAN__', fan(LEFT, CENTRE, RIGHT,
             '<b>Maquettes des écrans de résultat — pas des captures.</b> La carte IELTS au centre correspond à l’examen que SELM entraîne aujourd’hui&nbsp;; les deux cartes françaises renvoient à des examens en construction.'))
    .replace('__EXAM__', EXAM).replace('__LADDER__', LADDER)
    .replace('__LAYERS__', LAYERS).replace('__SHARE__', SHARE)
    .replace('__SKILLS__', cards)
    .replace('__BADGES__', badges(dict(apple='Télécharger dans l’', play='Disponible sur', web1='Ou utilisez-le', web2='Dans le navigateur')))
    .replace('__H_ETAT__', head('wrench', 'sky', 'Où en est le produit'))
    .replace('__H_SKILLS__', head('layers', '', 'Quatre compétences, chacune notée selon les règles de l’examen'))
    .replace('__H_TEACH__', head('book', 'violet', 'Ce que nous enseignerons, et ce que nous refuserons d’enseigner'))
    .replace('__D_PIN__', cico('pin')).replace('__D_BOOK__', cico('book')).replace('__D_GLOBE__', cico('globe')).replace('__D_SHIELD__', cico('shield'))
    .replace('__C_MAIL__', cico('mail')).replace('__C_PHONE__', cico('phone')).replace('__C_PIN__', cico('pin')))

p = os.path.join(REPO, 'fr/index.html')
s = open(p, encoding='utf-8').read()
i, j = s.index('<main id="main">'), s.index('</main>') + 7
open(p, 'w', encoding='utf-8').write(s[:i] + HTML + s[j:])
print('fr/index.html rebuilt —', len(HTML), 'bytes of main')
