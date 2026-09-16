# F1 — NotebookLM prompts

## Sources to select

The three numbered documents in this folder. Nothing else — extra sources dilute a targeted overview.

## Where each prompt goes

| Prompt | Where in NotebookLM |
|---|---|
| Audio Overview | Audio Overview card → **Customize** → *"What should the AI hosts focus on in this episode?"* |
| Video Overview | Video Overview card → **Customize** → the same focus box |
| Mind map | No prompt box — generated from the sources |
| Chat starters | The main chat box, after listening |

If the box truncates, use the compact version — it front-loads the constraints that matter most.

## Audio Overview — COMPACT version

> Assume no neuroscience background; explain every concept rather than referring to it. The listener is a strong programmer, comfortable with probability and calculus, so do not soften the mathematics — the gap is biological, not technical. Do not answer the questions in the learning-outcomes source; teach toward them. Spend the most time on why a firing rate has to be *estimated* and on the window trade-off: wide windows are stable but smear fast changes, narrow ones track change but are dominated by counting noise at realistic rates. Then spike-train statistics — the Poisson reference, interspike intervals, the Fano factor, and how a refractory period makes a train more regular than Poisson. Then tuning curves, briefly. Close on the rate-versus-timing question as genuinely unresolved, with evidence on both sides. Keep concrete numbers throughout. No "the brain is like a computer" framing.

## Audio Overview — FULL customisation prompt

> The listener is a strong programmer with no formal neuroscience background, starting an MSc. Assume no prior neuroscience whatsoever — whenever a concept is needed, explain it rather than referring to it. They are comfortable with probability, calculus and code, so do not soften the mathematics; the gap to cover is biological, not technical. This is the first lesson of the whole course, so nothing can be assumed as "covered earlier".
>
> Structure the episode in four parts. First, what is actually recorded — the voltage trace, the stereotyped spike, and the decision to discard the waveform and keep only timing. Make clear this is a modelling choice rather than a fact about neurons, and say what it buys.
>
> Second, and at the greatest length: firing rate as a construct rather than a measurement. Cover the three non-equivalent definitions — spike-count rate, time-dependent r(t), trial-averaged rate — and what data each one requires. Then the estimation methods (binning, sliding window, kernel smoothing) and the trade-off none of them escape: a wide window gives a stable estimate that smears fast changes, a narrow one tracks change but at realistic firing rates contains almost no spikes and so is dominated by counting noise. Use a concrete case — at 20 Hz a 10 ms window holds 0.2 spikes on average — so the problem is arithmetic rather than atmosphere.
>
> Third, spike-train statistics: the Poisson process as the reference model, exponentially distributed intervals, and the Fano factor as variance over mean. Explain what the refractory period does to a spike train and therefore to its statistics. Mention that for a renewal process the Fano factor approaches the squared coefficient of variation of the intervals, so the effect is predictable in advance rather than only measurable after the fact.
>
> Fourth, briefly, tuning curves — peak as preferred stimulus, width as sharpness of discrimination — and then close on rate versus temporal coding as an open question, giving the strongest evidence on each side. Sound localisation resolving delays of tens of microseconds is the sharpest case for timing; the pervasiveness of rate-based models that work is the case for rate. Do not resolve it.
>
> The learning-outcomes document lists the questions the listener will be assessed on. Do not answer them directly and do not read them out as a quiz — teach the mechanisms so they can construct the answers themselves.
>
> Keep the numbers: spikes about a millisecond wide, refractory periods of one to two milliseconds, a Fano factor of exactly 1 for Poisson, 20 Hz and 10 ms in the window example. Avoid "the brain is like a computer" and avoid calling anything beautiful. Precision is what makes this useful.

## Video Overview — customisation prompt

> Same audience and the same four parts, same instruction to assume no prior neuroscience. Prioritise what benefits from being seen: a raster plot of repeated trials with the trial-averaged rate beneath it; the same spike train smoothed with a wide and a narrow window side by side, so the trade-off is visible rather than described; an interspike-interval histogram with and without a refractory period; and a tuning curve with its peak and width annotated. Keep the mathematics on screen where it helps.

## Mind map — structure to check against

Spike train as the observable, then rate as a construct with its three definitions, then estimation methods and the window trade-off, then statistics (Poisson, intervals, Fano factor, departures), then tuning curves, then the open coding question. The three rate definitions should be distinct branches, not one.

## Chat starters

Ask these after listening:

1. Walk me through why a 10 ms window at 20 Hz gives a noisy rate estimate, using actual expected spike counts.
2. If a neuron's Fano factor is 0.4, what does that rule out about its spiking, and what could produce it?
3. Why is the exponential interval distribution the "most common interval is very short" one, when the mean interval is 50 ms?
4. Give me a worked case where the trial-averaged rate is misleading about what the neuron did on any single trial.
5. What would a neuron have to do for a rate code to be impossible in principle, not merely inefficient?
6. Is the choice of smoothing kernel ever a claim about biology rather than about data analysis?
