---
name: interface-craft
description: Raises the visual and interaction quality of an interface — layout, hierarchy, type, spacing, density, and the details that separate a considered product from a generic one. Use this when a screen works but looks unfinished or default, when a layout feels crowded or arbitrary, when a page has no clear focal point, or when an interface needs to feel trustworthy rather than merely functional.
---

# Interface craft

Most interfaces do not fail on ideas. They fail on execution — spacing that is nearly consistent,
hierarchy that is nearly clear, type that is nearly right.

## Diagnose before restyling

Ask what the screen is *for*. One primary action, at most one secondary. If you cannot name the
primary action, the layout problem is a product problem and no amount of styling fixes it.

## The things that actually read as quality

**Hierarchy.** A viewer should know where to look before they read anything. Achieve it with size,
weight, and space — in that order. Color is the weakest hierarchy tool and the most overused.

**Spacing rhythm.** Related things sit closer than unrelated things, and the gaps come from one
scale. Inconsistent spacing is the defect people feel but cannot name. Get proximity right and a
plain layout reads as designed.

**Type.** One family for the interface, two at most on the page. Set a real scale and use its steps
rather than inventing sizes. Body text wants a comfortable measure — roughly 60–75 characters — and
line height that grows as the measure widens.

**Restraint in surfaces.** Borders, shadows, and fills all separate things. Pick one per boundary.
Stacking all three is why interfaces look busy at normal density.

**Alignment.** Everything lines up with something. An element aligned to nothing reads as a mistake
even when it is intentional.

## Density is a decision

An information-dense tool and a marketing page want opposite treatments. Decide which this is and
commit — the uncomfortable middle, where a data table has landing-page padding, serves neither.

## Finish the states

Loading, empty, error, and overflow are where products feel unfinished. An empty state is a design
opportunity; a spinner with no context is an admission. Long strings, long lists, and small screens
must all be handled, not hoped about.

## Dark mode is a palette, not an inversion

Inverting a light theme produces the characteristic bad dark mode: pure black backgrounds, pure
white text, and shadows that do nothing.

- Use a very dark grey rather than pure black, and a slightly dimmed white rather than pure white.
  Maximum contrast between the two causes halation and is genuinely tiring to read.
- Elevation reverses: in light themes raised surfaces cast shadows, in dark themes they get
  *lighter*. Shadow alone conveys nothing on a dark ground.
- Saturated colors that worked on white will vibrate on dark. Desaturate and lighten accent colors
  for the dark palette rather than reusing them.
- Define both palettes together, at token level, from the start. Retrofitting means auditing every
  surface.

## Accessibility floor

These are not polish items — below them, some people cannot use the interface at all.

- Text contrast meeting the standard ratio against its actual background, including text over
  images and inside colored buttons.
- Never carry meaning by color alone. A red border indicating an error needs text or an icon too.
- Every interactive element reachable by keyboard, in a sensible order, with a visible focus state.
- Touch targets large enough to hit reliably, with spacing between adjacent ones.
- Respect the reduced-motion preference: animation that cannot be disabled causes real symptoms for
  some users.
- Real semantic elements — buttons that are buttons, headings in order. A styled div is invisible to
  assistive technology.

## Never

- Add visual weight to fix a hierarchy problem caused by too many equal elements. Remove instead.
- Center body text.
- Ship a hover state without the matching focus state.
