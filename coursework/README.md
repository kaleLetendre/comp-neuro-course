# Coursework

One file per lesson. Each holds four pieces — a derivation, a simulation, a guided reading and a written defence — with learning goals, a banded rubric, a private grader key and teacher constraints (a three-step hint ladder plus explicit prohibitions).

**Running order within a lesson:** audio overview (generate it from the lesson's pack in `../notebooklm/`) → guided reading (Piece 3) → derivation (Piece 1) → simulation (Piece 2) → written defence (Piece 4). Pieces are numbered by type, not sequence. Concepts are consumed first, made exact by the derivation, then applied and refined by building.

**Simulation numbers are targets, not thresholds.** Every grader key that quotes a figure from a run quotes it from an actual execution at a stated seed. Reruns drift: RNG call order, library version and step size all move the digits. Several files say so in their own keys; the rule holds for all of them. The teacher agent marks the *qualitative pattern and its direction* — the Fano factor falling below 1, the biased decoder pulling toward the dense region, the recovered filter matching the planted one — and treats an exact-digit mismatch as a prompt to check the learner's method, never as a wrong answer on its own.

The grading material is written for a constrained **teacher agent**: it marks, it hints, it never does the work. The grader keys are not for the learner to read before attempting a piece.

## The set — foundations

| Lesson | Simulation | What it demonstrates |
|---|---|---|
| F1 | Poisson trains, three rate estimates, a refractory condition | Estimates disagree; Fano 0.99 → 0.82 as regularity rises |
| F2 | Planted Gabor recovered by spike-triggered averaging | Similarity 0.998 under white noise, 0.728 under correlated input |
| F3 | Population vector vs ML vs MAP, uniform and clustered | The population vector's bias appears when tiling fails |
| F4 | Direct-method entropy rate at shrinking recording lengths | Downward bias, and CDF-matching flattening output to log2(20) |
| F5 | Full Hodgkin-Huxley | Threshold by bisection, gating through a spike, refractory period measured |
| F6 | LIF against HH on one current sweep; shunting inhibition | Depolarisation block HH shows and LIF cannot; current-based inhibition injecting exactly 0 nA |
| F7 | Multi-compartment passive cable | Attenuation matches exp(-x/lambda); violating the compartment rule breaks it |
| F8 | Linear recurrent network by eigenmode | Amplification 1/(1-lambda) and tau/(1-lambda), then instability, then saturation |
| F9 | Oja's rule against a hand-computed eigenvector | Convergence to PC1; Hebb diverging; the two normalisations compared |
| F10 | TD learning, then a blocking experiment | The error moving backward to the cue; the omission dip at exactly -1 |
| F11 | Sparse coding on synthetic patches from a planted dictionary | Oriented filters recovered at 0.999 similarity |
| Bridge | Hebbian drift on a spiking LIF fed by Poisson input | Needs F1, F6 and F9 together — a gap in any one stops the code |

## The set — advanced

| Lesson | Time | Simulation | Written defence produces |
|---|---|---|---|
| Bridge | 1h25 | Synaptic scaling vs unconstrained Hebbian drift | Synthesis across F1-F11 |
| A1 | 3h30 | Delay-only coincidence detector | Delay as plastic vs structural |
| A2 | 7-8h | Hopfield capacity, then the real CartPole diagnostic | — (the diagnostic is the deliverable) |
| A3 | 3h30-4h30 | E-I rate-model rhythm and its onset | Functional vs epiphenomenal oscillations |
| A4 | 3h30 | LIF under eight knob combinations | Whether the memristor synapse needs a second variable |
| A5 | 4-5h | Sparsity/event-count energy model | The efficiency case to a skeptic |
| B1 | 4h30 | Dopamine signatures from a TD agent | Whether stress needs more than one channel |
| B2 | 6h | Fast error, slow prediction | **The Step 5 cluster wiring proposal** |
| B3 | 4h30 | Branches as a hidden layer | Step 4: grow a pair vs add dendritic capacity |
| B4 | 2h30-3h | Overproduce-then-prune vs grow-on-demand | **The Step 4 growth/pruning policy** |
| B5 | 3h | Catastrophic forgetting and the cheapest fix | Whether step 2b needs replay |
| C1 | 4-6h | Settling is gradient descent | Scope of the locality claim |
| C2 | 4h30-6h | Sweeping the inner-loop budget | What triggers a weight update in a network that never stops |
| C3 | 4h45-5h30 | Sweeping precision and breaking joint learning | Whether stress should be precision-weighted |
| C4 | 5-7h | Settling on an adjacency matrix | The re-indexing claim, tied to Step 4 |
| C5 | 3h30-4h30 | One PC network, four clamp configurations + one failure | Clamping as boundary condition |
| C6 | 5h30 | Backprop-vs-PC update race | **The MSc proposal argument** |

Roughly 75 hours of work across the 17 lessons.

## Known gaps — read before trusting a grader key

**Guided-reading keys were written without opening the papers.** The agents that wrote this coursework were told not to read files, which unintentionally stopped them opening the very PDFs they were assigning. So for every reading piece whose target is a downloaded paper (A1, B2, B5, C1, C3, C4, C5, C6), the questions come from prior knowledge of those papers and the keys are *expected content*, not verified answers. C3's key states this requirement itself; B5's flags it. Verify the key against the text when the lesson is taught — you will have the paper open anyway.

**Source availability improved since these files were written.** Twenty-one of the twenty-eight papers are obtainable free — see `MATERIALS.md`. Nine of them are open access but blocked to scripts, so they need one browser click each. That includes **Bastos et al. 2012**, whose absence is the reason B2's laminar claims are marked as bridging inference; fetch it and B2 can be verified properly.

**Facts supplied in place of unavailable sources.** Where the natural reading is paywalled, agents stated the needed facts inside the assignment text and graded the reasoning from them. That affects:

- **B1** — volume-transmission distances and timescales, ACh vs NE roles, the D1/D2 sign flip
- **B2** — ~~the laminar/frequency-band mapping~~ **resolved**: Bastos et al. 2012 is open access at PubMed Central and its text confirms the mapping (superficial pyramidal cells broadcasting prediction errors, deep cells elaborating feedback that terminates outside L4, superficial gamma over beta and deep beta over gamma). B2 no longer rests on inference.
- **B3** — a self-written primer on NMDA spikes and apical gating
- **B4** — complement tagging, microglia, critical-period closure, adult neurogenesis, and the synaptogenesis rates (~5,000 vs ~484 synapses/neuron/year) that the growth-policy arithmetic is built on

These are recalled, not read. Check them against the sources when institutional access arrives — B4's numbers in particular propagate into a Step 4 policy.

**A5 is perishable by design.** Chip capabilities and benchmark figures date fast; its grader key says so and grades the argument rather than the numbers.

## What was verified

Where a piece rests on computed numbers, most agents ran the code before writing the key rather than inventing values: the Bridge set's runaway weights, A1's fire/no-fire split on delay alone (V=1.062 vs 0.937), A2's Hopfield capacity knee and a genuine spurious attractor, A3's rhythm vanishing at tau_I=70ms, A4's eight knob combinations, C5's over-constrained energy plateau (2.38 vs ~0.001). C1's algebra and C3's closed form were checked by hand afterwards and hold.
