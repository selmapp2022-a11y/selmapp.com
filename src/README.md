# Page generators — archived source, not a build step

These eight scripts generated the HTML in this repository. Until 25 August 2026
they lived only in an untracked folder on one laptop: the repository held the
output and nothing held the source. That is why they are here.

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
