---
name: design-styles
description: Applies a deliberate visual direction to an interface — minimalist editorial, industrial utilitarian, or high-polish commercial — each with its own type scale, palette behavior, surface treatment, and motion. Use this when a product needs a point of view rather than defaults, when choosing between visual directions, when an interface reads as generic, or when restyling something without changing its structure.
---

# Design styles

Three directions, each internally consistent. Pick one deliberately and apply it completely —
half-applied styles read as mistakes, not hybrids.

## Choosing

| Direction | Reads as | Fits when |
|---|---|---|
| **Minimalist editorial** | Calm, content-first, confident | The content is the product: docs, writing tools, reading surfaces, analytics where data should dominate |
| **Industrial utilitarian** | Precise, dense, tool-like | The user is an operator, not a visitor: developer tooling, dashboards, internal systems |
| **High-polish commercial** | Expensive, considered, reassuring | Perceived quality drives the decision: marketing surfaces, onboarding, anything asking for trust or money |

If the brief does not imply one, ask. Defaulting is how products end up looking like their
framework's starter template.

## Minimalist editorial

Near-monochrome with a single accent used sparingly. Hierarchy carried almost entirely by type size
and generous whitespace. Flat surfaces — no shadows, no gradients; separation by space and hairline
rules. Wide margins. Motion is almost absent: fades, no movement.

Fails when: applied to dense data, where the whitespace it needs is not available.

## Industrial utilitarian

Rigid grid, visible structure. Extreme type contrast — small dense body against large stark
headings. Monospace for anything numeric or identifying. Functional color only: state, not
decoration. Square or near-square corners, borders rather than shadows. Motion is instant or absent.

Fails when: applied to consumer surfaces, where it reads as unfinished rather than deliberate.

## High-polish commercial

Layered depth — considered shadows at two or three elevations, never more. Generous but not empty
spacing. A type pairing with real personality in headings against a neutral body. Restrained
gradients on key surfaces only. Motion is present and eased: things enter and settle rather than
appear.

Fails when: applied to high-frequency tools, where the motion and padding become friction.

## Applying any of them

1. Name the direction and why it fits this audience.
2. Set tokens to match before writing markup — the style lives in the token values.
3. Apply completely. A utilitarian grid with soft shadows is not a hybrid.
4. Do not change layout structure to suit the style. If structure must change, that is a separate
   decision, stated as one.
