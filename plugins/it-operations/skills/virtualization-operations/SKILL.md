---
name: virtualization-operations
description: Runs the hypervisor layer beneath the servers — host capacity and consolidation ratios, VM sprawl, snapshot discipline, resilience and live migration, and licensing that counts cores rather than instances. Use this to size or expand a cluster, work out why VMs are slow when the hosts look idle, clean up sprawl, set snapshot and template policy, or decide what stays virtualized and what moves to cloud.
---

# Virtualization operations

Virtualization is the layer most infrastructure problems actually live in, and the one most
monitoring is blind to. A guest reports healthy CPU while contending for a core it never gets. The
usual failure is diagnosing upward — into the application — when the constraint is a host two
layers below.

## Consolidation ratio is a decision, not a result

Every cluster has a ratio of virtual resources to physical ones, and most organizations discover
theirs rather than choosing it. Overcommitting memory and CPU is normal and correct; the question
is how far, and what happens at peak rather than average.

Two numbers worth knowing at all times: what the cluster runs at now, and what it runs at when one
host is gone. If losing a single host takes you past capacity, you have a cluster that survives
hardware failure on paper and not in practice. Size for N-1 and keep the spare capacity visible in
the budget, or the first thing cut is the headroom that makes the design work.

Memory is usually the real ceiling, not CPU. Cores oversubscribe gracefully; RAM does not.

## Sprawl is a lifecycle problem wearing an infrastructure costume

VMs are trivially easy to create and socially difficult to delete. Nobody remembers what the box
does, so it stays — consuming license, backup capacity, patching effort, and an attack surface
nobody reviews.

The fix is ownership recorded at creation, not an annual cleanup. Every VM gets a named owner and a
review date before it is built. Anything that cannot name an owner is a candidate for
decommissioning, and the decommission path is: power off, wait a defined period, then delete.
Powering off first turns an irreversible decision into a reversible one and produces the phone call
that tells you what the machine did.

Templates and golden images keep the estate consistent. Builds that started from a template drift
less than builds someone assembled, and drift is what makes patching unpredictable — see
`it-operations:systems-administration` for the configuration baseline this feeds.

## Snapshots are not backups, and old ones cause outages

A snapshot is a change log against a disk, and it grows until it is merged. Left running, it fills
the datastore and takes down every VM sharing that storage, which is a much worse incident than
whatever the snapshot was protecting against.

Treat them as a short-lived tool for a specific change: take one before a risky upgrade, merge it
the same day, and alert on any snapshot older than the threshold you set. They are not a retention
mechanism and they do not survive storage failure — real recovery belongs to
`it-operations:backup-and-recovery`.

## Live migration is a maintenance capability, not a resilience one

Moving running workloads between hosts is what makes patching the hypervisor possible without a
maintenance window, and that alone justifies it. It does not protect against a host failing
suddenly — that is a restart on another host, with downtime measured in boot time.

Know which of your workloads tolerate that restart and which do not. The ones that do not need
clustering inside the guest, and virtualizing them does not remove that requirement.

## Licensing counts what you provision, not what you use

Hypervisor and guest licensing is commonly priced per physical core or socket, which means a
consolidation decision is also a licensing decision, and adding hosts can cost more in license than
in hardware. Some vendors license every core in a cluster a workload could migrate to, not the one
it runs on — which turns an availability setting into a bill.

Model the license cost before the hardware purchase, and check it again when the cluster grows.
`it-operations:it-asset-management` owns the entitlement records; this skill owns knowing which
architectural choices move them.

## Where the boundary sits with cloud

Not everything should be virtualized on-premises, and not everything should move. The honest test
is not cost per VM — it is whether the workload's demand is steady or spiky. Steady, predictable
load runs cheaper on hardware you own. Spiky or seasonal load is what cloud elasticity is actually
for.

Hybrid is the normal end state, not a transitional embarrassment. What makes it painful is running
two operating models with two sets of habits, so decide deliberately which one owns identity,
monitoring, and backup rather than letting each side answer differently.
