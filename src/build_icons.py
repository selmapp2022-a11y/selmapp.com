# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _guard import confirm as _confirm
_confirm('build_icons.py')
from parts import head
REPO = os.path.expanduser('~/mnt/selm/selmapp.com')

MAP = {
 'scoring/index.html': [
   ('What actually produces the number', 'layers', ''),
   ('What we promise, and what we do not', 'shield', 'violet'),
   ('One limitation, stated plainly', 'scales', 'amber')],
 'fr/notation/index.html': [
   ('Ce qui produit réellement le chiffre', 'layers', ''),
   ('Ce que nous promettons, et ce que nous ne promettons pas', 'shield', 'violet'),
   ('Une limite, dite clairement', 'scales', 'amber')],
 'which-test/index.html': [
   ('What is not accepted for economic immigration', 'shield', 'rose'),
   ('DELF and DALF — accepted, but for something else', 'book', 'violet'),
   ('Why French is worth the effort', 'star', ''),
   ('What the tests cost, and how often you can retake', 'bars', 'sky'),
   ('Re-marking: read this before you book', 'clock', 'amber')],
 'fr/quel-test/index.html': [
   ("Ce qui n'est pas accepté pour l'immigration économique", 'shield', 'rose'),
   ('Le DELF et le DALF&nbsp;: acceptés, mais pour autre chose', 'book', 'violet'),
   ('Ce que le français vous rapporte', 'star', ''),
   ('Coûts et reprises', 'bars', 'sky'),
   ('Révision de note&nbsp;: à lire avant de réserver', 'clock', 'amber')],
 'calculator/index.html': [
   ('What this does, and what it deliberately does not', 'target', ''),
   ('Where these numbers come from', 'bars', 'sky')],
 'fr/calculateur/index.html': [
   ("Ce que l'outil fait, et ce qu'il ne fait pas volontairement", 'target', ''),
   ("D'où viennent ces chiffres", 'bars', 'sky')],
 'ielts/index.html': [
   ('What SELM does today', 'mic', ''),
   ('What we teach on the writing tasks', 'book', 'violet')],
 'legal/index.html': [
   ('Deleting your account and your data', 'shield', 'rose'),
   ('Company', 'globe', 'sky')],
}
for path, items in MAP.items():
    p = os.path.join(REPO, path)
    s = open(p, encoding='utf-8').read()
    n = 0
    for title, icon, tone in items:
        old = '<h2>%s</h2>' % title
        if old not in s:
            print('  !! not found in %s: %s' % (path, title)); continue
        s = s.replace(old, head(icon, tone, title), 1); n += 1
    open(p, 'w', encoding='utf-8').write(s)
    print('%-30s icons: %d' % (path, n))
