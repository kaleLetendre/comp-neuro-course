# F1 — NotebookLM prompts, one per capability

Each NotebookLM output has different physics. A podcast has no eyes, a video does, a flashcard has no room to argue. The same prompt across all of them produces an episode that reads out equations nobody can see. So there is one prompt per capability below, and they differ deliberately.

## Sources to select

The three numbered documents in this folder. **Do not add the coursework file** from `coursework/F1.md` — it contains formulas, code and the grader keys, and NotebookLM will both read the symbols aloud and give away the answers.

---

## 1. Audio Overview (podcast)

Card → **Customize** → *"What should the AI hosts focus on in this episode?"*

> The listener is a strong programmer with no neuroscience background, starting postgraduate study, and is listening while walking. Assume no prior neuroscience: explain each concept rather than referring to it. They are comfortable with mathematics, so do not condescend — but this is audio, so obey these rules absolutely.
>
> Never speak a formula, an equation, a symbol or a variable name. Not "r of t", not "tau sub m", not "lambda". Say "the firing rate at a given moment" and "the membrane time constant". If a relationship matters, describe how one quantity behaves as another changes, in words, with a worked number: not the formula for the noise in a rate estimate, but "a neuron firing at twenty hertz puts on average one fifth of a spike into a ten millisecond window, so most windows are empty and the occasional one reports a hundred hertz".
>
> Never refer to a figure, a plot, a graph, an axis, a table or anything visual, and never say "as you can see". Nothing is visible. If a shape matters, describe the shape: "the gap distribution falls away steeply, so short gaps are the most common even though the average gap is fifty milliseconds".
>
> Spend the episode in four parts, longest first. One: firing rate as a construct rather than a measurement — the three non-equivalent definitions, the estimation methods, and the trade-off none of them escape. Two: spike train statistics — the completely random reference process, the shape of the gap distribution, the Fano factor as a diagnostic, and what a refractory period does to it. Three: what is actually recorded and why the spike waveform is discarded. Four, briefly: tuning curves, then close on the rate versus timing question as open, with evidence on both sides.
>
> Do not answer the questions in the learning outcomes document. Teach the mechanisms so the listener can answer them.
>
> Keep the numbers, spoken as words: one millisecond, twenty hertz, a refractory period of one to two milliseconds, a Fano factor of one for the random reference case. No "the brain is like a computer". Do not call anything beautiful or fascinating.

## 2. Video Overview

Card → **Customize** → the focus box.

> Same audience and same four parts as the audio prompt, same instruction to assume no prior neuroscience — but this format has a screen, so use it. Here the symbols and figures the audio must avoid are the point.
>
> Show, on screen: a raster plot of repeated trials with the trial-averaged rate beneath it; the same spike train smoothed with a wide window and a narrow window side by side, so the trade-off is seen rather than described; a gap-distribution histogram with and without a refractory period; and a tuning curve with its peak and width annotated. Put the definition of the Fano factor on screen as variance over mean, and keep it on screen while it is discussed.
>
> Narration should point at what is displayed rather than duplicating it. Do not answer the learning-outcome questions.

## 3. Mind map

No prompt box; it generates from the sources. Check it against this structure: the spike train as the observable, then rate as a construct with its three definitions as separate branches, then estimation methods with the trade-off attached, then statistics (random reference process, gap distribution, Fano factor, departures in both directions), then tuning curves, then the open coding question.

## 4. Study guide

> Produce a study guide for someone who has listened to the overview and is about to read Dayan and Abbott chapter one. Organise it by the three definitions of firing rate, the three estimation methods, and the statistics. For each, give the one sentence that would let a reader reconstruct the idea, and the one question that would expose whether they actually have it. Do not include answers.

## 5. Quiz

> Write questions that require reasoning, not recall of a phrase. Each should demand a specific answer: a computed number, a direction of change, a comparison, or a named mechanism. Never ask to "explain" or "discuss" something. Include at least one question that gives a spike train and asks for a rate, and at least one that gives a Fano factor value and asks what it rules out. Avoid questions answerable by pattern-matching the wording of the source. Answers may be provided separately from the questions, not inline.

## 6. Flashcards

> One fact or relationship per card, phrased so the back is a specific answer rather than a paragraph. Favour cards that pair a quantity with its meaning — a Fano factor value with what it implies, a window width with what it costs. No card should contain a formula or a symbol; state relationships in words. Do not make cards from the learning outcomes document; those are assessment questions, not material.

## 7. Briefing document

> Summarise what a reader needs before the chapter, in under one page: what is recorded, why rate is constructed rather than measured, and what the open question is. Prose only, no bullet fragments.

---

## Chat starters

Ask these in the chat box after listening.

1. Walk me through why a ten millisecond window at twenty hertz gives a noisy rate estimate, using actual expected spike counts.
2. If a neuron's Fano factor is zero point four, what does that rule out about its spiking, and what could produce it?
3. Why is the most common gap between spikes a very short one, when the average gap is fifty milliseconds?
4. Give me a worked case where the trial-averaged rate is misleading about what the neuron did on any single trial.
5. What would a neuron have to do for a rate code to be impossible in principle, rather than merely inefficient?
6. Is choosing a smoothing kernel ever a claim about biology, or only ever about data analysis?
