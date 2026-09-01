---
name: quantitative-analysis
description: Answers a business question with data without fooling yourself — framing the question so an answer would change something, choosing the right comparison, checking the data before trusting it, recognizing the traps that produce confident wrong answers (aggregation reversals, survivorship, regression to the mean, multiple comparisons), and reporting uncertainty honestly. Use this to run an analysis, review one before acting on it, or work out why two people looking at the same data reached opposite conclusions.
---

# Quantitative analysis

A wrong answer here is rarely an arithmetic error. It is a correct calculation on the wrong
comparison, or on data that does not mean what the field name suggests.

## Frame the question so that an answer changes something

Start from the decision. "How is retention doing" has no answer; "is the cohort we changed
onboarding for retaining better than the one before it, enough to justify rolling it out" does.

Write down what you expect to find and what you would do in each case before you look. If every
possible result leads to the same action, the analysis is not worth running — and knowing that in
advance is worth more than the analysis would have been.

## Choose the comparison before the metric

Almost every meaningful number is a comparison, and the choice of what to compare against does more
work than the calculation.

- **Against what it was** — needs a period long enough to see through seasonality and noise.
- **Against what it would have been** — the strongest comparison and the hardest to construct. A
  holdout group, a matched segment, a pre-trend extended forward.
- **Against a peer or a benchmark** — only useful if the definitions genuinely match, which they
  usually do not.

**Name the counterfactual explicitly.** "Revenue rose after the campaign" is a comparison against
nothing, and it is the single most common way credit is claimed for a trend that was already
happening.

## Interrogate the data before you trust it

Look at the raw rows. Check when collection started and whether the definition changed partway.
Check null rates, duplicates, and test or internal accounts still in the set. Check whether recent
periods are still filling in — partial data at the tail is what produces the "sudden decline" that
resolves itself a week later.

**A field's name is not its definition.** Find out what actually writes it and under what
conditions, especially for anything named status, type, active, or created.

## Know the traps that produce confident wrong answers

- **Aggregation reversals.** A rate can improve in every segment and worsen overall if the mix
  shifted. Always check whether the segments agree with the total, and where they disagree, the
  segments are the truth.
- **Survivorship.** Analyzing only accounts still present answers a question about survivors. The
  ones that left are usually the ones the question was about.
- **Regression to the mean.** Anything selected for being extreme moves back toward average on its
  own. Interventions aimed at the worst performers get credited with this routinely.
- **Multiple comparisons.** Test twenty segments at the usual threshold and one will look
  significant by chance. Decide what you are testing before you slice.
- **Denominator drift.** A ratio moves when either half moves. Show both.
- **Correlation with an obvious common cause.** Two things driven by the same seasonality will
  track each other beautifully and explain nothing.

## Segment before concluding, and stop before you overfit

Blended numbers hide the finding almost every time — one segment moving hard while the rest sit
still. Split by the two or three dimensions that plausibly matter and check whether the effect is
general or local.

Then stop. Slicing until something looks interesting finds noise, reliably, and the result will not
replicate.

## Report the uncertainty rather than burying it

Give the estimate, the range around it, and what would change the answer. State the sample size and
the period. Say plainly what the analysis cannot determine — an analysis honest about its limits
gets trusted on the things it can determine.

**Distinguish what the data shows from what you infer.** Both belong in the report; conflating them
is how a plausible interpretation becomes a fact by the third time it is repeated.

## Never

- Run an analysis that leads to the same action whatever it finds.
- Report a change without naming what it is being compared against.
- Conclude from a total when the segments disagree with it.
- Slice until something is significant and report the slice that was.
