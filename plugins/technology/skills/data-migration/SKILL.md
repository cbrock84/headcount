---
name: data-migration
description: Moves data from one system to another without losing it or corrupting it — profiling the source before mapping, deciding between big-bang and parallel-run cutover, reconciling counts and values rather than assuming, handling the records that will not map cleanly, and planning a rollback that is actually executable. Use this to plan or run a migration, assess a migration plan someone else wrote, work out why a completed migration is producing wrong numbers, or size how long one will really take.
---

# Data migration

Migrations are estimated as a data-movement problem and turn out to be a data-quality problem. The
transfer is the easy part; discovering what the old system actually contains is where the time goes.

## Profile the source before you map anything

Look at the real data, not the schema and not what anyone tells you it contains. Every legacy
system has fields used for something other than their name, free-text where an enumeration was
intended, duplicates that both look canonical, and records predating a rule everyone believes has
always applied.

Count distinct values, null rates, format variance, and outliers on every field you intend to move.
This is the single highest-return activity in a migration and the one most often skipped in favor
of starting the mapping.

**Decide what not to move.** Migrating everything is the default and rarely the right answer.
Archive what has no live use and move a clean subset — it shrinks the mapping, the reconciliation,
and the cutover window all at once.

## Write the mapping down field by field, including the ugly parts

For each target field: source field, transformation, what happens when the source is empty, and
what happens when it does not fit. That last column is the one that decides how the migration goes.

**Records that will not map cleanly need a decision, not a default.** A row silently dropped, a
required field filled with a placeholder, or a truncated value is a defect discovered months later
by someone who trusted the number. Route exceptions to a list a human works through, and count
them.

## Rehearse on a full copy, more than once

A rehearsal on a sample proves the mapping compiles. A rehearsal on a full copy proves the timing,
finds the pathological records, and gives you a real number for the cutover window.

Expect several rehearsals. Each one should end with a reconciliation and a defect list, and the
last one should be clean and timed. Going into cutover having never completed a full run at
production volume means the cutover is the first full run.

## Choose the cutover style deliberately

- **Big-bang** — stop, migrate, start on the new system. Simplest to reason about, and the whole
  risk lands in one window. Viable when the window is affordable and rollback is real.
- **Parallel run** — both systems live, one authoritative. Safer and much more expensive, because
  something has to keep them in step and someone has to reconcile the divergence daily.
- **Phased** — by entity, region, or business unit. Reduces blast radius and creates the hardest
  problem in migration: records that reference each other across the boundary while it exists.

Whichever you pick, name the point of no return and what the rollback is on each side of it. **A
rollback that has never been executed is not a rollback**, and after the new system has taken live
writes, reverting means merging them back — which is a second migration nobody planned.

## Reconcile on counts and on values

Row counts alone catch a truncated load and nothing else. Reconcile control totals for anything
financial, distributions for key fields, and a sample compared record by record. Then have the
people who use the data check the records they know by heart — they find things no query will.

Reconcile again a week after cutover. Problems in the ongoing integrations that replaced the
migration usually show up then rather than on the day.

## Plan for the long tail

Migrations are declared done and then produce findings for months. Keep the source system readable
for longer than feels necessary, keep the mapping and the exception lists, and keep someone
assigned. The alternative is a question about a historical record that nobody can answer because
the old system was decommissioned on schedule.

## Never

- Map from the schema rather than from the data.
- Let a record fail to map and be dropped without landing on a list someone works.
- Cut over without a full-volume rehearsal that completed and reconciled.
- Decommission the source system before the reconciliation window has closed.
