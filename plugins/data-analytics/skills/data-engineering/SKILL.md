---
name: data-engineering
description: Builds and operates data pipelines — ingestion, transformation, orchestration, quality testing, and reliability of data delivery. Use this to design or debug a pipeline, decide batch versus streaming, add data quality checks, handle late or duplicate data, or work out why a dashboard's numbers changed without anyone changing the dashboard.
---

# Data engineering

Pipelines are production systems whose failures are quiet. A broken service pages someone; a broken
pipeline produces plausible numbers that people act on for a week.

This is movement and transformation. Schema and semantics belong to `data-analytics:data-modeling`,
policy and stewardship to `data-analytics:data-governance`.

## Land raw, transform downstream

Keep an immutable copy of source data exactly as received. Transformation logic will be wrong at some
point, and raw data is what lets you reprocess rather than re-request from a source that may no
longer have it.

Business logic belongs downstream where it is visible and testable, not buried in ingestion. The
exception is transformation required for privacy — minimization, pseudonymization, dropping fields
you have no basis to hold — which belongs at ingest precisely because raw storage is what the
obligation attaches to. See `legal-risk:privacy-and-data-protection`.

## Idempotence is the property that matters

Every pipeline will be re-run: after a failure, after a fix, after a late-arriving correction. A
re-run that double-counts is worse than a failure, because it produces a wrong answer silently.

Design for exactly-once effect at the destination — deterministic keys, merges rather than blind
appends, partitioned overwrites. Then re-running is safe and recovery stops being frightening.

## Late, duplicate and out-of-order data

Real sources deliver all three. Decide explicitly, per pipeline: how late is an event still accepted,
what happens to one arriving after its window closed, and how duplicates are identified.

Distinguish **event time** from **processing time** and partition on event time. Aggregations built
on arrival time silently reassign yesterday's activity to today whenever a delivery is delayed.

## Test data, not just code

Unit tests on transformation logic catch the wrong class of failure. Most damage comes from data that
is valid but wrong. Assert on the data itself, in the pipeline, and fail loudly:

- Row counts within an expected range, not merely non-zero.
- Uniqueness of keys, and referential integrity across joins.
- Freshness — the newest record is recent enough to be meaningful.
- Distribution shifts in important columns.

A silent failure is worse than a loud one. Prefer stopping the pipeline to publishing data you do not
trust.

## Tooling

Warehouses and lakehouses: Snowflake, BigQuery, Databricks, Redshift, and Postgres or
DuckDB at small scale, and similar.

Ingestion: Fivetran, Airbyte, Stitch, and similar. Transformation: dbt, SQLMesh.
Orchestration: Airflow, Dagster, Prefect, and similar.

Buy ingestion and build transformation. Connector maintenance returns nothing for the time
your team puts into it.

## Never

- Transform on ingest for business reasons and discard the raw copy.
- Build a pipeline whose re-run double-counts.
- Aggregate on processing time when event time is available.
- Let a pipeline fail silently and publish stale data as current.
