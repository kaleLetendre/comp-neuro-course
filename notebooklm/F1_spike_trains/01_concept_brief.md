F1 concept brief. Spike trains and firing rates.

Teaching substance for the first lesson of a computational neuroscience course, following Dayan and Abbott, Theoretical Neuroscience, chapter one. This document is written to be read aloud, so it carries no symbols, formulas or figures. Every relationship is stated in words.

What is actually measured.

Put an electrode near a neuron and what you record is a voltage trace with sharp events in it, each about one millisecond wide and around one hundred millivolts tall. Those are action potentials, or spikes. The first decision computational neuroscience makes, and it is a decision rather than a discovery, is to throw the waveform away. A spike is treated as a point in time. An event, not a shape.

The justification is that spikes from a given neuron are stereotyped. They all look much the same, so the shape carries little that varies with the stimulus. What varies is when they happen and how many there are. So the raw data of the field is a list of times, and everything else is built on top of it.

This matters more than it sounds. It means the quantities people talk about, firing rates and tuning curves and population codes, are all constructions laid over a list of timestamps. None of them are measured directly.

Firing rate is not one thing.

Ask what a neuron's firing rate is and there are at least three different answers, and they are not equal to one another.

The spike count rate is the crudest. Count the spikes in a window and divide by the length of the window. Twelve spikes in two seconds is six hertz. It is a single number for the whole window, it says nothing about when within that window the spikes fell, and it needs only one trial.

The time dependent firing rate is what you want when the stimulus changes over time. It is a rate defined at every instant. But a single spike train does not really contain an instantaneous rate, because at any given instant there is either a spike or there is not. Getting a time dependent rate means estimating one, which means smoothing the spikes somehow.

The trial averaged rate takes many repeats of the same stimulus, lines them up, and averages across them. That is what a peristimulus time histogram shows. It gives a clean time dependent rate, at the cost of assuming the neuron does the same thing on every repeat and that averaging across repeats is meaningful. A brain, in the middle of behaving, only ever gets one trial.

So when a paper says the firing rate, the honest question is always: which one, estimated how, over what window.

Estimation, and the trade off you cannot escape.

There are three standard ways to turn spikes into a time dependent rate.

Binning. Divide time into bins, count the spikes in each bin, divide by the bin width. Simple, and it produces a blocky estimate whose appearance depends on where you happened to put the bin edges.

Sliding window. Move a window of fixed width along the train and count within it as it goes. Smoother, and no edge artefacts, but the estimate at any moment is contaminated by spikes up to half a window away on either side.

Kernel smoothing. Replace each spike with a smooth bump, and add the bumps together. The width of the bump sets the smoothness. Whether the bump is symmetric or only looks backward in time matters if you care whether a downstream neuron could actually compute this estimate as it goes.

All three face the same trade off, and this is the central practical point of the lesson. A wide window averages over many spikes, so the estimate is stable, but it smears out fast changes. A stimulus transient lasting twenty milliseconds disappears inside a hundred millisecond window. A narrow window tracks fast changes, but it contains very few spikes, so the estimate is dominated by counting noise. Take a neuron firing at twenty hertz. In a ten millisecond window it fires, on average, one fifth of a spike. Most windows are empty, and the occasional window with a single spike reports a rate of one hundred hertz. The estimate is mostly zeros punctuated by wild overshoots.

You cannot have both. This is the bias variance trade off arriving in neuroscience wearing different clothes. Choosing a window width is a hypothesis about which timescale matters, smuggled in as a preprocessing step.

Spike train statistics.

If a neuron fired completely at random at a constant average rate, its spikes would follow what is called a Poisson process. Each spike is independent of the last. The process has no memory of when it last fired. Two consequences follow. The gaps between spikes are exponentially distributed, which means the most common gap is a very short one, even when the average gap is long. And the Fano factor, which is the variance of the spike count divided by the mean spike count measured over many repeated windows, comes out at exactly one, whatever window length you choose.

Poisson is the reference against which real data gets compared. Real cortical neurons are roughly Poisson like, which is itself surprising and a little embarrassing, because it means much of their variability looks like noise. But they depart from it in structured ways.

The clearest departure comes from the refractory period. After firing, a neuron cannot fire again for a millisecond or two. That forbids the very short gaps a Poisson process produces freely, which makes the spike train more regular than Poisson. Regularity shows up as a reduced Fano factor. There is a neat consequence worth holding on to: for a process where each gap is drawn independently, the Fano factor measured over long windows approaches the squared coefficient of variation of the gaps. The coefficient of variation is just the standard deviation of the gaps divided by their mean. So the effect of a refractory period on the Fano factor can be predicted with pencil and paper before any simulation is run. Other neurons go the other way. Bursting makes spikes clump together, variance rises, and the Fano factor climbs above one.

So the Fano factor is a compact diagnostic. At one, the neuron looks Poisson. Below one, something is imposing regularity. Above one, something is imposing clumping.

Tuning curves.

A tuning curve plots a neuron's firing rate against some property of the stimulus. Orientation, direction of motion, sound frequency, position in space. It is the simplest statement of what a neuron is about. The peak of the curve names the stimulus the neuron prefers. The width of the curve says how sharply it discriminates. A narrow curve means the neuron says a great deal when it fires but stays silent for most stimuli. A broad curve means it responds to a great deal but distinguishes little. That trade off comes back, much sharpened, when decoding is covered later in the course.

Notice what a tuning curve has already assumed. That a rate is the right summary of the response, and that the neuron's response is stable enough across repeats to be worth plotting at all.

The open question.

Does the brain use spike rates, or spike timing? This is not settled, and a course that presents it as settled is lying.

The case for rate. Cortical spiking is highly variable from trial to trial, rates vary systematically with stimuli, and rate based models predict a great deal of behaviour successfully.

The case for timing. Some systems demonstrably use it. Sound localisation in the barn owl and in mammals resolves differences between the two ears of tens of microseconds, which is far finer than any rate code could carry. And some behavioural decisions are made faster than a downstream neuron could plausibly have averaged a rate at all.

The honest position is that it is likely both, differently in different systems, and that the answer depends on the timescale of the computation being performed. Hold the question open. It comes back in every later lesson.
