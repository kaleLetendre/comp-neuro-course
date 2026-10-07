# Lesson page template — design

## 1. The decision: one page

A lesson stays one page. The three-page split (Lecture / Spec / Coursework) buys a shorter sidebar at the cost of the thing this course actually does: a reader works a lesson in several sittings, flipping constantly between "what does the lecture say about this" and "what does the piece I'm on ask for." Three pages means three loads and a lost scroll position every time that happens, on a tablet, mid-task, next to a handwriting app — the worst place to pay a navigation tax. One page also matches how the site already builds: `build_site.py` already concatenates three sources into one file per lesson, the offline `--figures` build is meant to be read start-to-finish with the book open, and `docs/comp_neuro_notes.md`-style cross-references point at a lesson, not a lesson-and-a-third. Splitting would also triple the nav entries (28 lessons → 84), fighting `navigation.prune`, which is already carrying the weight of keeping the sidebar sane.

The fix for "one enormous flat page" is not fewer pages, it's a page with real structure: a short, true table of contents; the rubric/coverage-map/scope material collapsed until wanted; the four coursework pieces as tabs instead of four stacked walls; and a header that tells the reader what they're committing to before they scroll past it.

## 2. Heading-level map

One H1. Five H2s, each a clean, short entry in the inline `[TOC]` (which stays configured to `toc_depth: 2`, so nothing below H2 appears there — this is the actual fix for the collision, not a cosmetic one).

| Element | Level | In TOC? |
|---|---|---|
| Lesson title | H1 | yes (implicit page title) |
| At-a-glance block | *(no heading — admonition, sits between H1 and `[TOC]`)* | no |
| `[TOC]` | — | — |
| **Lecture** | H2 | yes |
| → lecture's own internal sections (currently `## What is recorded`, etc.) | **demoted to H3** | no (by design — see §1) |
| **Lesson spec** | H2 | yes |
| → Goal | bold label, no heading | no |
| → Scope (collapsed) | bold label inside `???`, no heading | no |
| → "You should be able to answer" (acceptance criteria) | bold label, no heading | no |
| → Feeds / Done when | bold labels, no heading | no |
| **Authors' exercises** | H2 | yes |
| **Coursework** | H2 | yes |
| → Running order | plain sentence, no heading | no |
| → Coverage map (collapsed) | inside `???`, no heading | no |
| → Piece 1–4 | **tab labels (`===`), not headings at all** | no |
| → within each piece: Learning goals / Task / Deliverable | bold labels, no heading | no |
| → within each piece: Rubric, Grader key, Teacher constraints | each inside its own nested `???`, no heading | no |
| **Completion bar** | H2 | yes |

Net: the reader's inline contents box has exactly five lines — Lecture, Lesson spec, Authors' exercises, Coursework, Completion bar — instead of today's flat run-on of lecture subsections, spec fields, and four pieces' worth of sub-structure all competing at the same level.

## 3. Annotated skeleton (F1 — Spike trains and firing rates)

```markdown
# F1 — Spike trains and firing rates
<!-- Single H1. Title only — no "Lesson" or "Lecture" prefix clutter. -->

!!! abstract "At a glance"
    **Chapter:** D&A ch. 1 — *Introduction* · *Spike Trains and Firing Rates* ·
    *What Makes a Neuron Fire?* · *Spike-Train Statistics* · *The Neural Code*
    **Prerequisites:** none — the entry point
    **Size:** one to two sittings (~4–4.5h coursework)
<!-- No heading on this block: it's the first thing on the page by position,
     not by TOC entry. Combines the spec's "Source material"/"Prerequisites"/
     "Size" fields with the coursework file's "Total time" into one line
     each, so the reader knows what they're committing to before scrolling
     past the table of contents. -->

[TOC]
<!-- toc_depth: 2 (already set in mkdocs.yml) means only the five H2s below
     appear here. This is the actual fix: the lecture's own section
     headings and the four coursework pieces no longer leak into it. -->

## Lecture

### What is recorded
<!-- Demoted from the lecture source's own H2. Every one of the lecture's
     five section headings becomes H3 the same way — they're real waypoints
     for a reader mid-section, just not page-level structure, so they don't
     belong in the inline TOC. -->

[lecture text]

!!! quote "Figure 1.2"
    An action potential recorded intracellularly...
<!-- Figures are untouched by any of this — full width, inline, exactly
     where the lecture places them. They were never the problem; the owner
     was explicit that they should stay prominent. -->

### Three rates, and estimating them

[lecture text]

### Working backwards from the spikes

[lecture text]

### Poisson, and departures from it

[lecture text]

### The open question

[lecture text]

---

## Lesson spec

Understand that a spike train is the raw observable and "firing rate" is a
construct built on top of it, with several non-equivalent definitions...
<!-- Goal paragraph, unlabelled, straight after the heading — it's the one
     piece of the spec worth reading unprompted. Prerequisites/Size/Source
     already surfaced above, so they're not repeated here. -->

??? note "Scope"
    - The spike as an event: why the waveform is discarded...
    - Three notions of rate — spike-count, time-dependent r(t), trial-averaged...
    - Rate estimation mechanics: binning, sliding windows, kernel smoothing...
    - Poisson spike generation, the interspike-interval distribution...
    - The spike-triggered average introduced as the chapter introduces it...
    - Independent-spike, correlation and population codes...
    - Not covered: decoding (F3), information theory (F4), biophysics (F5)
<!-- Collapsed: skimmable boundary-setting, consulted when a reader wants
     to check "is this in scope", not on first read. -->

**You should be able to answer:**

1. Given a spike train with 12 spikes in a 2-second window, compute...
2. For a Poisson process at 20 Hz, what is the Fano factor...
3. A 100 ms sliding window versus a 10 ms one on the same train...
4. Sketch a tuning curve for an orientation-selective neuron...
5. State one concrete experimental observation arguing for temporal coding...
<!-- Never collapsed — these are the five things the whole page exists to
     produce, and they're the direct map onto the four coursework pieces. -->

**Feeds:** F3, F4, F6, and the whole A track.
**Done when:** You can take a raw spike train, produce two different rate
estimates, defend and critique each...

---

## Authors' exercises

!!! example "Do these — they take precedence over this course's own pieces"
    Dayan & Abbott's own chapter 1 problem set, in `exercises/c1.pdf`
    (code/data in `exercises/exercises/c1/`). **Work all ten.** Where a
    piece below duplicates one of theirs, do theirs — they're the authors',
    this course's are a supplement. Written for MATLAB; translating to
    numpy is part of the work. Chapter 1's set includes twenty minutes of
    real recordings from a blowfly H1 neuron; problems 8–10 have you
    compute the spike-triggered average from it yourself.
<!-- Pulled out of the coursework file's mid-page "Assigned exercises"
     subsection into its own top-level section, positioned before the
     course's own coursework, because the brief is explicit: this is the
     most important work on the page. An admonition, not a collapsed one —
     it should be impossible to miss on the way past. -->

---

## Coursework

Consume, then apply, then refine: guided reading (Piece 3) → derivation
(Piece 1) → simulation (Piece 2) → written explanation (Piece 4). Pieces
are numbered by type, not by sequence.
<!-- Running order survives as one plain sentence, not its own heading. -->

??? note "Coverage map"
    | Piece | Type | Lesson acceptance criteria addressed |
    |---|---|---|
    | 1 | derivation | 1, 3 |
    | 2 | simulation | 2, 3 |
    | 3 | guided reading | 2, 3, 4, 5 |
    | 4 | written explanation | 4, 5 |
<!-- Collapsed: administrative cross-reference, not reading material. -->

=== "Piece 1 — Rate arithmetic and the bias/variance cost"

    **Type:** derivation · **Time:** 45 min

    **Learning goals**
    - Compute a spike-count rate correctly and identify what it does and
      doesn't tell you.
    - Derive, with real numbers, why shrinking a counting window trades
      resolution for noise.

    **Task**

    Part A. A neuron fires 12 spikes in a 2.0 s window...

    Part B. Model spiking as a homogeneous Poisson process...

    **Deliverable**

    A worked derivation showing the Part A rate, the Part B formulas,
    both numeric evaluations with units, and the trade-off as a ratio.

    ??? info "Rubric"
        | Band | Criteria |
        |---|---|
        | Strong | Part A rate correct; identifies both... |
        | Adequate | Part A rate correct; mentions one of two... |
        | Not yet | Rate computed wrong, or Var(r̂) derived without... |

    ??? danger "Grader key (teacher build only)"
        Part A: rate = 12 / 2.0 = **6 Hz**...
        Part B: n ~ Poisson(r·T_w) ⇒ Var(r̂) = r/T_w...

    ??? tip "Hint ladder (teacher build only)"
        - Hint 1: Ask what Var(n) equals for a Poisson-distributed count...
        - Hint 2: Point to the r/T_w form...
        - Never: supply Var(r̂) = r/T_w directly.
<!-- Rubric/Grader key/Hint ladder nest inside the tab as their own
     collapsed blocks: reference material for after an attempt, each
     consulted separately (a reader checks the rubric before the grader
     key, often not at the same sitting). Indentation is 4 spaces for the
     tab body, 4 more for each nested detail block's content. -->

=== "Piece 2 — Simulation: three rate estimators and a Fano factor"

    [Piece 2 content, same shape: type/time, learning goals, task,
    deliverable, then nested Rubric / Grader key / Hint ladder.]

=== "Piece 3 — Guided reading"

    [Piece 3 content, same shape.]

=== "Piece 4 — Written explanation"

    [Piece 4 content, same shape.]

<!-- Four tabs, not four stacked sections and not four top-level `???`
     blocks. Justification: these are worked one at a time across separate
     sittings. A reader opens the lesson today to continue Piece 2 — with
     tabs, that's one click on a label that's visible immediately under
     "Coursework" with no scrolling, and the other three pieces are fully
     out of the way rather than present-but-collapsed above and below.
     Needs pymdownx.tabbed enabled (not currently in mkdocs.yml) — see §5. -->

---

## Completion bar

- [ ] Piece 1: both parts derived with correct numbers and units.
- [ ] Piece 2: script runs standalone; both conditions implemented.
- [ ] Piece 3: all five questions answered with traceable content.
- [ ] Piece 4: 300-600 words, all four required elements present.
- [ ] Reader can, unprompted, give two different numeric answers to
      "what is the firing rate of this train" and explain why both hold.
<!-- Own top-level section, always visible, so "am I done" is one TOC
     click away rather than buried at the tail of a coursework blob. -->
```

## 4. What `build_site.py` must do

Transformations, applied per lesson, replacing the current flat concatenation:

1. **Lecture body:** after stripping its own H1 (as now), demote every `^## ` to `### ` (regex, multiline). No other change — figures pass through untouched.

2. **Spec chunk:** stop promoting its `### F1.` heading to the page H1 (`demote()` goes away) — drop that heading line outright, since the page H1 already carries the title. Extract the `**Prerequisites:**`, `**Size:**`, and `**Source material:**` lines out of the body (regex on the bold label, as the coverage-map/rubric extraction already does elsewhere in the file) — they move into the At-a-glance block, not the spec section. Wrap the `**Scope:**` bullet list in `??? note "Scope"` with its lines indented 4 spaces. Leave Goal, "You should be able to answer," Feeds, and Done when in place, unindented, under `## Lesson spec`.

3. **At-a-glance assembly:** build the admonition from the three extracted spec fields plus the coursework file's `**Total time:**` value (parsed off its current first line) folded into the Size field as a parenthetical. Emit it between the page H1 and `[TOC]`.

4. **Coursework chunk — split instead of pass through.** Currently `coursework_for()` returns one blob appended after the spec. Instead, parse it into four parts and place them separately in the page:
   - the summary line (`**Lesson spec:** ... **Total time:** ...`) — consumed in step 3, dropped from output;
   - the "Assigned exercises" subsection — lifted out, its `## Assigned exercises — the book's own` heading replaced with `## Authors' exercises`, and emitted as its own page section *before* `## Coursework`;
   - "Running order" and "Coverage map" — demote their `## ` headings away; Running order becomes a plain paragraph under `## Coursework`, Coverage map's table gets wrapped in `??? note "Coverage map"`;
   - each `## Piece N — Title` — convert the heading line to `=== "Piece N — Title"` and indent the entire piece body 4 spaces;
   - `## Completion bar` — demoted from inside the coursework blob to its own top-level `## Completion bar` section at the end of the page.

5. **Rubric / Grader key / Teacher constraints, inside each piece:** wrap `**Rubric**` + its table in `??? info "Rubric"`; wrap the `**Grader key** (teacher AI only)` block in `??? danger "Grader key (teacher build only)"`; wrap `**Teacher constraints**` in `??? tip "Hint ladder (teacher build only)"`. All three nest inside the piece's tab body, so their content gets 8-space indentation (4 for the tab, 4 for the detail block).

6. **Student/teacher split — replace `strip_keys()`.** The current function deletes from a `**Grader key**` line to the next `## `; that delimiter no longer exists once step 5 nests things in `???` blocks. New version: in the student build, locate each `??? danger "Grader key...` and `??? tip "Hint ladder...` block by its marker line and its indentation, and either drop it entirely or replace it with a one-line `!!! note` ("Reserved for the teacher build") at the same indentation — same courtesy as today's placeholder, just operating on indentation-delimited blocks instead of heading-delimited ones.

7. **CSS:** extend `stylesheets/extra.css` (still written by the script) with a rule letting `.tabbed-labels` scroll horizontally rather than compress, since four piece-name tabs at 500–600px won't fit on one unscrolled row:
   ```css
   .md-typeset .tabbed-labels { overflow-x: auto; flex-wrap: nowrap; }
   ```

8. Everything else — `demote()`'s removal aside, figure expansion, the two-build (`--teacher`) split, the nav generation — is unchanged.

## 5. `mkdocs.yml` change

Add `pymdownx.tabbed` with the alternate (linked-tab-bar) style, in the `markdown_extensions` list the script writes:

```yaml
  - pymdownx.tabbed:
      alternate_style: true
```

Nothing else in the current extension list needs to change — `pymdownx.details` (for every `???`/`??? danger`/`??? info`/`??? tip`/`??? note`) and `admonition` (for `!!! abstract`/`!!! example`) are already enabled.
