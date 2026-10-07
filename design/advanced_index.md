# Advanced

Sixteen lessons in three tracks, past the textbook and into the literature. Gated behind the Bridge checkpoint. About 75 hours.

!!! note "Order"
    Track A is sequential and must finish before track C begins. Track C is sequential, starting after track A. Track B runs alongside the other two; B4 needs B2, B5 needs A2.

<div class="grid cards" markdown>

-   __Track A · Spiking network dynamics__

    ---

    Five lessons, sequential. Finishes before track C begins.

    [:octicons-arrow-right-24: Start at A1](A1.md)

-   __Track B · Biology for people building models__

    ---

    Five lessons, run alongside tracks A and C.

    [:octicons-arrow-right-24: Start at B1](B1.md)

-   __Track C · Predictive coding__

    ---

    Six lessons, sequential. Starts after track A.

    [:octicons-arrow-right-24: Start at C1](C1.md)

</div>

## Track A — spiking network dynamics

Sequential; must finish before track C begins.

| ID | Title | Summary |
|---|---|---|
| [A1](A1.md) | Synaptic delays and temporal structure | When a spike arrives matters as much as how strong it is; polychronous groups store memory in delays |
| [A2](A2.md) | Attractors and network state | State as a point on an energy landscape, and how to tell a real basin from a slow mode |
| [A3](A3.md) | Oscillations and synchrony | How excitation-inhibition loops produce rhythms, and whether rhythms do anything |
| [A4](A4.md) | Short-term plasticity, refractory period, reset modes | The implementation knobs that decide what a neuron carries from one moment to the next |
| [A5](A5.md) | State of the field | The energy argument, real neuromorphic hardware, and an honest account of the accuracy gap |

## Track B — biology for people building models

Runs alongside the other tracks. B4 needs B2; B5 needs A2.

| ID | Title | Summary |
|---|---|---|
| [B1](B1.md) | Neuromodulation: dopamine, acetylcholine, noradrenaline | What the broadcast chemicals actually signal, and where the three-factor abstraction breaks |
| [B2](B2.md) | Cortical microcircuits and laminar structure | Which layer does what, and the predictive-coding reading of the canonical microcircuit |
| [B3](B3.md) | Dendritic computation | Dendrites as nonlinear subunits rather than passive summers |
| [B4](B4.md) | Developmental pruning | Brains build far too many synapses and cut most back; elimination is active, not decay |
| [B5](B5.md) | Hippocampal replay and consolidation | Why one network cannot be both a fast learner and interference-free |

## Track C — predictive coding

Sequential; starts after track A.

| ID | Title | Summary |
|---|---|---|
| [C1](C1.md) | Predictive coding as energy minimization | Settling is gradient descent on a scalar function, computable from local quantities alone |
| [C2](C2.md) | Inference vs learning: two nested loops | Activity descends fast, weights descend slowly, and the order matters more than it looks |
| [C3](C3.md) | Precision weighting | The inverse-variance weight on each error, and why learning it jointly with weights is unstable |
| [C4](C4.md) | Predictive coding on arbitrary graphs | Dropping layers for neighbours is a re-indexing, not a new formalism |
| [C5](C5.md) | Clamping and frozen priors | Fixing nodes as a boundary condition; one mechanism for classification, generation and action |
| [C6](C6.md) | PC ≈ backprop | What the equivalence result claims, what it needs, and where it stops applying |
