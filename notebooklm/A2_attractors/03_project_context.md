# A2 project context — the unresolved experiment this lesson is aimed at

You is building a spiking neural network that uses predictive coding on a graph topology, as preparation. A hard constraint throughout: every learning rule must be purely local — each synapse updates from pre-synaptic activity, post-synaptic activity and a local error signal only. No backprop, no global loss.

A side investigation (called step 2b) keeps network activity state across environment timesteps rather than resetting it, and learns online during a CartPole control task. Inference settles the network for 100 iterations before reading out an action.

## The experiment and its result

On a trained 256-neuron network, twenty random initial activity states were clamped to the *same* observation and settled for 100, 500, 2000 and 10000 iterations.

- At every iteration count the runs settle to **distinct** fixed points.
- Maximum pairwise L2 distance across the free positions: about **2.1 at 100 iterations, 1.85 at 2000, 1.7 at 10000**. That is roughly a 19% reduction for a hundredfold increase in iterations.
- The settled value of the single ACTION readout — the number the controller acts on — ranges from **−0.69 to +0.67** across initial states. It crosses zero, so the same observation produces opposite committed actions depending on where the network started.

## Why it is unresolved

Two readings remain open:

1. The trained energy landscape genuinely has many local minima, and settling falls into whichever basin the initial state belongs to.
2. The descent is so flat in some directions that even 10000 iterations is not enough to converge, and the apparent distinctness is an artifact of stopping early.

At the iteration count actually used at inference time (100), state dominates output either way. What is not known is whether the basin selected at each timestep is the *right* one — distinct actions across initial states does not mean any of them are good. Roughly half of observed control behaviour is good, which is consistent with sometimes landing well and sometimes not.

## What the lesson is meant to produce

A protocol you can run against the saved model to settle the question — with perturbation magnitudes, repeat counts and a decision rule committed to *before* looking at the result. The material should equip them to design that protocol. It must not pretend to know the outcome.
