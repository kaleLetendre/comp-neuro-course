# Materials

Everything this course needs, and where to get it. One required purchase; everything else is free.

## Required

### The textbook

**Dayan, P. & Abbott, L.F. — *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems*. MIT Press, 2001.**

- Publisher: <https://mitpress.mit.edu/9780262041997/theoretical-neuroscience/>
- Paperback ISBN 978-0-262-54185-5 · Hardcover ISBN 978-0-262-04199-7
- Authors' companion site: <https://www.gatsby.ucl.ac.uk/~dayan/book/> — table of contents, figures, errata, teaching support

The whole foundation track (F1–F11) is this book, chapter by chapter, and it carries five of the advanced lessons outright. There is no substitute in the course as written.

Check your university library before buying: most institutions with a neuroscience or ML programme hold it, often with electronic access.

### The authors' exercise sets — free

<https://www.gatsby.ucl.ac.uk/~dayan/book/exercises.html>

Dayan & Abbott publish problem sets for all ten chapters, with MATLAB code and data files. These are assigned in every foundation lesson and **take precedence over this course's own exercises** where the two overlap — they are the authors' problems.

Chapter 1's set includes `c1p8.mat`: twenty minutes of real recordings from a fly H1 neuron responding to white-noise visual motion, collected by Rob de Ruyter van Steveninck, sampled at 500 Hz. Several problems build on it.

From the repo root:

```sh
./fetch_exercises.sh
```

That pulls all ten sets plus code and data into `exercises/` (gitignored — the files are the authors', we do not redistribute them).

### Python

Python 3 with `numpy`. `matplotlib` for the plotting exercises, `scipy` for a few, `torch` only if you prefer it — every simulation in the course runs on numpy alone. The exercise sets are written for MATLAB; translating them is part of the work.

## Supporting papers

Twenty-eight papers are cited across the advanced tracks. Ten are openly available and fetch automatically:

```sh
python3 fetch_papers.py
```

That script doubles as the bibliography — every entry carries a DOI resolved against Europe PMC. It lands files in `papers/` (gitignored).

**Openly available (10):** Izhikevich 2006 on polychronization · Hertäg & Sprekeler 2020 (eLife) · Ólafsdóttir, Bush & Barry 2018 · Bogacz 2017's free-energy tutorial · Millidge, Seth & Buckley 2021 · Feldman & Friston 2010 · Salvatori et al. 2022 · Friston, Daunizeau & Kiebel 2009 · Song et al. 2020 (NeurIPS) · Whittington & Bogacz 2017

**Needs institutional access (18):** Hopfield 1982 · Fries 2005 · Wang 2010 · Tsodyks & Markram 1997 · Attwell & Laughlin 2001 · Roy, Jaiswal & Panda 2019 · Schultz, Dayan & Montague 1997 · Yu & Dayan 2005 · Bastos et al. 2012 · Poirazi, Brannon & Mel 2003 · Larkum 2013 · London & Häusser 2005 · Schafer et al. 2012 · Hensch 2005 · Huttenlocher & Dabholkar 1997 · McClelland, McNaughton & O'Reilly 1995 · Foster & Wilson 2006 · Rao & Ballard 1999

DOIs for all of them are in `fetch_papers.py`. The lessons that depend on a closed paper say so and name a substitute where one exists.

## Optional

### NotebookLM — free

<https://notebooklm.google.com>

The packs in `notebooklm/` generate an audio overview for a lesson, which is the first step of the running order. A free Google account is enough. Each pack folder holds the sources to upload and the prompts to paste; the Drive mirror is convenient on a phone.

### Further reading, where the book stops

- **Gerstner, Kistler, Naud & Paninski — *Neuronal Dynamics*.** Free online at <https://neuronaldynamics.epfl.ch/>. Modern, spiking-focused, good where Dayan & Abbott is thin (synaptic delays, adaptive exponential models).
- **Buzsáki — *Rhythms of the Brain*.** Breadth on oscillations for A3.

## What is not here

No copy of the textbook is distributed with this repo, and none will be. Buy it, borrow it, or use a library copy.
