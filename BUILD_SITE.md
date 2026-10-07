# The study site

The course reads badly as raw markdown on a tablet, which is where most of the reading happens — half the screen on the lesson, the other half on a notes app for the derivations. `build_site.py` turns the repo into a [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site: sidebar nav, search across all 28 lessons, dark mode, and a layout that survives being squeezed into half a screen.

## Two builds, one source

| | |
|---|---|
| **Student** | `python3 build_site.py` → `site_src/` → `site/`. Grader keys and teacher hint ladders are stripped and replaced with a "hidden" notice. Rubrics stay, since marking yourself against the bands is part of the work. |
| **Teacher** | `python3 build_site.py --teacher` → `site_src_teacher/` → `site_teacher/`. Everything, for the marking agent. Never publish this one. |

Reading a lesson with its answers three paragraphs below defeats the point, so the split is not optional.

## Figures

Lectures place the book's own figures by number, written as `{{fig:1.4|caption}}`. The builder embeds them by default, each captioned with its source and a link to the authors' site.

`--no-figures` builds a version that cites figures by number instead.

The figures are Dayan & Abbott's, from the sets they publish for teaching. They are used here with attribution, in a free non-commercial guide that points readers at the book. The homepage says so, every caption says so, and anything a rights holder asks to have removed comes down.

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

## Page structure

A lesson is one page, assembled from three sources and structured rather than concatenated:

| | |
|---|---|
| **At a glance** | Length, prerequisites and reading, as an admonition under the title |
| **Lecture** | The prose, with the book's figures. Its internal headings sit at H3 so they do not compete with the page's own sections |
| **Lesson spec** | Goal, acceptance criteria, feeds, done-when. Scope bullets collapse |
| **Authors' exercises** | Lifted out of the coursework file into its own section — it is the most important work on the page |
| **Coursework** | Running order, a collapsed coverage map, then the four pieces as **tabs**, so one is worked at a time instead of scrolled past |
| **Completion bar** | What must be true before moving on |

Inside each piece, the rubric collapses (it is consulted after an attempt, not before). The grader key and hint ladder collapse too, and exist only in the teacher build.

Design decisions behind this are in `design/lesson_template.md`; the stylesheet and palette rationale are in `design/theme_notes.md`.

## What the page for a lesson contains

The **lecture** (where one is written), then the **spec** (goal, scope, acceptance criteria, source material, assigned exercises), then the **coursework** (four pieces with rubrics). That order matches the running order: read, then do. The authors' own exercise sets are linked rather than reproduced — they are Dayan & Abbott's, and `fetch_book_materials.sh` pulls them locally.
