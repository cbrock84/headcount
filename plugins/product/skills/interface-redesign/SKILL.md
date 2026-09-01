---
name: interface-redesign
description: Upgrades an existing interface to a higher standard without rebuilding it — auditing what is there, identifying what reads as generic or unfinished, and sequencing changes by impact. Use this when a product works but looks dated or default, when a redesign is being considered, when deciding whether to restyle or rebuild, or when a screen needs to look substantially better with limited effort.
---

# Interface redesign

Most interfaces do not need rebuilding. They need a dozen specific things fixed, in the right order.

## Audit first

Go through the real product, on a real device, doing a real task. Record what you find in these
categories — the order is the priority order:

1. **Structural** — unclear primary action, competing focal points, navigation that does not match
   the mental model. These are the only ones worth a rebuild.
2. **Systemic** — inconsistent spacing, more type sizes than a scale would allow, palette drift,
   components that exist in variants. High impact, mechanical to fix.
3. **Craft** — weak hierarchy, poor contrast, unfinished states, cramped density.
4. **Cosmetic** — dated shadows, default border radii, stock illustration.

## The generic-AI-product tells

These are the specific things that make a product read as unconsidered. They are worth naming
because they are all cheap to fix:

- Default framework styling left in place — the untouched button, the starter-template card.
- One accent color used for every emphasis, so nothing is emphasized.
- Uniform spacing everywhere, so nothing groups.
- Centered everything, including body copy.
- Emoji standing in for iconography.
- Gradients on surfaces that carry no meaning.
- Empty and error states that were never designed.

## Sequencing

Fix in this order, because each makes the next easier to see:

1. Tokens — spacing scale, type scale, palette. This alone resolves most systemic findings.
2. Hierarchy on the two or three highest-traffic screens.
3. States: empty, loading, error, overflow.
4. Component consolidation.
5. Cosmetic pass.

## Restyle or rebuild

Rebuild only when the structure is wrong — when the information architecture does not match how
people work. Everything else is a restyle, and a restyle that ships beats a rebuild that stalls.

## Never

- Restyle a screen whose problem is structural. New paint on a broken flow buys nothing.
- Change navigation and visual language in the same release. When something breaks you will not know which one did it.
- Remove a path because it looks unused without checking who uses it and what they do next.
- Ship a redesign with no way back. Keep the old path reachable until the new one is proven.

## Return contract

Findings by category with severity, the sequenced plan, what you would do first if only one day were
available, and what you deliberately are not touching.
