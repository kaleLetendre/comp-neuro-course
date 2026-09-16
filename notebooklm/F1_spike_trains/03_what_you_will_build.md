# F1 — what the learner does after listening

Context for the generator: this audio is the first step of a lesson, not the whole of it. Afterwards the learner works through Dayan & Abbott chapter 1, does a derivation by hand, and writes code. The overview should leave them equipped for that work and mildly impatient to start it — not feeling the topic is closed.

**The derivation.** Rate arithmetic on a short spike train, then the bias-variance algebra for a 100 ms versus a 10 ms smoothing window on a Poisson train at a known rate.

**The simulation.** Generate Poisson spike trains at a known rate, then recover that rate three ways — spike count, sliding window, kernel smoothing — and watch the three estimates disagree with each other and with the truth. Then impose a refractory period and watch the Fano factor fall below 1, in a run whose result can be predicted analytically beforehand.

**The written explanation.** Several hundred words arguing why "the firing rate" is not a single well-defined number, aimed at a reader who assumed it was.

The useful thing the audio can do is make the *questions* behind those tasks feel live: why the three estimates must disagree, what the refractory period is doing to the statistics, and why the Poisson model is worth caring about even though no real neuron is Poisson. Do not do the tasks. Do not give the numbers they are meant to produce.
