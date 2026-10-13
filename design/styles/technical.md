# Technical

An engineering-reference look: sans-serif throughout, rule-lines instead
of boxes, monospace carrying structure (section numbers, table bodies,
nav identifiers, captions) rather than decoration.

## Versus `theme.css`

- Drops the serif body font entirely — sans everywhere, no "book" voice.
- Headings get auto-numbered via CSS counters (`01`, `1.1`, `1.2`, ...)
  instead of a coloured banner block — section location is always
  explicit, with no markup changes needed on any of the 28 lesson pages.
- Admonitions, `details`, code blocks and the inline-contents box lose
  their background tint/box entirely in favour of hairline borders —
  the brief's "rule-lines over tinted panels" taken literally.
- Tables: monospace body cells, rule-lines between rows, no zebra
  striping (theme.css zebra-strikes; this style doesn't).
- Figure captions are left-aligned monospace with a trailing rule, not
  centered italic serif.
- Grid cards (home/track-index) go sharp-cornered with a border-colour
  hover instead of a shadow.
- Sidebar nav is set in monospace throughout, read as a flat index.

## `mkdocs.yml`

No font changes needed — this file uses only system stacks (see
`--cnc-sans` / `--cnc-mono` at the top of `technical.css`), so no
`extra_css` Google Fonts line is required. Whichever stylesheet is chosen
still needs to be the one referenced under `extra_css`, after `nav.css`.

## Left alone

- Didn't touch header/tabs/search geometry — colour/font only, per the
  brief; layout for those stays in `nav.css`.
- Didn't add numbering to H1 — the lesson ID is already in the title text
  and the nav ("F1 · ..."), so a third number would be redundant.
- Left MathJax's own rendering untouched beyond an `overflow-x: auto`
  safety on `.arithmatex` for wide equations on the narrow breakpoint.
- Didn't rewrite the figure-caption selector to require `<figure>`
  markup — the source never uses it; styled the actual pattern instead
  (`<p><em>caption</em></p>` as the sole content of a paragraph).
