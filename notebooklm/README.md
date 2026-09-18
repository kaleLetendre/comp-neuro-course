# NotebookLM packs

Source material for generating audio and video overviews in [NotebookLM](https://notebooklm.google.com), one folder per lesson. These are the **consume** step: the front door of a lesson, before the reading, the derivation and the build.

## Why this exists

A lesson that starts with fifty pages of Dayan & Abbott cold is a lesson that does not get done. An audio overview you listen to on a walk gets the concepts in once, so the reading afterwards is a second pass rather than a first contact. NotebookLM only knows what is in its sources, so the packs contain the actual substance — not pointers to it.

## Using a pack

1. Open NotebookLM and create a notebook for the lesson.
2. Add sources from Google Drive: `comp-neuro-course/<lesson folder>` (the same files are mirrored there).
3. Pick the capability you want and paste *its* prompt from that lesson's `PROMPTS.md` — they differ by format and are not interchangeable. For the podcast that is the Audio Overview card → **Customize** → the box labelled *"What should the AI hosts focus on in this episode?"*.
4. Listen. Then do the lesson's guided reading, derivation, simulation and written defence in that order — see `coursework/`.
5. The chat starters in `PROMPTS.md` are for afterwards, when something did not land.

## What is in a pack

| File | Purpose |
|---|---|
| `01_concept_brief.md` | The teaching substance — what the overview is generated from |
| `02_learning_outcomes.md` | What the listener must be able to do afterwards, plus an instruction not to answer the assessment questions outright |
| `03_project_context.md` | The learner's own open problem, so the overview uses it as the running example |
| `PROMPTS.md` | One prompt per capability — audio, video, mind map, study guide, quiz, flashcards, briefing — plus chat starters |

## Two rules learned the hard way

**Source hygiene: the documents must be audio-safe prose.** NotebookLM reads its sources literally, so markdown emphasis, headers, LaTeX and variable names get vocalised — a source containing `$\tau_m$` produces a podcast saying "dollar tau sub m". Write pack documents as plain spoken prose: no markup, no symbols, no formulas, no references to figures. State every relationship in words with a worked number. Never add a coursework file as a source; those contain formulas, code and grader keys, and NotebookLM will read out the symbols and give away the answers.

**One prompt per capability.** A podcast has no eyes; a video does; a flashcard has no room to argue. Using one prompt everywhere produces an episode that reads equations aloud and says "as you can see" to someone out walking. Each `PROMPTS.md` therefore carries a separate prompt for the audio overview, the video overview, the study guide, the quiz, the flashcards and the briefing document, plus a structure to check the mind map against. The audio prompt bans symbols and visual references outright; the video prompt requires exactly the figures the audio had to describe in words.

## Rules that keep the output targeted

- **State the substance, do not reference it.** NotebookLM cannot read the textbook. Anything that should appear in the audio has to be in the brief.
- **Name what the listener already knows** so the overview does not spend ten minutes re-explaining LIF dynamics.
- **Keep the numbers.** Specific figures are what separates a useful overview from a podcast about how fascinating brains are.
- **Never let it answer the assessment questions.** The five acceptance criteria per lesson are the check; an overview that answers them destroys the lesson's only feedback signal.
- **Do not let it resolve open questions.** Where the project has an unsettled result, the prompt says so explicitly. An overview that confidently asserts an answer nobody has established is worse than useless.

## Mirrored to Drive

Each pack is also in Google Drive under `comp-neuro-course/`, one subfolder per lesson, because NotebookLM imports sources from Drive. The repo copy is the source of truth; if you edit a pack here, re-upload it.

## Pack contents, and why the third document varies

Foundation packs carry `03_what_you_will_build` — a preview of the derivation, simulation and written work the lesson leads to, so the overview can make those questions feel live without answering them. Advanced packs carry `03_project_context` instead, where the lesson connects to the Adaptive-Web-PC-SNN work. Both do the same job: give the generator something concrete to aim the material at.

## Status

**F1 (spike trains and firing rates)** — the course's actual first lesson, and the pack to test.

**A2 (attractors and network state)** — written earlier, when A2 was near the front of the course. It is now gated behind the whole foundation track, so it will not be used for months. Its prompts have been corrected for the assume-no-prior-knowledge rule, but it has not been regenerated or heard.

The remaining lessons get packs once F1's format is confirmed in use.
