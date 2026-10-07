#!/usr/bin/env python3
"""Generate the MkDocs source tree from the course markdown.

One page per lesson, assembled from three sources: the lecture, the lesson
spec, and the coursework file. The page is structured rather than concatenated
— an at-a-glance header, the lecture, the spec, the textbook authors' own
exercises as their own section, then the coursework with its four pieces in
tabs so one can be worked at a time.

Two builds come out of the same source. The student build hides grader keys
and hint ladders; the teacher build keeps them. Reading a lesson with its
answers three paragraphs below defeats the point.

    python3 build_site.py              # student, figures cited by number
    python3 build_site.py --figures    # student, figures embedded (local only)
    python3 build_site.py --teacher    # everything
"""
import os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TEACHER = "--teacher" in sys.argv
FIGURES = "--no-figures" not in sys.argv
OUT = os.path.join(ROOT, ("site_src_teacher" if TEACHER else "site_src")
                   + ("" if FIGURES else "_nofigs"))
DOCS = os.path.join(OUT, "docs")

TRACKS = [
    ("foundations", "Foundations", "foundations.md", r"^### (F\d+|Bridge)\."),
    ("advanced", "Advanced", "lessons.md", r"^### ([ABC]\d+)\."),
]

# ---------------------------------------------------------------- helpers

def indent(text, n):
    pad = " " * n
    return "\n".join(pad + ln if ln.strip() else "" for ln in text.splitlines())

def split_sections(text):
    """Split markdown on '## ' headings -> [(heading_or_None, body)]."""
    parts, cur_head, cur = [], None, []
    for ln in text.splitlines():
        if ln.startswith("## "):
            parts.append((cur_head, "\n".join(cur).strip()))
            cur_head, cur = ln[3:].strip(), []
        else:
            cur.append(ln)
    parts.append((cur_head, "\n".join(cur).strip()))
    return parts

# ---------------------------------------------------------------- figures

FIG_RE = re.compile(r"\{\{fig:(\d+)\.(\d+)\|([^}]*)\}\}")

def figure_source(chapter, number):
    figdir = os.path.join(ROOT, "exercises", "figures")
    tar = os.path.join(figdir, f"ch{chapter}fig.tar.gz")
    target = os.path.join(figdir, f"ch{chapter}")
    if not os.path.isdir(target) and os.path.exists(tar):
        os.makedirs(target, exist_ok=True)
        os.system(f"tar xzf {tar} -C {target} 2>/dev/null")
    for root, _, files in os.walk(target):
        for f in files:
            if f == f"ch{chapter}fig{number}.png":
                return os.path.join(root, f)
    return None

def expand_figures(text, outdir):
    """Embed the figure locally; cite it by number when publishing.

    Figures are reproduced from the authors' own teaching materials, with
    attribution, for a free non-commercial study guide. --no-figures builds a
    version that cites them by number instead."""
    def repl(m):
        ch, num, cap = m.group(1), m.group(2), m.group(3).strip()
        if FIGURES:
            src = figure_source(ch, num)
            if src:
                dest = os.path.join(outdir, "figures")
                os.makedirs(dest, exist_ok=True)
                shutil.copy(src, os.path.join(dest, f"ch{ch}fig{num}.png"))
                return (f"![Figure {ch}.{num}](../figures/ch{ch}fig{num}.png)\n\n"
                        f"*Figure {ch}.{num} — {cap}. From Dayan & Abbott, "
                        f"[Theoretical Neuroscience]"
                        f"(https://www.gatsby.ucl.ac.uk/~dayan/book/), "
                        f"reproduced from the authors' teaching materials.*")
        return (f'!!! quote "Figure {ch}.{num}"\n'
                f"    {cap}.\n\n"
                f"    In the book at figure {ch}.{num}, and in the authors' figure "
                f"archive that `fetch_book_materials.sh` downloads.")
    return FIG_RE.sub(repl, text)

# ---------------------------------------------------------------- files

GATSBY = "https://www.gatsby.ucl.ac.uk/~dayan/book"
# lesson -> textbook chapter, for the exercise sets and figure decks
CHAPTER = {"F1": 1, "F2": 2, "F3": 3, "F4": 4, "F5": 5, "F6": 5,
           "F7": 6, "F8": 7, "F9": 8, "F10": 9, "F11": 10}
# chapters whose exercise sets ship data files
CHAPTER_DATA = {1: ["c1p8.mat"], 2: ["c1p8.mat", "c2p3.mat"], 10: ["c10p1.mat"]}

def _papers_by_lesson():
    """Read the bibliography out of fetch_papers.py so links stay in one place."""
    try:
        sys.path.insert(0, ROOT)
        import fetch_papers
        out = {}
        for entry in fetch_papers.PAPERS:
            name, lesson, citation, doi = entry[0], entry[1], entry[2], entry[3]
            out.setdefault(lesson, []).append((citation, doi))
        return out
    except Exception:
        return {}

PAPERS_BY_LESSON = _papers_by_lesson()
# openly readable in a browser, even where a script cannot fetch them
OPEN_IN_BROWSER = {
    "10.1073/pnas.79.8.2554": "https://www.ncbi.nlm.nih.gov/pmc/articles/346238",
    "10.1073/pnas.94.2.719": "https://www.ncbi.nlm.nih.gov/pmc/articles/19580",
    "10.1152/physrev.00035.2008": "https://www.ncbi.nlm.nih.gov/pmc/articles/2923921",
    "10.1016/j.neuron.2012.10.038": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3777738/",
    "10.1016/j.neuron.2012.03.026": "http://www.cell.com/article/S0896627312003340/pdf",
    "10.1016/S0896-6273(03)00149-1": "http://www.cell.com/article/S0896627303001491/pdf",
    "10.1016/j.neuron.2005.04.026": "http://www.cell.com/article/S0896627305003624/pdf",
    "10.1097/00004647-200110000-00001": "https://journals.sagepub.com/doi/pdf/10.1097/00004647-200110000-00001",
}

def files_block(lid):
    """Per-lesson download links: the authors' materials, and the papers."""
    rows = []
    ch = CHAPTER.get(lid)
    if ch:
        rows.append(f"[Exercises, chapter {ch} (PDF)]({GATSBY}/exercises/c{ch}/c{ch}.pdf)")
        rows.append(f"[Figures, chapter {ch} (PowerPoint)]({GATSBY}/figures/ch{ch}fig.ppt)")
        for d in CHAPTER_DATA.get(ch, []):
            rows.append(f"[Data: `{d}`]({GATSBY}/exercises/c{ch}/data/{d})")
        if ch == 7:
            rows.append(f"[Chapter 7 in full, free (PDF)]({GATSBY}/ch7.pdf)")
    for citation, doi in PAPERS_BY_LESSON.get(lid, []):
        short = citation.split(",")[0]
        url = OPEN_IN_BROWSER.get(doi, f"https://doi.org/{doi}")
        tag = "" if doi in OPEN_IN_BROWSER else " *(may need library access)*"
        rows.append(f"[{short}]({url}){tag}")
    if not rows:
        return ""
    body = "\n".join("    - " + r for r in rows)
    return ('??? abstract "Files for this lesson"\n\n'
            "    Open on any device; nothing here needs a login.\n\n"
            + body + "\n\n"
            f"    Also: [errata]({GATSBY}/errata.pdf) · "
            f"[all exercise code and data]({GATSBY}/exall.tar.gz) · "
            f"[all figures]({GATSBY}/figures/complete.tar.gz)\n")

# ---------------------------------------------------------------- sources

def lecture_for(lid, outdir):
    path = os.path.join(ROOT, "lectures", f"{lid}.md")
    if not os.path.exists(path):
        return None
    body = re.sub(r"^# .*\n", "", open(path).read(), count=1)
    body = re.sub(r"^## ", "### ", body, flags=re.M)   # sit below the page's H2s
    return expand_figures(body, outdir)

def parse_spec(chunk):
    """Pull the at-a-glance fields out of a lesson spec; collapse Scope."""
    chunk = re.sub(r"^### .*\n", "", chunk, count=1)
    fields = {}
    for key in ("Prerequisites", "Size", "Source material", "Local copies"):
        m = re.search(rf"^\*\*{key}:\*\*\s*(.+)$", chunk, re.M)
        if m:
            fields[key] = m.group(1).strip()
            chunk = chunk.replace(m.group(0) + "\n", "")
    m = re.search(r"^\*\*Scope:\*\*\s*\n((?:[-*] .*\n?)+)", chunk, re.M)
    if m:
        collapsed = '??? note "Scope — what the lesson covers"\n\n' + indent(m.group(1).rstrip(), 4)
        chunk = chunk.replace(m.group(0), collapsed + "\n")
    return fields, chunk.strip()

PIECE_RE = re.compile(r"^(Piece \d+)\s*[—-]\s*(.+)$")

def parse_coursework(lid):
    name = "BRIDGE" if lid == "Bridge" else lid
    path = os.path.join(ROOT, "coursework", f"{name}.md")
    if not os.path.exists(path):
        return None
    text = re.sub(r"^# .*\n", "", open(path).read(), count=1)
    total_time = None
    m = re.search(r"\*\*Total time:\*\*\s*([^.]+(?:\.[^*]*)?)", text)
    if m:
        total_time = m.group(1).strip().rstrip(".")
    out = {"time": total_time, "exercises": None, "running": None,
           "coverage": None, "pieces": [], "completion": None, "extra": []}
    for head, body in split_sections(text):
        if head is None:
            continue
        h = head.lower()
        if h.startswith("assigned exercises"):
            out["exercises"] = body
        elif h.startswith("running order"):
            out["running"] = body
        elif h.startswith("coverage map"):
            out["coverage"] = body
        elif h.startswith("completion bar"):
            out["completion"] = body
        elif PIECE_RE.match(head):
            out["pieces"].append((head, body))
        else:
            out["extra"].append((head, body))
    return out

def fold_piece(body):
    """Collapse rubric, grader key and hint ladder inside a piece."""
    def grab(label, until):
        pat = re.compile(rf"(^\*\*{label}\*\*[^\n]*\n.*?)(?=^\*\*(?:{until})\*\*|\Z)",
                         re.M | re.S)
        m = pat.search(body)
        return m.group(1).rstrip() if m else None

    rubric = grab("Rubric", "Grader key|Teacher constraints")
    key = grab("Grader key", "Teacher constraints")
    hints = grab("Teacher constraints", "ZZZ")
    for blk in (rubric, key, hints):
        if blk:
            body = body.replace(blk, "").rstrip()

    out = body.rstrip() + "\n"
    if rubric:
        rubric = re.sub(r"^\*\*Rubric\*\*[^\n]*\n", "", rubric)
        out += '\n??? info "Rubric — how this is marked"\n\n' + indent(rubric.strip(), 4) + "\n"
    if key:
        if TEACHER:
            key = re.sub(r"^\*\*Grader key\*\*[^\n]*\n", "", key)
            out += '\n??? danger "Grader key — teacher build"\n\n' + indent(key.strip(), 4) + "\n"
        else:
            out += ('\n!!! note "Grader key hidden"\n\n'
                    "    The marking criteria for this piece are in the teacher build.\n")
    if hints and TEACHER:
        hints = re.sub(r"^\*\*Teacher constraints\*\*[^\n]*\n", "", hints)
        out += '\n??? tip "Hint ladder — teacher build"\n\n' + indent(hints.strip(), 4) + "\n"
    return out

# ---------------------------------------------------------------- assembly

def build_page(lid, title, spec_chunk, outdir):
    fields, spec_body = parse_spec(spec_chunk)
    cw = parse_coursework(lid)
    lec = lecture_for(lid, outdir)

    glance = ['!!! abstract "At a glance"', ""]
    if fields.get("Size"):
        t = f" · about {cw['time']}" if cw and cw.get("time") else ""
        glance.append(f"    **Length** — {fields['Size']}{t}")
    if fields.get("Prerequisites"):
        glance.append(f"    **Before this** — {fields['Prerequisites']}")
    if fields.get("Source material"):
        glance.append(f"    **Reading** — {fields['Source material']}")
    page = f"# {title}\n\n" + "\n".join(glance) + "\n\n"
    fb = files_block(lid)
    if fb:
        page += fb + "\n"
    page += "[TOC]\n\n"

    if lec:
        page += "## Lecture\n\n" + lec + "\n\n"
    page += "## Lesson spec\n\n" + spec_body + "\n\n"

    if cw:
        if cw["exercises"]:
            page += "## Authors' exercises\n\n" + cw["exercises"] + "\n\n"
        page += "## Coursework\n\n"
        if cw["running"]:
            page += cw["running"] + "\n\n"
        if cw["coverage"]:
            page += '??? note "Coverage map"\n\n' + indent(cw["coverage"], 4) + "\n\n"
        for head, body in cw["pieces"]:
            page += f'=== "{head}"\n\n' + indent(fold_piece(body), 4) + "\n\n"
        for head, body in cw["extra"]:
            page += f"## {head}\n\n{body}\n\n"
        if cw["completion"]:
            page += "## Completion bar\n\n" + cw["completion"] + "\n"
    else:
        page += "*No coursework written for this lesson yet.*\n"
    return page

def split_specs(path, pattern):
    text = open(os.path.join(ROOT, path)).read()
    marks = [(m.start(), m.group(1)) for m in re.finditer(pattern, text, re.M)]
    out = []
    for i, (pos, lid) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        chunk = text[pos:end].rstrip()
        title = chunk.splitlines()[0].lstrip("# ").strip()
        title = re.sub(r"^(F\d+|Bridge|[ABC]\d+)\.\s*", "", title)
        out.append((lid, title, chunk))
    return out

# ---------------------------------------------------------------- build

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(DOCS)
os.makedirs(os.path.join(DOCS, "stylesheets"), exist_ok=True)
shutil.copy(os.path.join(ROOT, "design", "theme.css"),
            os.path.join(DOCS, "stylesheets", "theme.css"))
with open(os.path.join(DOCS, "stylesheets", "theme.css"), "a") as f:
    f.write("\n/* Four piece-name tabs will not fit unscrolled at tablet width. */\n"
            ".md-typeset .tabbed-labels { overflow-x: auto; flex-wrap: nowrap; }\n")

nav_tracks = {}
for key, label, src, pattern in TRACKS:
    os.makedirs(os.path.join(DOCS, key), exist_ok=True)
    entries = []
    for lid, title, spec in split_specs(src, pattern):
        open(os.path.join(DOCS, key, f"{lid}.md"), "w").write(
            build_page(lid, f"{lid} · {title}", spec, DOCS))
        entries.append((f"{lid} · {title}", f"{key}/{lid}.md"))
    nav_tracks[key] = entries
    index = os.path.join(ROOT, "design", f"{key}_index.md")
    if os.path.exists(index):
        shutil.copy(index, os.path.join(DOCS, key, "index.md"))

REPO = "https://github.com/kaleLetendre/comp-neuro-course/blob/main/"
LINK_FIXES = [("(foundations.md)", "(foundations/index.md)"),
              ("(lessons.md)", "(advanced/index.md)"),
              ("(foundations/F1.md)", "(foundations/index.md)"),
              ("(advanced/A1.md)", "(advanced/index.md)"),
              ("(learning_plan.md)", "(plan.md)"),
              ("(MATERIALS.md)", "(materials.md)"),
              ("(fetch_papers.py)", f"({REPO}fetch_papers.py)"),
              ("(fetch_book_materials.sh)", f"({REPO}fetch_book_materials.sh)"),
              ("(fetch_closed_papers.py)", f"({REPO}fetch_closed_papers.py)"),
              ("(coursework/README.md)", f"({REPO}coursework/README.md)")]

home = os.path.join(ROOT, "design", "homepage.md")
dl = os.path.join(ROOT, "design", "downloads.md")
for src, dest in [(home if os.path.exists(home) else "README.md", "index.md"),
                  ("learning_plan.md", "plan.md"),
                  ("MATERIALS.md", "materials.md")] + ([(dl, "downloads.md")] if os.path.exists(dl) else []):
    body = open(src if os.path.isabs(src) else os.path.join(ROOT, src)).read()
    for a, b in LINK_FIXES:
        body = body.replace(a, b)
    open(os.path.join(DOCS, dest), "w").write(body)

def nav_lines():
    out = ["  - Home: index.md"]
    for key, label, _, _ in TRACKS:
        out.append(f"  - {label}:")
        out.append(f"      - Overview: {key}/index.md")
        for title, path in nav_tracks[key]:
            out.append(f'      - "{title}": {path}')
    out += ["  - Materials: materials.md", "  - Downloads: downloads.md", "  - Plan: plan.md"]
    return "\n".join(out)

site_name = "Computational Neuroscience" + (" (teacher)" if TEACHER else "")
open(os.path.join(OUT, "mkdocs.yml"), "w").write(f"""site_name: {site_name}
site_description: A self-study course in computational neuroscience built on Dayan & Abbott
docs_dir: docs
site_dir: ../site{'_teacher' if TEACHER else '' if FIGURES else '_nofigs'}
theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: blue grey
      accent: indigo
      toggle: {{icon: material/weather-night, name: Dark}}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: blue grey
      accent: indigo
      toggle: {{icon: material/weather-sunny, name: Light}}
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.indexes
    - navigation.top
    - navigation.prune
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.tabs.link
extra_css:
  - stylesheets/theme.css
markdown_extensions:
  - toc: {{permalink: true, toc_depth: 2}}
  - admonition
  - attr_list
  - md_in_html
  - tables
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed: {{alternate_style: true}}
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.arithmatex: {{generic: true}}
extra_javascript:
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
plugins:
  - search
nav:
{nav_lines()}
""")
print(f"{'teacher' if TEACHER else 'student'}{' +figures' if FIGURES else ''} -> {OUT}")
for k in nav_tracks:
    print(f"  {k}: {len(nav_tracks[k])} lessons")
