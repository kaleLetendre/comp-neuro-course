# A2 learning outcomes — what the listener should be able to do afterwards

This document tells the generator what the lesson is *for*. The audio should build toward these capabilities.

By the end the learner should be able to:

1. **Explain why symmetric weights guarantee the energy never increases**, in terms of what a single unit's update does to E, and say what changes when weights are asymmetric.
2. **Design a diagnostic** that distinguishes a genuine multi-basin landscape from unconverged slow modes in a trained network — naming what to perturb, what to measure, and what result supports which conclusion.
3. **Read a convergence-rate curve** and say whether it is consistent with geometric convergence to separated minima or with a slow mode still relaxing, and name the further measurement that would settle it.
4. **Separate the two memories** — what is fixed and what changes when a network *learns* versus when it *settles to an answer for one input*.
5. **Describe a bump attractor** and explain how persistent spiking activity implements a fixed point when no single neuron can hold a static value.

## Important constraint for generation

These outcomes are also the lesson's assessment questions. **Do not answer them directly, and do not present them as questions with answers attached.** Teach the concepts and mechanisms they depend on, so that a listener who has understood the material can construct the answers themselves. Explaining *how* to tell a basin from a slow mode is correct; announcing what the learner's own experiment shows is not — that result is unknown and is theirs to establish.
