# Org chart

```
                                  Chief Executive
                                         │
   ┌──────────┬──────────┬──────────┬────┴─────┬──────────┬──────────┬──────────┐
  CTO/CIO    CPO        CMO        CRO        CFO        COO        CDO        CSO
Technology  Product  Marketing +  Revenue   Finance  Operations   Data &    Corporate
   │                 Demand Gen                          │       Analytics   Strategy
  CIO                                                  EPMO
IT Operations                              Program Management Office

  CHRO                CCO
 People       Customer Experience

   ┌─────────────────────────────────────────────────────────────────────────┐
   │   Security (CISO)                            Legal & Risk (CLO / CCO)   │
   │                        reviewer-class                                   │
   └─────────────────────────────────────────────────────────────────────────┘
```

An interactive version — searchable across every skill, linking out to each one — is generated at
[`docs/org-chart.html`](org-chart.html).

Security and Legal & Risk sit across every function rather than under one. Both are reviewer-class:
they review what the other departments commit to, and their blocking findings are not overrulable by
the department under review. That is why the CISO and the CLO report to the chief executive rather
than into the function they oversee.

## Departments

<!-- BEGIN GENERATED: departments -->
| Department | Function | Executive | Skills |
|---|---|---|---|
| `executive` | Office of the CEO | Chief Executive | 6 |
| `technology` | Technology | CTO / CIO | 18 |
| `security` | Security | CISO | 6 · reviewer-class |
| `it-operations` | IT Operations | CIO | 12 |
| `product` | Product | CPO | 9 |
| `marketing` | Marketing | CMO | 18 |
| `demand-generation` | Demand Generation | CMO | 11 |
| `revenue` | Revenue | CRO | 8 |
| `finance` | Finance | CFO | 13 |
| `operations` | Operations | COO | 11 |
| `pmo` | Program Management Office | EPMO / COO | 9 |
| `customer-experience` | Customer Experience | CCO | 5 |
| `data-analytics` | Data & Analytics | CDO | 6 |
| `corporate-strategy` | Corporate Strategy | CSO | 5 |
| `people` | People | CHRO | 12 |
| `legal-risk` | Legal & Risk | CLO / CCO | 6 · reviewer-class |

16 departments, 155 skills.
<!-- END GENERATED: departments -->

## Remaining gaps

Validated against two public taxonomies rather than intuition: the **BLS Standard Occupational
Classification** major groups 11-0000 (Management) and 13-0000 (Business and Financial Operations),
and the shape of a cross-industry business. Every management occupation in 11-0000 that is not
industry-specific now maps to a skill, and the gaps below are what remains.

### Tier 1 — worth building next

**Customer Experience depth.** Five skills, now the thinnest department. Missing
`customer-onboarding`, `churn-and-recovery`, and `community`.

**Legal depth.** Missing `ip-and-licensing` and `audit-readiness` — the latter pairing with
`finance:internal-controls-and-audit`, which covers controls over financial reporting but not
readiness for a wider audit.

**Corporate Strategy depth.** Five skills. Missing `competitive-intelligence` and `market-entry`.

**Product depth.** Nine skills, but weighted toward design and interface craft. Missing
`product-discovery` and `roadmap-prioritization`.

### Tier 2 — real, but situational

**Internal and executive communications.** `marketing:public-relations` covers earned media;
nothing covers all-hands, change communication, or executive voice. `pmo:change-and-adoption`
covers rollout communication only.

**Investor relations.** Matters once there are investors, and not before.

**Labor and union relations.** SOC 13-1075. `people:employee-relations` covers individual
grievances and investigations; collective bargaining is a different discipline. Weighted toward
manufacturing, logistics and retail, so it belongs with the vertical packs rather than the core.

**Industrial production management.** SOC 11-3051. `operations:quality-management` and
`operations:capacity-and-demand-planning` cover the general disciplines; plant-floor management is
vertical.

### Tier 3 — when the business needs them

- **Chief Sustainability / ESG** — emissions reporting and supply-chain diligence, increasingly
  statutory rather than optional.
- **Corporate Secretary** — currently inside `legal-risk:corporate-governance`.
- **Internal Audit** — with a structural caveat: internal audit reports to the audit committee, not
  the CEO. Placing it under `executive` would reproduce the independence failure it exists to
  prevent. It needs a reviewer-class agent no chief can overrule.

### Deliberately out of scope

The industry-specific management occupations in SOC 11-9000 — education, medical and health
services, food service, lodging, gambling, funeral, agricultural and construction management — are
correctly absent from a cross-industry core. They belong to the vertical variants in D8.

## Structural notes

**Reviewer independence is now modeled, not just described.** `security` and `legal-risk` each
appear twice in `docs/AGENT-SURFACES.md`: once as a builder owning their own tree, once as a
reviewer holding no write surface at all. The guard fails if a reviewer declares one, so the
read-only property is structural rather than a promise.

**Two departments report to the CMO.** `marketing` holds brand, content, and communications;
`demand-generation` holds acquisition, conversion, and measurement. The split keeps specialization
while halving what any one install loads.

**How gap skills are scoped.** Specialists in `finance`, `people`, `legal-risk`, `operations`, and
`security` were drafted against current senior job postings for those functions, so each remit
reflects what the role is actually accountable for rather than an assumption about it.
