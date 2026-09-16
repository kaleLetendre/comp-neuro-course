# Learning Plan — SNN, PC, and Computational Neuroscience

The single place the study plan lives. Merges two tracks that had been running separately:

- **Track A — SNN fundamentals**, taught conversationally (previously only recorded in Claude's memory files, session `0aada431-69b8-4802-8ce3-eb8efc926fe1`, 2026-06-19).
- **Track B — comp neuro / biology**, written up in [`comp_neuro_notes.md`](comp_neuro_notes.md) with a "relevance to this project" block per topic.
- **Track C — predictive coding theory**, deliberately deferred until Track A is finished.

Per-lesson specs live in [`lessons.md`](lessons.md) — 17 lessons (A0-A5, B1-B5, C1-C6), each with a goal, scope, starting reading, a rough size, and five acceptance criteria describing what the lesson must leave you able to reason through. Those are criteria for the lesson, not a test; coursework comes later. Roughly 28-30 sittings end to end: ~9 for track A, ~8 for track B, ~11 for track C. The core text is **Dayan & Abbott, *Theoretical Neuroscience*** (2001), mapped chapter-by-chapter in `lessons.md`; it carries A2/A3/A4/B1/B3 outright, grounds six more, and is silent on six (including predictive coding itself). This file stays the map; that one is the detail.

Last updated: 2026-09-15.

---

## The ordering rule (set 2026-06-19, still in force)

**Finish raw SNN → then raw PC → only then decide how to fuse them.**

No PC≈backprop, no fusion design, no "how would this work in the graph" detours until Track A's queue is empty. The rule exists because the fusion is the novel contribution (Steps 3–5) and it needs both halves understood independently first.

Track B runs alongside on its own cadence — biology reading feeds design flags, it doesn't gate anything.

---

## Status at a glance

| Track | Position | Next item |
|---|---|---|
| A — SNN fundamentals | ~70% through the raw-SNN list | A0 (consolidation), then A1 (synaptic delays) |
| B — comp neuro | 4 topics written up, dormant since ~June 2026 | Any of B1-B5 |
| C — PC theory | Not started (blocked by A, intentionally) | — |

Nothing happened on any track between 2026-07-20 and 2026-09-15 — that gap was step 2b (persistent state / online CartPole) work.

---

## Track A — SNN fundamentals

### Covered

- [x] Hebbian → STDP → three-factor learning rules
- [x] Pre/post directionality (who-fired-before, not who-caused-whom)
- [x] LIF neuron dynamics
- [x] Graph topology with reciprocal / dual connections
- [x] Encoding & decoding — rate, latency, population; the "retina = fixed, backprop-trained sensory front-end that doesn't adapt as it lives" framing
- [x] Inhibition & E-I balance — negative weights vs dedicated inhibitory neurons; lateral inhibition / winner-take-all
- [x] Homeostasis — threshold adaptation + synaptic scaling, on a slow per-example/epoch cadence
- [x] The credit-assignment problem — spikes are non-differentiable (derivative 0/∞)
- [x] Eligibility traces as the local answer (surrogate gradients skipped on purpose)

Working mental model established for three-factor learning, and confirmed correct:

> A success/error chemical is misted over the whole network at once; each synapse changes in proportion to how brightly it's still glowing from recent activity, in the direction the chemical dictates.

Glow = eligibility trace (per-synapse, recency). Chemical = the third factor (broadcast neuromodulator — dopamine-like — sets sign and magnitude). Key point held onto: this is **not** backprop. No backward layer-by-layer wave; it's one broadcast plus local parallel updates.

### Remaining queue

- [ ] **A0** — consolidation of everything above, after the 3-month gap. Diagnostic only, no new material.
- [ ] **A1** — synaptic delays and temporal structure
- [ ] **A2** — attractors and network state. Connects directly to the attractor test in `comp_neuro_notes.md` §2.
- [ ] **A3** — oscillations and synchrony
- [ ] **A4** — short-term plasticity, refractory period, reset modes, glow-stacking
- [ ] **A5** — state of the field: why SNNs, where they stand vs ANNs (absorbs the brain energy budget)

When these three are done, Track A is closed and Track C opens.

---

## Track B — comp neuro / biology

Full write-ups live in [`comp_neuro_notes.md`](comp_neuro_notes.md). One-line takeaway and the design flag each one left behind:

| Topic | Takeaway | Design flag |
|---|---|---|
| Electrical vs chemical synapses | Electrical = fast, fixed, bidirectional; chemical = slow, tunable, where learning lives | Two edge classes: structural (fixed, for prediction↔error pair wiring) vs learnable. Plus the "evolutionary pretrained substrate vs learnable mind" framing → fixed survival subnets anchoring an adaptive cortex (Steps 4–5) |
| Inference vs learning in PC; state persistence | State = memory; a network that resets between inputs has no continuity. Attractor test (2026-04-15) confirmed state dominates output: same clamp, different inits → ACTION spans −0.69 to +0.67 | Two interacting timescales — weights (slow) and activity state (fast). Fed directly into step 2b |
| Excitatory vs inhibitory | Signed weights capture the sign but miss **Dale's principle** (E or I is a property of the neuron, not the synapse) | Typed interneurons are the right granularity for Step 5: SST = prediction mean, VIP = uncertainty, PV = precision of feedforward drive |
| Astrocytes | A slow modulatory network gating *when and where* plasticity happens, covering territories rather than single synapses | The stress variable is astrocyte-shaped. Suggests per-cluster rather than per-neuron, and a clean fast-neural / slow-modulatory split. Separate stress (error-driven, growth) from a homeostatic variable (activity-driven, normalization) |

### Remaining queue

Any order, alongside track A. B4 assumes B2; B5 assumes A2.

- [ ] **B1** — neuromodulation proper (dopamine, ACh, noradrenaline) vs the "third factor" abstraction
- [ ] **B2** — cortical microcircuits and laminar structure. Closes the flagged Hertäg & Sprekeler read and sets the Step 5 cluster layout.
- [ ] **B3** — dendritic computation. Raises a second Step 4 growth lever: more internal capacity instead of a new neuron pair.
- [ ] **B4** — developmental pruning. The biological precedent for the Step 4 stress/pruning equilibrium.
- [ ] **B5** — hippocampal replay and consolidation. Bears on online learning and forgetting in step 2b.

(The brain's energy budget, listed here earlier as its own topic, is folded into A5.)

---

## Track C — predictive coding theory (blocked until Track A closes)

Not started. Expected shape when it opens, to be refined then:

- [ ] **C1** — PC as energy minimization: the energy function, and what settling actually does
- [ ] **C2** — inference vs learning as two nested loops, and the schedules each needs
- [ ] **C3** — precision weighting: why errors are scaled, and what that corresponds to biologically
- [ ] **C4** — PC on arbitrary graphs (Salvatori et al.): what changes when layers are dropped
- [ ] **C5** — clamping / frozen priors as one mechanism for classification, generation, reconstruction, goal-seeking
- [ ] **C6** — PC ≈ backprop: the equivalence result and exactly what it does and doesn't claim. Flagged as "next up" in June 2026 before the ordering rule pushed it behind raw SNN.

Only after this: fusion design (Step 3 onward).

---

## Open flags carried forward

Questions raised but not resolved. Each needs closing before the step it's tied to.

- [ ] Has any PC-on-graph or SNN work explicitly modelled **astrocyte-like modulation**? If not, that's a candidate contribution angle for Step 4/5.
- [ ] Read **Hertäg & Sprekeler (eLife 2020)** and recent PV/SST/VIP microcircuit papers before committing Step 5 to a cluster layout.
- [ ] Decide whether **Dale's principle** gets enforced. Probably yes by Step 5 (cortex structure, neuromorphic sign constraints); definitely not before Step 3.
- [ ] Keep **stress** (error-driven, triggers growth) separate from a **homeostatic variable** (activity-driven, normalizes) rather than making stress do everything.
- [ ] Does the **structural vs learnable edge** distinction pay off across Steps 3–5, or collapse back into one edge type?

---

## How these sessions run

Formats that work: concrete worked examples with real numbers, tick-by-tick walkthroughs, small ASCII diagrams, comparison tables, and a running "what you know / what's left" checklist. Push back when something is asserted without grounding — the answer should correct the specific misconception, not re-explain the whole topic. Concepts get tied back to the project where they map (stress ≈ homeostasis, error neuron ≈ third factor, clamping ≈ encode/decode).

End of a teaching session: tick the boxes above, and append any biology write-up to `comp_neuro_notes.md` with its "relevance to this project" block.
