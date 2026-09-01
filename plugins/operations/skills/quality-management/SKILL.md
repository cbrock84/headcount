---
name: quality-management
description: Builds quality into operations — defining standards, catching defects at the right point, root cause analysis, and continuous improvement. Use this to reduce a defect or error rate, design quality controls into a process, run a root cause analysis, respond to a customer quality complaint, or set up quality metrics that drive behavior.
---

# Quality management

Inspection at the end sorts good from bad. It never makes anything good. Quality is decided by the
process that produced the work, so that is where the effort belongs.

## Define quality as the customer experiences it

A standard nobody outside the team recognises is a preference. State quality in terms a customer
would agree with: correct, on time, complete, usable — with a threshold, so conformance is a fact
rather than an opinion.

Then distinguish:

- **Specification quality** — does it match what was specified?
- **Fitness for purpose** — does the specification serve the actual need?

A process can hit specification perfectly while producing something nobody wants. Only the second
question protects against that.

## Catch defects where they are cheap

Cost of correction rises steeply with distance from the point of creation. Order of preference:

1. **Prevent** — make the defect impossible. Constraints, defaults, required fields, fixtures.
2. **Detect at source** — the person doing the work sees the error immediately.
3. **Detect downstream** — the next step catches it. Slower, and adds rework.
4. **Detect at the customer** — the most expensive possible option, and it costs trust as well.

Every control pushed one step earlier is worth more than an additional control at the end.

## Root cause, not first cause

"Human error" is where analysis stops, not where it should. Ask what made the error easy to make and
hard to notice: an ambiguous form, an unenforced sequence, a target that rewarded speed.

Work backwards through the causal chain until you reach something you can change structurally. A
corrective action that depends on people being more careful is not a corrective action — the same
conditions will produce the same result with different people.

Verify the fix by watching the defect rate, not by confirming the action was completed.

## Metrics that do not corrupt

Any quality metric attached to individual performance will be gamed, usually by reclassifying
defects rather than preventing them. Measure at the process level, review trends rather than points,
and pair any rate metric with a volume metric so improvement by doing less is visible.

Escaped defects — those the customer found — are the honest measure. Everything else is a proxy.

## Tooling

A quality management system is a regulatory purchase before it is an operational one. Greenlight
Guru, Qualio, MasterControl, ETQ and similar exist because regulated industries need document
control, training records and corrective actions in an auditable system. Outside those industries
a well-run issue tracker and a document repository cover the same ground.

Corrective and preventive action tracking is the part worth having in one place regardless of tool,
because the recurring finding is always an action from last time that was never closed.

Statistical process control needs measurement more than software. A control chart in a spreadsheet
built on real measurements beats a platform fed by nobody.

## Never

- Attribute a defect to carelessness and stop there.
- Add an inspection step in place of fixing the process that produced the defect.
- Set a quality target for an individual that they can meet by reclassifying.
- Close a corrective action without evidence the rate moved.
