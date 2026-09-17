---
name: cloud-infrastructure
description: Designs and runs cloud infrastructure — environments, infrastructure as code, networking and isolation, scaling, and cost. Use this to design a cloud environment, control infrastructure spend, set up environment separation, plan for scale or region failure, or review infrastructure someone configured by hand.
---

# Cloud infrastructure

Cloud replaces capital cost with an operating cost that scales with carelessness. The discipline is
mostly about making the environment reproducible and the spend visible.

## Everything reproducible from code

Infrastructure created by hand cannot be reviewed, reproduced, or recovered. Define it as code,
review it like code, and apply it through a pipeline rather than from a laptop.

The test: could you rebuild the environment from an empty account, and do you know that because you
have done it? Untested reproducibility is a belief.

Console access for humans should be read-only in production by default. Write access exists for
emergencies, is time-bound, and is logged — see `security:access-and-identity` for the policy this
implements.

## Environments that mean something

Separate environments by blast radius, not by name. Separate accounts or subscriptions give a hard
boundary; separate namespaces in one account give a soft one that a misconfigured permission
crosses.

Production data does not belong in lower environments. Where realistic data is needed, mask or
synthesize it — a copied production database is a breach waiting for a misconfigured bucket, and it
is one of the most common ways personal data escapes.

## Networking and isolation

Default deny, then open what is needed. Public exposure should be a deliberate, reviewable act rather
than the residue of a default.

Keep the trust boundary explicit and few: what is reachable from the internet, what is reachable
between services, what reaches data stores. Most cloud incidents are not exotic — they are a storage
bucket, a database, or a management interface that was reachable and should not have been.

## Scaling and failure

Scale horizontally where you can and know your actual limits — the database connection ceiling, the
third-party rate limit, the single-threaded component nobody remembers. Autoscaling in front of a
hard downstream limit converts a slow system into an outage.

Design for the failure of a single instance and a single zone as routine. Region failure is a
business continuity decision with a real price attached, made with
`operations:business-continuity-and-resilience` rather than assumed by engineering.

## Cost

Cost is an architectural property. Attribute spend by team and workload from the start; without
tagging, cost becomes an unattributable aggregate that only ever gets addressed in a panic.

The usual large wins are unglamorous: idle non-production resources, over-provisioned instances,
storage nobody deleted, and cross-zone data transfer nobody accounted for.

## Never

- Make a production change by hand that is not reflected in code.
- Put production data in a lower environment unmasked.
- Autoscale a tier in front of a hard downstream limit.
- Run without cost attribution until the bill forces it.
