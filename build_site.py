#!/usr/bin/env python3
"""Generate the MkDocs source tree from the course markdown.

One page per lesson: its spec followed by its coursework. Two builds come out
of the same source — a student build with grader keys and teacher hint ladders
stripped, and a teacher build with everything. Reading a lesson with the answer
three paragraphs below it defeats the point, hence the split.

    python3 build_site.py            # student site into site_src/
    python3 build_site.py --teacher  # teacher site into site_src_teacher/
"""
import os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TEACHER = "--teacher" in sys.argv
OUT = os.path.join(ROOT, "site_src_teacher" if TEACHER else "site_src")
DOCS = os.path.join(OUT, "docs")

TRACKS = [
    ("foundations", "Foundations", "foundations.md", r"^### (F\d+|Bridge)\."),
    ("advanced", "Advanced", "lessons.md", r"^### ([ABC]\d+)\."),
]

def split_specs(path, pattern):
    """Return [(id, title, body)] for each lesson spec in a source file."""
    text = open(os.path.join(ROOT, path)).read()
    marks = [(m.start(), m.group(1), m.group(0)) for m in re.finditer(pattern, text, re.M)]
    out = []
    for i, (pos, lid, heading) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        chunk = text[pos:end].rstrip()
        title = chunk.splitlines()[0].lstrip("# ").strip()
        out.append((lid, title, chunk))
    return out

def strip_keys(text):
    """Remove grader keys and teacher constraints: everything from a
    '**Grader key**' line up to the next '## ' heading."""
    lines, keep, dropping = text.splitlines(), [], False
    for ln in lines:
        if ln.startswith("**Grader key**"):
            dropping = True
            keep.append("!!! note \"Grader key hidden\"")
            keep.append("    The marking criteria and hint ladder for this piece are in the teacher build.")
            keep.append("")
            continue
        if dropping:
            if ln.startswith("## "):
                dropping = False
            else:
                continue
        keep.append(ln)
    return "\n".join(keep)

def coursework_for(lid):
    name = "BRIDGE" if lid == "Bridge" else lid
    path = os.path.join(ROOT, "coursework", f"{name}.md")
    if not os.path.exists(path):
        return None
    body = open(path).read()
    body = re.sub(r"^# .*\n", "", body, count=1)          # its own H1 duplicates the page title
    return body if TEACHER else strip_keys(body)

def demote(text):
    """Lesson spec arrives as H3; make it the page H1 and push the rest down."""
    text = re.sub(r"^### ", "# ", text, count=1, flags=re.M)
    return text

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(DOCS)

nav_tracks = {}
for key, label, src, pattern in TRACKS:
    os.makedirs(os.path.join(DOCS, key), exist_ok=True)
    entries = []
    for lid, title, spec in split_specs(src, pattern):
        page = demote(spec) + "\n\n---\n\n"
        cw = coursework_for(lid)
        page += cw if cw else "*No coursework written for this lesson yet.*\n"
        fname = f"{lid}.md"
        open(os.path.join(DOCS, key, fname), "w").write(page)
        entries.append((title, f"{key}/{fname}"))
    nav_tracks[key] = entries

# top-level pages
REPO = "https://github.com/kaleLetendre/comp-neuro-course/blob/main/"
LINK_FIXES = [
    ("(foundations.md)", "(foundations/F1.md)"),
    ("(lessons.md)", "(advanced/A1.md)"),
    ("(learning_plan.md)", "(plan.md)"),
    ("(MATERIALS.md)", "(materials.md)"),
    ("(fetch_papers.py)", f"({REPO}fetch_papers.py)"),
    ("(fetch_book_materials.sh)", f"({REPO}fetch_book_materials.sh)"),
    ("(fetch_closed_papers.py)", f"({REPO}fetch_closed_papers.py)"),
    ("(coursework/README.md)", f"({REPO}coursework/README.md)"),
]
for src, dest, title in [("README.md", "index.md", None),
                         ("learning_plan.md", "plan.md", None),
                         ("MATERIALS.md", "materials.md", None)]:
    body = open(os.path.join(ROOT, src)).read()
    for a, b in LINK_FIXES:
        body = body.replace(a, b)
    open(os.path.join(DOCS, dest), "w").write(body)

def nav_lines():
    out = ["  - Home: index.md", "  - Plan: plan.md", "  - Materials: materials.md"]
    for key, label, _, _ in TRACKS:
        out.append(f"  - {label}:")
        for title, path in nav_tracks[key]:
            out.append(f"      - \"{title}\": {path}")
    return "\n".join(out)

site_name = "Comp Neuro Course" + (" (teacher)" if TEACHER else "")
open(os.path.join(OUT, "mkdocs.yml"), "w").write(f"""site_name: {site_name}
site_description: A self-study computational neuroscience curriculum built on Dayan & Abbott
docs_dir: docs
site_dir: ../site{'_teacher' if TEACHER else ''}
theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle: {{icon: material/weather-night, name: Dark}}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle: {{icon: material/weather-sunny, name: Light}}
  features:
    - navigation.sections
    - navigation.top
    - toc.follow
    - search.suggest
    - content.code.copy
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.arithmatex:
      generic: true
  - tables
  - attr_list
extra_javascript:
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
plugins:
  - search
nav:
{nav_lines()}
""")
print(f"{'teacher' if TEACHER else 'student'} source written to {OUT}")
print(f"  foundations: {len(nav_tracks['foundations'])} pages")
print(f"  advanced:    {len(nav_tracks['advanced'])} pages")
