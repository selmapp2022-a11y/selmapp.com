# -*- coding: utf-8 -*-
"""The safety catch on the page generators.

These scripts still emit the PRE-BRAND DARK SITE. Running any of them
against the repository would overwrite the current HTML, relink
`selm.v2.css`, drop the Poppins and Inter font links, and undo commit
`c80fad2` — the whole of STEP 02 — in a single command.

A warning in a README is not a guard, so this is one. Every generator calls
`confirm()` before it opens a file for writing, and without the explicit
acknowledgement below it exits without touching anything.

To run one deliberately:

    SELM_EMIT_PREBRAND_SITE=yes python3 build_home.py

Removing this file, or the `confirm()` calls, is the last step of bringing
the generators forward to emit the v3 brand system — not a shortcut to be
taken before that work is done. What that work involves is in README.md.
"""
import os
import sys

FLAG = 'SELM_EMIT_PREBRAND_SITE'


def confirm(script: str) -> None:
    if os.environ.get(FLAG) == 'yes':
        sys.stderr.write(
            '\n  %s: %s=yes is set. Writing the PRE-BRAND DARK site.\n'
            '  This reverts STEP 02. Check `git diff` before committing.\n\n' % (script, FLAG))
        return
    sys.stderr.write(
        '\n  REFUSING TO WRITE — %s\n\n'
        '  These generators emit the pre-brand dark site. Running this would\n'
        '  overwrite the current HTML and undo commit c80fad2.\n\n'
        '  Nothing has been written. If you truly mean to do it:\n\n'
        '      %s=yes python3 %s\n\n'
        '  See src/README.md for what updating them to the v3 brand involves.\n\n'
        % (script, FLAG, script))
    raise SystemExit(2)
