# Editorial

A feature-magazine reading: a confident Fraunces display headline over a
sans-serif byline strip on every lesson, numbered section banners, and
card-driven landing pages with a single oxblood-to-coral accent that
survives the light/dark toggle. Figures run full width with weight;
native blockquotes get full pull-quote treatment.

## Versus `theme.css`

- **Flips the pairing**: `theme.css` runs serif body / sans headings;
  this runs sans body / display-serif (Fraunces) headings, for the
  "strong contrast between display and body faces" the brief asks for.
- **New accent mechanism**: redefines `--md-primary-fg-color` /
  `--md-primary-bg-color` to a constant dark "ink" masthead (independent
  of the light/dark toggle) and `--md-accent-fg-color` to a single warm
  red/coral accent, scheme-scoped. `theme.css` left Material's own
  palette (blue grey / indigo) alone and only recoloured admonitions.
- **Fixes a figure-width bug `theme.css` has**: Material wraps every
  image in its own `<p>`, so `theme.css`'s global `p { max-width: 42rem }`
  silently caps every figure to prose width. This file excludes
  image-only paragraphs (`p:not(:has(img))`) so figures and their
  captions run full width, per the brief.
- **New**: numbered H2 section banners (CSS counter, no markup change),
  a restyled "At a glance" admonition doing standfirst/byline duty
  (`h1 + .admonition.abstract`), an `h1 + p` lede rule that only fires on
  the home/track-index pages (their H1 is followed directly by a `<p>`;
  lesson pages' H1 is followed by the admonition instead), and a
  pull-quote treatment for native `> ` blockquotes — not currently used
  anywhere in `site_src/docs` (checked), so this is a capability for
  future lessons, not a rule exercised by today's content.
- **Left alone**: the single-row header/tabs merge `theme.css` did with
  `position`/`width` on `.md-tabs` — that is explicitly `nav.css`'s job
  now; this file only recolours header/tabs via the custom properties
  above plus `font`/`letter-spacing`, never their geometry.

## `mkdocs.yml` line needed

```yaml
extra_css:
  - https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,900;1,9..144,500&display=swap
  - stylesheets/editorial.css
```

Fallback is Georgia/Iowan/Palatino/serif at the same sizes used for
Fraunces, so a blocked or slow font request degrades to a quieter
headline, never a layout break.
