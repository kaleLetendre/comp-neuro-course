# The study site

The course reads badly as raw markdown on a tablet, which is where most of the reading happens — half the screen on the lesson, the other half on a notes app for the derivations. `build_site.py` turns the repo into a [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site: sidebar nav, search across all 28 lessons, dark mode, and a layout that survives being squeezed into half a screen.

## Two builds, one source

| | |
|---|---|
| **Student** | `python3 build_site.py` → `site_src/` → `site/`. Grader keys and teacher hint ladders are stripped and replaced with a "hidden" notice. Rubrics stay, since marking yourself against the bands is part of the work. |
| **Teacher** | `python3 build_site.py --teacher` → `site_src_teacher/` → `site_teacher/`. Everything, for the marking agent. Never publish this one. |

Reading a lesson with its answers three paragraphs below defeats the point, so the split is not optional.

## Building

```sh
python3 -m venv .venv
.venv/bin/pip install mkdocs-material
python3 build_site.py
cd site_src && ../.venv/bin/mkdocs build
```

The result is static HTML in `site/` — open `site/index.html` directly, or sync that folder to a tablet to read offline.

## Publishing

```sh
cd site_src && ../.venv/bin/mkdocs gh-deploy --remote-branch gh-pages
```

Publishes the **student** build to GitHub Pages. Check which build you are in before running it.

## What the page for a lesson contains

Its spec (goal, scope, acceptance criteria, source material, assigned exercises) followed by its coursework (the four pieces with rubrics). The authors' own exercise sets are linked rather than reproduced — they are Dayan & Abbott's, and `fetch_book_materials.sh` pulls them locally.
