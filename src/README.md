# Page generators — archived source, not a build step

These eight scripts generated the HTML in this repository. Until 25 August 2026
they lived only in an untracked folder on one laptop: the repository held the
output and nothing held the source. That is why they are here.

## They now refuse to run

As of 27 August 2026 every generator calls `_guard.confirm()` before it opens
anything for writing, and exits with status 2 if it is not explicitly
acknowledged. An accidental invocation writes nothing.

To run one deliberately — which reverts STEP 02 — the flag is
`SELM_EMIT_PREBRAND_SITE=yes`.

## Read this before running any of them

**They predate the STEP-02 brand pass and they still emit the dark navy site.**
Running `build_home.py` today would overwrite `index.html` with the pre-brand
version, link `selm.v2.css`, drop the Poppins and Inter font links, and undo
commit `c80fad2` in one command.

So they are committed as the **source of record**, not as a working build. The
current HTML in this repository is the truth. Bringing the generators forward
to emit the v3 brand system is a real task and it has not been done.

| file | emits |
|---|---|
| `build_home.py` | `index.html` |
| `build_home_fr.py` | `fr/index.html` |
| `build_pages.py` | the inner pages |
| `build_icons.py` | the icon set |
| `home_en.py`, `home_fr2.py` | page copy, per language |
| `parts.py` | shared components — header, footer, the phone mockup |
| `gfx.py` | the inline SVG diagrams |

## What updating them would involve

Not done, and deliberately out of scope for step 06. For whoever picks it up:

1. `parts.py` — `head()` links `selm.v2.css` and emits no font links. It needs
   `selm.v3.css` plus the Poppins and Inter `<link>` tags.
2. `gfx.py` — every diagram is drawn light-on-dark: `#e8f0f7` text, `#b9cbdb`
   and `#8ba3b8` rules, white washes. On a white card they are invisible. The
   colour map that was applied to the committed HTML is in
   `SELM-STEP-02-report.md` §5 item 1.
3. Sky `#4aa8ff`, violet `#8b7cf6` and rose `#f2748a` appear throughout and are
   not in the published palette. All three fold to navy.
4. Teal and amber must not appear on any `<text>` element: they measure 2.04:1
   and 1.90:1 on the page background.
5. One caption in `home_en.py` / `home_fr2.py` names the old diagram colours and
   has to be reworded, as it was in the committed HTML.

Then run each generator with the flag, diff the output against the committed
HTML, and expect the difference to be nothing.
