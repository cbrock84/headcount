---
name: data-modeling
description: Designs the warehouse and semantic layer — source-to-mart structure, dimensional modeling, grain, slowly changing dimensions, and the metric layer analytics reads through. Use this to design or restructure a warehouse, model a new source, decide on grain or table structure, build a semantic or metric layer, or diagnose why queries are slow, wrong, or impossible to write.
---

# Data modeling

## Layers, and why the middle one matters

Three layers, each with one job:

1. **Raw** — source data, unmodified, append-only. Never transform on ingest; you cannot recover what
   you discarded, and you will want it.
2. **Staging** — cleaned and conformed: consistent types, standardized names, deduplicated, no
   business logic yet.
3. **Marts** — business-facing models shaped for how questions are asked.

The discipline that pays is keeping business logic out of layers 1 and 2. Logic embedded in ingestion
cannot be changed retroactively, and it will need to change.

## Grain is the decision everything follows from

State the grain of every table in one sentence: *one row per what*. "One row per order line per day"
is a grain. "Order data" is not.

Most modeling errors are grain errors, and they surface as fan-out — a join multiplying rows so every
downstream sum is inflated. If a number is mysteriously too high, check the grain before checking the
logic.

## Dimensional structure

Facts for events and measurements; dimensions for the things being described. Keep facts narrow and
long, dimensions wide and short.

Conform dimensions across facts — one customer dimension, used everywhere. Separate customer tables
per domain is how the same customer gets counted differently in two reports.

**Handle history deliberately.** Overwriting a dimension attribute rewrites the past: last year's
revenue silently re-attributes to this year's segment. Decide per attribute whether history matters,
and where it does, keep versions with valid-from and valid-to.

## The semantic layer

Define metrics once, above the marts, and have every consumer read through it. Without it, the same
metric is reimplemented in each dashboard and they drift — not because anyone is careless, but
because a filter differs.

The semantic layer is where the metric dictionary becomes executable rather than documentary.

## Performance

Model for the query pattern you actually have. Pre-aggregate what is queried constantly; leave the
long tail to compute on demand.

Partition and cluster on what people filter by — usually time, then a tenant or entity key. Most slow
warehouse queries are full scans of a table that could have been partitioned by date.

Denormalize deliberately, and write down why. Undocumented denormalization is indistinguishable from
a modeling error six months later.

## Never

- Build a mart directly on raw. The coupling means every source change breaks the business layer.
- Mix grains in one table.
- Let a dashboard contain business logic the warehouse does not. That logic is invisible and
  unversioned.
