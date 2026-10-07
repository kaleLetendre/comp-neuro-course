# Plan and progress

The map over the whole course. [`foundations.md`](foundations/index.md) and [`lessons.md`](advanced/index.md) hold the lesson specs; this page is the order they go in and a place to track what is done.

## The two halves

**Foundations (F1–F11)** work through Dayan & Abbott end to end, assuming no neuroscience. **Advanced (A, B, C)** go past the textbook into the literature, and depend on the foundations being in place. Between them sits the **Bridge**, a synthesis checkpoint.

Roughly 135 hours: ~60 for foundations, ~75 for advanced.

## The ordering rule

**Foundations first, in order.** F1 before F2 before F3, and so on. The dependency graph:

```
F1 ──┬── F2 ── F3 ── F4
     └── F5 ──┬── F6 ── F8 ── F9 ──┬── F10
               └── F7                └── F11 (also needs F3)
```

Then the **Bridge**, which gates entry to the advanced half.

In the advanced half: **track A is sequential and finishes before track C starts.** Track C is sequential too. Track B runs alongside either and gates nothing, with three dependencies — B4 assumes B2, B2 assumes B3's E/I material, and B5 assumes A2.

The reason A precedes C: spiking dynamics and predictive coding are separate bodies of theory, and the lessons that combine them only make sense once each stands on its own.

## Progress

### Foundations

- [ ] **F1** Spike trains and firing rates
- [ ] **F2** Receptive fields and reverse correlation
- [ ] **F3** Neural decoding
- [ ] **F4** Information theory for neurons
- [ ] **F5** Membrane biophysics and the action potential
- [ ] **F6** Integrate-and-fire neurons and synaptic input
- [ ] **F7** Cable theory and neuronal morphology
- [ ] **F8** Network models: feedforward and recurrent
- [ ] **F9** Synaptic plasticity and learning rules
- [ ] **F10** Classical conditioning and reinforcement learning
- [ ] **F11** Representational learning and generative models
- [ ] **Bridge** Synthesis checkpoint

### Track A — spiking network dynamics

- [ ] **A1** Synaptic delays and temporal structure
- [ ] **A2** Attractors and network state
- [ ] **A3** Oscillations and synchrony
- [ ] **A4** Short-term plasticity, refractory period, reset modes
- [ ] **A5** State of the field: why spiking networks, where they stand

### Track B — biology for people building models

- [ ] **B1** Neuromodulation: dopamine, acetylcholine, noradrenaline
- [ ] **B2** Cortical microcircuits and laminar structure
- [ ] **B3** Dendritic computation
- [ ] **B4** Developmental pruning
- [ ] **B5** Hippocampal replay and consolidation

### Track C — predictive coding

- [ ] **C1** Predictive coding as energy minimization
- [ ] **C2** Inference vs learning: two nested loops and their schedules
- [ ] **C3** Precision weighting
- [ ] **C4** Predictive coding on arbitrary graphs
- [ ] **C5** Clamping and frozen priors
- [ ] **C6** PC ≈ backprop: what the equivalence does and does not claim

## Questions the course leaves open

These are live research questions, not gaps in the material. Each is raised by the lesson named.

- Whether enforcing Dale's principle — that a neuron is excitatory or inhibitory, never both — matters for a model that is not trying to be a brain (B2).
- Whether a model that grows its own structure should add units or add capacity inside existing ones (B3).
- Whether an error-driven growth signal and an activity-driven homeostatic signal should be separate variables (B4).
- Whether a network learning online from a correlated stream needs a replay mechanism, and what the cheapest version looks like (B5).
- Whether the equivalence between predictive coding and backpropagation survives arbitrary topologies, spiking nonlinearities and structural change (C6). It does not, and C6 is about why that matters.

## How to use the coursework

Each lesson has a lecture, a spec with five acceptance criteria, and four pieces of coursework, plus the textbook authors' own exercises for that chapter. Work them in the published order: read, derive, build, explain.

The acceptance criteria are criteria for the *lesson*. If you cannot reason your way to them afterwards, the lesson did not do its job — go back to the section rather than grinding at the question.
