---
name: ux-product-auditor
description: Audits a website, app, onboarding flow, or design for usability, conversion, and product problems, tying every finding to a business outcome and a severity. Use this to review an interface, diagnose low conversion or activation, find where users drop off, get structured product feedback, or decide which UX fixes to ship first. For raising visual quality rather than finding problems, use `interface-craft`.
---

# UX and product auditor

A finding that does not name a consequence is an opinion. Every item in an audit connects a specific
friction to a specific outcome.

## Audit by walking the real path

Do the actual task, on the actual device, as a first-time user with no context — not a tour of the
screens. Most serious problems live in transitions between screens, which a screen-by-screen review
never sees.

Then walk it again as a returning user, whose needs are opposite: speed over explanation, and
recovery from whatever state they left in.

## Lenses

Run each separately; combined, you find only what you were already looking for.

- **Comprehension** — can a stranger tell what this does and whether it is for them?
- **First value** — how many steps to the first genuinely useful moment, and how many are avoidable?
- **Friction** — every field, click, decision, and wait. Which are load-bearing and which are
  habit?
- **Trust** — does anything ask for more than it has earned at that point?
- **Recovery** — what happens on error, empty, slow, offline, or wrong input?
- **Accessibility** — contrast, keyboard reachability, target size, meaning carried by color alone.
  Below this floor, some people cannot use the product at all.

## Severity

Assign one to every finding, and be strict — an audit where everything is critical has ranked
nothing:

- **Critical** — blocks the primary task, loses data, or excludes a group of users entirely.
- **High** — measurably costs conversion or activation for many users.
- **Medium** — friction with a workaround, or affects a narrower path.
- **Low** — polish, inconsistency, or a preference.

## Finding format

Each finding carries: **where** (the exact screen and step), **what** the user experiences, **why**
it costs something, **the consequence** in business terms, **severity**, and **the fix** with rough
effort.

"The signup form asks for company size before the account exists; users who do not know it guess or
abandon; this sits before the only conversion event on the page" is a finding. "Form is too long" is
a note.

## Diagnosing low conversion or activation

Instrument the funnel to find *where*, then observe sessions to find *why*. Analytics say the step;
only watching says the reason. Teams that skip the second half fix the wrong thing confidently.

Common causes, in rough order of frequency: asked for too much too early, value not visible before
effort is required, an empty state with no path out of it, and a required integration the user
cannot authorize.

## Scoring

Where a numeric score is useful — tracking over time, comparing surfaces, reporting to someone who
did not read the audit — score each lens from one to five against stated criteria, and publish the
criteria alongside the score. An unexplained score is unfalsifiable and will be argued with rather
than acted on.

Use the same scale everywhere so scores are comparable between audits. Do not average the lenses
into one headline number: a product that is excellent everywhere and inaccessible scores well on the
average and is still unusable for some people.

## Moving from findings to solutions

An audit that stops at problems transfers the hard part back. For each finding above medium
severity, propose a specific fix — the actual change, not a direction — with rough effort and what
it would improve.

Where several findings share a root cause, say so and propose the one change. Fifteen findings
traceable to a missing design system is one finding.

Where the right fix is uncertain, propose the cheapest way to find out rather than guessing.

## Prioritizing

Rank by users affected × severity ÷ effort. Then state the one thing to fix first, and be willing to
say that most of the list is not worth doing yet. A prioritized audit is more useful than a complete
one.
