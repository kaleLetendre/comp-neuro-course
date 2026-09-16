# NotebookLM packs

Source material for generating audio and video overviews in [NotebookLM](https://notebooklm.google.com), one folder per lesson. These are the **consume** step: the front door of a lesson, before the reading, the derivation and the build.

## Why this exists

A lesson that starts with fifty pages of Dayan & Abbott cold is a lesson that does not get done. An audio overview you listen to on a walk gets the concepts in once, so the reading afterwards is a second pass rather than a first contact. NotebookLM only knows what is in its sources, so the packs contain the actual substance — not pointers to it.

## Using a pack

1. Open NotebookLM and create a notebook for the lesson.
2. Add sources from Google Drive: `comp-neuro-course/<lesson folder>` (the same files are mirrored there).
3. Generate an Audio Overview, and paste the customisation prompt from that lesson's `PROMPTS.md` verbatim.
4. Listen. Then do the lesson's guided reading, derivation, simulation and written defence in that order — see `coursework/`.
5. The chat starters in `PROMPTS.md` are for afterwards, when something did not land.

## What is in a pack

| File | Purpose |
|---|---|
| `01_concept_brief.md` | The teaching substance — what the overview is generated from |
| `02_learning_outcomes.md` | What the listener must be able to do afterwards, plus an instruction not to answer the assessment questions outright |
| `03_project_context.md` | The learner's own open problem, so the overview uses it as the running example |
| `PROMPTS.md` | Customisation prompts for audio, video and mind map, plus chat starters |

## Rules that keep the output targeted

- **State the substance, do not reference it.** NotebookLM cannot read the textbook. Anything that should appear in the audio has to be in the brief.
- **Name what the listener already knows** so the overview does not spend ten minutes re-explaining LIF dynamics.
- **Keep the numbers.** Specific figures are what separates a useful overview from a podcast about how fascinating brains are.
- **Never let it answer the assessment questions.** The five acceptance criteria per lesson are the check; an overview that answers them destroys the lesson's only feedback signal.
- **Do not let it resolve open questions.** Where the project has an unsettled result, the prompt says so explicitly. An overview that confidently asserts an answer nobody has established is worse than useless.

## Mirrored to Drive

Each pack is also in Google Drive under `comp-neuro-course/`, one subfolder per lesson, because NotebookLM imports sources from Drive. The repo copy is the source of truth; if you edit a pack here, re-upload it.

## Status

Only **A2 (attractors and network state)** exists so far — a pilot, to find out whether a targeted overview is genuinely better than a generic one before writing sixteen more.
