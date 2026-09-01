---
name: design-system
description: Builds and maintains the design system a product is assembled from — tokens for color, type, spacing and elevation, component contracts, and the rules that keep them coherent as the product grows. Use this when starting a new interface, when screens have drifted apart visually, when the same component exists three times in slightly different forms, or when a token or component needs adding without breaking what exists.
---

# Design system

A design system is a set of constraints that makes consistency the cheap path. If the system is
harder to follow than to ignore, it will be ignored.

## Tokens first

Define the primitives before any component. Every visual decision references a token; nothing
hard-codes a value.

- **Color** — semantic names, not literal ones. `surface`, `surface-raised`, `text-primary`,
  `text-muted`, `border`, `accent`, `danger`. A token named `blue-500` cannot be re-themed.
- **Type** — a scale with a stated ratio, and a line-height per step. Four to six steps. More than
  that and nobody can tell them apart.
- **Spacing** — one scale, geometric, used for every gap and inset. Arbitrary spacing is the single
  most common source of "it looks off but I can't say why."
- **Radius, elevation, motion** — small closed sets. Two or three each.

Every token needs a light and dark value defined together. Adding dark mode later means auditing
every surface.

## Component contracts

A component in the system carries: the states it supports (default, hover, focus, active, disabled,
loading, error, empty), the props that vary it, and what it will *not* do. The last one matters
most — a component that accepts arbitrary overrides is a styling function, not a component.

Every interactive component needs a visible focus state and a target big enough to hit. This is not
a polish item; it is whether people can use it.

## Growth rules

- A new component enters the system only after the same need appears three times. Before that it is
  local.
- Changing a token is a system-wide change — treat it like an API change, because it is.
- Never remove a token or component because it looks unused. You cannot see every consumer from
  inside the system. Deprecate, announce, then remove.

## Tooling

Design source: Figma, and similar. Component documentation and review: Storybook.

Token pipelines: Style Dictionary, Tokens Studio, Figma variables exported to code, and
similar. Visual regression: Chromatic, Percy, Playwright snapshots, and similar.

The system is the code, not the design file. When the two disagree, the code is what ships.

## Never

- Add a component for a single screen. A one-use component is a snippet, not a system.
- Hard-code a value a token already covers. The exception becomes the next inconsistency.
- Redefine what an existing token means instead of adding one. Changing a semantic silently redecorates everything downstream.
- Ship a component without its states documented — empty, loading, error, disabled.

## Return contract

Report tokens added or changed, components affected, anything now inconsistent with the system, and
what needs migrating.
