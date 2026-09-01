---
name: experimentation
description: Designs, runs, and reads A/B tests and growth experiments — hypothesis, sample size, duration, and honest interpretation. Use this to plan a test, judge whether a result is real, build an experimentation program, decide what to test next, or diagnose why tests keep producing inconclusive or non-replicating results.
---

# Experimentation

Most A/B testing programs produce confident conclusions from insufficient data. The discipline is
almost entirely in what you do before launch.

## Before running

- **Hypothesis with a mechanism.** "Moving the pricing table above the fold will raise trial starts,
  because visitors currently leave before seeing pricing." Not "let's try a green button."
- **One primary metric**, chosen in advance. Secondary metrics are context, never the verdict.
- **Sample size calculated in advance**, from your baseline rate and the smallest lift that would
  change a decision. If the required sample is unreachable, do not run the test — decide by judgment
  and say so.
- **Duration set in advance**, covering at least one full weekly cycle, and two if the buying cycle
  is long.
- **Guardrail metrics** that would make you reject a win: refunds, support volume, downstream
  retention.

## While running

Do not look at results and act on them mid-flight. Peeking and stopping at significance is the
single most common way to generate false positives, and it is very effective at it.

Check only that the test is running correctly — even split, no broken variant, tracking firing.

## Reading

- **At the pre-set duration**, not before, and not extended because it is nearly significant.
  Extending until significance manufactures it.
- **Significance is not size.** A statistically significant 0.3% lift may not be worth shipping.
- **Inconclusive is a real result** and the most common one. It means the change did not matter
  enough to detect, which is useful.
- **Check the guardrails** before declaring a win.
- **Segment afterward for hypotheses only**, never for verdicts. Slice enough ways and something is
  always significant.

## Program level

Test where the traffic and the leverage are. Most sites can only run a handful of adequately powered
tests a year — spend them on structural questions, not button colors.

Keep a log of every test: hypothesis, result, decision. Without it, teams re-run the same tests every
eighteen months and re-learn the same things.

## Never

- Stop a test because it reached significance early. Peeking until it looks conclusive manufactures the result.
- Run a test that cannot reach adequate sample size in a reasonable window. Ship the change on judgment instead and say so.
- Change more than one variable and attribute the outcome to the one you liked.
- Count a flat result as a failure. A well-run test that rules out a plausible idea has bought information.
