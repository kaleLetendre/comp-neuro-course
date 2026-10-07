# Bridge · Synthesis checkpoint

!!! abstract "At a glance"

    **Length** — one sitting — no new material; the work is connecting what is already there · about ~100 minutes, one sitting
    **Before this** — F1-F11, all of them
    **Reading** — none new. The foundation lessons themselves, and your own notes from them.

[TOC]

## Lesson spec

**Goal:** Establish that the foundation track is a connected body of ideas rather than eleven separate ones, by forcing connections the individual lessons never made. Each question deliberately spans lessons that were taught apart. A miss here is not a gap in one lesson — it is a seam that never closed, and it is cheaper to find now than inside track A.

??? note "Scope — what the lesson covers"

    - Tracing one signal end to end across the encoding, decoding and information lessons
    - Reconciling the several distinct things the word "rate" means across F1, F6 and F8
    - Working out which claims survive an abstraction and which need the layer underneath it
    - The convergence argument: three lessons arriving independently at oriented filters
    - Comparing two error-driven learning rules that look alike and are not
    - Not covered: anything new. If a question cannot be answered, the fix is to return to the named lesson.

**You should be able to answer:**
1. Trace one signal from a light stimulus to a decoded estimate: which lesson's machinery governs each stage, and where is information irreversibly lost along the way?
2. "Firing rate" appears in F1 as a quantity estimated from spikes, in F6 as the output of an f-I curve, and in F8 as the state variable of a population model. Are these the same quantity? Name the assumption that has to hold for the identification to be legitimate, and one regime where it fails.
3. F5 derives the all-or-none spike from channel kinetics; F6 replaces that with threshold-and-reset; F9's STDP depends on precise spike timing. Which of F9's claims survive the F6 abstraction, and which quietly need F5's biophysics?
4. F2 *measured* oriented, localised filters in V1. F9's Oja rule extracts principal components. F11's sparse coding, fit to natural images, *produces* oriented localised filters. State the argument that connects these three results, and name its weakest link.
5. F9's delta rule and F10's TD error both multiply an error signal by an activity term. Where does each get its error from, and why does one require a teacher while the other does not?

**Feeds:** track A, which begins immediately after and assumes every foundation lesson is in place.

**Done when:** All five can be reasoned through unaided — or each miss is logged against the specific foundation lesson it exposes, and that lesson is revisited before A1.

## Coursework

This set has **three** pieces, not the usual four — there is no guided reading, because a synthesis checkpoint has no new source to read. Everything the three pieces draw on is already sitting in F1–F11; the work is entirely connective.

**synthesis write-up (Piece 1) → integrative simulation (Piece 2) → gap audit (Piece 3)**

The write-up is done first because it forces you to state the connections in your own words before any code can paper over a gap with a default parameter. The simulation is done second because it is where an unstated assumption in the write-up gets caught mechanically — a lesson's machinery that you described correctly in prose but don't actually have working code for will fail here, not there. The gap audit is done last and is the actual gate: it is the honest per-lesson ledger that decides whether track A starts.

??? note "Coverage map"

    | Piece | Type | Acceptance criteria addressed |
    |---|---|---|
    | 1 — Synthesis write-up | synthesis write-up | 1, 2, 3, 4, 5 (all five — this is their direct vehicle) |
    | 2 — Integrative simulation | simulation | 2 (made concrete in running code: is a spike-count rate estimate the same quantity as a model neuron's driving current?) |
    | 3 — Gap audit | structured self-report | none directly — it audits the F1–F11 foundations that 1–5 depend on, and is the piece that catches a criterion answered correctly by luck rather than by a solid lesson underneath it |

    All five acceptance criteria are addressed, primarily by Piece 1; Piece 2 re-exercises criterion 2 as running code instead of prose; Piece 3 is the safety net under all five.

=== "Piece 1 — Synthesis write-up"

    **Type:** synthesis write-up · **Time:** ~45 min

    **Learning goals**
    - State which foundation lesson's machinery governs each stage of a stimulus-to-estimate pipeline, and identify where information is destroyed rather than merely transformed.
    - Distinguish "same name" from "same quantity" across models that use "firing rate" at different levels of abstraction.
    - Separate which claims of a fine-grained model (STDP, spike-timing) survive a coarser abstraction (LIF threshold-and-reset) from which claims quietly still depend on the layer the abstraction discarded (channel biophysics).
    - Trace a three-step empirical argument (measured V1 filters, two different unsupervised objectives) to its weakest inferential link, rather than accepting it because the conclusion is familiar.
    - Distinguish two error-driven learning rules by where each one's error signal originates, and connect that to whether a teacher is required.

    **Task**

    Answer all five in prose. Cite the specific foundation lesson(s) behind each claim you make (e.g. "F3's Fisher information bound," not "decoding theory"). At least one answer — recommended: Q1 — must include a diagram or table.

    1. Trace one signal from a light stimulus to a decoded estimate: which lesson's machinery governs each stage, and where is information irreversibly lost along the way?
    2. "Firing rate" appears in F1 as a quantity estimated from spikes, in F6 as the output of an f-I curve, and in F8 as the state variable of a population model. Are these the same quantity? Name the assumption that must hold for the identification to be legitimate, and one regime where it fails.
    3. F5 derives the all-or-none spike from channel kinetics; F6 replaces that with threshold-and-reset; F9's STDP depends on precise spike timing. Which of F9's claims survive the F6 abstraction, and which quietly need F5's biophysics?
    4. F2 measured oriented, localised filters in V1. F9's Oja rule extracts principal components. F11's sparse coding, fit to natural images, produces oriented localised filters. State the argument connecting these three results, and name its weakest link.
    5. F9's delta rule and F10's TD error both multiply an error signal by an activity term. Where does each get its error from, and why does one require a teacher while the other does not?

    **Deliverable**

    A written document, roughly 150–300 words per question (750–1500 words total), each answer labelled 1–5, with a diagram or table for at least one answer.

    ??? info "Rubric — how this is marked"

        | Band | Criteria |
        |---|---|
        | Strong | Q1: a labelled stage→lesson→loss table or diagram naming at least two genuinely different loss points (e.g. spike-generation quantization/Poisson noise, and the LN cascade's linear projection discarding orthogonal stimulus components), not just "noise is added somewhere." Q2: correctly names the averaging/ergodicity assumption (long window or large population so estimator variance→0) and gives a concrete failing regime (short window, small population — ties to F1's Fano-factor argument). Q3: correctly separates "spike order/causality" (survives F6) from "fine Δt-dependent magnitude/shape of the STDP window" (needs F5's channel/calcium kinetics), not just "some things survive, some don't." Q4: identifies that Oja/PCA does *not* reproduce oriented localised filters on natural images (its components are smooth/global) and that sparse coding's different objective is what does the work — names this substitution as the weakest link, not just "there's a weak link somewhere." Q5: correctly states delta-rule error = target − output (externally supplied) vs. TD error = r + γV(s′) − V(s) (self-generated via bootstrapping), and explains that only an externally-supplied target requires a teacher. |
        | Adequate | Right general shape on each answer but with a rougher justification: Q1 has a table/diagram but only one clear loss point; Q2 names *some* averaging condition without pinning down what regime breaks it; Q3 correctly separates the two categories but mischaracterises which one needs F5; Q4 correctly names sparse coding as the real explanation without explicitly flagging PCA as the weak link; Q5 gets the teacher/no-teacher conclusion right without stating both error formulas. |
        | Not yet | Any answer that treats "firing rate" (Q2), "survives the abstraction" (Q3), or "the argument's weakest link" (Q4) as if the question weren't asking for a specific mechanism — e.g. Q4 answered as "all three show Hebbian learning finds structure," which conflates PCA and sparse coding into the same result. No diagram/table anywhere. |

    !!! note "Grader key hidden"

        The marking criteria for this piece are in the teacher build.

=== "Piece 2 — Integrative simulation"

    **Type:** simulation · **Time:** ~25 min

    **Requires machinery from three foundation lessons: F1 (Poisson spike generation and rate estimation from spike counts), F6 (leaky integrate-and-fire dynamics — threshold and reset), and F9 (unconstrained Hebbian potentiation vs. multiplicative synaptic scaling).** A learner shaky on any one of the three will get a script that either doesn't run, or runs but produces numbers that don't match the expected pattern below — that mismatch *is* the diagnostic.

    **Learning goals**
    - Build one pipeline where a broken assumption in F1, F6, or F9 shows up as code that fails or diverges from the stated pattern, rather than as a wrong answer on a quiz about that lesson alone.
    - Observe, in actual generated numbers, that a rate-based Hebbian rule driving a real spiking (not just linear) neuron is still an unbounded positive-feedback loop, and that periodic multiplicative rescaling is what bounds it.
    - Confront criterion 2's tension directly in running code: is the spike-count-based rate estimate (F1) the same kind of quantity as the current driving a model neuron's membrane (F6)?

    **Task**

    Implement the following in NumPy, under 100 lines, exactly as specified:

    ```python
    import numpy as np

    def run(scaling_on, seed=0):
        rng = np.random.RandomState(seed)
        N = 20                                      # presynaptic synapses onto one LIF neuron
        r_pre_true = rng.uniform(3.0, 8.0, size=N)  # Hz, true presynaptic rates (F1)
        w = np.full(N, 0.5)                         # initial synaptic weights
        eta, w_max = 0.01, 2.0                      # Hebbian learning rate, weight ceiling
        r_target, K = 30.0, 25                      # scaling target (Hz), correction period (windows)
        n_windows, T_window, dt = 300, 0.2, 0.001   # 300 windows of 200 ms, 1 ms bins
        n_bins = int(T_window / dt)
        tau_m, V_th, Q = 0.01, 10.0, 4.0            # LIF membrane tau, threshold, synaptic gain (F6)
        log = {}

        def lif_spike_count(weights, pre_spikes):
            """Simulate the LIF membrane bin-by-bin, count postsynaptic spikes (F6)."""
            V = 0.0
            count = 0
            for b in range(pre_spikes.shape[0]):
                V += (dt / tau_m) * (0.0 - V) + Q * np.dot(weights, pre_spikes[b])
                if V >= V_th:
                    count += 1
                    V = 0.0
            return count

        for step in range(n_windows):
            pre_spikes = rng.rand(n_bins, N) < (r_pre_true * dt)   # Poisson-approx spikes (F1)
            r_pre_est = pre_spikes.sum(axis=0) / T_window            # F1: rate = count / window

            post_count = lif_spike_count(w, pre_spikes)
            r_post_est = post_count / T_window

            dw = eta * r_pre_est * r_post_est / N                     # F9: Hebbian update
            w = np.clip(w + dw, 0, w_max)

            if scaling_on and (step + 1) % K == 0:
                r_post_now = lif_spike_count(w, pre_spikes) / T_window
                factor = np.clip(r_target / max(r_post_now, 1e-6), 0.5, 1.5)
                w = np.clip(w * factor, 0, w_max)                      # F9: multiplicative scaling

            if step + 1 in (50, 150, 300):
                log[step + 1] = (w.mean(), r_post_est, w.max())

        return log
    ```

    Run twice: **Condition A** (`scaling_on=False`) and **Condition B** (`scaling_on=True`), both with `seed=0`. Print `mean(w)`, `r_post_est`, and `max(w)` at steps 50, 150, 300 for each. Also report the first step at which every weight in Condition A equals `w_max` exactly.

    Then answer in 2–3 sentences each:
    (b) Trace the loop `r_pre_est → LIF current → post spikes → r_post_est → dw → w → (current again)`. Why does nothing in this loop decrease as `w` grows — why is it a positive-feedback loop rather than a settling process?
    (c) `r_pre_est` is a quantity from which lesson? Using it directly as the "current" driving the LIF membrane in `lif_spike_count` quietly assumes it behaves like a genuine continuous physical quantity (F6/F5's sense) rather than a noisy finite-window estimate (F1's sense) — tie this to your answer to Piece 1, Q2.

    **Deliverable**

    The script, its printed output for both conditions, the first-full-saturation step for Condition A, and the two written answers.

    ??? info "Rubric — how this is marked"

        | Band | Criteria |
        |---|---|
        | Strong | Reproduces both conditions within the expected pattern (Condition A saturates to `w_max=2.0` and stays there from step 100 onward, ending with `r_post_est=45.0` Hz at both 150 and 300; Condition B never permanently saturates — it may transiently touch `w_max` between corrections but is pulled back by the next K=25-step correction, ending at a stable `mean(w)≈1.333`, `max(w)≈1.333`, well below `w_max`, at both step 150 and 300). (b) names the loop explicitly and states there is no term that decreases as `w` grows — growth compounds until the external clip stops it. (c) correctly names F1 for `r_pre_est`, states the assumption explicitly, and connects it to Piece 1 Q2's averaging-window argument. |
        | Adequate | Qualitatively right pattern (A saturates and stays there; B stays bounded overall) even if the exact numbers or the first-saturation step are off by a step or two; (b) identifies "more w → more post activity → more potentiation" without naming it as a loop with no restoring term; (c) names F1 but doesn't explicitly connect to Piece 1 Q2. |
        | Not yet | A and B show no meaningful difference, or B also permanently saturates; no attempt at (b) or (c); or the script needs more than superficial fixes to run at all (a strong signal that the F6 LIF mechanics or the F1 rate-from-count step wasn't understood, not just mistyped). |

    !!! note "Grader key hidden"

        The marking criteria for this piece are in the teacher build.

=== "Piece 3 — Gap audit"

    **Type:** structured self-report · **Time:** ~20 min

    **Learning goals**
    - Produce an honest, lesson-by-lesson self-assessment instead of a single global "I think I'm fine."
    - For every lesson flagged as not holding, name the specific sub-topic to revisit — not "review F6" but "review the shunting-inhibition section of F6."
    - Use the write-up and the simulation's actual outcome as evidence for the audit, rather than a memory-based gut check performed in isolation from what just happened in Pieces 1–2.

    **Task**

    Fill in one row per foundation lesson (F1–F11, in order). Do not skip any row.

    | Lesson | Holds? (yes / shaky / no) | Evidence (which of Piece 1's five questions, or Piece 2, surfaced this — or "none, self-assessed") | If shaky/no: specific sub-topic to revisit |
    |---|---|---|---|
    | F1 | | | |
    | F2 | | | |
    | F3 | | | |
    | F4 | | | |
    | F5 | | | |
    | F6 | | | |
    | F7 | | | |
    | F8 | | | |
    | F9 | | | |
    | F10 | | | |
    | F11 | | | |

    For any row marked "shaky" or "no," the sub-topic entry must name a specific concept, formula, or result (e.g. "Fisher information as a Cramér–Rao bound," not "decoding"), not a re-statement of the lesson's title.

    **Deliverable**

    The completed 11-row table.

    ??? info "Rubric — how this is marked"

        | Band | Criteria |
        |---|---|
        | Strong | All 11 rows filled; every "shaky"/"no" row has a genuinely specific sub-topic (a named concept/formula/result, not a lesson title); at least one row's "Evidence" column cites a concrete moment from Piece 1 or Piece 2 rather than "none" for every row. |
        | Adequate | All 11 rows filled; most "shaky"/"no" sub-topics are specific but one or two are vague (just the lesson name repeated); evidence column mostly says "self-assessed" without linking back to Pieces 1–2. |
        | Not yet | Rows missing or left blank; every lesson marked "yes" with no engagement with whether Pieces 1–2 actually stressed it; any "shaky"/"no" row with a vague or missing sub-topic. |

    !!! note "Grader key hidden"

        The marking criteria for this piece are in the teacher build.

## Completion bar

This lesson counts as done when all three pieces have been attempted, the gap audit's 11 rows are all filled with specific (not vague) entries, and every foundation lesson marked "shaky" or "no" has either been reviewed against its named sub-topic or explicitly logged as a deferred gap with that sub-topic named. Track A does not start until the gap-audit table has zero rows with a missing or vague sub-topic entry — it may still start with logged, named gaps outstanding, since the point of this checkpoint is to make gaps visible and specific, not to eliminate them before moving on.
