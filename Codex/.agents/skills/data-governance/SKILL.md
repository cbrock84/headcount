---
name: data-governance
description: Establishes ownership, definitions, quality, access, and lineage for the organization's data. Use this when metrics disagree between teams, when nobody knows which dataset is authoritative, when setting up data ownership or access policy, when data quality is unreliable, or before opening a dataset to a wider audience.
---

# Data governance

Governance has a reputation for bureaucracy because it is usually implemented as approval queues.
Done properly it is the opposite: it makes data usable without asking anyone.

## Start with definitions, not policy

The highest-value governance artifact is a metric dictionary. For each business metric:

- The **plain-language definition** — what it counts, and what it deliberately excludes.
- The **computation**, unambiguously: source table, filters, time grain, timezone.
- The **owner** — a person who decides when it is disputed.
- **Known caveats** — when it is misleading, and what changed historically.

Most metric disputes dissolve once both parties read the same definition and discover they were
measuring different things. Almost none require a policy.

Watch the ones that look obvious. "Active customer," "revenue," and "signup" each have half a dozen
defensible definitions, and the ambiguity surfaces at the worst moment.

## Ownership

Every dataset has a named owner accountable for its quality and access — a person, not a team.
Unowned datasets decay, and nobody notices until a decision is made on stale data.

The owner should sit with the business meaning, not with the pipeline. The team that generates the
data understands what it means; the platform team understands how it moves.

## Quality, measured rather than asserted

Test data like code, continuously, and alert on failures:

- **Freshness** — did it arrive when expected?
- **Volume** — is the row count within its normal range? A silent drop to zero is the classic
  failure.
- **Uniqueness and nullity** on key fields.
- **Referential integrity** across joins.
- **Distribution** — has the shape shifted in a way nothing explains?

The point is finding breakage before a decision is made on it. A pipeline that fails loudly is
better than one that silently produces yesterday's numbers.

## Access

Default to open for internal, non-personal data. Restrictive-by-default drives the shadow spreadsheet
layer, which is genuinely less safe than a governed warehouse.

Personal, financial, and regulated data are the exception: least privilege, purpose stated, reviewed
periodically, with Legal & Risk involved on anything with a lawful-basis question.

## Lineage

Know where a number came from and what feeds it. Without lineage, you cannot answer the two
questions that matter during an incident: what broke upstream, and what downstream is now wrong.

## Never

- Let two systems each claim to be the source of truth for the same fact.
- Fix a data-quality issue in a dashboard. Fix it upstream or it recurs in every other consumer.
- Retire a dataset because it looks unused — you cannot see every consumer. Deprecate, announce,
  then remove.
