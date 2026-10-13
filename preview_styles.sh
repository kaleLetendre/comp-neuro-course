#!/bin/sh
# Build every candidate stylesheet in design/styles/ into its own preview site,
# write a chooser page linking them, and serve the lot from one port.
#
# One port and relative links (MkDocs emits those by default) means the whole
# set works from a phone or tablet on the same network as well as from this
# machine — which is the point, since the course is read on a tablet.
#
#   ./preview_styles.sh          # build + serve on 8800
#   ./preview_styles.sh 9000     # build + serve on 9000
#
# Each variant is rebuilt from scratch every run; site_preview/ is gitignored.

# set -e: a half-built preview set is worse than no preview set, because you
# would compare one variant against another variant's stale output.
set -e
cd "$(dirname "$0")"
PORT="${1:-8800}"

rm -rf site_preview
mkdir -p site_preview

NAMES=""
for css in design/styles/*.css; do
    name=$(basename "$css" .css)
    echo "=== $name ==="
    python3 build_site.py "--variant=$name"
    .venv/bin/mkdocs build -q -f "site_src_var_$name/mkdocs.yml"
    NAMES="$NAMES $name"
done

# The baseline, so the candidates are judged against what is live today.
echo "=== current (design/theme.css) ==="
python3 build_site.py
.venv/bin/mkdocs build -q -f site_src/mkdocs.yml
cp -r site site_preview/current
NAMES="current $NAMES"

{
    echo '<!doctype html><meta charset=utf-8>'
    echo '<meta name=viewport content="width=device-width,initial-scale=1">'
    echo '<title>Style variants</title>'
    echo '<style>body{font:16px/1.5 system-ui,sans-serif;max-width:34rem;'
    echo 'margin:3rem auto;padding:0 1rem}a{display:block;padding:.7rem 0;'
    echo 'font-size:1.1rem}</style>'
    echo '<h1>Style variants</h1>'
    echo '<p>Same 28 lesson pages, four candidate stylesheets plus the current one.</p>'
    for name in $NAMES; do
        echo "<a href=\"$name/\">$name</a>"
    done
} > site_preview/index.html

echo
echo "serving site_preview/ on port $PORT"
python3 -m http.server "$PORT" --directory site_preview
