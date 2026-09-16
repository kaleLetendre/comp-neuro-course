# Comp Neuro Course

## What this is

A self-study curriculum in spiking neural networks, computational neuroscience and predictive coding — 17 lessons across three tracks. This repo holds the *plan and the specs*, not lesson content: the coursework itself is written later, lesson by lesson, as each one is taught.

Pre-dissertation groundwork for an MSc Computer Science (University of London / Birkbeck, starts April 2026). It feeds a sibling research project at `~/personal/Adaptive-Web-PC-SNN` — a spiking network using predictive coding on a graph topology. Lessons carry "project tie-in" lines pointing at that project's steps; the biology track's long-form write-ups live there, in `docs/comp_neuro_notes.md`, because each ends in a design decision for it.

## Files

- `foundations.md` — the foundation track (F1-F11), Dayan & Abbott end to end, assuming no prior neuroscience. Runs before everything else.
- `learning_plan.md` — the map: all four tracks, the ordering rule, progress checkboxes, open questions carried forward
- `lessons.md` — the detail: one spec per lesson (goal, scope, size, source material, five acceptance criteria)
- `fetch_papers.py` — the reading list as code: 28 citations with verified DOIs; downloads the 10 that are openly available
- `papers/` — downloaded sources, gitignored. The bibliography is the artifact and lives in the script; the PDFs are reproducible.
- `coursework/` — one file per lesson: four pieces each (derivation, simulation, guided reading, written defence) with rubrics, private grader keys and teacher constraints
- `notebooklm/` — per-lesson source packs for generating audio/video overviews, mirrored to Google Drive under `comp-neuro-course/`. The audio is the consume step and comes first in a lesson.

## The ordering rule (set 2026-06-19, still in force)

**Foundations (F1-F11) come first** — the textbook end to end, assuming no prior neuroscience. Then raw SNN (track A) → raw predictive coding (track C), with biology (track B) alongside. No fusion design, and no PC≈backprop, until both halves stand on their own. F, A and C are each strictly sequential.

Do not assume the learner already knows a topic because an earlier note says it was covered. An earlier version of this course did that and skipped material as a result.

## Teaching contract

The formats that land: **concrete worked examples with actual numbers**, tick-by-tick walkthroughs, small ASCII diagrams, comparison tables, and a running "what you know / what's left" checklist. Default to examples-with-numbers over prose.

- The learner reasons out loud and checks their mental model against you. When they say "I don't get X", correct the *specific* misconception — do not re-explain the whole topic.
- Tie concepts back to the sibling project where they map: stress variable ≈ homeostasis, error neuron ≈ third factor, clamping ≈ encode/decode.
- End a teaching turn by offering the natural next topic rather than dumping it.
- The five acceptance criteria per lesson are **criteria for the lesson, not a test**. Where one names a figure, the number is the vehicle — the reasoning it forces is the point. A lesson that produces recall without reasoning has missed.
- After teaching: tick the boxes in `learning_plan.md`, and append any biology write-up to `docs/comp_neuro_notes.md` in the Adaptive-Web-PC-SNN repo with its "relevance to this project" block.

## Core text

Dayan & Abbott, *Theoretical Neuroscience* (MIT Press, 2001) — physical copy on hand. It carries A2, A3, A4, B1 and B3 outright, grounds six more lessons, and is silent on six (including predictive coding itself, which postdates it). Chapter-by-chapter mapping is in each lesson's **Source material** line.

## Working here

- Markdown only so far; `fetch_papers.py` is stdlib Python 3, no dependencies, safe to re-run (it skips what is on disk).
- 18 of the 28 sources need institutional access and are marked as such on the lesson that uses them. Do not present them as available.
- Flat structure. Subdirectories only for `papers/`, `coursework/` and `notebooklm/` (one folder per lesson).
- `coursework/` grading material is written for a future constrained "teacher" agent: banded rubric, private grader key, hint ladder, and explicit prohibitions. It marks and hints; it never does the work.
