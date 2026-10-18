---
name: financial-modeling
description: Builds and stress-tests financial models for forecasting, scenario planning, and decision support — revenue build, cost structure, driver logic, and the sensitivities that show where a plan breaks. Use this to model a decision's financial consequence, build a forecast or long-range plan, evaluate an investment or hire, or pressure-test someone else's model before relying on it.
---

# Financial modeling

A model is an argument about how the business works, expressed in arithmetic. Its value is the
argument, not the output precision.

## Structure

Three separated layers, always:

1. **Inputs** — every assumption, in one place, each with a source and a date. An assumption buried
   inside a formula is invisible and therefore never challenged.
2. **Calculations** — no hard-coded numbers. Ever. A constant inside a formula is an untraceable
   assumption.
3. **Outputs** — the statements and the summary a decision-maker actually reads.

One row, one calculation, carried consistently across periods. Models become unauditable through
inconsistent rows more than through complexity.

## Build revenue from drivers

Never grow a top-line by a percentage. Build it: volume × price, or accounts × retention ×
expansion. Driver-based models can be argued with, and being argued with is the point — a growth
rate cannot be wrong, only optimistic.

Cost structure separated into fixed, variable, and step-fixed. The step-fixed items are where plans
break, because they move in jumps nobody modeled.

## Sensitivities are the deliverable

A single-scenario model tells you nothing about risk. For every model, produce:

- **Which two or three assumptions actually move the answer.** Usually far fewer than expected.
- **Breakeven on each** — how wrong can this be before the decision reverses?
- **Downside case** — not a haircut on the base case, but a coherent story where things go badly.

If a plan only works in the base case, that is the finding.

## Presenting

Lead with the answer, then the two assumptions it rests on most heavily, then what would change it.
Never present a model without stating what it is most sensitive to — the recipient will assume
robustness you did not claim.

## Never

- Report a number to more precision than the assumptions support. Five significant figures from a
  guessed growth rate is false confidence.
- Build a model whose logic you cannot explain in three sentences.
- Change an assumption to reach a desired output without labeling it as a target case.
