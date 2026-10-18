---
name: marketing-analytics
description: Sets up, audits, and reports on marketing measurement — tracking plans, event schemas, attribution models, and the dashboards built on them. Use this to instrument a site or product, audit tracking nobody trusts, choose or interpret an attribution model, build reporting that answers a specific question, or reconcile numbers that disagree between tools.
---

# Marketing analytics

## The tracking plan comes first

Dashboards built on bad instrumentation are confident and wrong, which is worse than having none.

Define, in writing, before implementing: every event, when it fires, its properties and their types,
and the question each one exists to answer. An event with no question behind it is noise that will
be maintained forever.

Naming convention decided once and enforced: `object_action`, lowercase, past tense. Inconsistent
naming is unfixable later without breaking historical data.

## Auditing existing tracking

Numbers nobody trusts usually come from one of:

- **Double-firing** on route changes in single-page apps.
- **Events that stopped** when someone changed a selector or a component.
- **Definition drift** — two tools counting "signup" at different moments.
- **Bot and internal traffic** never filtered out.
- **Consent and blockers** removing a meaningful and non-random share of data.

Verify by doing the action yourself and watching the event arrive with the properties you expect.
Not by reading the dashboard.

## Attribution

Every model is wrong in a known direction. Pick deliberately and state the bias:

- **Last-touch** — over-credits closing channels: brand search, retargeting. Under-credits
  everything that created demand.
- **First-touch** — the mirror image; over-credits discovery.
- **Multi-touch** — better, and dependent on complete tracking you probably do not have.
- **Incrementality testing** — the only method that answers "would this have happened anyway." The
  most expensive and the most trustworthy.

Use one model consistently for decisions, and check it periodically against a holdout. Switching
models to make a channel look better is how organizations mislead themselves.

## Reporting

Every report answers one question for one audience. Reports built to display everything get read by
nobody.

Show the metric, its comparison period, and the decision it informs. A number with no comparison is
not information. Where a number moved, the report should say why or say that the cause is unknown —
"unknown" is a legitimate and useful finding.
