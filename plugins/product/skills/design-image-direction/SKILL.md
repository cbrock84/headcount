---
name: design-image-direction
description: Generates premium design reference images for a product surface before any code is written — screen concepts, flows, and conversion-aware layouts for web or mobile. Use this when a visual target is needed to design against, when a brief is verbal and needs to be made concrete, when comparing layout directions, or when handing a designer or developer something to build toward. Covers both web pages and native mobile screens.
---

# Design image direction

Produce the picture before the markup. A generated reference makes a vague brief arguable, and
arguing about an image is cheaper than arguing about a build.

## Pick the target first

- **Web** — landing pages, marketing sites, dashboards, conversion-aware layouts. See
  `references/imagegen-frontend-web.md`.
- **Mobile** — iOS, Android, and cross-platform native screens and flows. See
  `references/imagegen-frontend-mobile.md`.

The two differ in more than aspect ratio: touch targets, native chrome, and scroll behavior change
what a good layout is. Read the matching reference in full before generating.

## Rules

- **One image per concept.** Do not tile several ideas into one canvas — they cannot be compared or
  iterated separately.
- **Generate before you build**, not after. A reference produced to justify existing markup is
  decoration.
- **State what the image is optimizing for** — a conversion, a task completion, a first impression —
  so it can be judged against something.
