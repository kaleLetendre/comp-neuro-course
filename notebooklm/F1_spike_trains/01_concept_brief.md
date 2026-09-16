# F1 concept brief — spike trains and firing rates

Teaching substance for the first lesson of a computational neuroscience course. Written to be the source an audio overview is generated from, so it states the ideas rather than pointing at them. Textbook: Dayan & Abbott, *Theoretical Neuroscience*, chapter 1.

## What is actually measured

Put an electrode near a neuron and what you record is a voltage trace with sharp events in it, each about a millisecond wide and around 100 mV tall. Those are action potentials — spikes. The first decision computational neuroscience makes, and it is a decision rather than a discovery, is to **throw the waveform away**. A spike is treated as a point in time: an event, not a shape.

The justification is that spikes from a given neuron are stereotyped — they all look much the same — so the shape carries little that varies with the stimulus. What varies is *when* they happen and *how many* there are. So the raw data of the field is a list of times: 12.3 ms, 47.9 ms, 51.2 ms, and so on. That list is the spike train, and everything else is built on top of it.

This matters more than it sounds. It means the quantities people talk about — firing rates, tuning curves, population codes — are all constructions laid over a list of timestamps. None of them are measured directly.

## Firing rate is not one thing

Ask what a neuron's firing rate is and there are at least three different answers, which are not equal.

**The spike-count rate** is the crudest: count the spikes in a window and divide by its length. Twelve spikes in two seconds is 6 Hz. It is a single number for the whole window, it says nothing about when within that window the spikes fell, and it requires only one trial.

**The time-dependent firing rate r(t)** is what you want when the stimulus changes over time. It is a rate defined at each instant — but a single spike train does not really contain an instantaneous rate, because at any given instant there is either a spike or there is not. Getting r(t) means estimating: smoothing the spikes somehow.

**The trial-averaged rate** takes many repeats of the same stimulus, aligns them, and averages. This is what a peristimulus time histogram shows. It gives a clean r(t), at the cost of assuming the neuron does the same thing each time and that averaging across trials is meaningful. A brain, mid-behaviour, only gets one trial.

So when a paper says "the firing rate", the honest question is: which one, estimated how, over what window?

## Estimation, and the trade-off you cannot escape

Three standard ways to get r(t) from spikes:

**Binning.** Divide time into bins, count spikes in each, divide by bin width. Simple, and it produces a blocky estimate whose appearance depends on where you happened to put the bin edges.

**Sliding window.** Move a window of fixed width along the train and count within it. Smoother, no edge artefacts, but the estimate at time t is contaminated by spikes up to half a window away.

**Kernel smoothing.** Replace each spike with a smooth bump — Gaussian, exponential, alpha function — and add them. The kernel's width sets the smoothness, and a causal kernel (one that only looks backward) matters if you care whether a downstream neuron could actually compute this estimate in real time.

All three face the same trade-off, and it is the central practical point of the lesson. A **wide** window averages over many spikes, so the estimate is stable, but it smears fast changes — a stimulus transient lasting 20 ms vanishes inside a 100 ms window. A **narrow** window tracks fast changes but sees few spikes, so the estimate is dominated by counting noise. At 20 Hz, a 10 ms window contains 0.2 spikes on average: mostly zeros, occasionally a huge spike in the estimate.

You cannot have both. This is bias versus variance, arriving in neuroscience wearing different clothes. The choice of window is a hypothesis about what timescale matters, smuggled in as a preprocessing step.

## Spike train statistics

If a neuron fired completely randomly at a constant mean rate, its spikes would follow a **Poisson process**: each spike independent of the last, no memory. Two properties follow. The intervals between spikes are exponentially distributed, meaning the most common interval is a very short one. And the **Fano factor** — the variance of the spike count divided by its mean, over repeated windows — is exactly 1, at any window length.

Poisson is the reference against which real data is compared. Real cortical neurons are roughly Poisson-like, which is itself surprising and somewhat embarrassing: it means much of the variability looks like noise. But they depart from it in structured ways.

The clearest departure comes from the **refractory period**. After firing, a neuron cannot fire again for a millisecond or two. That forbids the very short intervals a Poisson process produces freely, which makes the spike train more regular than Poisson — and regularity shows up as a reduced Fano factor. For a renewal process, the Fano factor over long counting windows approaches the squared coefficient of variation of the interval distribution, so you can predict the effect before measuring it. Other neurons go the other way: bursting makes spikes clump, variance rises, and the Fano factor exceeds 1.

So the Fano factor is a compact diagnostic. Equal to 1, Poisson-like. Below 1, something is imposing regularity. Above 1, something is imposing clumping.

## Tuning curves

A tuning curve plots a neuron's firing rate against some property of the stimulus — orientation, direction, frequency, position. It is the simplest statement of what a neuron is "about". Its peak names the neuron's preferred stimulus; its width says how sharply it discriminates. A narrow curve means the neuron says a lot when it fires but stays silent for most stimuli; a broad one means it responds to much but distinguishes little. That trade-off returns, sharpened, when decoding is covered later.

Note what a tuning curve already assumes: that a rate is the right summary, and that the neuron's response to a stimulus is stable enough to plot.

## The open question

Does the brain use spike *rates* or spike *timing*? This is not settled, and a course that presents it as settled is lying.

The case for rate: cortical spiking is highly variable, rates vary systematically with stimuli, and rate-based models predict a great deal of behaviour. The case for timing: some systems demonstrably use it — sound localisation resolves interaural delays in the tens of microseconds, far finer than any rate code could carry — and behavioural decisions are sometimes made faster than a downstream neuron could plausibly average a rate.

The honest position is that it is likely both, differently in different systems, and that the answer depends on the timescale of the computation being performed. Hold the question open; it recurs in every later lesson.
