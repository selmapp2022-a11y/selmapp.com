# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gfx import interval_svg, ladder_svg
from parts import head, cico, badges, phone
REPO = os.path.expanduser('~/mnt/selm/selmapp.com')

FR_IV = interval_svg(dict(
    alt='Un niveau prédit affiché sous forme d’intervalle qui traverse le seuil visé',
    kicker='INTERVALLE PRÉDIT',
    target='cible NCLC 7',
    range='NCLC 6 à 8',
    scale='Expression orale &#183; intervalle à 90&#160;% &#183; TEF Canada',
    note1='L’intervalle traverse le niveau requis par cette candidate.',
    note2='La lecture honnête est indécise — c’est donc celle que nous affichons.'))
FR_LADDER = ladder_svg(dict(
    alt='Ce que chaque test accepté exige aux niveaux NCLC et CLB 4 à 10, expression orale',
    kicker='EXPRESSION ORALE — CE QUE CHAQUE TEST EXIGE', lvl='NCLC / CLB', atleast='≥',
    foot='Transcrit des tables d’équivalence d’IRCC. Le TCF Canada ne figure qu’au NCLC 7.'))
FR_PHONE = phone(dict(
    attempt='Tentative d’entraînement 3', test='TEF Canada · expression orale', to='à',
    sub='intervalle à 90&nbsp;% · cible NCLC 7', en='',
    r1='Aisance', r2='Prononciation', r3='Variété des structures',
    note='Les deux correcteurs ont divergé d’un niveau&nbsp;: l’intervalle est donc plus large que d’habitude.',
    cap='<b>Une maquette de la carte de résultat, pas une capture d’écran.</b> Les examens français concernés sont en construction.'))

FR = '''<main id="main">
<div class="wrap">

  <section class="hero">
    <div class="reveal">
      <span class="eyebrow">Sur iOS, Android et le Web</span>
      <h1>Connaissez votre score avant de réserver l'examen.</h1>
      <p class="lede">Quatre compétences, corrigées comme un vrai examinateur les corrige — avec un intervalle honnête, pas un chiffre flatteur.</p>
      <p class="muted" style="max-width:56ch"><strong>Votre score est produit par un logiciel, et non par un examinateur humain.</strong> La parole est transcrite automatiquement, la prononciation et la fluidité sont notées au niveau du phonème, la grammaire et l'orthographe sont vérifiées de façon déterministe, et un modèle de langue applique les critères publiés de l'examen. <a href="/fr/notation/">Exactement comment, couche par couche →</a></p>
      <div class="cta-row">
        <a class="btn" href="/fr/quel-test/">Quel test le Canada accepte-t-il&nbsp;?</a>
        <a class="btn ghost" href="/fr/calculateur/">Calculer mon niveau</a>
      </div>
    </div>
    __PHONE__
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
        <span class="kicker">Le résultat</span>
        <h2>Un intervalle, pas un chiffre unique</h2>
        <p>Chaque score prédit sera accompagné de son incertitude. Quand nos deux correcteurs indépendants seront en désaccord, l'intervalle s'élargira et nous le dirons. En cas de désaccord important, <strong>aucun chiffre ne sera affiché</strong> avant l'arbitrage d'un troisième correcteur.</p>
        <p class="muted">L'intervalle est le résultat. Aucune estimation ponctuelle ne se cache derrière&nbsp;: c'est précisément ce genre de chiffre unique, que personne ne peut assumer, qui rend ces produits sûrs d'eux et faux.</p>
        <div class="cta-row" style="margin:16px 0 0"><a class="btn ghost" href="/fr/notation/">Comment le score est construit →</a></div>
      </div>
      <figure class="figure">__FR_IV__</figure>
    </div></div>
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

  <section class="reveal">
    __H_EXAM__
    <p>Vous ne voyez jamais votre copie. Vous n'entendez jamais votre enregistrement. Et à partir du 1<sup>er</sup> septembre 2026, les candidats au TCF ne pourront plus demander de révision de note&nbsp;: France Éducation international suspendra le service jusqu'à l'automne 2027.</p>
    <p>Vous payez 390&nbsp;$&nbsp;CA, vous passez l'examen, et vous apprenez après coup si vous étiez prêt. SELM existe pour répondre à une seule question avant ce moment-là&nbsp;: <strong>suis-je prêt à passer cet examen&nbsp;?</strong></p>
  </section>

  <section class="reveal">
    <div class="band"><div class="band__grid wide">
      <div>
        <span class="kicker">Un niveau, quatre échelles</span>
        <h2>IRCC lit le NCLC et le CLB, pas votre note brute</h2>
        <p>Chaque test accepté rend ses résultats sur sa propre échelle, et toutes se convertissent vers le seul chiffre qu'IRCC utilise. Votre niveau retenu est le <strong>plus faible</strong> de vos quatre compétences&nbsp;: c'est là que la plupart des candidats perdent des points qu'ils avaient déjà.</p>
        <p class="muted">Le NCLC 7 dans les quatre compétences vaut 50 points CRS si votre anglais atteint le CLB 5.</p>
        <div class="cta-row" style="margin:16px 0 0"><a class="btn" href="/fr/calculateur/">Calculer mon niveau</a><a class="btn ghost" href="/fr/quel-test/">Quel test le Canada accepte-t-il&nbsp;?</a></div>
      </div>
      <figure class="figure">__FR_LADDER__<figcaption>L'expression orale, à chaque niveau. L'IELTS General Training et le CELPIP-général indiquent un minimum&nbsp;; le TEF Canada indique une plage. Le TCF Canada ne figure qu'au NCLC 7 — le reste de sa table est omis plutôt que deviné.</figcaption></figure>
    </div></div>
  </section>

  <section class="reveal">
    __H_FRENCH__
    <p>Du 1<sup>er</sup> janvier au 19 août 2026, IRCC a émis 119&nbsp;865 invitations dans Entrée express. <strong>La catégorie « compétence en français » en représente 50&nbsp;500, soit 42,1&nbsp;%</strong> — la plus importante de toutes, devant la catégorie de l'expérience canadienne.</p>
    <p>La ronde francophone la plus récente s'est arrêtée à <strong>382 points</strong>; celle de l'expérience canadienne, à <strong>523</strong>. La dernière ronde générale, sans catégorie, remonte au 23 avril 2024.</p>
    <p>Démontrer le NCLC 7 dans les quatre compétences vaut <strong>50 points</strong> si votre anglais atteint le CLB 5, et <strong>25 points</strong> si votre anglais se situe au CLB 4 ou moins — ou si vous n'avez pas passé de test d'anglais.</p>
    <div class="cta-row">
      <a class="btn" href="/fr/calculateur/">Calculer mon niveau</a>
      <a class="btn ghost" href="/fr/quel-test/">Quel test le Canada accepte-t-il&nbsp;?</a>
    </div>
  </section>

  <div class="rule"></div>

  <section class="reveal">
    __H_TEACH__
    <p>Nous enseignons la technique d'examen sans réserve&nbsp;: ce que chaque épreuve demande vraiment, les contraintes strictes, les erreurs qui valent zéro quel que soit votre niveau, et où les minutes rapportent des points.</p>
    <p>Nous vous donnerons une structure à remplir avec vos propres idées. Nous ne vous donnerons pas un texte à réciter&nbsp;: l'examen attribue la note la plus basse au texte appris par cœur.</p>
    <p class="quote">Chaque point que votre niveau mérite, plus la technique que la plupart des candidats perdent. Pas un point de plus.</p>
  </section>

</div>
</main>'''

FR = (FR.replace('__PHONE__', FR_PHONE)
        .replace('__FR_IV__', FR_IV)
        .replace('__FR_LADDER__', FR_LADDER)
        .replace('__BADGES__', badges(dict(apple='Télécharger dans l’', play='Disponible sur', web1='Ou utilisez-le', web2='Dans le navigateur')))
        .replace('__H_ETAT__', head('wrench', 'sky', 'Où en est le produit'))
        .replace('__H_EXAM__', head('clock', 'amber', 'L’examen ne vous dit presque rien'))
        .replace('__H_FRENCH__', head('star', 'rose', 'Ce que le français vous rapporte réellement'))
        .replace('__H_TEACH__', head('book', 'violet', 'Ce que nous enseignerons, et ce que nous refuserons d’enseigner')))

p = os.path.join(REPO, 'fr/index.html')
s = open(p, encoding='utf-8').read()
i, j = s.index('<main id="main">'), s.index('</main>') + 7
open(p, 'w', encoding='utf-8').write(s[:i] + FR + s[j:])
print('rewrote fr/index.html', len(FR))
