---
name: endpoint-management
description: Manages laptops, desktops and mobile devices — enrolment, configuration, patching, software distribution, and lost or compromised devices. Use this to set up device management, standardise builds, roll out software or an OS upgrade, handle a lost device, or bring an unmanaged fleet under control.
---

# Endpoint management

Endpoints are the most exposed and least controlled part of the estate: they leave the building, run
arbitrary software, and are operated by people whose job is not IT.

## Enrolment is the control point

A device that never enrolled is a device with no patching, no encryption guarantee, and no remote
wipe. Enrolment must be a precondition of access to company data, not a request made afterwards.

Automate it from procurement so a device is enrolled before the user opens it. Manual enrolment as a
post-delivery step is skipped exactly when the desk is busy.

Handle personal devices as a deliberate policy decision, not an accident. If personal devices reach
company data, either manage the work container or restrict what they can reach — and be explicit with
people about what the organization can and cannot see on their own hardware, because ambiguity there
destroys trust quickly.

## A small number of standard builds

Every additional build variant multiplies testing, support and failure modes. Converge on few, and
handle exceptions by adding software to a standard build rather than by creating a new one.

Enforce the security baseline through configuration policy rather than instruction: disk encryption
on, screen lock, firewall, up-to-date agents. Anything relying on a user to configure it is
configured on some devices.

## Patch on a cadence with a deadline

Endpoints patch worse than servers because they are off, asleep, or the user keeps deferring. Allow
deferral with a hard deadline and force after it, and communicate the deadline in advance — an
unexpected forced reboot during a customer call is what teaches people to avoid management.

Report coverage as a percentage of the fleet, and specifically chase the long tail. The devices that
never appear in patch reports are usually the interesting ones: travelling users, spares, and the
machine in a cupboard still holding a domain account.

## Lost, stolen, or leaving

Have the sequence ready in advance: lock, locate if possible, wipe, revoke credentials and sessions,
and record what data was on it for `legal-risk:privacy-and-data-protection` to assess notification.

Encryption is what turns a lost laptop from an incident into paperwork. Verify enforcement
continuously rather than trusting the policy is applied — the device where it silently failed is the
one that gets left in a taxi.

Departures are coordinated with `people:onboarding-and-offboarding`, with asset return tracked
against `it-operations:it-asset-management`.

## Never

- Allow company data onto a device that never enrolled.
- Rely on users to apply security configuration.
- Allow indefinite patch deferral.
- Assume encryption is on without verifying it per device.
