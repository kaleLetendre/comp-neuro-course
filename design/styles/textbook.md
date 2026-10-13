> Chosen. Promoted to `design/theme.css`; the stylesheet no longer
> lives here, only this record of why it looks the way it does.

# Textbook

A warm-paper, serif-bodied reading page with one restrained accent that marks
structure and nothing else — links, section rules, active nav, the inline
contents box — so the page reads like a well-set book rather than a web app.

## What changed versus theme.css

- **Colour.** theme.css never touched Material's palette, so it was still
  stark white / cool slate despite the brief. Fixed via Material's own
  properties: warm ink-on-cream for light; for dark, one `--md-hue: 32deg`
  override (Material derives slate's whole palette from that hue, so this
  one line warms everything it generates). A single rubric red
  (`--md-primary-fg-color`/`--md-accent-fg-color`) does every wayfinding
  job — links, rules, active nav, active tab. Warnings get their own
  mustard so two reds don't collide in meaning.
- **`<details>` was unstyled.** theme.css only styled `.admonition` (`!!!`);
  every folded section (`??? abstract`, `??? note "Scope"`, every rubric)
  compiles to `<details>` and still rendered Material's stock blue,
  drop-shadowed box. Now shares the admonition treatment.
- **`abstract` and `info` leaked Material's native colours.** Each of
  Material's twelve admonition types gets its own border colour at a
  specificity a generic reset can't beat; theme.css only named
  `note`/`quote`/`tip`/`warning`, so "At a glance" (`abstract`) and every
  rubric (`info`) were still cyan/green. All twelve now named explicitly.
- **Figures never matched.** Markup is a plain `<p><img></p>` then a plain
  `<p><em>caption</em></p>` — not `<figure>/<figcaption>`, which is what
  theme.css's dead rule targeted. Retargeted with `:has()`; caption set
  upright (book captions aren't italic).
- **H2 was a filled card.** Reads as a UI panel. Replaced with a hairline
  rule plus a short rubric mark under the text — how a book marks a part.
- **Tables** lost their box border and zebra striping for rule-only book
  tables (heavy top/bottom rule, light rule under the header).
- **Added:** content-tab label typography (previously unstyled), MathJax
  comfort margins + horizontal scroll for display equations, a blockquote
  rule, an H1 title-rule.

## Left alone

Georgia/system-sans pairing and its theme_notes.md reasoning (no Google
Font, no `mkdocs.yml` change). Header/tabs/search geometry — `nav.css`'s
territory; reached only through shared colour variables. The admonition
box shape itself (left rule, radius, padding) — extended, not replaced.
