---
name: ai-ml-governance
description: Governs models and AI systems in production — intended use, evaluation, monitoring, human oversight, documentation, and the decision to deploy or retire. Use this before deploying a model or AI feature, when defining evaluation criteria, when a model's behavior has drifted, when assessing AI risk or regulatory exposure, or when deciding whether an AI system is fit for a consequential decision.
---

# AI and ML governance

> Regimes governing automated decision-making differ by jurisdiction and sector and are changing
> quickly. Anything affecting credit, employment, housing, insurance, healthcare, or education
> carries specific legal obligations — involve Legal & Risk and qualified counsel rather than
> treating it as an engineering question.

## Define intended use before evaluating anything

Write down what the system is for, what it is **not** for, who is affected by its output, and what
happens when it is wrong. Most AI failures are use outside intended scope by someone who did not
know the scope existed.

Then decide the consequence tier, because it sets everything after it:

- **Advisory** — a human decides, the model suggests. Lightest oversight.
- **Assistive** — the model acts, a human reviews before effect.
- **Autonomous** — the model acts with effect. Highest bar, and rarely appropriate where a person is
  materially affected.

## Evaluation

A held-out evaluation set that reflects real inputs, including the awkward ones. Built before
deployment and kept stable, or you cannot compare versions.

- **Measure the failure that matters.** Aggregate accuracy hides the errors you care about. A model
  that is 95% accurate and wrong disproportionately on one group is not 95% good.
- **Evaluate by segment**, always. This is where fairness problems and quiet degradation appear.
- **Both error directions.** False positives and false negatives usually have different costs, and
  the threshold should reflect that ratio rather than a default.
- **Establish a baseline.** Compare against the current process — often a simple rule — not against
  zero. Plenty of models fail to beat the heuristic they replaced.

## Monitoring

Models degrade silently: the world moves, inputs drift, and accuracy falls without any error being
raised.

Monitor input distribution against training, output distribution over time, performance against
whatever ground truth arrives later, and the rate of human override. **A rising override rate is the
best early warning you have**, and it is usually already visible in a queue nobody reads.

## Human oversight

Meaningful, not nominal. A reviewer approving hundreds of decisions an hour is not overseeing
anything — they are laundering the model's output through a person.

Meaningful oversight requires the reviewer to see why the model decided, to have time to disagree,
and to have their disagreement change the outcome and be recorded.

## Documentation

Per model: intended use and exclusions, training data and its provenance, evaluation results by
segment, known limitations, monitoring in place, and the owner. This is what you need when someone
asks why a decision was made — and increasingly what a regulator expects to see.

## Retirement

Have a way to turn it off. Know what happens to the process when you do, and confirm the fallback
still works — a manual path that has not been exercised in two years is not a fallback.

## Never

- Deploy without an evaluation set and a monitoring plan.
- Use a model outside its documented intended use because it seems to work.
- Train or fine-tune on customer data without confirming the lawful basis covers it. The basis for
  collecting it rarely extends to this.
- Let a model make a consequential decision about a person with no route to human review.
