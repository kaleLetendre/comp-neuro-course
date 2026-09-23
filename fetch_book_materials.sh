#!/bin/sh
# Dayan & Abbott publish everything but the book itself, free, from
# gatsby.ucl.ac.uk/~dayan/book. The MIT Press address printed in the book
# (mitpress.mit.edu/dayan-abbott) is dead; this is where the material moved.
#
# Fetches: exercise sets + code + data, per-chapter figures, the errata, and
# the free sample chapter 7. All gitignored - they are the authors' files and
# we do not redistribute them.
set -e
BASE="https://www.gatsby.ucl.ac.uk/~dayan/book"
DIR="$(dirname "$0")/exercises"
mkdir -p "$DIR/figures"
cd "$DIR"

echo "Exercise sets..."
for c in 1 2 3 4 5 6 7 8 9 10; do
    curl -sS --max-time 60 -o "c$c.pdf" "$BASE/exercises/c$c/c$c.pdf"
done

echo "Exercise code and data..."
curl -sS --max-time 180 -o all.tar.gz "$BASE/exall.tar.gz"
tar xzf all.tar.gz
rm all.tar.gz

echo "Figures, per chapter..."
for c in 1 2 3 4 5 6 7 8 9 10; do
    curl -sS --max-time 90 -o "figures/ch${c}fig.tar.gz" "$BASE/figures/ch${c}fig.tar.gz"
    curl -sS --max-time 90 -o "figures/ch${c}fig.ppt" "$BASE/figures/ch${c}fig.ppt"
done
curl -sS --max-time 90 -o "figures/mathfig.tar.gz" "$BASE/figures/mathfig.tar.gz"

echo "Errata and the free sample chapter..."
curl -sS --max-time 60 -o errata.pdf "$BASE/errata.pdf"
curl -sS --max-time 60 -o ch7_free_sample.pdf "$BASE/ch7.pdf"

echo
echo "Done. Everything is in $DIR"
echo "Check errata.pdf before teaching any chapter - it lists corrections by printing."
