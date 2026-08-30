# Headcount Multi-Agent Organization

An agent organization structured as a company: a chief executive over 16 departments, 143 skills,
and 19 agent charters.

## Roster & Surface Authority

| Department | Role | Surface Remit | Authority |
|---|---|---|---|
| `executive` | Builder | `plugins/executive/**` | autonomous |
| `technology` | Builder | `plugins/technology/**` | autonomous |
| `product` | Builder | `plugins/product/**` | autonomous |
| `marketing` | Builder | `plugins/marketing/**` | autonomous |
| `demand-generation` | Builder | `plugins/demand-generation/**` | autonomous |
| `revenue` | Builder | `plugins/revenue/**` | autonomous |
| `finance` | Builder | `plugins/finance/**` | autonomous |
| `operations` | Builder | `plugins/operations/**` | autonomous |
| `people` | Builder | `plugins/people/**` | autonomous |
| `legal-risk` | Builder | `plugins/legal-risk/**` | autonomous |
| `customer-experience` | Builder | `plugins/customer-experience/**` | autonomous |
| `data-analytics` | Builder | `plugins/data-analytics/**` | autonomous |
| `corporate-strategy` | Builder | `plugins/corporate-strategy/**` | autonomous |
| `security` | Builder | `plugins/security/**` | autonomous |
| `it-operations` | Builder | `plugins/it-operations/**` | autonomous |
| `pmo` | Builder | `plugins/pmo/**` | autonomous |
| `repo-meta` | Builder | Project metadata, docs, and configs | proposes |
| `legal-risk-review` | Reviewer | Cross-department legal audit (read-only) | autonomous |
| `security-review` | Reviewer | Cross-department security audit (read-only) | autonomous |

## Reviewer Independence

- **`security-review`** and **`legal-risk-review`** hold no write surfaces.
- Their blocking findings cannot be overruled by the department under review.
- Disagreements escalate directly to the Chief Executive.

## Using Skills

All 143 skills follow the open Agent Skills standard (`agentskills.io`) and reside in
`.agents/skills/<skill-name>/SKILL.md`. Skills load on demand when your prompt matches the
skill description.
