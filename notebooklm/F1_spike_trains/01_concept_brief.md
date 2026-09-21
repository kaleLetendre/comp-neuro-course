# F1 concept brief — spike trains and firing rates

Teaching substance for the first lesson of a computational neuroscience course, generated into an audio overview. It follows **Dayan & Abbott, *Theoretical Neuroscience*, chapter 1** section by section, in the book's own order, so a listener can follow along with the physical copy open.

**A caveat on authority.** This brief was written without the book open. It is standard material aligned to the chapter's actual section headings, but where it and the book disagree, **the book is right**. Terminology and notation in particular may differ in detail.

## How this maps to the chapter

| D&A ch. 1 section | Covered below as |
|---|---|
| Introduction | What computational neuroscience is doing |
| Spike Trains and Firing Rates | The neural response function, and three rates |
| What Makes a Neuron Fire? | Working backwards from spikes to the stimulus |
| Spike-Train Statistics | Poisson, intervals, variability |
| The Neural Code | The unresolved question |

---

## Introduction: what the field is doing

Computational neuroscience builds quantitative models at a chosen level of description, and the choice of level is itself a modelling decision. The book distinguishes descriptive models (what does the system do), mechanistic models (how does it do it) and interpretive models (why does it do it that way). Chapter 1 is descriptive: it is about characterising what neurons do in response to stimuli, without yet asking how.

The raw material is extracellular recording — an electrode near a neuron, producing a voltage trace with sharp events about a millisecond wide.

## Spike trains and firing rates

**The neural response function.** The first move is to discard the spike waveform and keep only the times. Spikes from a given neuron are stereotyped, so the shape carries little stimulus-dependent information; what varies is when they occur and how many. The book formalises the train as a sum of delta functions at the spike times — the neural response function. This is a sequence of events, nothing more, and every quantity that follows is constructed on top of it.

**Three rates, which are not the same quantity.**

The *spike-count rate* counts spikes over a window and divides by its length. Twelve spikes in two seconds is 6 Hz. One number, one trial, no information about when within the window the spikes fell.

The *time-dependent firing rate r(t)* is a rate defined at each moment. A single train does not contain one — at any instant there is a spike or there is not — so r(t) must be estimated by smoothing.

The *trial-averaged rate* repeats the same stimulus many times, aligns the trials and averages. This is what a peristimulus time histogram shows. It buys a clean r(t) by assuming the neuron does the same thing each time; an animal behaving in the world gets one trial.

**Estimating r(t).** The book treats the estimate as a linear filter applied to the spike train — each spike replaced by a kernel, the kernels summed. Rectangular kernels give binning or a sliding window; Gaussian kernels give smooth estimates; an alpha function or exponential gives a causal kernel, one that looks only backwards, which matters if you want the estimate to be something a downstream neuron could actually compute.

Every choice faces the same trade-off. A **wide** kernel averages many spikes, so the estimate is stable, but it smears fast changes — a 20 ms transient disappears inside a 100 ms window. A **narrow** kernel follows fast changes but contains almost no spikes: at 20 Hz, a 10 ms window holds 0.2 spikes on average, so the estimate is mostly zeros punctuated by spikes. Bias against variance, in neural clothing. The width you choose is a hypothesis about what timescale matters, entering the analysis as a preprocessing step.

## What makes a neuron fire?

Having described the response, the chapter turns it around: rather than asking what the neuron does given a stimulus, ask what the stimulus was doing when the neuron fired.

The tool is the **spike-triggered average** — take the stimulus in the window preceding each spike, and average those segments over all spikes. What emerges is the stimulus feature that reliably precedes firing. Related to it is the correlation between firing and the stimulus, which measures how the two covary at different time lags.

Two things to hold onto. First, this is a *reverse* correlation: it runs backwards in time from each spike. Second, the average is only interpretable if the stimulus itself has no structure to impose on the result — which is why white noise is the standard choice. This is introduced here and developed properly in the receptive-fields lesson that follows.

## Spike-train statistics

Real spike trains are variable: repeat a stimulus and the spikes land differently each time. The chapter characterises that variability.

The reference model is the **Poisson process** — spikes independent of one another, no memory of the last one. Two consequences. The intervals between spikes are exponentially distributed, so short intervals are the most common ones even when the mean interval is long. And the **Fano factor**, the variance of the spike count divided by its mean over repeated windows, is exactly 1 at any window length.

Cortical neurons are roughly Poisson-like, which is a genuinely awkward result: it means much of their variability looks like noise rather than signal. But they depart from Poisson in structured ways, and the departures are informative.

The clearest comes from the **refractory period**. Having fired, a neuron cannot fire again for a millisecond or two, which forbids exactly the very short intervals a Poisson process generates freely. Suppressing short intervals makes the train more regular. The **coefficient of variation** of the interval distribution measures that regularity directly — 1 for Poisson, lower for a more regular train — and for a renewal process the Fano factor over long windows approaches the squared coefficient of variation, so the effect can be predicted before it is measured. Bursting pushes the other way: spikes clump, variance rises, the Fano factor exceeds 1.

The **autocorrelation** of the spike train shows the same structure in the time domain, with a dip at short lags where the refractory period suppresses spikes.

## The neural code

The chapter closes on what all of this is in service of: how does a spike train carry information?

An **independent-spike code** assumes each spike contributes separately, so the train's information is the sum over spikes and the rate is a sufficient description. A **correlation code** holds that the relationships between spikes — their relative timing — carry information beyond what the rate contains. Beyond single neurons, a **population code** distributes the message across many cells, and the question becomes whether their correlations matter or whether the cells can be treated independently.

Underneath sits the rate-versus-timing question, and it is open. For rate: cortical firing is highly variable, rates track stimuli systematically, and rate-based models explain a great deal. For timing: some systems clearly depend on it — sound localisation resolves interaural delays in the tens of microseconds, far finer than any rate could encode — and some behavioural decisions happen faster than a downstream neuron could average a rate.

The likely answer is both, in different systems and at different timescales. Do not resolve it; the question recurs in every lesson that follows.
