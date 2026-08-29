---
name: release-and-deployment
description: Ships changes safely and often — pipelines, deployment strategies, feature flags, rollback, and database changes. Use this to design a deployment pipeline, reduce release risk, roll out a risky change gradually, plan a schema migration, or work out why releases are infrequent and frightening.
---

# Release and deployment

Release risk is dominated by batch size. Large infrequent releases are dangerous because many changes
land at once and nobody can tell which one broke it — so teams release less often, which makes each
release larger. The loop is the problem.

## Separate deploy from release

Deploying code and exposing behaviour to users are different acts, and coupling them forces every
deployment to be a business decision.

Decouple with flags: deploy continuously, expose deliberately. This makes rollback a configuration
change rather than a redeployment, which is the difference between seconds and minutes at the worst
possible time.

Flags are inventory and rot. Give each an owner and a removal date; a codebase full of stale flags
has combinatorial states nobody has tested.

## The pipeline is the quality gate

Automate everything between commit and production, and let the pipeline reject. Manual steps get
skipped under pressure, which is exactly when they matter.

Order gates fast-to-slow so failure is cheap: lint and unit tests, then integration, then anything
requiring a deployed environment. A pipeline slow enough to be circumvented is worse than a fast one
with fewer checks, because it will be circumvented.

Build once and promote the same artefact through environments. Rebuilding per environment means the
thing you tested is not the thing you shipped.

## Roll out gradually

Expose to a small population first and watch real signals before widening. Canary or percentage
rollout turns a total failure into a contained one.

Define the abort condition **before** starting, with a threshold and a named decision-maker. Under
pressure, and with the change fresh, the instinct is always to wait a little longer and see.

## Database changes are the asymmetric risk

Code rolls back; data does not. Make schema changes backward-compatible and multi-step: add the new
structure, write to both, migrate, switch reads, then remove the old — with the application tolerant
of both shapes throughout.

Test the migration against production-scale data. A migration that is instant on a development
dataset can lock a large table for a length of time nobody modelled.

## Never

- Couple deploying code to exposing behaviour.
- Promote a different artefact than the one that was tested.
- Begin a rollout without a defined abort condition.
- Ship a schema change that requires the application and database to deploy simultaneously.
