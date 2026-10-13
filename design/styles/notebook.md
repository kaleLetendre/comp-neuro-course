# notebook.css — notes

A working scientist's notebook under a desk lamp: a warm espresso-dark
ground (not slate, not black) with parchment-toned text in slate mode, a
warm cream page in default mode, and two inks — blue-black for the
document's own structure, red for the reader's landmarks — instead of one
accent doing every job.

## Versus `theme.css`

Same typographic register (serif prose / sans headings, full-width
content, hidden right ToC, same ~500-600px breakpoint), but both colour
schemes are rebuilt via direct `--md-*` custom-property overrides instead
of a `theme.palette` primary/accent preset — no `mkdocs.yml` change
needed, works with whatever preset is already configured. Adds a third
type voice (monospace, for metadata/marginalia: captions, table headers,
the "At a glance" box, nav labels) and the red/blue-black ink split. Does
**not** touch header/tabs/search/nav/sidebar geometry — that's
`design/nav.css`'s job; colour only, where it touches them at all.

## The white-figure-on-dark-ground problem

The book's figures are black line art on white. Every `<img>` gets a
fixed, scheme-independent "paper" background (`--nb-paper`, warm
off-white, not `#fff`), a border and a lifted-plate shadow, so in slate
mode it reads as a print pasted onto the page rather than a glaring
rectangle, and in default mode it barely differs from the page (correct —
no clash to solve there). Where `:has()` is supported (Chromium, the
tablet's own browser), the wrapping paragraph also gets a shallow
graph-paper "specimen tray" behind the plate; without it the page still
works, since the mat and shadow alone already solve the contrast problem.

Graph paper otherwise appears in exactly two more places — the inline
contents box and card-grid tiles on the home/track-index pages — never
behind running prose or MathJax. Below 44.9375em its cell shrinks further
(20px to 14px) so it stays out of the cramped viewport's way.

## Fonts

System stacks only, no Google Font: Georgia-led serif for prose, system
sans for headings/nav, system monospace (`ui-monospace, "SF Mono", ...`)
for metadata/marginalia. No `extra_css` change needed beyond the
variant's own stylesheet line.

## Left alone

Code syntax-highlight colours (`--md-code-hl-*`), MathJax rendering
itself, table-sort icons, and anything geometric on
`.md-header*`/`.md-tabs*`/`.md-search*`/`.md-nav*`/`.md-sidebar*` — either
fine as Material ships it, or owned by `design/nav.css`.
