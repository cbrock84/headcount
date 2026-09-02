---
name: visual-reference-generation
description: Produces design reference imagery before implementation — screen concepts, layout directions, and flows for web or mobile that make a verbal brief concrete enough to argue with. Use this when a brief needs visualizing before anyone builds, when comparing layout directions, when handing a developer a target, or when stakeholders are describing different things with the same words.
---

# Visual reference generation

Arguing about an image costs an hour. Arguing about a build costs a sprint. Generate the picture
first.

## Before generating

Settle these, or the output is decoration:

- **Surface and platform** — web page, native mobile screen, dashboard. These are not the same
  problem at different aspect ratios: touch targets, native chrome, and scroll behavior change what
  a good layout is.
- **What it optimizes for** — one conversion, one task completion, one first impression. Stated, so
  the image can be judged against something.
- **Content reality** — real headline lengths, real data volumes, real edge cases. A concept built
  on three-word labels collapses on contact with actual copy.

## Generating

- **One concept per image.** Tiling several ideas onto one canvas makes them impossible to compare
  or iterate separately.
- **Generate genuinely different directions**, not variations of one. Three near-identical options
  is one option presented three times.
- Include the states that will exist: a populated view and an empty one, at minimum.

## Web versus mobile

**Web** — the fold is a real constraint but not a hard one; horizontal space allows genuine layout
choices; hover exists. Design for a range of widths, and decide what the narrow case does.

**Mobile** — thumb reach dictates where primary actions sit; native navigation patterns are
expectations, not suggestions; there is no hover, so affordance must be visible. Design the scroll,
not the screenshot.

## After generating

Say explicitly what in the reference is **direction** and what is **placeholder**. A developer
handed a concept will otherwise implement the lorem ipsum faithfully.
