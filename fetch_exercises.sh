#!/bin/sh
# Download Dayan & Abbott's official exercise sets, code and data.
# They are free from the authors' site; we do not redistribute them, so this
# script refetches them into exercises/ (gitignored) on a fresh clone.
set -e
BASE="https://www.gatsby.ucl.ac.uk/~dayan/book"
DIR="$(dirname "$0")/exercises"
mkdir -p "$DIR"
cd "$DIR"
for c in 1 2 3 4 5 6 7 8 9 10; do
    curl -sS --max-time 60 -o "c$c.pdf" "$BASE/exercises/c$c/c$c.pdf"
done
curl -sS --max-time 120 -o all.tar.gz "$BASE/exall.tar.gz"
tar xzf all.tar.gz
rm all.tar.gz
echo "Exercise sets and data are in $DIR"
