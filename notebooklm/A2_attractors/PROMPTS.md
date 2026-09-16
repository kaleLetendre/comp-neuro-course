# A2 — NotebookLM prompts

Paste these verbatim. They are written against this lesson's five learning outcomes and the learner's own unresolved experiment, which is what keeps the output from drifting into a generic explainer.

## Sources to select

All three documents in this folder (`01_concept_brief`, `02_learning_outcomes`, `03_project_context`). Nothing else — extra sources dilute a targeted overview.

---

## Where each prompt goes

| Prompt | Where it goes in NotebookLM |
|---|---|
| Audio Overview | Audio Overview card → **Customize** → the box labelled *"What should the AI hosts focus on in this episode?"* |
| Video Overview | Video Overview card → **Customize** → same kind of focus box |
| Mind map | No prompt box — it generates from the sources. The structure below is what to check it against. |
| Chat starters | The main **chat box** in the notebook, one at a time, after listening |

If the customisation box truncates your text, use the **compact version** below instead — it front-loads the constraints that matter most, so a cut tail costs least.

## Audio Overview — compact version (use if the box is length-limited)

> Build from first principles and assume no prior knowledge — if a concept is needed, explain it rather than referring to it. Do not answer the questions in the learning-outcomes source; teach toward them. Treat the listener's CartPole experiment as unresolved; do not say which interpretation is right. Focus, longest section first: how to distinguish genuine multi-basin structure from unconverged slow modes — convergence-rate signature, perturbation-and-return test, curvature at the fixed point. Then why symmetric weights guarantee energy never increases and what breaks when asymmetric. Then state vs weights as fast and slow memory. Then briefly bump attractors and persistent activity. Keep the numbers: 0.138N capacity, 2.1 to 1.7 over a hundredfold iteration increase, action range −0.69 to +0.67. Go to the mathematics; no marbles-in-bowls.

## Audio Overview — full customisation prompt

> The listener is a strong programmer with no formal neuroscience background, studying before an MSc. Assume no prior neuroscience: whenever a concept is needed — membrane dynamics, firing rates, excitation and inhibition — explain it rather than referring to it. They are comfortable with linear algebra, calculus and code, so do not soften the mathematics; the gap to cover is biological, not technical. Where something was met in an earlier lesson, a one-line recap is welcome rather than an assumption.
>
> Spend the episode on four things, in this order. First, why a symmetric weight matrix guarantees the energy function never increases, and what specifically breaks when weights are asymmetric — work through what a single unit's update does to the energy. Second, the difference between state as fast per-trial memory and weights as slow cross-trial memory, and why the same weights can produce different committed answers from different starting states. Third, and at the greatest length: how you would actually tell a genuine multi-basin landscape apart from slow modes that have not converged — the convergence-rate signature, the perturbation-and-return test, and local curvature at the fixed point. Be concrete about what each one measures and what result points which way. Fourth, briefly, bump attractors and how persistent firing implements a fixed point in a spiking network.
>
> The listener also has a research project of their own, described in the project context document. Use it as ONE worked example toward the end, not as the frame for the episode — the subject is attractor dynamics in general, and the project is an application of it. When you do reach it: twenty initial states, the same clamped observation, settled states that stay distinct, an action readout spanning −0.69 to +0.67. Treat it as an open question, not a solved one. Do not assert which of the two interpretations is correct; nobody knows yet, and the listener is about to run the experiment that decides it.
>
> The learning outcomes document contains the questions they will be assessed on. Do not answer them directly and do not read them out as a quiz. Teach the mechanisms so the listener can construct the answers.
>
> Keep the numbers in: 0.138N capacity, the 19% distance reduction over a hundredfold iteration increase, the −0.69 to +0.67 action range. Precision is what makes this useful. Avoid analogies to marbles in bowls after the first one — go to the actual mathematics.

## Video Overview — customisation prompt

> Same audience and same four topics as above. Prioritise anything that benefits from being seen: the energy landscape with multiple minima and their basins, a trajectory descending into one of them, the difference between a landscape of separate pits and a single flat valley, and a side-by-side of geometric convergence versus a slow mode on a log-scale distance plot. Show the perturbation test as a picture — a settled point, a small displacement, and the two possible outcomes. Keep narration tied to the listener's own experiment and do not claim to know its result.

## Mind map

> Organise around: energy landscape → fixed points → basins → what selects a basin (initial state) versus what shapes the landscape (weights) → diagnosing basins against slow modes → attractors in spiking networks. Keep the three diagnostics as distinct branches with their measurements attached.

## Chat starters

Ask these in the notebook after listening:

1. Work through the energy argument for a 4-unit symmetric network — what happens to E when one unit flips, and why can it never increase?
2. If my settled states are 1.7 apart after 10000 iterations and 2.1 apart after 100, what do I expect the distance to be at 50000 under each of the two hypotheses?
3. What perturbation magnitude should I use, and how do I choose it without already knowing the basin radius?
4. Why does a spurious attractor look identical to a real one from inside the dynamics?
5. What would I expect to see in the Hessian eigenvalues if this is a flat valley rather than separate minima?
6. My network is not symmetric-weighted. Which parts of the Hopfield energy argument survive that, and which do not?
