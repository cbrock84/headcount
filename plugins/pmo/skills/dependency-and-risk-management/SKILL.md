---
name: dependency-and-risk-management
description: Manages delivery risk and cross-team dependencies — identifying, sizing, mitigating and escalating what could stop the work. Use this to build a risk register that gets used, manage dependencies between teams, decide what to escalate and when, or work out why the same risks keep materializing unmanaged.
---

# Dependency and risk management

This is delivery risk: what could prevent this work from landing. Enterprise risk — the framework,
appetite and register at company level — is `legal-risk:enterprise-risk`, and the two should not be
merged.

## Dependencies are commitments or they are wishes

A dependency in your plan that the owning team has not agreed to, with a date they have committed
to, is a wish. Most plans contain several.

For each: what exactly is needed, from whom by name, by when, and what happens if it is late. Then
confirm it with the owning team in a way they would recognize as a commitment — an item on their
plan, not a mention in a meeting.

Track dependencies both ways. Teams reliably track what they are owed and forget what they owe, which
is why everyone believes they are being let down.

The dangerous ones are **transitive**: your dependency has a dependency you cannot see. Trace at
least one hop further than feels necessary, particularly where a shared specialist or a single team
appears repeatedly.

## A risk register people actually use

Most registers are written once for a gate and never opened. What makes one useful:

- **Specific.** "Integration delay" is a topic. "Vendor's API v2 is not released until March; our
  migration starts in February" is a risk you can act on.
- **Sized on both axes** — likelihood and impact — because the response differs entirely between a
  likely nuisance and an unlikely catastrophe.
- **Owned by someone who can act**, not by the project manager who can only report.
- **Carrying a decision date** — the point past which mitigation is no longer possible. This is the
  field most often omitted and the one that makes the register operational rather than decorative.

Review by exception: what changed, what is approaching its decision date. Reading the whole register
aloud is how registers stop being read.

## Mitigate, or accept explicitly

Four responses: avoid by changing the plan, reduce likelihood or impact, transfer to someone better
placed to carry it, or accept. Acceptance is legitimate and must be explicit, with a named accepter
— an unacknowledged acceptance is just an unmanaged risk.

Distinguish mitigation from contingency. Mitigation lowers the chance; contingency is what you do
when it happens anyway. Serious risks need both, and contingency needs to be prepared before it is
required.

## Escalate early and specifically

An escalation naming the decision needed, the options, and the date by which it is needed gets
resolved. A general expression of concern gets acknowledged and nothing happens.

Escalate when the decision exceeds your authority or the decision date is approaching — not when the
risk has already materialized, at which point it is a status report.

## Never

- Carry a dependency the owning team has not committed to.
- Log a risk without an owner who can act on it.
- Accept a risk without naming who accepted it.
- Escalate a concern without naming the decision required.
