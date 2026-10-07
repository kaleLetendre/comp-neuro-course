# Downloads

Everything the course uses that can be opened or saved directly. Nothing here needs a login.

## From the textbook authors

Dayan & Abbott publish all of this free at [gatsby.ucl.ac.uk/~dayan/book](https://www.gatsby.ucl.ac.uk/~dayan/book/). The address printed inside the book itself is dead; this is where the material moved.

| | | |
|---|---|---|
| **Exercise sets** | [c1](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c1/c1.pdf) · [c2](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c2/c2.pdf) · [c3](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c3/c3.pdf) · [c4](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c4/c4.pdf) · [c5](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c5/c5.pdf) · [c6](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c6/c6.pdf) · [c7](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c7/c7.pdf) · [c8](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c8/c8.pdf) · [c9](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c9/c9.pdf) · [c10](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c10/c10.pdf) | One per chapter, PDF |
| **All code and data** | [exall.tar.gz](https://www.gatsby.ucl.ac.uk/~dayan/book/exall.tar.gz) | 11 MB, every chapter |
| **Fly H1 recordings** | [c1p8.mat](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c1/data/c1p8.mat) | Twenty minutes of real spikes, used by F1's exercises 8–10 |
| **Other data** | [c2p3.mat](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c2/data/c2p3.mat) · [c10p1.mat](https://www.gatsby.ucl.ac.uk/~dayan/book/exercises/c10/data/c10p1.mat) | For F2 and F11 |
| **Figures** | [complete set](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/complete.tar.gz) · per chapter: [1](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch1fig.ppt) [2](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch2fig.ppt) [3](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch3fig.ppt) [4](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch4fig.ppt) [5](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch5fig.ppt) [6](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch6fig.ppt) [7](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch7fig.ppt) [8](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch8fig.ppt) [9](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch9fig.ppt) [10](https://www.gatsby.ucl.ac.uk/~dayan/book/figures/ch10fig.ppt) | PowerPoint, also as PNG archives |
| **Errata** | [errata.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/errata.pdf) | Two printings exist — check page iv of your copy |
| **Chapter 7, free** | [ch7.pdf](https://www.gatsby.ucl.ac.uk/~dayan/book/ch7.pdf) | *Network Models* in full, the authors' own sample |
| **Reference list** | [teaching support page](https://www.gatsby.ucl.ac.uk/~dayan/book/teaching.html) | The book's full bibliography |

## The textbook

Not free, and not distributed here. [MIT Press](https://mitpress.mit.edu/9780262041997/theoretical-neuroscience/) · paperback ISBN 978-0-262-54185-5. Check a university library first.

## Papers for the advanced tracks

Each lesson page lists its own under **Files for this lesson**, with direct links where a paper is openly readable and a DOI otherwise. Of the twenty-eight, twenty-one cost nothing — nine of those are open access but blocked to scripts, so they need one click in a browser.

The repository's `fetch_papers.py` downloads what can be fetched automatically and doubles as the bibliography, with every DOI resolved.

## This course

| | |
|---|---|
| Repository | [github.com/kaleLetendre/comp-neuro-course](https://github.com/kaleLetendre/comp-neuro-course) |
| Offline copy | Clone it, then `python3 build_site.py && cd site_src && ../.venv/bin/mkdocs build` — `site/` is a self-contained folder you can copy to a tablet and open without a connection |
| Marking material | `python3 build_site.py --teacher` builds a version including the grader keys and hint ladders |
