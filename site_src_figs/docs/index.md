# Computational Neuroscience: a self-study course

A complete, self-paced course in computational neuroscience, built around **Dayan & Abbott's *Theoretical Neuroscience*** and the exercise sets its authors publish free. Twenty-eight lessons, roughly 135 hours, from "what is a spike" to the predictive-coding literature of the last decade.

Everything here is free except the textbook.

## What it teaches

**Foundations — F1 to F11.** The textbook, chapter by chapter, assuming no neuroscience whatsoever.

| | | Chapter |
|---|---|---|
| F1 | Spike trains and firing rates — what is measured, and why a firing rate is a construct rather than a measurement | 1 |
| F2 | Receptive fields and reverse correlation — how a neuron's stimulus preference is measured | 2 |
| F3 | Neural decoding — reading a stimulus back out of spikes, and the bound on how well you can | 3 |
| F4 | Information theory for neurons — what a spike train carries, in bits | 4 |
| F5 | Membrane biophysics and the action potential — why a spike is all-or-none, from channel kinetics | 5 |
| F6 | Integrate-and-fire neurons and synaptic input — the abstraction everything downstream uses, and what it discards | 5 |
| F7 | Cable theory and morphology — why a synapse's position on the dendrite is itself a weight | 6 |
| F8 | Network models — populations, recurrence, and why a weight matrix's eigenvalues govern its behaviour | 7 |
| F9 | Synaptic plasticity and learning rules — Hebb, STDP, and the result that Hebbian learning computes principal components | 8 |
| F10 | Classical conditioning and reinforcement learning — prediction error, from Rescorla-Wagner to actor-critic | 9 |
| F11 | Representational learning — generative models, EM, and why sparse coding on natural images reproduces V1 | 10 |

Then a **synthesis checkpoint** that makes you connect those eleven to each other before anything builds on them.

**Advanced — sixteen lessons in three tracks**, going past the textbook into the literature.

- **A — spiking network dynamics.** Synaptic delays and polychronisation · attractors and network state · oscillations and synchrony · short-term plasticity, refractoriness and reset modes · the state of the field against conventional networks.
- **B — biology for people building models.** Neuromodulation as it actually works · cortical microcircuits and laminar structure · dendritic computation · developmental pruning · hippocampal replay and consolidation.
- **C — predictive coding.** Energy minimisation · inference against learning as two nested loops · precision weighting · arbitrary graph topologies · clamping and frozen priors · what the equivalence with backpropagation does and does not claim.

## Source material

| | |
|---|---|
| **Textbook** | Dayan, P. & Abbott, L.F., *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems* (MIT Press, 2001). The one purchase. Chapter 7 is free from the authors if you want to sample it. |
| **Exercises** | The authors' own problem sets for all ten chapters, with code and data — including twenty minutes of recordings from a fly H1 neuron. Free. These take precedence over this course's exercises wherever they overlap. |
| **Figures, errata, references** | Also free from the authors, and worth having: the errata differs by printing. |
| **Papers** | Twenty-eight for the advanced tracks. Twenty-one can be had for nothing; seven need library access. Two scripts fetch what is fetchable. |

See [Materials](materials.md) for links and the fetch scripts.

## How a lesson works

Each lesson is a **lecture** to read, a **spec** stating what you should be able to answer afterwards, and **coursework** in four pieces:

1. **Guided reading** — specific questions answerable from the named chapter sections
2. **Derivation** — pen and paper, worked with real numbers
3. **Simulation** — a self-contained script, usually under a hundred lines, producing a result you can check
4. **Written explanation** — several hundred words that expose whether the understanding is real

Plus the authors' own exercises for that chapter.

Work them in that order: read, make it exact, build it, explain it. Every simulation in the foundation track was executed before its answers were written down, so the numbers in them are measured rather than plausible.

Each lesson states five things you should be able to answer when it is done. They are acceptance criteria for the lesson, not an exam — if you cannot reason your way to them afterwards, the lesson failed, not you.

## Prerequisites

Comfort with linear algebra, calculus, probability and code. No biology. The course assumes you can read an equation and write a simulation, and assumes nothing about neurons.

## Building the site

This repository is the source. [`BUILD_SITE.md`](https://github.com/kaleLetendre/comp-neuro-course/blob/main/BUILD_SITE.md) explains how to build it yourself, including an offline copy for reading away from a connection, and a separate build that includes the marking criteria.
