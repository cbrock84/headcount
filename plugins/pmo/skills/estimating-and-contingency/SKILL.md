---
name: estimating-and-contingency
description: Produces a cost or effort estimate someone can defend — decomposing the work, choosing between analogous, parametric and bottom-up methods, documenting the basis and its assumptions, expressing confidence as a range, and sizing contingency and management reserve separately. Use this to build an estimate, challenge one you have been handed, work out why estimates keep coming in low, or decide how much reserve a portfolio actually needs.
---

# Estimating and contingency

An estimate is a claim about an uncertain future. Most organizations treat it as a commitment made
by whoever said the number, which is why estimates are padded, disbelieved, and padded again.

## Decompose before you estimate

Estimate the work, not the project. Break it down until each piece is small enough that someone who
would do it can picture doing it — usually a week or two of effort. Below that you are estimating
noise; above it you are guessing.

Two decomposition failures are worth naming. **Missing scope** is the larger one: integration,
data migration, environments, testing, documentation, training, and the coordination overhead of
everyone involved routinely go unestimated because nobody owns them. **Double-counted contingency**
is the other: padding inside every task, then adding a reserve on top of the padded total.

## Pick the method that matches what you know

- **Analogous** — scale from a comparable past effort. Fast, needs real history, and the comparison
  has to survive being stated out loud: what is genuinely similar and what is not.
- **Parametric** — a rate applied to a count. Cost per endpoint, per interface, per square foot,
  per test case. Credible only when the rate comes from your own data and the count is knowable.
- **Bottom-up** — estimate each decomposed piece and roll up. Most accurate, most expensive, and
  worth it once the work is understood well enough for the pieces to be real.

Use two methods and compare them where the number matters. When they disagree by more than a
quarter, one of them is built on an assumption nobody has stated.

## Write the basis down, because that is the durable part

The number is the least useful output. The basis of estimate is what lets someone re-estimate
later instead of starting over: what is included, what is explicitly excluded, the rates and
quantities used, the assumptions the number depends on, and who provided each input.

An estimate without a basis cannot be defended, cannot be updated, and cannot be learned from. When
the project comes in at double, the basis is what tells you whether the estimate was wrong or the
work changed — and those call for opposite responses.

## Express it as a range, and say what the range means

A single number is a forecast disguised as a fact. Give a range, and state the confidence: "we
would hit this eight times in ten" is a different commitment from "this is the best case."

Ranges narrow as work is understood, not as deadlines approach. Re-estimate at genuine information
points — after discovery, after the first integration, after the first delivered increment — and
publish the revision rather than quietly holding the old number.

## Separate contingency from management reserve

- **Contingency** covers the known unknowns inside the estimate: things that will vary, at a size
  you can bound. It belongs to the project and is drawn against as risks materialize.
- **Management reserve** covers scope nobody has thought of yet. It belongs to whoever governs the
  portfolio, not to the project team, and it is released deliberately.

Collapsing the two produces the familiar pattern where contingency is spent early on ordinary
variance and nothing remains for the thing that actually goes wrong.

## Why estimates keep coming in low

Optimism is real but it is rarely the main driver. The larger ones are structural: the estimate was
made before scope was understood and never revisited; the estimator knew the number that would be
accepted; only the happy path was estimated; or the organization punishes revised estimates more
than it punishes overruns, so nobody revises.

Fix the incentive before fixing the arithmetic. An organization that treats a re-estimate as a
failure will get accurate estimates from no one.

## Never

- Present a point estimate for work nobody has decomposed.
- Add contingency to an estimate that already has padding inside every task.
- Let an estimate stand as a commitment without recording what it assumed.
- Cut an estimate to fit a budget and leave the scope unchanged. That is not an estimate, it is a
  decision to overrun, taken early and left unsaid.
