---
name: business-intelligence
description: Builds reporting and self-serve analytics that people actually use — metric trees, dashboard design, distribution, and the discipline that stops dashboards proliferating. Use this to build a dashboard or report, design a metrics framework, set up self-serve analytics, decide what to measure, or diagnose why reporting exists but nobody uses it or trusts it.
---

# Business intelligence

Most organizations have too many dashboards and too little insight. The two are related: when
everything is measured, nothing is watched.

## Start from the decision

Every report answers one question for one audience who can act on it. Before building, name the
decision it informs and what a viewer would do differently based on it.

If nothing would change, do not build it. That single filter removes most dashboard requests, and
the ones surviving it get used.

## Metric trees

Structure metrics as a tree, not a list. One primary outcome at the top, decomposed into the drivers
that mathematically produce it, each decomposed again.

Revenue = customers × average value. Customers = new + retained. New = traffic × conversion. And so
on.

This does two things a metric list cannot: when the top number moves, you can walk down to find
*where*; and it makes clear which metrics are levers and which are outcomes. Teams should be
measured on levers they control, not on outcomes they influence.

## Dashboard design

- **One screen, one question.** Scrolling dashboards are several dashboards that were not separated.
- **Lead with the answer** — the primary number, its comparison, and whether that is good. A number
  with no comparison is not information.
- **Comparison always**: prior period, target, or cohort. Choose deliberately, because each tells a
  different story.
- **Say what "good" is.** A viewer who cannot tell whether 4.2% is good will not act.
- **Annotate the anomalies.** The spike everyone asks about should carry its explanation, or you
  will explain it every month.
- **Cut the rest.** Charts nobody uses cost attention on every visit and make the useful ones harder
  to find.

## Self-serve

Self-serve works when the semantic layer is trustworthy and the questions are anticipated. It fails
when people are handed raw tables and left to define metrics themselves — that produces confident
wrong answers, which is worse than a queue.

Give governed metrics, curated datasets, and templates for common questions. Keep the raw layer for
analysts.

## Trust

Reporting nobody trusts is not used, and trust is lost far faster than it is rebuilt. Protect it by
showing freshness on every dashboard, surfacing failures rather than serving stale data silently, and
reconciling against the system of record for anything financial.

When a number is wrong, say so prominently and fast. Quietly correcting it is how a team learns to
check every figure by hand.

## Maintenance

Dashboards accumulate. Review usage periodically and retire what nobody opens — with a notice period,
since the one person using it may be using it for something important.

## Tooling

BI: Power BI, Looker, Tableau, Metabase, Omni, Hex, and similar.

Metric definitions belong in a semantic layer — dbt's, Looker's LookML, Cube — rather than
in each dashboard's SQL, or the same metric will disagree with itself across two tabs.

Spreadsheets remain the most-used BI tool in every organization. Plan for the export rather
than pretending it will not happen.

## Never

- Build a dashboard nobody has a decision for. Start from the decision.
- Ship a metric with two definitions live at the same time.
- Leave a dashboard published with no owner. Unowned dashboards get trusted, then get wrong.
- Show a number without the denominator and the window it covers.
