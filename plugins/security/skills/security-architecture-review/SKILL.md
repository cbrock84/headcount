---
name: security-architecture-review
description: Reviews a design or change for security before it ships — authentication and authorization, data handling, secrets, dependencies, and the secure-development practices around it. Use this to review an architecture or pull request for security, set secure coding standards, choose or tune SAST and DAST tooling, assess a third-party integration, or decide whether a design is safe to build.
---

# Security architecture review

## Review in this order

Attention spent in this order finds the most consequential problems first.

**1. Authentication.** How identity is established, how sessions are represented, how they expire,
what happens on password reset and account recovery. Recovery flows are the most commonly weakest
path into an account and the least reviewed.

**2. Authorization.** The one that matters most and gets least attention. For every endpoint and
every object: who is allowed, and where is that checked? The characteristic failure is checking on
the way in but not on the object itself, so any authenticated user can reach any record by changing
an identifier.

Check multi-tenant isolation explicitly and by test, not by reading. Assume every identifier in a
request is attacker-controlled, because it is.

**3. Data.** What is collected, where it goes, where it rests, and who can read it. Sensitive data
in logs, in error responses, in analytics payloads, and in client bundles — all four are routine
findings.

**4. Input and output.** Untrusted input reaching a query, a template, a command, a deserializer, or
a URL the server fetches. Parameterize rather than escape. Validate against an allowlist rather than
a denylist.

**5. Secrets.** Never in source, never in client bundles, never in build logs. Rotatable, scoped to
what needs them, and with a documented rotation path that someone has actually walked.

**6. Dependencies and supply chain.** What is pulled in, how it is pinned, how updates are reviewed,
and what would happen if a maintainer account were compromised. Lockfiles committed, builds
reproducible.

## Reviewing a change rather than a design

Look for: new endpoints without an authorization check, new external input, changed authentication
or session logic, new dependencies, anything touching cryptography, and anything that widens what a
role can do. Everything else is usually lower yield.

**Never write your own cryptography.** Use the vetted primitives, and be suspicious of any diff that
implements a comparison, a token, or a signature by hand.

## Tooling

- **SAST** catches classes of bug cheaply and produces false positives at volume. Tune it or the
  team will learn to ignore it, which is worse than not running it.
- **DAST** and dependency scanning find different things; neither replaces review.
- **Secret scanning in CI and pre-commit** is the highest-value automation per unit of effort.

By name today: Semgrep, CodeQL, or SonarQube for SAST; Snyk, Dependabot, or Trivy for
dependencies; Burp Suite or OWASP ZAP for DAST; gitleaks, TruffleHog, or GitHub secret
scanning for secrets — and similar in each category.

Automation is a floor, not a review. It finds known patterns, not design flaws — and design flaws
are what actually cause the expensive incidents.

## Third-party integrations

What data leaves, under what agreement, with what access, and what happens if they are breached.
Scope credentials to the minimum, prefer short-lived tokens, and know how to revoke without an
outage.

## Never

- Approve a design on the promise of a control with no named owner and no date.
- Accept "it is internal" as an authorization boundary.
- Review the diagram instead of the change. Read what is actually being built.
- Sign off on a third-party integration without knowing what data leaves and under what terms.

## Return contract

Findings by severity, each with: the concrete attack, what the attacker gains, whether it blocks
release, and the specific fix. A finding with no attack path stated is a preference.
