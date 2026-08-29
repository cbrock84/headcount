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
| `it-operations` | IT Operations | CIO | 7 |
| `product` | Product | CPO | 9 |
| `marketing` | Marketing | CMO | 17 |
| `demand-generation` | Demand Generation | CMO | 11 |
| `revenue` | Revenue | CRO | 8 |
| `finance` | Finance | CFO | 9 |
| `operations` | Operations | COO | 8 |
| `pmo` | Program Management Office | EPMO / COO | 6 |
| `customer-experience` | Customer Experience | CCO | 5 |
| `data-analytics` | Data & Analytics | CDO | 6 |
| `corporate-strategy` | Corporate Strategy | CSO | 5 |
| `people` | People | CHRO | 9 |
| `legal-risk` | Legal & Risk | CLO / CCO | 5 · reviewer-class |

16 departments, 135 skills.
<!-- END GENERATED: departments -->

## Remaining gaps

### Tier 1 — worth building next

**Legal depth.** Five skills. Missing `ip-and-licensing`, `regulatory-compliance`, and
`audit-readiness` — the last pairing with `finance:internal-controls-and-audit`, which covers
controls over financial reporting but not readiness for a wider audit.

**Customer Experience depth.** Five skills, the thinnest department. Missing `customer-onboarding`,
`churn-and-recovery`, and `community`.

**Corporate Strategy depth.** Five skills. Missing `competitive-intelligence` and
`market-entry`.

**Built since this list was written**, and removed from it: operations gained supply chain, quality
management and capacity planning; finance gained revenue recognition, cash management as
`treasury-and-liquidity`, investment appraisal as `capital-allocation`, and financial controls as
`internal-controls-and-audit`; people gained performance management, employee relations, learning
and development, and workforce planning. `procurement` was judged already covered by
`operations:vendor-management` and `it-operations:it-asset-management` rather than needing its own
skill.

### Tier 2

**Communications and Investor Relations.** `marketing:public-relations` covers earned media. No
internal communications, executive communications, crisis communications, or IR. IR only matters
once there are investors.

**Product depth.** No dedicated `product-discovery`, `roadmap-prioritization`, or
`pricing-experimentation` — the last overlapping `revenue:pricing-and-packaging`, so it may not
warrant its own skill.

### Tier 3 — when the business needs them

- **Chief Sustainability / ESG** — emissions reporting and supply-chain diligence, increasingly
  statutory rather than optional.
- **Corporate Secretary** — currently inside `legal-risk:corporate-governance`.
- **Internal Audit** — with a structural caveat: internal audit reports to the audit committee, not
  the CEO. Placing it under `executive` would reproduce the independence failure it exists to
  prevent. It needs a reviewer-class agent no chief can overrule.

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
