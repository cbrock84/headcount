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

## Never

- Add visual weight to fix a hierarchy problem caused by too many equal elements. Remove instead.
- Center body text.
- Ship a hover state without the matching focus state.
