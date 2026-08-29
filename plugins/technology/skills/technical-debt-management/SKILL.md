---
name: technical-debt-management
description: Makes technical debt visible and decidable — distinguishing real debt from mess, quantifying its cost, and arguing for remediation in business terms. Use this to assess and prioritise debt, decide whether to fix or live with something, justify remediation work to non-engineers, or plan a migration off a system nobody wants to touch.
---

# Technical debt management

Debt is a deliberate trade: taking on future cost to move faster now. Most of what gets called debt
is not that — it is mess, which was never a decision, or drift, where the world moved and the code
did not. The distinction matters because the arguments and remedies differ.

## Classify before prioritising

- **Deliberate debt** — a known shortcut with a reason. Has a principal and interest. Legitimate.
- **Mess** — nobody chose it; it accumulated. No trade was made, so there is nothing to defend.
- **Drift** — the code was right for a context that has changed. Neither shortcut nor carelessness.
- **Not debt at all** — code someone dislikes, or would have written differently. Taste is not debt,
  and rewriting on taste is how remediation budgets get spent with nothing to show.

## Cost is a rate, not a total

Debt matters proportional to how often you pay it. Ugly code in a module nobody has touched in three
years costs nothing; a moderate awkwardness in the file every feature crosses costs continuously.

Measure by contact: change frequency, how long changes there take relative to elsewhere, how often
changes there cause incidents, and how many people avoid the area. Overlay change frequency on
complexity and the priorities become obvious and defensible — the expensive parts are where both are
high, which is rarely where intuition points.

## Argue in the language of the decision-maker

"The code is bad" loses to any feature request. What wins is the rate: this area consumes a
disproportionate share of delivery time, causes a disproportionate share of incidents, and the gap
widens.

Frame remediation as capacity recovery with a payback period — the same terms as
`finance:capital-allocation`, which is where any large migration will eventually be judged.

## Remediate incrementally

Large rewrites fail at a well-documented rate: they take longer than estimated, deliver no value
until the end, and are cancelled halfway leaving two systems. Prefer strangling the old system
gradually behind a stable interface, so value lands continuously and the work can stop at any point
without leaving a mess.

Improve opportunistically where you are already working — the code you are touching anyway is the
cheapest code to improve, and it is by definition the code that is being touched.

## Never

- Present debt as a quality argument to someone accountable for delivery dates.
- Prioritise by how bad code looks rather than how often it is paid for.
- Start a rewrite with no value delivered until completion.
- Classify taste as debt.
