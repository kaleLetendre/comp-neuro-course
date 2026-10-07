# Materials

Everything this course needs, and where to get it. One required purchase; everything else is free.

## Required

### The textbook

**Dayan, P. & Abbott, L.F. — *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems*. MIT Press, 2001.**

- Publisher: <https://mitpress.mit.edu/9780262041997/theoretical-neuroscience/>
- Paperback ISBN 978-0-262-54185-5 · Hardcover ISBN 978-0-262-04199-7
- Authors' companion site: <https://www.gatsby.ucl.ac.uk/~dayan/book/> — table of contents, figures, errata, teaching support

The whole foundation track (F1–F11) is this book, chapter by chapter, and it carries five of the advanced lessons outright. There is no substitute in the course as written.

Check a university library before buying: most institutions with a neuroscience or machine-learning programme hold it, often with electronic access.

### Everything else the authors publish — free

The address printed in the book, `mitpress.mit.edu/dayan-abbott`, is **dead**. The material moved to the authors' own site and is more extensive than the book suggests:

<https://www.gatsby.ucl.ac.uk/~dayan/book/>

One script fetches all of it into `exercises/` (gitignored):

```sh
./fetch_book_materials.sh
```

| What | Why it matters |
|---|---|
| **Exercise sets** for all ten chapters, with MATLAB code and data | Assigned in every foundation lesson; see below |
| **Figures**, per chapter, as PowerPoint and PNG collections | Every figure in the book. The PowerPoint files upload to Google Drive as Slides, which NotebookLM accepts as a source — so a video overview can work from the book's own diagrams |
| **Errata**, by printing | Two printings exist; the second (identified by "10 9 8 7 6 5 4 3 2" on page iv) already carries the first printing's corrections. Check yours, and check the errata before teaching a chapter |
| **Complete reference list**, as PDF and LaTeX | The book's bibliography, ready to cite |
| **Chapter 7 in full**, free | *Network Models* — the authors' own sample chapter, and the text behind F8. Anyone can read that one without buying the book |

### Direct links

Everything below is free, from the authors. `fetch_book_materials.sh` downloads it all, but the links are here so you can browse without cloning.

| | |
|---|---|
| Companion site | <https://www.gatsby.ucl.ac.uk/~dayan/book/> |
| Table of contents | <https://www.gatsby.ucl.ac.uk/~dayan/book/toc.html> |
| **Exercises index** | <https://www.gatsby.ucl.ac.uk/~dayan/book/exercises.html> |
| Teaching support (figures, references) | <https://www.gatsby.ucl.ac.uk/~dayan/book/teaching.html> |
| Errata | <https://www.gatsby.ucl.ac.uk/~dayan/book/errata.html> · [PDF](https://www.gatsby.ucl.ac.uk/~dayan/book/errata.pdf) |
| Chapter 7 in full, free | <https://www.gatsby.ucl.ac.uk/~dayan/book/ch7.pdf> |
| All exercise code and data (one archive) | <https://www.gatsby.ucl.ac.uk/~dayan/book/exall.tar.gz> |
| All figures (one archive) | <https://www.gatsby.ucl.ac.uk/~dayan/book/figures/complete.tar.gz> |

### Exercise set per lesson

| Lesson | Chapter | Exercises | Figures |
|---|---|---|---|
| F1 Spike trains and firing rates | 1 | [c1.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c1/c1.pdf) · [fly H1 data](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c1/data/c1p8.mat) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch1fig.ppt) |
| F2 Receptive fields and reverse correlation | 2 | [c2.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c2/c2.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch2fig.ppt) |
| F3 Neural decoding | 3 | [c3.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c3/c3.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch3fig.ppt) |
| F4 Information theory | 4 | [c4.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c4/c4.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch4fig.ppt) |
| F5 Membrane biophysics | 5 | [c5.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c5/c5.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch5fig.ppt) |
| F6 Integrate-and-fire and synapses | 5 | [c5.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c5/c5.pdf) (shared with F5) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch5fig.ppt) |
| F7 Cable theory and morphology | 6 | [c6.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c6/c6.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch6fig.ppt) |
| F8 Network models | 7 | [c7.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c7/c7.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch7fig.ppt) |
| F9 Plasticity and learning | 8 | [c8.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c8/c8.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch8fig.ppt) |
| F10 Conditioning and reinforcement learning | 9 | [c9.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c9/c9.pdf) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch9fig.ppt) |
| F11 Representational learning | 10 | [c10.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c10/c10.pdf) · [data](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c10/data/c10p1.mat) | [ppt](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch10fig.ppt) |

### The exercise sets

<https://www.gatsby.ucl.ac.uk/~dayan/book/exercises.html>

Dayan & Abbott publish problem sets for all ten chapters, with MATLAB code and data files. These are assigned in every foundation lesson and **take precedence over this course's own exercises** where the two overlap — they are the authors' problems.

Chapter 1's set includes `c1p8.mat`: twenty minutes of real recordings from a fly H1 neuron responding to white-noise visual motion, collected by Rob de Ruyter van Steveninck, sampled at 500 Hz. Several problems build on it.

`fetch_book_materials.sh` pulls these along with everything else. The files are the authors', so they are gitignored rather than committed.

### Python

Python 3 with `numpy`. `matplotlib` for the plotting exercises, `scipy` for a few, `torch` only if you prefer it — every simulation in the course runs on numpy alone. The exercise sets are written for MATLAB; translating them is part of the work.

## Supporting papers

Twenty-eight papers are cited across the advanced tracks. Ten are openly available and fetch automatically:

```sh
python3 fetch_papers.py
```

That script doubles as the bibliography — every entry carries a DOI resolved against Europe PMC. It lands files in `papers/` (gitignored).

Of the twenty-eight, **twenty-one can be had for nothing** and seven need a library. The split is not the one a publisher page suggests, so it is worth stating precisely.

**Downloaded by script (12).** `fetch_papers.py` gets these: Izhikevich 2006 · Hertäg & Sprekeler 2020 · Ólafsdóttir, Bush & Barry 2018 · Bogacz 2017 · Millidge, Seth & Buckley 2021 · Feldman & Friston 2010 · Salvatori et al. 2022 · Friston, Daunizeau & Kiebel 2009 · Song et al. 2020 · Whittington & Bogacz 2017. Then `fetch_closed_papers.py` adds two more from author-hosted copies: McClelland, McNaughton & O'Reilly 1995 (Stanford) and Rao & Ballard 1999 (UT Austin) — both of which the open-access indexes wrongly list as closed.

**Free, but you have to click (9).** These are genuinely open access — OpenAlex confirms it — but PubMed Central, SAGE and Cell all refuse automated downloads, so no script will get them. Open each in a browser and save it:

| Paper | Lesson | Link |
|---|---|---|
| Hopfield 1982 | A2 | <https://www.ncbi.nlm.nih.gov/pmc/articles/346238> |
| Tsodyks & Markram 1997 | A4 | <https://www.ncbi.nlm.nih.gov/pmc/articles/19580> |
| Wang 2010 | A3 | <https://www.ncbi.nlm.nih.gov/pmc/articles/2923921> |
| Attwell & Laughlin 2001 | A5 | <https://journals.sagepub.com/doi/pdf/10.1097/00004647-200110000-00001> |
| Yu & Dayan 2005 | B1 | <http://www.cell.com/article/S0896627305003624/pdf> |
| Bastos et al. 2012 | B2 | <https://doi.org/10.1016/j.neuron.2012.10.038> |
| Poirazi, Brannon & Mel 2003 | B3 | <http://www.cell.com/article/S0896627303001491/pdf> |
| Schafer et al. 2012 | B4 | <http://www.cell.com/article/S0896627312003340/pdf> |
| Hensch 2005 | B4 | via OpenAlex: `https://api.openalex.org/works/doi:10.1038/nrn1787` → `best_oa_location` |

Save them into `papers/` using the filenames in `fetch_closed_papers.py` and the scripts will stop asking for them. That closes B2, which was the lesson most damaged by a missing source — Bastos is the canonical-microcircuit paper the Step 5 layout depends on.

**Genuinely needs institutional access (7).** Fries 2005 · Roy, Jaiswal & Panda 2019 · Schultz, Dayan & Montague 1997 · Larkum 2013 · London & Häusser 2005 · Huttenlocher & Dabholkar 1997 · Foster & Wilson 2006. a university library will cover these; the lessons that use them name a substitute.

DOIs for all twenty-eight are in `fetch_papers.py`, each resolved against Europe PMC.

## Optional

### NotebookLM — free

<https://notebooklm.google.com>

The packs in `notebooklm/` generate an audio overview for a lesson, which is the first step of the running order. A free Google account is enough. Each pack folder holds the sources to upload and the prompts to paste; the Drive mirror is convenient on a phone.

### Further reading, where the book stops

- **Gerstner, Kistler, Naud & Paninski — *Neuronal Dynamics*.** Free online at <https://neuronaldynamics.epfl.ch/>. Modern, spiking-focused, good where Dayan & Abbott is thin (synaptic delays, adaptive exponential models).
- **Buzsáki — *Rhythms of the Brain*.** Breadth on oscillations for A3.

## What is not here

No copy of the textbook is distributed with this repo, and none will be. Buy it, borrow it, or use a library copy.
