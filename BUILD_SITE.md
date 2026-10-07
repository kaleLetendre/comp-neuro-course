# The study site

The course reads badly as raw markdown on a tablet, which is where most of the reading happens — half the screen on the lesson, the other half on a notes app for the derivations. `build_site.py` turns the repo into a [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site: sidebar nav, search across all 28 lessons, dark mode, and a layout that survives being squeezed into half a screen.

## Two builds, one source

| | |
|---|---|
| **Student** | `python3 build_site.py` → `site_src/` → `site/`. Grader keys and teacher hint ladders are stripped and replaced with a "hidden" notice. Rubrics stay, since marking yourself against the bands is part of the work. |
| **Teacher** | `python3 build_site.py --teacher` → `site_src_teacher/` → `site_teacher/`. Everything, for the marking agent. Never publish this one. |

Reading a lesson with its answers three paragraphs below defeats the point, so the split is not optional.

## Figures

Lectures place the book's own figures by number, written as `{{fig:1.4|caption}}`. The builder expands them two ways:

| Build | What a figure becomes |
|---|---|
| `--figures` | The authors' PNG, embedded, with its caption |
| default | A quoted reference — figure number plus caption, pointing at the book |

The figures are Dayan & Abbott's, published for teaching support. Embedding them on a public website is redistribution, so **the published site cites them and the offline build shows them**. The offline build is for the person who owns the book; keep it off the web.

`fetch_book_materials.sh` downloads the figure archives; the builder extracts whatever chapter it needs.

## Building

```sh
python3 -m venv .venv
.venv/bin/pip install mkdocs-material
python3 build_site.py                 # public: figures cited
cd site_src && ../.venv/bin/mkdocs build

python3 build_site.py --figures       # offline: figures embedded
cd site_src_figs && ../.venv/bin/mkdocs build
```

The result is static HTML in `site/` — open `site/index.html` directly, or sync that folder to a tablet to read offline.

## Publishing

```sh
cd site_src && ../.venv/bin/mkdocs gh-deploy --remote-branch gh-pages
```

Publishes the **student** build to GitHub Pages. Check which build you are in before running it.

## What the page for a lesson contains

The **lecture** (where one is written), then the **spec** (goal, scope, acceptance criteria, source material, assigned exercises), then the **coursework** (four pieces with rubrics). That order matches the running order: read, then do. The authors' own exercise sets are linked rather than reproduced — they are Dayan & Abbott's, and `fetch_book_materials.sh` pulls them locally.
