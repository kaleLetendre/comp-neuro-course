# nav.css notes

Pairs with `nav.css`, replacing the "Single-row header" block at the end
of `theme.css` (not deleted here — see owner note at the bottom).

## Bug 1 — hardcoded `margin-right: 11rem`

Was: a guess at the tabs strip's rendered width, reserved as a margin on
`.md-header__option`/`.md-search`. Wrong the moment a label changes.

Fix: `.md-header { display: flex }`, `.md-header__inner { flex: 1 1 auto;
min-width: 0 }`, `.md-tabs { flex: 0 0 auto; width: auto }`. Tabs claim
exactly their own width; title/search get the rest — no margin needed.

Established via the compiled CSS: `.md-header__inner` is already a flex
container for its own children (nesting is safe); `.md-tabs{width:100%}`
is why `width: auto` is required (else `flex-basis:auto` resolves to
100%); `.md-tabs__item`/`.md-header__title` are both already `height:
2.4rem`, so rows line up with no height rules added. Dropped as no
longer needed: `position: absolute` (default static is correct for a
flex child), the z-index 10/11 escalation (only needed out of flow), and
the `.md-tabs__list`/`__item` height copy (redundant with that 2.4rem).

## Bug 2 — `navigation.tabs.sticky`

Not edited. Not just meaningless leftover: Material's
`partials/header.html` statically adds `md-header--lifted` to `<header>`
only when this flag is set, and that class drives the (now wrong) 4.8rem
sidebar / 6rem anchor offsets fixed below. `nav.css`'s fixes are scoped
to `.md-header--lifted` so they're correct whether the flag stays or is
later removed. Set at `build_site.py:404` (mkdocs.yml is generated).

## Bug 3 — redundant `position: sticky; top: 0`

Dropped — already Material's own unconditional rule on `.md-header`
(confirmed in the compiled CSS); the copy added only a needless z-index.

## Bug 4 — scroll states / search / breakpoint

- `--shadow`/`--lifted`: grepped the bundled JS — only `--shadow` is ever
  `classList.toggle`'d; `--lifted` isn't touched by JS at all, so with
  `navigation.tabs.sticky` on it's always present. Sidebar/anchor fixes
  above are correct as unconditional, not scroll-dependent.
- Search expand: at >=76.25em Material expands `.md-search__inner` to a
  fixed 34.4rem inline, which now shares `.md-header__inner` with
  `.md-tabs` instead of having the full header to itself. **Unverified
  without a browser**: whether it still fits just above 76.25em with long
  tab labels — inherent one-row trade-off, not a number this file can fix.
- Breakpoint: Material's tabs-hide rule is `max-width: 76.234375em`, not
  `76.25em` — a ~0.015em sliver, no visible effect; used `76.25em` to
  match Material's own sidebar/anchor selectors.

## mkdocs.yml / owner follow-up

No manual mkdocs.yml change needed — `build_site.py` already copies
`design/nav.css` into `extra_css` ahead of `theme.css` when the file
exists. Do delete the "Single-row header" block from `design/theme.css`:
its `.md-header`/`.md-tabs`/`margin-right: 11rem` rules load after
`nav.css` and would win the cascade, undoing the fixes above.
