# Lessons — goals and acceptance criteria

Companion to [`learning_plan.md`](learning_plan.md), which holds the tracks, the ordering rule and the running progress. This file holds one spec per lesson: what the lesson is for, what it must cover, and the five questions that decide whether it worked.

These are **specs, not lessons**. No lesson content is written yet, and the coursework — worked examples, exercises, anything graded — is a later step.

The five questions under each lesson are **acceptance criteria for the lesson, not an exam**. They describe the reasoning the lesson has to leave you capable of; if you cannot work your way to them afterwards, the lesson failed, not you. Where a question names a figure, the number is the vehicle — the point is the reasoning it forces, and a lesson that produces recall without the reasoning has missed the criterion.

Written 2026-09-15.

## Core text

**Dayan, P. & Abbott, L.F., *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems* (MIT Press, 2001)** — the spine wherever it reaches. Physical copy on hand. Every lesson's **Source material** line names the chapter and section where it applies, and says plainly when it does not.

Coverage, honestly:

| | Lessons | Notes |
|---|---|---|
| **Carries the lesson** | A2, A3, A4, B1, B3 | ch. 7 (recurrent, stochastic and E-I networks), ch. 5 (integrate-and-fire, synaptic conductances, short-term plasticity), ch. 6 (cable equation, compartments), ch. 9 (conditioning and the dopamine prediction-error account) |
| **Grounds part of it** | A0, B4, C1, C2, C5, C6 | ch. 8 (plasticity rules, unsupervised development, supervised learning), ch. 10 (density estimation, causal/generative models, EM) — useful scaffolding that the PC literature then builds on |
| **Absent** | A1, A5, B2, B5, C3, C4 | polychronization, neuromorphic hardware, canonical microcircuits, replay/consolidation, precision weighting, PC on graphs — all postdate the book or sit outside its scope |

Two things the book is worth reading for beyond its chapters: **ch. 10's EM split** is structurally the inference/learning two-loop pattern of C2, and **ch. 7's Boltzmann clamped/free phases** are the same boundary-condition idea as C5's clamping, one formalism over. Both parallels are flagged in the relevant Source material lines.

Nine sources are downloaded to `papers/` (gitignored — regenerate with `fetch_papers.py` at the repo root, which also holds the full verified bibliography with DOIs). Three of those are Europe PMC full text saved as `.txt` rather than PDF, because the publisher's PDF is not openly served: readable prose, but no figures and no rendered equations — for Bogacz 2017 in particular, get the real PDF when you have library access, since the equations are the point. The other sixteen references need institutional access and are marked as such on each lesson. Every DOI and PMID was resolved against Europe PMC, so the citations themselves are verified even where the file is not on disk.

Its blind spot for this project is predictive coding itself — Rao & Ballard came out in 1999 and did not make the book. Bogacz's 2017 tutorial is the substitute entry point for track C.

## Order and gating

```
Track A (raw SNN)      A0 → A1 → A2 → A3 → A4 → A5 ──┐
                                                      ├──► Track C opens
Track B (biology)      B1 · B3 · B2 → B4 · B5 (needs A2)   — any order, anytime
                                                      │
Track C (PC theory)                    C1 → C2 → C3 → C4 → C5 → C6 → fusion design (Steps 3-5)
```

- Track A is strictly sequential and must finish before track C starts. That rule was set 2026-06-19 and still holds.
- Track B runs alongside on its own cadence and gates nothing, with three dependencies: B4 assumes B2, B2 assumes the E/I and PV/SST/VIP material already written up in `comp_neuro_notes.md` (Adaptive-Web-PC-SNN repo), and B5 assumes A2 (attractors and state).
- Track C is sequential. C1 additionally needs A2 (energy landscapes), which is automatic given the A-before-C rule.
- C6 is the last lesson. Passing it unlocks fusion design on Steps 3-5.

---

## Track A — raw SNN

### A0. Consolidation: what you already know

**Prerequisites:** none — this re-tests everything covered before A1 (STDP, LIF, encoding schemes, E-I balance, homeostasis, credit assignment, eligibility traces + three-factor rule)

**Size:** one sitting — diagnostic only, no new material

**Source material:** **D&A ch. 5** *Integrate-and-Fire Models* (LIF); **ch. 1** *Spike Trains and Firing Rates* and *The Neural Code*, **ch. 3** *Population Decoding* (encoding/decoding); **ch. 8** *Synaptic Plasticity Rules* (Hebb, STDP, normalization); **ch. 7** *Excitatory-Inhibitory Networks*. Eligibility traces and three-factor rules are **not** in D&A — nearest is **ch. 9** on temporal-difference learning. Plus your own `comp_neuro_notes.md`.

**Local copies:** none needed — this lesson is D&A plus your own notes.

**Goal:** Confirm the pre-A1 foundation still holds after the ~3-month gap, or find exactly where it has decayed, before A1 onward builds on it. No new concepts — a diagnostic pass that either clears the learner to proceed or names specific topics to re-teach.

**Scope:**
- STDP: sign of the weight change vs spike-timing order, and how magnitude falls off with |Δt| across the ~20 ms window
- LIF: reproducing a membrane trajectory, threshold crossing and refractory behaviour with concrete numbers, not just the shape of the equation
- Encoding schemes (rate, latency, population): the specific trade-off each makes
- E-I balance and homeostasis: why synaptic scaling runs on a slow cadence distinct from STDP's tens-of-ms, and what it corrects that STDP cannot
- Not covered: any new mechanism — delays, attractors, oscillations are A1–A3

**You should be able to answer:**
1. A pre-synaptic spike fires 8 ms before the post-synaptic spike, under a standard ~20 ms exponential STDP window. Does the synapse potentiate or depress, and is the change closer to the window's peak or its tail compared to a Δt of 2 ms?
2. A LIF neuron with τ_m = 10 ms sits at −65 mV (threshold −55 mV); a constant input drives the steady state toward −50 mV. Roughly how many time constants until it crosses threshold, and why does it never actually reach −50 mV in a real run?
3. Latency coding can convey a value in a single spike's timing, faster than rate coding's ~50–100 ms averaging window. Name one concrete weakness of latency coding that gives rate coding back the advantage in a specific task.
4. Synaptic scaling operates on hours-to-days, STDP on tens of milliseconds. What specific runaway failure mode does synaptic scaling correct that STDP, left alone, cannot?
5. Your "misted chemical" model broadcasts one scalar over the whole network, and each synapse scales its own change by how recently it was active. Name one thing backprop's chain rule can do — assigning credit differently across neurons — that a single global broadcast scalar structurally cannot.

**Project tie-in:** The three-factor rule under test here is what the purely-local constraint depends on for Steps 3–5; a shaky grasp of STDP or eligibility traces now surfaces as a bug in Step 3 rather than as a gap in understanding.

**Done when:** Each question can be reasoned through unaided — or the miss is logged as a named gap to close before A1.

---

### A1. Synaptic delays and temporal structure

**Prerequisites:** A0; LIF dynamics, the STDP timing window, rate/latency/population encoding

**Size:** one to two sittings

**Source material:** Thin in D&A — **ch. 5** *Synaptic Conductances* and **ch. 6** *The Cable Equation* give transmission and propagation, but not delay as a computational resource. Primary: Izhikevich 2006, *Polychronization: Computation with Spikes*. Supporting: Gerstner et al., *Neuronal Dynamics* (free online) on transmission delays.

**Local copies:** `papers/A1_izhikevich_2006_polychronization.pdf`. *Neuronal Dynamics* is free at neuronaldynamics.epfl.ch.

**Goal:** Replace the instantaneous weight-matrix picture — spike in, weighted sum out, same tick — with one where *when* a spike arrives matters as much as how strong it is. Topology plus delays is a computation over time, not just space. Walks away able to distinguish delay-based mechanisms (coincidence detection, delay lines) from weight-based ones.

**Scope:**
- Real figures: axonal conduction delay (~0.5–10 ms depending on myelination and distance) vs synaptic transmission delay (~0.3–3 ms), and where these numbers come from physically
- How delay converts a static weight matrix into a temporal computation: coincidence detection and delay lines
- Delay as a third learnable or evolvable parameter alongside weight and connectivity — what it means for a virtual-memristor synapse to store a delay as well as a weight
- Polychronous groups (Izhikevich 2006): memory that lives in the delay structure, requiring no weight change
- Not covered: network-wide rhythms and synchrony (A3), attractor dynamics (A2)

**You should be able to answer:**
1. Give typical ms ranges for axonal conduction delay vs synaptic transmission delay, and name one anatomical factor that shortens each.
2. Describe a concrete 2-input circuit where a delay difference — not a weight difference — is what makes a downstream neuron fire.
3. If two synapses feeding the same neuron have delays of 3 ms and 7 ms, under a ±20 ms STDP window, does that 4 ms gap meaningfully change which side of the STDP curve a near-simultaneous pre/post pairing lands on?
4. What does a polychronous group store — weights, delays, or both — and why can one fixed network support many more such groups than it has neurons?
5. Name one way delay could be treated as a plastic parameter like a weight, and one way it is more naturally treated as fixed structural wiring.

**Project tie-in:** Feeds Step 3 directly — whether the virtual-memristor synapse carries a delay field alongside its weight, and whether the prediction→error neuron link inside a neuron pair should account for transmission lag.

**Done when:** The learner can sketch a coincidence-detection circuit with explicit delay values and state why polychronous-group memory needs no weight update.

---

### A2. Attractors and network state

**Prerequisites:** A1; LIF dynamics, graph topology with reciprocal connections, homeostasis

**Size:** two to three sittings — includes running the diagnostic against the saved model

**Source material:** **D&A ch. 7** *Recurrent Networks* (selective amplification, continuous line attractors, bump/ring attractors) and *Stochastic Networks* (energy functions, Hopfield/Boltzmann) — the core text for this lesson. Supporting: Hopfield 1982 (PNAS) for the original.

**Local copies:** none — Hopfield 1982 (doi:10.1073/pnas.79.8.2554) needs institutional access. D&A ch. 7 carries the lesson without it.

**Goal:** Describe network state as a point moving on an energy landscape, explain why a trained recurrent network settles to discrete fixed points instead of drifting, and separate state (fast, per-trial) from weights (slow, cross-trial) as two memory timescales. Closes the gap exposed by the learner's own CartPole attractor test: they can observe distinct settled states but have no principled way to decide whether those are real basins or an artifact of stopping too early.

**Scope:**
- Energy/Lyapunov framing: fixed points as local minima, basins of attraction, why symmetric recurrent weights guarantee convergence
- Hopfield network as the worked example: patterns as attractors, capacity limits, spurious attractors
- State as short-term memory vs weights as long-term memory — why the same weights give different committed outputs from different starting states
- Diagnosing genuine multi-basin structure vs unconverged slow modes: convergence-rate check (geometric decay vs plateau), perturbation test, Jacobian/eigenvalue check near the fixed point
- Attractors in spiking networks: bump attractors, persistent activity
- Not covered: limit cycles and rhythmic dynamics (A3), the PC energy function itself (C1)

**You should be able to answer:**
1. In a Hopfield network, why does a symmetric weight matrix guarantee the energy never increases as the state updates?
2. Give a concrete perturbation-test protocol for the saved 256-neuron CartPole network that distinguishes "20 genuine basins" from "20 slow-converging trajectories" — what do you perturb, what do you measure, and what result rules out which hypothesis?
3. In your attractor test, pairwise L2 distance dropped from ~2.1 (100 iters) to ~1.7 (10000 iters) — ~19% over a 100× increase in iterations. Is that consistent with geometric convergence to fixed points, or with a slow mode still relaxing? What further datapoint settles it?
4. What stays fixed and what changes when you compare "the network learns" to "the network settles to an answer for one input"?
5. What is a bump attractor, and how does persistent spiking activity implement a fixed point when individual neurons cannot hold a static real-valued output?

**Project tie-in:** Resolves the open interpretation question left by the 2026-04-15 attractor test in `comp_neuro_notes.md`, and explains why state persists across CartPole timesteps in `network.py` / `online_rollout.py` independently of weight updates.

**Done when:** The learner designs and describes, unprompted, the diagnostic in question 2 and runs it against the saved model — evidence, not intuition.

---

### A3. Oscillations and synchrony

**Prerequisites:** A1, A2; E-I balance, lateral inhibition / WTA, Dale's principle

**Size:** one to two sittings

**Source material:** **D&A ch. 7** *Excitatory-Inhibitory Networks* — D&A derives oscillation onset from E-I dynamics directly, which is exactly the PING mechanism. Not in D&A: communication-through-coherence and phase coding — Fries 2005; Wang 2010 (Physiol Rev) for a rhythms review; Buzsáki, *Rhythms of the Brain*, for breadth.

**Local copies:** none — Fries 2005 (doi:10.1016/j.tics.2005.08.011) and Wang 2010 (doi:10.1152/physrev.00035.2008) both need institutional access.

**Goal:** Understand how an E-I feedback loop plus conduction delays produces a population rhythm, why different frequencies map to different circuit time constants and functions, and that relative phase — not just rate — can carry information and gate which inputs get through. Closes the gap between "oscillations are a side effect of recurrent circuits" and "oscillations are a functional routing mechanism", with both positions statable.

**Scope:**
- PING vs ING: how the E→I→E loop and its time constants set cycle period; why inhibition, not excitation, paces the rhythm
- Bands with real numbers: theta ~4–8 Hz (long loop, navigation and sequence memory) vs gamma ~30–80 Hz (short local loop, feature binding and attention)
- Communication-through-coherence: spikes arriving inside vs outside a receiving neuron's excitability window
- The binding problem and phase alignment across assemblies
- Phase-of-firing as an information channel additional to rate
- Not covered: replay and sharp-wave ripples (B5), attractor fixed points (A2)

**You should be able to answer:**
1. Given excitatory decay ~5 ms, inhibitory decay ~10 ms and a 2 ms loop delay, estimate whether the rhythm lands in gamma or theta, and why.
2. Why does a short local E-I loop produce gamma while a longer loop produces theta — what specifically about loop delay changes?
3. In a 25 ms gamma cycle with a 5 ms postsynaptic excitability window, work out whether two inputs 12 ms apart in phase both get through, and what determines the answer.
4. Give a concrete example of information carried in phase-of-firing that could not be recovered from rate alone.
5. State the strongest evidence that oscillations are causally functional, and the strongest evidence they are epiphenomenal — one piece each.

**Project tie-in:** Bears on Step 3 — whether coordination across graph nodes needs an explicit phase/synchrony mechanism, or whether the purely-local constraint (no global clock) can achieve equivalent routing without a shared oscillatory reference.

**Done when:** The learner sketches the PING loop timing diagram unprompted, places theta and gamma with their functions, and gives one concrete piece of evidence for each side of the functional-vs-epiphenomenal debate.

---

### A4. Short-term plasticity, refractory period, reset modes

**Prerequisites:** A1; STDP, LIF dynamics, eligibility traces and three-factor rules

**Size:** one sitting

**Source material:** **D&A ch. 5** *Synaptic Conductances* (release probability, short-term depression and facilitation) and *Integrate-and-Fire Models* (refractoriness, reset) — both knobs in one chapter. Supporting: Tsodyks & Markram 1997 (PNAS) for the canonical STP model. Trace-stacking is an implementation choice, not in either.

**Local copies:** none — Tsodyks & Markram 1997 (doi:10.1073/pnas.94.2.719) needs institutional access. D&A ch. 5 covers short-term plasticity.

**Goal:** Split short-term plasticity off from the single "synaptic change over time" bucket: STP is a separate, self-reversing mechanism that scales transmission without touching the stored weight. Then pin down two implementation knobs — reset mode and trace-stacking rule — that decide what a neuron carries forward tick to tick.

**Scope:**
- Short-term facilitation (residual calcium) and depression (vesicle depletion): what variable changes — a resource/utilization term, not w — its ~100s-of-ms decay, and why it undoes itself with no input
- STP vs STDP: the variable each modifies, timescale, permanence
- Absolute vs relative refractory period and the firing-rate ceiling each imposes
- Reset-to-zero vs subtract-threshold: the fate of overshoot voltage and its effect on next-spike timing
- Eligibility-trace stacking on repeated spikes: additive vs saturating accumulation
- Not covered: neuromodulator dynamics (B1), long-term plasticity rules (already known)

**You should be able to answer:**
1. A neuron has an absolute refractory period of 2 ms. What is its maximum possible firing rate in Hz?
2. In a Tsodyks-Markram-style facilitation model with baseline U = 0.2, each spike updating U ← U + 0.2(1 − U), and three spikes 10 ms apart (decay negligible) — what is U just after the third spike?
3. A neuron's membrane hits 1.2× threshold at spike time. Under reset-to-zero, what happens to the 0.2× overshoot? Under subtract-threshold, what happens to it, and how does that change next-spike timing?
4. Three spikes land within an eligibility trace's decay window. Under additive stacking, what happens to the peak trace value? Under saturating stacking, what caps it? Why does this matter for the size of a weight update triggered by a delayed reward signal?
5. Does short-term depression modify the weight w or a separate resource variable? If the synapse then receives no input for 500 ms, what happens to that variable?

**Project tie-in:** The virtual-memristor synapse currently models one persistent weight; STP needs an additional transient resource variable decaying independently of w — a Step 3 design question, and distinct from the persisted weights in `online_rollout.py`.

**Done when:** The learner computes a firing-rate ceiling from a refractory period and explains, without conflating them, how STP, reset mode and trace stacking each separately affect what a neuron carries forward.

---

### A5. State of the field: why SNNs, where they stand vs ANNs

**Prerequisites:** A0–A4. Closing lesson of track A; passing it opens track C.

**Size:** one to two sittings

**Source material:** **Not in D&A** — the book predates the neuromorphic hardware era. Attwell & Laughlin 2001 for the cortical energy budget; Roy, Jaiswal & Panda 2019 (Nature) on spike-based machine intelligence; current vendor documentation at teaching time — see the perishability note in Scope.

**Local copies:** none — Attwell & Laughlin 2001 (doi:10.1097/00004647-200110000-00001) and Roy et al. 2019 (doi:10.1038/s41586-019-1677-2) both need institutional access.

**Goal:** State the brain's energy budget with real numbers and use it to make — or refute — the energy argument for SNNs; classify the major neuromorphic chips by what they actually support; give an honest account of the accuracy and tooling gap. Turns "SNNs are efficient" from a slogan into a claim defensible with figures in front of an examiner.

**Scope:**
- Brain energy budget: ~20 W, ~86B neurons, ~10¹⁴–10¹⁵ synapses, sparse mean firing rates (~1–5 Hz), and what that implies per synaptic event versus a GPU's per-MAC energy
- Event-driven vs clocked computation: why "no spike, no computation" changes the equation, and the dense/high-rate regime where it stops applying
- Real hardware as illustration: Loihi 2, SpiNNaker 2, IBM TrueNorth/NorthPole, memristor crossbars — and the recurring axes they differ on (digital vs analog, on-chip learning or inference-only, topology freedom, weight precision)
- The honest gap: accuracy on MNIST / CIFAR-10 / ImageNet-scale, tooling maturity (PyTorch vs snnTorch/Norse/vendor SDKs), and the ANN-to-SNN conversion criticism
- Where SNNs genuinely win: event cameras, always-on sensing, low-latency control — with numbers
- Not covered: PC-specific efficiency and locality claims (track C), biological energy detail beyond the headline budget
- Perishable: specific chip capabilities and benchmark numbers date fast. Check them when the lesson is taught. What should survive is the shape of the argument, not the table.

**You should be able to answer:**
1. From ~20 W across ~10¹⁵ synapses firing at a few Hz, derive the rough energy per synaptic event — and say what has to be true of a workload before that figure is the right thing to compare against a GPU's per-MAC energy.
2. What are the recurring axes on which neuromorphic chips differ, and which of them actually constrain this project's design? Use two current chips as illustrations rather than as the answer.
3. What is the ANN-to-SNN conversion criticism, and what does a conversion-based accuracy number hide about the cost of getting it?
4. How would you establish the current accuracy gap between natively trained SNNs and ANNs — and what would a large gap tell you about where the difficulty sits: the neuron model, the learning rule, or the tooling?
5. What property must a task have for event-driven hardware to win on latency or power? Name one task that has it and one that plainly does not.

**Project tie-in:** Grounds why the project insists on purely local learning and virtual-memristor synapses — that choice targets the hardware surveyed here, not accuracy parity with backprop-trained ANNs on the Step 1–2 benchmarks.

**Done when:** The learner can derive the per-event energy figure rather than recall it, argue the efficiency case to a skeptic without leaning on a memorized table, and explain why the Step 1–2 benchmark numbers are not an apples-to-apples accuracy contest.

---

## Track B — biology, running alongside

### B1. Neuromodulation proper: dopamine, acetylcholine, noradrenaline

**Prerequisites:** three-factor rules, eligibility traces, E-I balance; the astrocyte write-up in `comp_neuro_notes.md`

**Size:** one to two sittings

**Source material:** **D&A ch. 9** *Classical Conditioning* and *Static/Sequential Action Choice* — Rescorla-Wagner, temporal-difference learning and the dopamine prediction-error account, written by Dayan himself. Not in D&A: ACh and noradrenaline as uncertainty signals — Yu & Dayan 2005 (Neuron). Supporting: Schultz, Dayan & Montague 1997 (Science) for the recordings.

**Local copies:** none — Schultz et al. 1997 (doi:10.1126/science.275.5306.1593) and Yu & Dayan 2005 (doi:10.1016/j.neuron.2005.04.026) need institutional access. D&A ch. 9 is the standing substitute.

**Goal:** Replace "a success/error chemical is misted over the whole network, each synapse scales by how brightly it is glowing" with what the modulators actually do: distinct signals (reward prediction error vs uncertainty vs gain), released with real spatial and temporal structure, read out with a sign that depends on local receptor type.

**Scope:**
- Dopamine as reward-prediction-error: Schultz's recordings at cue, at reward, and at omission
- ACh and noradrenaline per Yu & Dayan: expected vs unexpected uncertainty, plus gain control on cortical responsiveness
- Volume transmission: real diffusion radius (tens to hundreds of microns) and timescale (hundreds of ms to seconds) vs synaptic transmission, and vs the instantaneous global broadcast a three-factor rule assumes
- Where the abstraction holds (slow, spatially broad, gates plasticity) and where it breaks (multiple co-active modulators, receptor-dependent sign such as D1 vs D2, target-specific innervation density)
- Not covered: astrocytic modulation (already written up), specific interneuron types (B2)

**You should be able to answer:**
1. In Schultz's paradigm, what does a dopamine neuron do at cue, at reward, and at omission of an expected reward — and why is the omission response the strongest evidence against "reward = fixed brightness signal"?
2. Give rough numbers: diffusion radius and timescale of volume transmission vs a synaptic release event.
3. A cue's meaning shifts unpredictably. Which modulator dominates, ACh or NE, and why?
4. Why can the same dopamine concentration increase plasticity at a D1-expressing synapse and decrease it at a D2-expressing one — and what does that break in the "one chemical, one direction" model?
5. State one concrete, specific way your "misted chemical" model is factually wrong about real biology.

**Project tie-in:** Any three-factor-style rule in Steps 3–4, and the stress variable itself, currently assumes a single scalar broadcast. This is the check on whether that is a defensible simplification or needs separate reward-like and uncertainty-like channels before it gates growth and pruning.

**Done when:** Question 5 is answered with a specific correct mechanism — not a restatement of the goal — without further prompting.

---

### B2. Cortical microcircuits and laminar structure

**Prerequisites:** the PV/SST/VIP-to-PC-quantities mapping and the Dale's principle discussion in `comp_neuro_notes.md`

**Size:** two to three sittings

**Source material:** **Largely absent from D&A** — closest is **ch. 2** *Introduction to the Early Visual System* and *Constructing V1 Receptive Fields* for the feedforward story, which is the part this lesson complicates. Primary: Bastos et al. 2012 (Neuron), *Canonical microcircuits for predictive coding*; Hertäg & Sprekeler 2020 (eLife), the read already flagged in `comp_neuro_notes.md`.

**Local copies:** `papers/B2_hertag_sprekeler_2020_prediction_error_neurons.pdf`. Bastos et al. 2012 (doi:10.1016/j.neuron.2012.10.038) needs institutional access.

**Goal:** Name which cortical layer does what, and map Bastos et al. (2012)'s canonical microcircuit onto predictive coding: superficial layers carrying error, deep layers carrying predictions, with a feedforward/feedback asymmetry in both wiring and frequency band. Closes the gap between "PV/SST/VIP compute PC quantities" (functional, no wiring) and "those quantities live in a specific six-layer scaffold" (structural), and forces a decision on whether the column is real enough to justify a Step 5 cluster unit.

**Scope:**
- The six layers and their canonical roles: L4 thalamic input, L2/3 cortico-cortical output, L5 subcortical output, L6 corticothalamic feedback
- Bastos et al. 2012: superficial pyramidal cells as error units sending driving feedforward connections terminating in L4 of the target area (gamma); deep pyramidal cells as prediction units sending modulatory feedback that avoids L4 (beta/alpha)
- Where PV, SST and VIP sit in that scaffold (Hertäg & Sprekeler): PV perisomatic inhibition gating feedforward drive, SST dendrite-targeting inhibition onto L1 apical tufts gating predictions, VIP disinhibiting SST — reconciled with the precision / prediction-mean / uncertainty mapping already known
- Cortical columns: the evidence for (anatomical repetition, Mountcastle) and against (functional heterogeneity across areas and species) treating the column as a real functional unit
- Not covered: dendritic computation within a pyramidal cell (B3), neuromodulatory gain control of the circuit (B1)

**You should be able to answer:**
1. Which numbered layer receives thalamic feedforward input, and which projects back to thalamus?
2. In Bastos et al. 2012, which layers are the error units and which the prediction units, and which frequency band is linked to each direction?
3. Trace a feedforward error signal from L2/3 of area A — which layer does it terminate in, in area B, and why does that matter for the feedforward/feedback asymmetry?
4. Where does SST inhibition land anatomically, and how does that location support SST encoding the mean of a top-down prediction rather than precision?
5. Give one piece of evidence for and one against the cortical column as a real functional unit, then say which way your evidence points.

**Project tie-in:** Step 5 wants cortices as dense clusters with sparse inter-cluster links. This supplies the internal layout — a superficial error sub-population, a deep prediction sub-population, feedforward links terminating on the error layer, feedback links avoiding it — making the cluster a specific circuit rather than an unstructured blob.

**Done when:** The learner sketches a six-layer canonical microcircuit with PV/SST/VIP placement and proposes a specific Step 5 cluster wiring diagram from it, without re-deriving the PC-quantity mapping.

---

### B3. Dendritic computation

**Prerequisites:** the point-neuron LIF model; E/I and Dale's principle

**Size:** one to two sittings

**Source material:** **D&A ch. 6** *The Cable Equation* and *Multi-compartment Models* — the passive grounding for why location is a weight, and the machinery for compartmental models. Not in D&A: the two-layer and apical-gating accounts — Poirazi, Brannon & Mel 2003 (Neuron); Larkum 2013 (TINS); London & Häusser 2005 for an overview.

**Local copies:** none — all three need institutional access (Poirazi doi:10.1016/S0896-6273(03)00149-1; Larkum doi:10.1016/j.tins.2012.11.006; London & Häusser doi:10.1146/annurev.neuro.28.061604.135703). D&A ch. 6 covers the cable-theory half.

**Goal:** Replace the point neuron — soma sums weighted inputs — with dendrites as active, spatially structured compartments. Why a synapse's location on the tree changes its effective weight, why a branch can spike on its own, and how apical input can gate somatic firing: a top-down prediction mechanism inside a single cell, before any network-level PC machinery.

**Scope:**
- Passive cable properties: distal current attenuates before reaching the soma, so location is an implicit weight independent of synaptic strength
- Active dendrites: NMDA and calcium spikes as branch-local thresholded events, distinct from the somatic Na⁺ spike
- Poirazi & Mel's two-layer-network-in-a-neuron: branches as a hidden layer of nonlinear subunits feeding a somatic output unit, and the rough capacity gain over a linear point neuron
- Larkum's apical-tuft mechanism: apical (feedback) and basal (feedforward) input on separate compartments, and how coincidence at the tuft gates or amplifies the somatic response
- Not covered: which cortical layers apical and basal inputs come from (B2), spine pruning (B4)

**You should be able to answer:**
1. Two synapses deliver the same peak current, one proximal, one 300 μm out on a distal branch — which produces the larger somatic EPSP, and why in terms of cable properties?
2. What distinguishes an NMDA spike from the somatic Na⁺ spike — what triggers it, and does it stay local to the branch?
3. In Poirazi & Mel's model, what are the two layers, and roughly how much does capacity rise compared to a linear point neuron?
4. In Larkum's model, which compartment receives basal input and which apical, and what happens to somatic output when both arrive together vs apical alone?
5. If basal input alone produces a normal spike but apical input alone produces none, what does that predict about a neuron receiving strong bottom-up drive with no matching top-down signal?

**Project tie-in:** Step 4's stress mechanism currently has one lever when a neuron cannot predict its input — grow a new neuron pair. Active dendrites suggest a second: give the existing prediction neuron more internal capacity instead.

**Done when:** All five answered unprompted, and the learner can state the two-lever design tension (grow a pair vs add dendritic capacity) that B3 hands to Step 4.

---

### B4. Developmental pruning: how brains choose their own size

**Prerequisites:** B2; homeostasis (synaptic scaling, threshold adaptation)

**Size:** one sitting

**Source material:** **D&A ch. 8** *Unsupervised Learning* — Hebbian development, synaptic competition and normalization, ocular dominance. Not in D&A: the elimination machinery and critical-period closure — Schafer et al. 2012 (Neuron) on microglia and complement; Hensch 2005 (Nat Rev Neurosci) on critical periods; Huttenlocher & Dabholkar 1997 for the density-over-development numbers.

**Local copies:** none — Schafer et al. 2012 (doi:10.1016/j.neuron.2012.03.026), Hensch 2005 (doi:10.1038/nrn1787) and Huttenlocher & Dabholkar 1997 (doi:10.1002/(SICI)1096-9861(19971020)387:2<167::AID-CNE1>3.0.CO;2-Z) all need institutional access.

**Goal:** State, with real developmental numbers, that mammalian brains build far too many synapses and cut most back rather than growing to a target — and that elimination is an active, cell-mediated process, not passive decay. Closes the gap between Step 4's "stress triggers growth" and the fact that biological growth is front-loaded and largely undirected, while the real control lever is selective, signal-marked removal.

**Scope:**
- Overproduction and elimination timeline: peak synaptic density age in human cortex, elimination continuing into adolescence, and the fraction gone by adulthood (~40–50%)
- Activity-dependent competition: what correlated vs uncorrelated activity does to a synapse's survival odds, distinct from Hebbian strengthening
- The marking signal: complement tagging (C1q/C3) flags weak or inactive synapses; microglia phagocytose the tagged ones — machinery, not weight decay
- Critical periods: what one is operationally, ocular dominance as the example, and what closes it (inhibitory maturation, perineuronal nets)
- Adult neurogenesis: where it demonstrably occurs and how restricted it is — a direct reality check on the project's growth mechanism
- Not covered: the PC error signal that would drive stress (track C), synaptic scaling mechanics (already known)

**You should be able to answer:**
1. At what age does human cortical synapse density peak, and roughly what fraction of synapses present at peak are gone by adulthood?
2. Two synapses have identical weight but different recent activity correlation with their partners — which survives, and what is the actual tagging step between "weak" and "physically removed"?
3. Name the two cellular/molecular players in synapse elimination and say which one tags and which one eats.
4. What closes the ocular-dominance critical period, and why can the same manipulation not reopen it in an adult?
5. Name one adult mammalian region that still generates neurons — then say whether Step 4's growth should be modelled as constant background neurogenesis or as front-loaded overproduction plus pruning, and why.

**Project tie-in:** Directly sets Step 4 policy: the overproduction data argues for seeding excess neuron pairs early and pruning down rather than growing on demand per stress spike, and complement tagging argues for a two-stage mark-then-remove rule rather than a single near-zero-weight threshold.

**Done when:** The learner states a specific growth-rate and pruning-threshold policy for Step 4, citing the elimination fraction and the tag-then-remove principle as justification.

---

### B5. Hippocampal replay and consolidation

**Prerequisites:** A2 (attractors and network state); the Step 2b online-learning results

**Size:** one to two sittings

**Source material:** **Not in D&A.** McClelland, McNaughton & O'Reilly 1995 (Psych Review) for the CLS argument; Foster & Wilson 2006 (Nature) on reverse replay; Ólafsdóttir, Bush & Barry 2018 for a current review.

**Local copies:** `papers/B5_olafsdottir_2018_replay_memory_planning.txt` (full text, no OA PDF). McClelland et al. 1995 (doi:10.1037/0033-295X.102.3.419) and Foster & Wilson 2006 (doi:10.1038/nature04587) need institutional access.

**Goal:** State why a fast one-shot store and a slow interference-free store are in tension (the CLS argument), what sharp-wave ripple replay actually looks like in data, and how both map onto catastrophic forgetting and experience replay in ML. Closes the gap between "replay sounds like a buzzword" and "replay is the specific fix for a specific interference problem the online-learning work has already hit".

**Scope:**
- Sharp-wave ripple replay as observed: forward and reverse place-cell sequences, ~10-20x temporal compression, in quiet wake and slow-wave sleep rather than during active behaviour
- Systems consolidation: hippocampus as fast episodic store, neocortex as slow interleaved store, replay as the offline training signal between them
- Complementary Learning Systems (McClelland, McNaughton & O'Reilly): the explicit argument that one network cannot be both fast-learning and interference-free, stated as a trade-off rather than an assertion
- Catastrophic forgetting as the ML restatement of the same problem, and RL experience-replay buffers as the engineering answer - what corresponds to hippocampal replay and what does not
- Preplay of never-experienced trajectories, and what it implies about planning versus pure rehearsal
- Not covered: the mechanisms generating ripple oscillations (A3), the PC inference/learning schedule (C2)

**You should be able to answer:**
1. Roughly what compression factor does hippocampal replay run at relative to the original behavioural sequence, and in which behavioural states does it occur?
2. State the CLS argument in one sentence: why can a single network not be both a fast one-shot learner and interference-free?
3. In the Step 2b online rollout, what symptom would indicate catastrophic forgetting, and how would you tell it apart from the state-dependent output the attractor test already demonstrated?
4. What does preplay of an unvisited trajectory rule out as an explanation for replay?
5. Name one concrete difference between a hippocampal replay episode and a sample drawn from an RL experience-replay buffer - ordering, compression, or source of samples.

**Project tie-in:** The Step 2b online rollout updates weights live from a single correlated stream with no buffer and no replay step. This lesson supplies the basis for diagnosing whether the instability seen there is starvation for interleaved replay rather than a learning-rate or optimizer-state problem.

**Done when:** The learner states, unprompted, whether the current Step 2b setup needs a replay mechanism and sketches the cheapest version of one in a sentence or two.

---

## Track C — predictive coding theory

### C1. Predictive coding as energy minimization

**Prerequisites:** A2 (energy landscapes, fixed points); working familiarity with the Step 1/2 settling loop

**Size:** two to three sittings — the hand derivation is the point, don't rush it

**Source material:** **D&A ch. 10** *Causal Models for Density Estimation* — generative models, EM and the Helmholtz machine: the textbook grounding for "a node predicts its input and the residual is the error". PC itself is not in D&A. Primary: Bogacz 2017 (J Math Psychol), *A tutorial on the free-energy framework* — the best entry point; Rao & Ballard 1999 (Nat Neurosci) for the original.

**Local copies:** `papers/C1_bogacz_2017_free_energy_tutorial.txt` (full text, no OA PDF). Rao & Ballard 1999 (doi:10.1038/4580) needs institutional access.

**Goal:** Write down the PC energy function for a small layered network, take its gradient with respect to one node's activity by hand, and explain why that gradient depends only on quantities local to the node. Closes the gap between "I have run settling loops" and "settling is gradient descent on a specific scalar function".

**Scope:**
- Generative-model framing: each node predicts its inputs from its neighbours' activities and the weights on those edges
- Energy as a sum of squared prediction errors; its relation to negative-log Gaussian free energy at precision 1
- Hand derivation: write E for a 3-node chain, take ∂E/∂x for the middle node, show which terms survive
- The error neuron as the physical carrier of one error term in that sum
- Settling as gradient descent on E with weights fixed, connecting to A2's fixed points as energy minima
- Not covered: weight updates and schedule (C2), precision ≠ 1 (C3), non-layered graphs (C4)

**You should be able to answer:**
1. For a 3-node chain x₀ → x₁ → x₂ with prediction x̂₁ = w·x₀, write the full energy E as a sum of two error terms.
2. Given x₀ = 1, w = 2, x₁ = 1.5, compute the local error e₁ = x₁ − x̂₁.
3. Take ∂E/∂x₁ by hand for that chain and state which two terms in E contribute, and which do not.
4. Name the three quantities ∂E/∂x₁ depends on, and say why none of them require information from outside x₁'s immediate neighbours.
5. If settling is gradient descent on E, what does it mean for a node's activity to be at a fixed point, in terms of ∂E/∂x?

**Project tie-in:** The formal justification for the purely-local constraint — the settling loops in `steps/02_pc_graphs/` and `steps/02b_persistent_state/network.py` are running exactly this gradient descent, and the error-neuron-as-energy-term view is what makes the neuron-pair abstraction principled rather than merely convenient.

**Done when:** The learner derives ∂E/∂x₁ for the 3-node example from scratch without being shown the formula, and identifies it as depending only on local pre/post activity and local error.

---

### C2. Inference vs learning: two nested loops and their schedules

**Prerequisites:** C1

**Size:** one to two sittings

**Source material:** **D&A ch. 10** *Density Estimation* — the E-step/M-step split of EM is structurally the same two nested loops (infer activity with parameters fixed, then update parameters), and worth reading precisely for that parallel. Primary: Bogacz 2017, the learning sections; Millidge, Seth & Buckley 2021, *Predictive Coding: a Theoretical and Experimental Review*.

**Local copies:** `papers/C2_millidge_2021_predictive_coding_review.pdf`.

**Goal:** Name which variable each loop minimizes energy over — activity in the inner loop, weights in the outer — and why the weight update assumes the inner loop already reached a fixed point. Turns "settle 100 iterations, then update" from an arbitrary hyperparameter into a schedule with a reason, and connects it to why carrying state across inputs and running Adam mid-rollout are architectural decisions with real failure modes.

**Scope:**
- Two loops, one energy: inner descends activity (fast, per input), outer descends weights (slow, per batch); what each holds fixed
- Why weight updates use the converged error, and what breaks in the gradient when weights update from a partially settled state
- Batch/offline schedule vs a deployed network with no "done" — where the inner loop's stopping condition comes from when input never stops
- State persistence as a choice: when carrying settled activity forward speeds re-settling, and when it traps the network in a stale basin
- Why a momentum-based optimizer's state assumes a stationary training distribution, which a live rollout is not
- Not covered: precision-weighted errors (C3), clamping patterns (C5), the backprop-equivalence proof (C6)

**You should be able to answer:**
1. In the CartPole rollout, which loop runs 100 iterations, and which variable does it hold fixed while doing so?
2. If weights update after only 10 of the 100 settling iterations, what specifically is wrong with the gradient computed?
3. Name one condition where carrying settled state into the next input's inner loop speeds convergence, and one where it produces a wrong answer.
4. Why does SGD tolerate a live rollout's shifting distribution better than Adam's carried-over moment estimates?
5. In a deployed network that never stops receiving input, what replaces the epoch boundary as the trigger to update weights?

**Project tie-in:** Explains the Step 2b finding that SGD works but carried-over Adam state blows up in `online_rollout.py`, and why the 100-iteration inference settle in `train_cartpole.py` is not an arbitrary constant.

**Done when:** The learner states the fixed-prediction assumption the outer loop relies on, without notes, and names the specific Step 2b consequence of violating it.

---

### C3. Precision weighting

**Prerequisites:** C1, C2; the PV/SST/VIP roles from `comp_neuro_notes.md`

**Size:** one to two sittings

**Source material:** **Not explicit in D&A**, though **ch. 10** *Density Estimation* carries the Gaussian variances that precision is the inverse of. Primary: Feldman & Friston 2010 on attention as precision; Bogacz 2017, the precision sections.

**Local copies:** `papers/C3_feldman_friston_2010_attention_uncertainty.pdf`.

**Goal:** See precision as the inverse-variance weight multiplying each squared error term, and recognize that C1's flat energy silently assumed every error channel equally trustworthy. Be able to say why learning precision jointly with weights is unstable, and compute how a node's settled value shifts when one error term's precision changes — not just recite that precision matters.

**Scope:**
- Precision in the energy function: F = ½·Σ πᵢ·eᵢ², π = 1/σ², and what precision 1 everywhere quietly assumed
- Precision set by hand vs learned, and the small-error/growing-precision feedback loop that makes joint learning unstable
- Precision as formal attention (top-down) and formal sensor confidence (bottom-up)
- The biological mapping made precise: PV scaling precision on feedforward error, VIP scaling precision on top-down prediction error
- Practical consequence: precision changes both which node moves most during settling and the magnitude of each local weight update
- Not covered: graph topology (C4), clamping as the precision→∞ limit (C5 owns it), backprop equivalence (C6)

**You should be able to answer:**
1. Write F for two error terms e₁, e₂ with precisions π₁, π₂, and state how π relates to σ².
2. A node settles by balancing e₁ = (v − 3) with π₁ = 1 against e₂ = (v − 6) with π₂ = 2. Solve dF/dv = 0 for v.
3. Same node, π₂ rises from 2 to 8. Solve for the new settled v and state the direction of the shift in one sentence.
4. Given Δw = η·π·e·(pre-synaptic activity) and a naive online rule π ← π + η_π(π·e² − 1), describe the runaway when e stays near zero, and why that makes joint precision-and-weight learning unstable.
5. Which error channel's precision does PV scale, which does VIP scale, and what does high VIP-driven precision imply about confidence in that channel's prediction?

**Project tie-in:** The soft desired-next-state clamp in Step 2b is mechanically a precision choice relative to the sensory clamp's precision. Step 4's stress variable currently tracks unweighted persistent error and will eventually need a precision-aware version.

**Done when:** The learner writes the precision-weighted energy unaided and gets v = 5, then v ≈ 5.67, for questions 2 and 3.

---

### C4. Predictive coding on arbitrary graphs (Salvatori et al. 2022)

**Prerequisites:** C1–C3; A2 and graph topology with reciprocal connections

**Size:** two to three sittings

**Source material:** **Not in D&A** — arbitrary-topology PC postdates it by two decades. Salvatori et al. 2022, *Learning on Arbitrary Graph Topologies via Predictive Coding* (arXiv:2201.13180) — the paper Step 2 reproduces.

**Local copies:** `papers/C4_salvatori_2022_arbitrary_graph_topologies.pdf`.

**Goal:** See that going from layered PC to graph PC is a re-indexing, not a new formalism: "layer above/below" becomes "in-neighbours/out-neighbours" in the energy sum, and every update term stays local. Closes the misconception that arbitrary topology needs new maths or breaks locality, and shows what a fixed input/output split was buying and giving up.

**Scope:**
- Energy generalization: a per-node error term summed over that node's actual neighbours, replacing the layer-indexed sum — same local rule, different neighbour set
- Input/output flexibility: any node clampable or free per trial, no reserved input or output layer
- The paper's results: associative memory, generation and classification from one trained model; the topologies tested
- Cycles and recurrence: whether settling still converges with loops, and what guarantees or threatens convergence
- Not covered: spiking neurons on the graph (Step 3 work, not a lesson), clamping patterns in depth (C5), backprop equivalence (C6)

**You should be able to answer:**
1. Write the generalized per-node energy term for graph PC and identify exactly which layered-PC term it replaces.
2. In a 3-node fully connected graph A–B–C with A clamped and C free, what does B's prediction depend on, and how does that differ from a layered network where layer l depends only on l−1?
3. Name two of the paper's three task types run from a single trained model without retraining, and state what changes between them.
4. Does energy minimization on a graph with cycles still converge to a fixed point? What property guarantees it, or under what condition can it fail to settle?
5. Why does "any node can be input, output, both or neither" matter for a network that later adds and removes nodes at runtime? Name the mechanism it removes the need for.

**Project tie-in:** The theory behind `steps/02_pc_graphs/`, already built and working, and the direct prerequisite for Steps 3–4 where node roles and topology are not fixed in advance.

**Done when:** The learner writes the generalized energy equation unaided and can say what guarantees or threatens convergence on a cyclic graph.

---

### C5. Clamping and frozen priors

**Prerequisites:** C3 (hard clamp as the infinite-precision limit), C4

**Size:** one to two sittings

**Source material:** **D&A ch. 7** *Stochastic Networks* — Boltzmann machine learning runs clamped and free phases, which is the same boundary-condition idea one formalism over. Primary: Friston, Daunizeau & Kiebel 2009, *Reinforcement Learning or Active Inference?* (PMC2713351); Salvatori et al. 2022 for the per-task clamp patterns.

**Local copies:** `papers/C5_friston_2009_active_inference.pdf`.

**Goal:** State clamping as a boundary condition on the settling dynamics — not a classification-only trick — and explain, for a goal-directed clamp, exactly what stops the network from resolving the error by revising its belief instead of acting. Closes the gap between "clamp = fixed input" and "clamp = frozen prior that redirects error resolution toward action".

**Scope:**
- Clamping as a boundary condition: fixed nodes vs free nodes minimizing local error; hard clamp as the π→∞ limit of a soft one
- A comparison table of clamp patterns across the four task types — classification, generation, reconstruction, goal-directed action: what is fixed, what is free, what is read off after settling
- Active inference and frozen priors (Friston et al. 2009): clamping a desired future state, and the asymmetry — current sensory state also clamped to real data, only the action node free — that forces resolution via action rather than belief revision
- Failure modes: over-constrained clamps with no settled solution, and clamps satisfied by hallucination
- Not covered: the precision machinery itself (C3), graph connectivity (C4), online weight updates (C2)

**You should be able to answer:**
1. For the CartPole online rollout, write out which nodes are clamped, which are free, and which node's settled value is read out as the answer.
2. A soft clamp on node x contributes π(x − x_clamped)² to the energy. What happens to x's settled value as π→∞, and why does that make a hard clamp a special case rather than a different mechanism?
3. Fill in the clamp table for reconstruction from a corrupted input (half an MNIST digit) — and contrast it with generation (label clamped, image free).
4. In a frozen-prior setup with desired future state clamped and current state clamped to the real sensor reading, name the one node type left free and explain why that choice forces the network to act rather than change its belief about the goal.
5. Give one concrete over-constrained clamp scenario and say what the network does instead of settling; then one scenario where a clamp is satisfied by hallucination rather than a correct answer.

**Project tie-in:** Describes the CartPole clamp pattern in `online_rollout.py` and `train_cartpole.py` — observations hard-clamped, desired next state soft-clamped, ACTION free and read off after settling — the mechanism the project plan calls "a running mind that you steer", not an inference API.

**Done when:** The learner reconstructs the four-task clamp table and the CartPole clamp diagram unaided, and can say *why* each node is fixed or free rather than reciting which.

---

### C6. PC ≈ backprop: what the equivalence does and does not claim

**Prerequisites:** C1–C5; standard backprop; the spiking credit-assignment problem. Final lesson — passing it opens fusion design on Steps 3–5.

**Size:** two sittings

**Source material:** **D&A ch. 8** *Supervised Learning* for the backprop baseline the equivalence is stated against. The equivalence itself is not in D&A: Whittington & Bogacz 2017 (Neural Computation); Song et al. 2020 (NeurIPS), *Can the brain do backpropagation?* for the exact conditions.

**Local copies:** `papers/C6_song_2020_exact_backprop_in_pc.pdf` and `papers/C6_whittington_bogacz_2017_backprop_approximation.txt` (full text, no OA PDF).

**Goal:** State the exact assumption (fixed prediction) under which Whittington & Bogacz's layered-PC gradient matches backprop's, and the timing/initialization conditions Z-IL and Song et al. add to make the match exact. Closes the misconception that "PC = backprop" is an unconditional identity, and names which features of this project's target — arbitrary graphs, spiking dynamics, runtime topology change, online updates — fall outside every version of the proof.

**Scope:**
- Whittington & Bogacz (2017): the fixed-prediction assumption — what is held fixed during inference, and why that is what makes the layered-PC update converge to the backprop gradient
- Z-IL and Song et al.: the timing and initialization conditions that make the correspondence exact, and what enforcing them costs
- The honest reading: evidence that a purely local rule can recover a global gradient — not proof that PC is better, more biological, or the right model of cortex
- The double-edged argument: if PC reproduces backprop's gradient, what independently motivates PC — locality, no separate backward pass, arbitrary topology, hardware mapping
- What breaks the equivalence: arbitrary graphs, spiking nonlinearities, structural change at runtime, online updates without settling to convergence
- Not covered: the fusion design itself (Steps 3–5 work, not a lesson), surrogate gradients (deliberately skipped)
- Perishable: this literature is still moving. Check for results published since the papers named above when the lesson is taught; the durable part is which assumption each result needs, not the citation list.

**You should be able to answer:**
1. State precisely what the fixed-prediction assumption requires — which quantity is held fixed, and at what point in the inference loop.
2. What timing condition on weight updates does Z-IL impose to make the correspondence exact, and what does enforcing it cost?
3. Name one specific step in the Whittington & Bogacz derivation, and one specific feature of this project's target architecture that breaks it.
4. If PC exactly recovers backprop's gradient in the layered case, give one argument for using PC anyway that does not reduce to "it computes the same gradient".
5. True or false, with justification: the equivalence proves PC is a plausible model of cortical learning.

**Project tie-in:** Steps 3–5 deliberately leave the layered case where the equivalence holds, moving to arbitrary graphs, spiking dynamics and stress-triggered structural change — exactly the conditions where no version of the proof applies, so the project cannot lean on the equivalence for justification.

**Done when:** The learner distinguishes W&B's approximate correspondence from the Z-IL/Song exact one, and states unprompted that the equivalence does not cover the project's target architecture.
