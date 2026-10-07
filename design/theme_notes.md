# Theme configuration notes

Pairs with `theme.css`. That file assumes the `mkdocs.yml` changes below;
without them some rules (palette-dependent colours, the slate-mode warning
tint) fall back to Material defaults rather than breaking.

## Palette (`theme.palette`)

Set primary to **`blue grey`** and accent to **`indigo`**, on both the light
and dark palette entries already in `site_src/mkdocs.yml`:

```yaml
theme:
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: blue grey
      accent: indigo
      toggle: {icon: material/weather-night, name: Dark}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: blue grey
      accent: indigo
      toggle: {icon: material/weather-sunny, name: Light}
```

Why: the subject is neuroscience and the figures are greyscale plots —
a saturated primary (Material's default `indigo`-as-primary plus red
accent) competes with the plots instead of framing them. Blue-grey reads
as a lab/clinical neutral, sits close to true grey so it doesn't clash
with greyscale figures, and still gives enough chroma to be visibly a
colour (not just another grey) for nav highlights and the H2 banner
border. Indigo as the accent is kept only for `tip` admonitions and link
hover — a small, cool highlight, not a second competing hue.

## `theme.features`

Current: `navigation.tabs`, `navigation.tabs.sticky`, `navigation.top`,
`navigation.prune`, `search.suggest`, `search.highlight`,
`content.code.copy`.

- **Keep** `navigation.tabs` — moving Foundations/Advanced into the header
  is correct and is *why* the sidebar was empty; the fix is in `theme.css`
  (section 3), not in reverting this.
- **Keep** `navigation.tabs.sticky`, `navigation.top`, `search.*`,
  `content.code.copy` — no interaction with this stylesheet.
- **Add** `navigation.sections` — expands the current tab's page list
  without a click, which helps the barren-rail problem further on the
  short sections.
- **Do not add** `navigation.indexes` or `toc.integrate` — both assume a
  right-hand ToC column, which this site deliberately removes in favour
  of the inline `[TOC]` block.

## Font

`theme.css` uses system/OS serif and sans stacks (Georgia-led serif for
body, system sans for headings/nav) — no external font, no network
fetch, no flash of unstyled text, nothing to add to `extra_css` or
`extra.css`'s `@import`. This is the recommended default for a tablet
reading app.

If a true book serif is wanted instead of the Georgia stack, add to
`mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/theme.css
```

(`theme.css` replaces the existing `stylesheets/extra.css` — delete that
file or stop referencing it once this one is wired in, to avoid two
stylesheets fighting over the same selectors.)

To switch to a Google Fonts serif such as **Source Serif 4** or
**Lora**, add before the stylesheet line:

```yaml
extra_css:
  - https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap
  - stylesheets/theme.css
```

then in `theme.css` prepend the font name to `--cnc-serif`'s stack. Not
done by default because it adds a render-blocking network request on
first load, which matters more on a tablet than on desktop.

## Nothing else required

Everything else in `theme.css` reads only Material's existing CSS custom
properties (`--md-default-fg-color`, `--md-primary-fg-color`,
`--md-code-bg-color`, `--md-accent-fg-color`, the `[data-md-color-scheme
="slate"]` selector) and the `admonition`, `pymdownx.details`,
`pymdownx.superfences`, and `tables` extensions already enabled — no
further `markdown_extensions` or `plugins` changes needed.
