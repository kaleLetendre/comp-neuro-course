# A2 concept brief — attractors and network state

A teaching brief for the lesson "Attractors and network state". It is written to be the substance an audio overview is generated from, so it states the concepts rather than pointing at them. Textbook grounding: Dayan & Abbott, *Theoretical Neuroscience*, ch. 7 (*Recurrent Networks* and *Stochastic Networks*).

## State, and why it is a separate kind of memory

A recurrent network at any instant has a **state**: the vector of every unit's activity. Feed it an input and let it run, and that vector moves — a trajectory through a space with one dimension per neuron. Two quantities move on very different timescales. **Weights** change slowly, across trials, and they define the shape of the space. **State** changes fast, within a trial, and it is where in that space you currently are.

This matters because it gives a network two memories. The weights remember what it learned. The state remembers what just happened — and it does so without any weight changing at all. A network that resets its state between inputs throws that second memory away on every step.

## Energy landscapes and why settling stops

For a recurrent network with **symmetric** weights (w_ij = w_ji), you can write an energy function

    E(x) = -1/2 * sum_ij w_ij x_i x_j  +  sum_i theta_i x_i

and show that updating one unit at a time in the direction that minimises its local contribution can never increase E. Each update either lowers the energy or leaves it unchanged. Since the state space is finite (binary units) or the energy is bounded below (continuous units), the dynamics cannot wander forever: they must come to rest at a local minimum.

That is the whole argument for why settling terminates, and it is worth noticing what it rests on. Symmetry is doing the work. If w_ij differs from w_ji, the same update can raise E, and the network can cycle forever instead of settling — the trajectory becomes a limit cycle rather than a fixed point.

A local minimum of E is an **attractor**. The set of starting states that end up at a given attractor is its **basin of attraction**. A landscape with many minima is a network with many possible answers, selected by where you started.

## Hopfield networks: storing memories as minima

The canonical construction sets weights from the patterns you want to store, by Hebbian outer product:

    w = (1/N) * sum_p (xi_p xi_p^T),  with the diagonal zeroed

Each stored pattern becomes a local minimum, so presenting a corrupted version of a pattern and letting the network settle recovers the original. That is content-addressable memory: the address is a partial version of the content.

Two facts constrain it.

**Capacity.** For random patterns, reliable recall holds up to roughly 0.138N patterns for N units. At N = 100 that is about 14. Below the limit recall is essentially perfect; above it, performance collapses quickly rather than degrading gently.

**Spurious attractors.** The landscape contains minima you never put there. Mixtures of an odd number of stored patterns — the sign of the sum of three patterns, for instance — are themselves stable fixed points. The network settles confidently into a state that corresponds to no memory it was taught. Nothing in the dynamics distinguishes a spurious minimum from a real one; both are just places the energy is locally lowest.

## Continuous and spiking versions

Not every attractor is a point. If the landscape has a flat valley rather than isolated pits, the network has a **continuous attractor** — a line or ring of equally stable states. Head-direction systems are the standard example: a bump of activity sits somewhere on a ring of neurons, and any position on the ring is stable, so the bump encodes a continuous variable by where it rests.

In a spiking network the same idea appears as **persistent activity**. An individual spike is a transient event; it cannot hold a value. What holds the value is a self-sustaining pattern of firing across a subpopulation, maintained by recurrent excitation against inhibition. The fixed point exists in the firing rates, not in any one neuron's membrane.

## Telling a real basin from a slow mode

This is the practical skill, and it is subtle. Suppose you start a network from many different initial states, let it settle, and find the settled states remain distinct. Two explanations fit:

1. **Genuine multi-basin structure.** The landscape has many separate minima and each run fell into a different one. The states would stay distinct at infinite iterations.
2. **Slow modes.** There is really one minimum (or a flat valley), but the descent is extremely slow in some directions, and the run was stopped before convergence. Given enough iterations the states would merge.

Three diagnostics separate them.

**Convergence rate.** Near a quadratic minimum, gradient descent converges geometrically: the distance to the fixed point shrinks by a constant factor per step, so plotted on a log axis it is a straight line falling steadily. A distance that decays sharply and then plateaus, or that creeps down as a slow power law, indicates a flat direction rather than settled basins. Crucially, a distance that barely changes when you run 100 times longer is evidence *against* ordinary geometric convergence to well-separated minima — but it does not by itself distinguish flat valley from separate pits.

**Perturbation and return.** Take a settled state, add a small perturbation, and let it settle again. If it returns to the same point, that point is a genuine attractor and the perturbation stayed inside its basin. If it drifts to a nearby but different resting place and stays there, you are on a flat manifold, not in a pit. Sweep the perturbation size: a real basin has a radius, and you can find it.

**Local curvature.** At the fixed point, examine the Jacobian of the dynamics (or the Hessian of the energy). Eigenvalues tell you the shape: a direction with a very small curvature is a slow mode — the landscape is nearly flat there, so descent along it takes enormous numbers of iterations. A genuine isolated minimum has meaningful curvature in every direction.

The honest position is that convergence-rate evidence alone is usually ambiguous, and the perturbation test is what settles it, because it asks the question directly: is there a restoring force here or not?

## Why any of this matters for a predictive-coding network

In a PC network, settling is gradient descent on an energy function, so everything above transfers: the settled answer is a minimum, the initial state selects which minimum, and carrying state across timesteps means each new input starts its descent from wherever the last one finished. That is either a feature — continuity, faster re-settling, memory across time — or a trap, if the network stays in a stale basin that no longer suits the current input.

The distinction is not decorative. If the settled output depends on the starting state, then two identical observations can produce different committed actions, and the network's behaviour is not a function of its input alone. Whether that is desirable depends entirely on whether the basin being selected is the right one.
