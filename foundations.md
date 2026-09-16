# Foundation track — F1 to F11

Computational neuroscience as a field, worked through Dayan & Abbott's *Theoretical Neuroscience* end to end. This track comes **before** the advanced tracks in [`lessons.md`](lessons.md) and assumes no neuroscience whatsoever.

It exists because the first version of this curriculum did not. That version was assembled from prior tutoring notes and from the design questions of a research project, so it assumed membrane dynamics, spike statistics, encoding and plasticity were already understood, and it skipped chapters 1 to 4 of the textbook entirely — no receptive fields, no decoding, no information theory. This track is the correction: the field taught properly, with the project demoted from the spine to an application that comes later.

## Chapter mapping

| | Lesson | D&A |
|---|---|---|
| F1 | Spike trains and firing rates | ch. 1 |
| F2 | Receptive fields and reverse correlation | ch. 2 |
| F3 | Neural decoding | ch. 3 |
| F4 | Information theory for neurons | ch. 4 |
| F5 | Membrane biophysics and the action potential | ch. 5 (biophysics half) |
| F6 | Integrate-and-fire neurons and synaptic input | ch. 5 (I&F half) |
| F7 | Cable theory and neuronal morphology | ch. 6 |
| F8 | Network models: feedforward and recurrent | ch. 7 |
| F9 | Synaptic plasticity and learning rules | ch. 8 |
| F10 | Classical conditioning and reinforcement learning | ch. 9 |
| F11 | Representational learning and generative models | ch. 10 |

## Order

```
F1 ──┬── F2 ── F3 ── F4
     └── F5 ──┬── F6 ── F8 ── F9 ──┬── F10
               └── F7                └── F11 (also needs F3)
```

Strictly: F1 first. F2 needs F1; F3 needs F1 and F2; F4 needs F1 and F3. F5 needs F1; F6 and F7 both need F5; F8 needs F6; F9 needs F6 and F8; F10 needs F9; F11 needs F3 and F9.

Track A's **A0** changes job. It was the entry diagnostic for a course that assumed prior knowledge; it is now the **bridge checkpoint** between this track and the advanced ones — a check that the foundations hold before A1 builds on them.

## Size

Roughly 24 sittings, about 60 hours. Nine of the eleven came out as "two to three sittings", which is worth watching: if the track drags in practice, F5, F8 and F9 are the ones to split rather than skim.

## What is deliberately not here

Sensory systems beyond the early visual pathway, motor control, and cognitive-level modelling. D&A does not cover them either. If the MSc wants them, they are a second textbook, not a patch to this track.

---

### F1. Spike trains and firing rates

**Prerequisites:** none — the entry point

**Size:** one to two sittings — chapter 1 is conceptual rather than derivational; the long side comes from sitting with the Poisson and Fano-factor material until it is load-bearing rather than merely read

**Source material:** D&A ch. 1 — *Introduction* · *Spike Trains and Firing Rates* · *What Makes a Neuron Fire?* · *Spike-Train Statistics* · *The Neural Code*

**Goal:** Understand that a spike train is the raw observable and "firing rate" is a construct built on top of it, with several non-equivalent definitions. Close the misconception that neural data arrives pre-packaged as a rate — it has to be estimated, and the estimation method changes the answer. Come away treating "the neural code" as an open question rather than settled background.

**Scope:**
- The spike as an event: why the waveform is discarded and only timing kept
- Three notions of rate — spike-count, time-dependent r(t), trial-averaged — and when each is the only one the data supports
- Rate estimation mechanics: binning, sliding windows, kernel smoothing, and the bias/variance trade-off each introduces
- Poisson spike generation, the interspike-interval distribution, the Fano factor, and concrete ways real cortical trains depart from Poisson
- Tuning curves as stimulus-to-rate maps; rate versus temporal coding stated as unresolved, not adjudicated
- Not covered: decoding a stimulus from spikes (F3), information-theoretic treatment (F4), the biophysics that produces a spike (F5)

**You should be able to answer:**
1. Given a spike train with 12 spikes in a 2-second window, compute the spike-count rate, then say what additional data you would need to compute r(t) at t = 0.5 s.
2. For a Poisson process at 20 Hz, what is the Fano factor over any counting window, and what value in real data would tell you the neuron is *more* regular than Poisson?
3. A 100 ms sliding window versus a 10 ms one on the same train — which costs temporal resolution, which costs a noisy estimate, and why can you not avoid both?
4. Sketch a tuning curve for an orientation-selective neuron: where is the rate maximal, and what does the curve's width mean operationally?
5. State one concrete experimental observation arguing for temporal coding over pure rate coding, and one arguing against.

**Feeds:** F3 (decoding assumes the encoding model given here), F4 (information theory needs these statistics), F6 (integrate-and-fire generates the trains characterised here), and the whole A track.

**Done when:** The learner can take a raw spike train, produce two different rate estimates, defend and critique each, and articulate why "the firing rate" is not a single well-defined number.

---

### F2. Receptive fields and reverse correlation

**Prerequisites:** F1

**Size:** two to three sittings — the reverse-correlation mathematics and the retina/LGN/V1 anatomy are each substantial, and complex cells plus the LN cascade add a third block

**Source material:** D&A ch. 2 — *Introduction* · *Estimating Firing Rates* · *Introduction to the Early Visual System* · *Reverse-Correlation Methods: Simple Cells* · *Static Nonlinearities: Complex Cells* · *Receptive Fields in the Retina and LGN* · *Constructing V1 Receptive Fields*

**Goal:** Learn how a real sensory neuron's stimulus preference is measured and modelled, with the visual system as the running example. Build the spike-triggered average as an estimate of a linear filter, understand why white-noise stimuli make that estimate valid, and see where the linear model breaks and what repairs it.

**Scope:**
- The retina to LGN to V1 pathway at the level of what each stage computes
- Spike-triggered average and reverse correlation as a method, including the white-noise assumption and why it is needed for an unbiased estimate
- Centre-surround receptive fields as a spatial difference-of-Gaussians operation, not an intensity detector
- Orientation-selective, phase-sensitive simple cells as oriented spatiotemporal filters
- Complex cells as phase-invariant, the static nonlinearity mapping filter output to rate, and the linear-nonlinear cascade as the general model with its known failure modes
- Not covered: decoding a stimulus from spikes (F3), the laminar and microcircuit structure of V1 (B2)

**You should be able to answer:**
1. Given a white-noise stimulus and a recorded spike train, write the formula for the spike-triggered average and state which two quantities it averages over.
2. Why must the stimulus be white noise rather than, say, natural images, for the STA to estimate the linear filter without bias?
3. A centre-surround cell has a positive centre and negative surround. Compute the sign and rough magnitude of its response to a spot covering only the centre, versus one covering centre and surround equally.
4. What distinguishes a complex cell's response from a simple cell's when an oriented grating is shifted 90 degrees in phase, and how is that implemented in terms of combining filter outputs?
5. Name the two stages of the LN cascade in order, and give one concrete stimulus manipulation the linear stage alone would get wrong and the full cascade gets right.

**Feeds:** F3 (decoding inverts the encoding model built here), B2 (which assumes this feedforward story before complicating it).

**Done when:** The learner can derive a spike-triggered average by hand on a short synthetic example, and predict from a filter description whether a cell will behave as simple or complex.

---

### F3. Neural decoding

**Prerequisites:** F1, F2

**Size:** one to two sittings — four decoding methods plus a Fisher-information derivation; splits cleanly at discrimination-and-population-decoding versus Fisher-information-and-spike-train-decoding

**Source material:** D&A ch. 3 — *Encoding and Decoding* · *Discrimination* · *Population Decoding* · *Spike-Train Decoding*

**Goal:** Establish decoding as the inverse of encoding — given a response, infer the stimulus — by Bayes' rule rather than a new formalism. Cover discrimination via ROC, four population estimators, the Fisher-information bound, and linear spike-train reconstruction as instances of one inference problem.

**Scope:**
- Encoding p(r|s) versus decoding p(s|r): why they are different problems, and how Bayes connects them
- Two-alternative discrimination, ROC curves, and the result that a single well-tuned neuron can match an animal's psychophysical performance
- Population decoding compared — population vector, maximum likelihood, MAP, Bayesian — what each assumes and when the population vector is biased
- Fisher information and the Cramér-Rao bound on decoding accuracy, and its relation to tuning-curve width
- Spike-train decoding: reconstructing a time-varying stimulus from spike timing
- Not covered: quantifying readout capacity in bits (F4)

**You should be able to answer:**
1. Write Bayes' rule relating p(r|s) and p(s|r). Which does a single-neuron recording directly estimate, and what extra term do you need for the other?
2. In a two-alternative task, which single number computed from the ROC curve equals proportion correct, and how did that compare to the animal's own threshold in the classic MT experiment?
3. Write the population vector estimator. Under what condition on the tuning curves is it unbiased, and what happens when that condition fails?
4. State the Cramér-Rao bound linking Fisher information to estimator variance. As tuning curves narrow with neuron count fixed, does accuracy improve monotonically — what is the trade-off?
5. Write the linear estimator reconstructing a time-varying stimulus from a spike train as a sum over spike times of a kernel.

**Feeds:** F4 (mutual information formalises how much can be read out), F11 (the same inference machinery moved inside the model).

**Done when:** Given a population of tuning curves and a spike-count vector, the learner computes the maximum-likelihood and population-vector estimates by hand and says which is biased and why.

---

### F4. Information theory for neurons

**Prerequisites:** F1, F3 (F2 useful for the efficient-coding account of receptive fields)

**Size:** one to two sittings — the entropy and mutual-information worked example plus the infomax predictions make one sitting; spike-train entropy rates and estimator bias warrant a second

**Source material:** D&A ch. 4 — *Entropy and Mutual Information* · *Information and Entropy Maximization* · *Entropy and Information for Spike Trains*

**Goal:** Turn "this neuron carries information about the stimulus" into a computable quantity in bits. Derive entropy and mutual information on a small worked example, connect mutual information to decoder-independent bounds, and use the infomax hypothesis to predict concrete receptive-field properties.

**Scope:**
- Entropy H(R) and mutual information I(R;S) computed by hand on a small discrete table, in bits
- Why mutual information is the right currency: symmetric, assumption-free about the decoder, and an upper bound on any decoder's performance
- Infomax and efficient coding: maximising entropy under a fixed output range predicts histogram equalisation; decorrelating natural-image statistics predicts centre-surround receptive fields
- Entropy and information rates for spike trains via the direct method, binning trains into words
- Why finite data biases entropy estimates downward, and what that means for reported values
- Not covered: population codes and correlation-based information, spike-timing decoding beyond entropy rates

**You should be able to answer:**
1. Given a two-stimulus, two-response table with specified joint probabilities, compute H(R), H(R|S) and I(R;S) in bits.
2. Why is I(R;S) = I(S;R), and what does that symmetry rule out that a "goodness of decoding" metric would allow?
3. Under infomax with a fixed number of output levels, what response distribution maximises entropy, and what does that imply about the input/output curve relative to the stimulus's cumulative distribution?
4. In the direct method, which two entropy rates are subtracted to get the information rate, and which one needs the stimulus-repeat protocol?
5. Why does the direct method's entropy estimate fall as recording length falls, and what does that imply for comparing estimates across recordings?

**Feeds:** A5 (the sparsity and energy argument depends on bits per spike being high while rates are low).

**Done when:** Given a small joint distribution or a binned spike train, the learner computes entropy, mutual information and an information rate by hand, and says which receptive-field property a given infomax constraint predicts.

---

### F5. Membrane biophysics and the action potential

**Prerequisites:** F1

**Size:** two to three sittings — the Hodgkin-Huxley gating kinetics and the stochastic-channel material each take real time to work through numerically

**Source material:** D&A ch. 5 — *Introduction* · *Electrical Properties of Neurons* · *Single-Compartment Models* · *Voltage-Dependent Conductances* · *The Hodgkin-Huxley Model* · *Modeling Channels*

**Goal:** Establish the membrane as a physical RC circuit driven by ionic gradients, then show how voltage-dependent sodium and potassium conductances turn that circuit into a spike generator. By the end, "threshold", "all-or-none" and "refractory period" should be facts about channel kinetics rather than modelling conventions.

**Scope:**
- Membrane capacitance and leak conductance; the membrane time constant with typical values (C_m about 1 microfarad per square centimetre, tau_m in the 10 to 20 ms range)
- Nernst equation and reversal potentials for sodium, potassium and chloride; why a synapse's reversal potential relative to rest is what makes it excitatory or inhibitory
- Gating variables as fractions of open channels, with voltage-dependent rate functions
- Hodgkin-Huxley: fast sodium activation and inactivation, the delayed-rectifier potassium current, and how their interaction produces a stereotyped spike and a refractory period
- Stochastic channel models, with the deterministic conductance as the average over many channels
- Not covered: reducing this to integrate-and-fire (F6), extending it to multiple compartments (F7)

**You should be able to answer:**
1. Given C_m = 1 microfarad per square centimetre and a leak conductance g_L, compute tau_m, and say what changes if g_L doubles.
2. Using the Nernst equation, compute the potassium reversal potential at 37 degrees C for 140 mM inside and 5 mM outside.
3. Which gating variable terminates the spike's rising phase, and by what mechanism — state what it does to the sodium conductance, not just that it inactivates.
4. Why does the delayed onset of the potassium conductance produce a refractory period, rather than the neuron simply repolarising and firing again immediately?
5. When channels are modelled stochastically, what does the deterministic conductance represent — what is being averaged over what?

**Feeds:** F6 (integrate-and-fire is the abstraction that discards these dynamics), F7 (compartments extend this circuit spatially), A4 (reset modes and refractoriness stand in for the mechanisms fixed here).

**Done when:** The learner can derive why a spike is all-or-none and why a refractory period follows, from sodium and potassium kinetics alone, without invoking threshold-and-reset.

---

### F6. Integrate-and-fire neurons and synaptic input

**Prerequisites:** F5

**Size:** two to three sittings — three distinct payloads (the LIF derivation and f-I curve, the Hodgkin-Huxley loss ledger, and conductance-based synapses) rather than one continuous argument

**Source material:** D&A ch. 5 — *Integrate-and-Fire Models* · *Synaptic Conductances* · *Synapses on Integrate-and-Fire Neurons*

**Goal:** Derive the leaky integrate-and-fire model as a reduction of the single-compartment model from F5 and work its f-I curve with real numbers. State explicitly, with one concrete cost each, what the reduction discards. Replace current-based synaptic input with conductance-based input and show why the difference is not cosmetic.

**Scope:**
- LIF derived from the membrane equation, with tau_m, threshold and reset as explicit parameters rather than fitted constants
- The f-I curve derived from the subthreshold solution and evaluated at two or three real current values; the refractory period added and its effect on saturation shown numerically
- What LIF discards relative to Hodgkin-Huxley — spike shape, adaptation, bursting — with one named phenomenon lost per omission
- Synaptic input as a conductance rather than a current: shunting inhibition and the input-dependent effective membrane time constant, derived rather than asserted
- AMPA, NMDA and GABA-A time courses in milliseconds and their reversal potentials, tabulated
- Not covered: reset-mode variants and short-term plasticity (A4), wiring these units into networks (F8), learning rules on these synapses (F9)

**You should be able to answer:**
1. With V_rest = −65 mV, V_threshold = −50 mV, V_reset = −70 mV, tau_m = 10 ms and R = 10 megohm, solve for the interspike interval at an injected current of 2 nA.
2. Adding a 2 ms refractory period to that interval, what is the firing rate in Hz, and at what input current does the refractory period start to dominate the curve's shape?
3. Name one spiking phenomenon a real cortical neuron shows that plain LIF cannot produce, and identify which discarded mechanism is responsible.
4. Derive why a synapse modelled as a conductance times a driving force can shorten the effective membrane time constant even when it delivers no net current at rest, and name the effect.
5. Order AMPA, NMDA and GABA-A by decay time constant, with a millisecond value for each.

**Feeds:** F8 (networks are built from these units), F9 (plasticity acts on this synaptic machinery), A4 (which extends reset modes and short-term plasticity).

**Done when:** The learner derives the LIF f-I curve with a refractory period from the bare membrane equation, states the Hodgkin-Huxley trade-offs with a named phenomenon per loss, and explains shunting inhibition as a consequence of conductance-based input.

---

### F7. Cable theory and neuronal morphology

**Prerequisites:** F5

**Size:** two to three sittings — the cable equation derivation and the discretisation step are the parts that run long

**Source material:** D&A ch. 6 — *Levels of Neuron Modeling* · *Conductance-Based Models* · *The Cable Equation* · *Multi-compartment Models*

**Goal:** Move the neuron from a point to a spatially extended structure. Derive the cable equation from current conservation along a leaky cylinder, extract the electrotonic length constant, and use it to show that a synapse's dendritic location sets how much of its current survives to the soma — making location an implicit weight.

**Scope:**
- The levels-of-modelling spectrum from point neuron to full reconstruction: what each tracks, what it discards, and how to choose
- Conductance-based models with ionic currents beyond the standard sodium and potassium pair
- The cable equation derived from axial and membrane current balance, with the electrotonic length constant defined and typical values (hundreds of micrometres up to about a millimetre for dendrites)
- Steady-state attenuation of a distal EPSP at the soma as a function of distance in units of the length constant
- Multi-compartment discretisation into coupled ODEs, and the rule for compartment length relative to the length constant
- Not covered: active dendritic currents, NMDA spikes and the two-layer dendritic model (B3)

**You should be able to answer:**
1. For a dendritic cylinder with membrane resistivity 20,000 ohm-square-centimetre, axial resistivity 200 ohm-centimetre and diameter 2 micrometres, compute the length constant in micrometres.
2. A synapse sits two length constants from the soma. What fraction of its steady-state local voltage reaches the soma?
3. Write the cable equation and identify which term is axial current flow and which is transmembrane leak.
4. Why must compartment length be chosen relative to the length constant rather than to the neuron's physical size — what breaks in the discretised ODEs otherwise?
5. Name two ionic currents a conductance-based model might add beyond sodium and potassium, and what each contributes that those two cannot.

**Feeds:** B3 (active dendrites, NMDA spikes and apical gating are nonlinear modifications on top of this passive framework).

**Done when:** Given a cylinder's resistivities and diameter, the learner computes the length constant, uses it to find steady-state attenuation at the soma, and explains why compartment size is chosen relative to it.

---

### F8. Network models: feedforward and recurrent

**Prerequisites:** F6

**Size:** two to three sittings — six sections spanning the firing-rate derivation, feedforward and recurrent linear algebra, E-I stability, and a stochastic preview; the eigenvalue work is the long pole

**Source material:** D&A ch. 7 — *Introduction* · *Firing-Rate Models* · *Feedforward Networks* · *Recurrent Networks* · *Excitatory-Inhibitory Networks* · *Stochastic Networks*

**Goal:** Move from single neurons to populations described by firing rates, and show that a linear recurrent network's behaviour is fully characterised by the eigenstructure of its weight matrix. Establish selective amplification, effective time constants and stability as the load-bearing ideas that A2 and A3 each extend in a different direction.

**Scope:**
- The firing-rate model as an approximation to a spiking population, with its assumptions stated and a regime where it breaks
- Feedforward networks: what a weight matrix does to an input pattern
- Linear recurrent networks by eigen-decomposition: selective amplification of eigenvector-aligned components, the effective time constant per mode, and the stability condition
- Nonlinear saturating recurrent networks: winner-take-all and gain control as consequences of saturation
- Excitatory-inhibitory networks: the conditions for stable, damped or oscillatory return to equilibrium
- Stochastic networks as a bridge to energy functions and noise, introduced but not developed
- Not covered: attractors, basins and Hopfield memory built from the energy function (A2); E-I dynamics developed into rhythms, bands and synchrony (A3)

**You should be able to answer:**
1. A linear recurrent network has largest real eigenvalue 0.8. Given membrane time constant tau, what is that mode's effective time constant, and what happens as the eigenvalue approaches 1?
2. State the stability condition for a linear recurrent network in terms of the eigenvalues of the recurrent weight matrix.
3. In a linearised E-I network, what condition on the eigenvalues distinguishes damped oscillatory return to equilibrium from monotonic decay?
4. For an input aligned with an eigenvector of eigenvalue lambda, give the expression for steady-state amplification compared to the feedforward-only case.
5. Name two computations saturation enables that a linear recurrent network cannot perform, and say specifically why linearity precludes each.

**Feeds:** A2 (energy functions and recurrent dynamics), A3 (E-I dynamics), F9 (plasticity acts on these architectures).

**Done when:** From a given recurrent weight matrix the learner computes eigenvalues and predicts which input components are amplified, how fast each mode relaxes, and whether the network is stable — without reaching for attractor or oscillation vocabulary.

---

### F9. Synaptic plasticity and learning rules

**Prerequisites:** F6, F8

**Size:** two to three sittings — the biology, the rule taxonomy, the PCA-equivalence result and the supervised contrast are four separable bodies of content, each needing its own worked numbers

**Source material:** D&A ch. 8 — *Introduction* · *Synaptic Plasticity Rules* · *Unsupervised Learning* · *Supervised Learning*

**Goal:** Establish synaptic weights as variables changing under local activity-dependent rules rather than fixed parameters. Derive the basic Hebbian rule's instability and the normalisation fixes, then show that running such a rule on a population is doing statistics — Oja's rule extracts the principal component of the input covariance. Contrast with supervised rules that need an external teacher.

**Scope:**
- LTP and LTD as bidirectional weight change; STDP's timing window as the biological grounding for rate-based rules
- The basic Hebbian rule, its unbounded growth, and subtractive versus multiplicative normalisation as two fixes producing two different weight distributions
- Covariance and BCM rules, with BCM's sliding threshold as its stability mechanism
- Oja's rule converging on the principal eigenvector of the input covariance; ocular dominance and receptive-field formation as what this computes developmentally
- The delta rule and the perceptron as the supervised contrast case
- Not covered: reward-based three-factor rules (F10)

**You should be able to answer:**
1. A presynaptic spike leads the postsynaptic spike by 10 ms — is the synapse strengthened or weakened, and roughly what is the half-width in milliseconds of the STDP window it falls inside?
2. For an unnormalised Hebbian rule, what happens to the weight magnitude as time goes to infinity, and why does that make the rule implausible on its own?
3. Subtractive and multiplicative normalisation both bound total weight — which drives individual weights to saturate at their bounds, and which leaves a smoother distribution?
4. For Oja's rule, what vector does the weight converge to, expressed in terms of the input covariance matrix?
5. Write the delta-rule update for a linear unit with target d and output y, and name the one input it needs that Hebbian, covariance and BCM rules do not.

**Feeds:** A0 (the bridge checkpoint), A4 (short-term plasticity and eligibility traces), B4 (developmental pruning builds on the competition material), F10 (reward-based learning as the third regime).

**Done when:** For any rule in this lesson the learner states its update equation, what it converges to or diverges toward, and whether it needs a teacher signal — without consulting the chapter.

---

### F10. Classical conditioning and reinforcement learning

**Prerequisites:** F9

**Size:** two to three sittings — four distinct formal machines (Rescorla-Wagner, TD, indirect actor, actor-critic), each needing worked numbers before the next builds on it

**Source material:** D&A ch. 9 — *Introduction* · *Classical Conditioning* · *Static Action Choice* · *Sequential Action Choice*

**Goal:** Establish reinforcement learning as a third paradigm distinct from supervised and unsupervised: learning driven by a scalar evaluative signal rather than a target output or input statistics. Derive Rescorla-Wagner from the phenomena it must explain, extend to TD learning for within-trial timing, then to action selection.

**Scope:**
- The behavioural phenomena — acquisition, extinction, blocking, overshadowing, secondary conditioning — and why blocking rules out contiguity as the mechanism
- The Rescorla-Wagner rule derived, worked trial by trial, and shown to account for blocking, overshadowing and extinction with one equation
- TD learning: the TD error defined over within-trial time, with its value at cue, at reward and at reward omission derived rather than asserted
- Static action choice: exploration versus exploitation, and the indirect actor
- Sequential action choice: the actor-critic architecture, policy evaluation and improvement, and how the critic bootstraps from its own future prediction
- Not covered: dopamine recordings and where the TD abstraction empirically breaks (B1)

**You should be able to answer:**
1. For a cue-reward pairing with learning rate 0.2, asymptote 1 and initial value 0, fill in a four-trial table of value and prediction error before and after each trial.
2. In a blocking experiment — A trained to reward, then AB trained to reward — what associative strength does Rescorla-Wagner assign to B, and which term in the update forces that result?
3. With a cue at t = 0 and reward at t = 5, at which timesteps is the TD error nonzero before learning converges, and what is it at reward once the value function has converged?
4. In actor-critic, which equation does the critic use to update its value estimate, and what quantity from that update is handed to the actor?
5. How does the indirect actor's action-value update differ mechanically from a direct policy update?

**Feeds:** B1, which takes the TD error defined here as the candidate account of dopamine firing and tests it against recorded data, including where the single-scalar abstraction fails.

**Done when:** The learner derives Rescorla-Wagner and TD updates from raw trial data by hand, and attributes blocking, overshadowing and actor-critic bootstrapping to specific terms in those equations.

---

### F11. Representational learning and generative models

**Prerequisites:** F3, F9 (F2 helps the sparse-coding result land)

**Size:** two to three sittings — the EM worked example and the sparse-coding derivation each need dedicated time; the framing and discussion are quick by comparison

**Source material:** D&A ch. 10 — *Introduction* · *Density Estimation* · *Causal Models for Density Estimation* · *Discussion*

**Goal:** Show that representation learning can be posed as fitting p(input) rather than a stimulus-response map, via causal models with latent variables and a recognition model that inverts them. Establish EM as the fitting procedure and walk it on a concrete numeric case. Connect sparse coding and ICA to the empirical fact that fitting them to natural images reproduces V1 simple-cell receptive fields.

**Scope:**
- Density estimation as the goal of unsupervised representation learning, contrasted with supervised stimulus-response mapping
- Causal models: latent causes, a generative model of the input they would produce, and a recognition model inferring causes from input
- EM as two alternating phases — the E-step inferring latents at fixed parameters, the M-step updating parameters at fixed latents — worked by hand on a small example
- Sparse coding and independent components as specific causal models, and their fit to natural images producing oriented, localised, bandpass filters matching measured simple cells
- Not covered: precision-weighted inference and the free-energy formulation of this same fitting problem (C1, C3)

**You should be able to answer:**
1. For a two-cause discrete generative model with given priors and likelihoods, compute the E-step posterior responsibilities for a specific input.
2. Using those responsibilities, carry out the M-step update and state the new parameter value.
3. What penalty term makes sparse coding sparse, and how does that differ mechanically from ICA's independence constraint?
4. Sparse-coding filters fit to natural images come out oriented and localised rather than Fourier-like — which statistical property of natural images forces that?
5. In the E-step/M-step split, which step corresponds to inference and which to learning, and what goes wrong if you run one repeatedly without the other?

**Feeds:** C1 (the generative model's prediction error becomes the energy function), C2 (the E-step/M-step split is the template for the two nested loops), and C4 to C6 generally.

**Done when:** The learner works an EM step by hand on a toy causal model and states, without notes, why sparse coding on natural images yields V1-like filters.
