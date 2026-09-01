---
name: data-protection-and-encryption
description: Protects data itself rather than the systems around it — classifying what you hold, encrypting in transit and at rest and understanding what each actually defends against, managing keys and their rotation, handling secrets in applications and pipelines, minimizing and de-identifying, and deleting on purpose. Use this to design data protection for a system, assess an encryption claim, set up key or secret management, or work out what a stolen backup would actually expose.
---

# Data protection and encryption

Perimeter and identity controls protect access to data. These controls protect the data when those
have already failed, which is the scenario worth designing for.

## Classify before you protect, because you cannot protect everything equally

A short scale beats a detailed one — three or four levels that people can apply without a manual.
What matters is that each level carries concrete handling rules: where it may be stored, who may
access it, whether it may leave the environment, and how long it is kept.

**Find it before you classify it.** Sensitive data is rarely only where the architecture says it
is: it accumulates in exports, analytics environments, test databases seeded from production,
support tickets, and log files.

## Know what each kind of encryption actually defends against

This is where claims get made loosely and expectations diverge from reality.

- **In transit** protects against interception on the network. Enforce it everywhere, including
  internal service-to-service traffic, and prefer a modern configuration over one accumulated
  over years.
- **At rest, provider-managed** protects against physical media theft and disk disposal. It does
  not protect against an application bug, a compromised credential, or an over-broad query — the
  storage layer decrypts transparently for anything with legitimate access. Full-disk encryption
  on a running server protects almost nothing about that server.
- **Application-level or field-level** protects specific fields from anything below the
  application, including database administrators and backups. It costs you searchability and
  indexing on those fields, which is a real design constraint rather than a footnote.

Choose deliberately. "Encrypted at rest" as a blanket assurance usually means the first of these,
and answers far less than the person asking believes.

## Keys are the whole control

Encryption moves the problem to key management; it does not remove it. A key stored beside the
data it protects provides documentation, not protection.

- **Use a managed key service or hardware-backed store.** Keys in configuration files, environment
  variables committed to a repository, or application code are the common real-world failure.
- **Separate duties** so the people who administer the data are not the people who administer the
  keys.
- **Plan rotation before you need it**, including how you re-encrypt existing data. Rotation nobody
  has practiced is a policy, and the moment you need it is after a suspected exposure.
- **Know what key destruction means.** Deleting a key makes the data unrecoverable, which is either
  a deletion mechanism you designed for or an outage you did not.

## Secrets are the credential case of the same problem

Application secrets — database passwords, API keys, service tokens — belong in a secret manager,
injected at runtime, scoped narrowly, and rotated on a schedule and on staff departure.

**Scan for committed secrets in CI and pre-commit**, and treat any secret that has ever reached a
repository as compromised. Removing the commit does not un-publish it; rotation is the only
remediation.

## Minimize, de-identify, and delete

The most reliable protection is not holding the data.

- **Collect what the purpose needs.** Every extra field is a permanent liability with no owner.
- **Do not seed test environments from production** without de-identification. This is one of the
  most common exposures and one of the easiest to fix.
- **Understand that removing names is not anonymization.** A combination of ordinary fields often
  re-identifies people; treat de-identified data as still sensitive unless someone has actually
  tested that it is not.
- **Delete on a schedule you can evidence**, and confirm deletion reaches backups, replicas,
  analytics copies and archives — where it usually does not.

## Never

- Describe data as encrypted without saying against which threat.
- Store a key or secret in the same place as the data or code it protects.
- Rotate credentials without confirming the old ones stop working.
- Copy production data into a test environment without de-identifying it first.
