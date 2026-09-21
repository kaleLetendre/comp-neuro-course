# Comp Neuro Course

A self-study curriculum in spiking neural networks, computational neuroscience and predictive coding. Three tracks, 17 lessons, each with a goal, a scope, source material and the acceptance criteria that say whether the lesson worked.

Built as pre-dissertation groundwork for an MSc Computer Science (University of London / Birkbeck, starting April 2026), and feeding a research project — [Adaptive Web PC-SNN](https://github.com/kaleLetendre/Adaptive-Web-PC-SNN), a spiking network using predictive coding on a graph topology. The lessons carry "project tie-in" lines pointing at that work; they are what keeps the theory anchored to something being built, and can be ignored if you are reading this for the theory alone.

## Files

| | |
|---|---|
| [`learning_plan.md`](learning_plan.md) | The map — three tracks, the ordering rule, progress checkboxes, open questions |
| [`lessons.md`](lessons.md) | The detail — one spec per lesson: goal, scope, size, source material, acceptance criteria |
| [`fetch_papers.py`](fetch_papers.py) | The reading list as code — 28 verified citations; downloads what is openly available |
| [`fetch_exercises.sh`](fetch_exercises.sh) | Pulls Dayan & Abbott's own exercise sets, code and data |
| [`MATERIALS.md`](MATERIALS.md) | What you need and where to get it — one purchase, everything else free |

## The ordering rule

Raw SNN first (track A), then raw predictive coding (track C). Biology (track B) runs alongside and gates nothing. No fusion design until both halves stand on their own — set 2026-06-19 and still in force.

## Core text

Dayan & Abbott, *Theoretical Neuroscience* (MIT Press, 2001). It carries five lessons outright, grounds six more, and is silent on six — chapter-by-chapter mapping in `lessons.md`.

## Getting the papers

```bash
python3 fetch_papers.py
```

Fetches into `papers/` (gitignored). Ten of the 28 sources are openly available; the rest need institutional access and are marked as such on the lesson that uses them. Every citation has been resolved against Europe PMC, so the DOIs are good even where the file is not.

## Notes on the biology track

Track B's write-ups live in `docs/comp_neuro_notes.md` in the Adaptive-Web-PC-SNN repo, not here — each section ends in a design decision for that project, so the notes stayed with the code they inform.
