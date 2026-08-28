# Decision log

One heading per decision, numbered sequentially. **Numbers are addresses: a number is assigned when
the question is asked, not when it is answered, and is never reused.** Every decision carries
lettered options and an explicit recommendation — never a bare question, never options without a
recommendation.

Answer by number and letter (`D7b`). Resolved decisions stay in the log with their resolution
recorded rather than being deleted.

## Status

| # | Decision | Status |
|---|---|---|
| D1 | Import scope from discovered collections | ✅ Resolved |
| D2 | Organizational structure | ✅ Resolved |
| D3 | Handling of third-party licensed content | ✅ Resolved |
| D4 | Rewrite-before-purge ordering | ✅ Resolved |
| D5 | Vendored content remaining in branch history | ✅ Resolved |
| D6 | Provenance of the 12 Drive-sourced skills | ✅ Resolved |
| D7 | Audience for vertical variants | ✅ Resolved |
| D8 | Architecture for vertical variants | ✅ Resolved |
| D9 | Security as its own department | ✅ Resolved |
| D10 | Which department to deepen next | ✅ Resolved |
| D11 | Cross-org sweep of public repos | ✅ Resolved |
| D12 | Administration department disposition | ✅ Resolved |
| D13 | Reviewer-class agents and audit independence | ✅ Resolved |
| D14 | Enforcing the surface map in CI | ✅ Resolved |
| D15 | PR #2 readiness and merge timing | ✅ Resolved |
| D16 | Repo visibility versus marketplace distribution | ✅ Resolved |

---

## D1. Import scope from discovered collections — ✅ Resolved

Five MIT-licensed skill collections were found across the account's own repositories, holding 106
skills between them.

- **(a) Curated subset** — take the non-overlapping, highest-quality skills. ← **chosen**
- (b) Everything, namespaced by source.
- (c) Engineering and org layer only.
- (d) Inventory first, decide later.

**Resolution:** (a). 84 of 106 taken; 22 skipped as duplicates, superseded variants,
author-personalized, or intrusive meta-skills.

---

## D2. Organizational structure — ✅ Resolved

How to structure the org as it grew past ~100 skills, given that every skill's description loads
into context.

- **(a) Departments as separate plugins**, enabled per project. ← **chosen**
- (b) Flat `.claude/skills/`.
- (c) Subdirectories for human organization only (no context saving).
- (d) Defer until volume hurts.

**Resolution:** (a), later extended into a C-suite hierarchy: a chief executive over eleven
departments, each an independently installable plugin.

---

## D3. Handling of third-party licensed content — ✅ Resolved

MIT requires the copyright notice be retained in copies and substantial portions. The repository is
a marketplace intended to be installed, which is distribution.

- (a) Keep the notices in each department's `licenses/`.
- **(b) Rewrite every affected skill from scratch, then remove the originals and their notices
  entirely.** ← **chosen**
- (c) Paraphrase — rejected as the worst option: still derivative, still requires attribution, and
  degrades the content.

**Resolution:** (b). All 77 vendored skills, their references, datasets, font binaries, and license
files removed; capabilities re-authored. A clean-room audit returns nothing for license text,
notices, SPDX tags, upstream names, or vendored assets.

**Known consequence:** part of what was removed was *data*, not prose — a bundled style/palette
database and licensed font binaries. Those cannot be re-authored, so the replacement design skills
teach method rather than shipping a dataset. This is a real capability reduction, accepted
knowingly.

---

## D4. Rewrite-before-purge ordering — ✅ Resolved

The first execution of D3 deleted the originals and then wrote replacements from a catalogue of
names and descriptions, so coverage was never verified against actual content.

**Resolution:** Corrected. All 100 superseded skills were restored from git history to a scratch
directory and audited against their successors. Every original maps to one; six had lost real
substance and were patched — site performance and Core Web Vitals, lead scoring, SMS consent law,
dark-mode and accessibility, campaign naming. One capability (applied behavioral science) had no
home and became `marketing:behavioral-marketing`.

**Standing rule adopted:** never delete a source before the replacement has been diffed against it.

---

## D5. Vendored content remaining in branch history — ✅ Resolved

The working tree is clean, but commits `36d1be3`, `d091eac`, and `cd1cd22` on
`claude/import-agents-drive-gmci3h` each still contain ~103 licensed paths. `main` is unaffected —
PR #1 only ever carried the 12 Drive-sourced skills.

- **(a) Squash-merge PR #2.** `main` gets one clean commit. Non-destructive, PR review trail intact.
  The branch history survives on GitHub until the branch is deleted. ← **recommended**
- (b) Rebuild the branch as a single commit and force-push. Actually satisfies "remove entirely" —
  the old commits become unreferenced. Cost: dangles the PR's commit list and any review threads
  anchored to those commits.
- (c) Leave it. The content is MIT and was lawfully obtained; history is an accurate record.

**Recommendation: (a), then delete the branch after merge.** That reaches the same end state as (b)
without destroying the review trail, since deleting the merged branch unreferences the commits
anyway. Choose (b) only if you want them gone before merge.

**Resolution: (a).** Squash-merge PR #2, then delete the branch — the merged branch's deletion
unreferences the three commits carrying vendored paths.

---

## D6. Provenance of the 12 Drive-sourced skills — ✅ Resolved

Twelve skills came from the shared Drive folder "12 ready-to-use Claude Skills that turn Claude into
your own AI team," owned by an unfamiliar Gmail account. They carry **no licence and no stated terms**,
and they were never rewritten — they are the only skills in the repository that are not original work.

They are already merged to `main` via PR #1, and they sit in six departments: `ceo-advisor`,
`business-growth-consultant`, `saas-idea-validator`, `ai-research-analyst`, `ai-workflow-architect`,
`prompt-optimizer`, `chief-content-officer`, `marketing-campaign-planner`, `newsletter-writer`,
`landing-page-cro-expert`, `youtube-producer`, `ux-product-auditor`.

This matters because the whole point of D3 was to remove third-party licensed content. No licence is
a *weaker* position than MIT, not a stronger one: MIT grants redistribution rights explicitly, while
absent terms grant nothing. If that folder is someone's paid product, the repository currently
redistributes it.

- (a) Leave them. They were shared with you; treat that as permission.
- **(b) Rewrite all twelve from scratch**, the same treatment the MIT collections got. Removes the
  question entirely and fixes a second problem — they are the only skills not in the house voice, so
  the repo currently reads as two documents. ← **recommended**
- (c) Establish provenance first — find where the folder came from and what terms applied — then
  decide.
- (d) Remove them without replacement.

**Recommendation: (b).** It resolves the licensing question, the voice inconsistency, and the
quality variance in one pass, and it is the only option that does not depend on an answer you may
not be able to get. Roughly a day of work. If you know the folder's origin and the terms are
permissive, (a) becomes reasonable — but say so explicitly so it is recorded.

**Resolution: (b).** Rewrite all twelve from scratch, the same treatment the MIT collections
received. Removes the unlicensed content, brings them into the house voice, and unblocks D15 and D16.

---

## D7. Audience for vertical variants — ✅ Resolved

Whether industry variants (healthcare, manufacturing, retail, food & beverage, financial, services)
are for your own businesses or are products handed to clients.

- **(a) Own use** across your businesses. ← **recommended as the working assumption**
- (b) Distributed products sold or delivered to clients in each vertical.
- (c) Both — internal first, productized later.

**Recommendation: (a) as the assumption until you say otherwise**, because it is the reversible one.
An overlay architecture built for own use can be packaged into standalone deliverables later; a
generator built for distribution is heavier than internal use warrants. Answer this before D8 — it
changes the recommendation there.

**Resolution: (c) — both, internal first.** Build for own use now; treat productization as a later
decision rather than designing for both up front. D8 therefore resolves to overlays, with the
constraint that overlay content must stay packageable into standalone deliverables later: no
cross-vertical references inside an overlay, and no assumption that sibling overlays are installed.

---

## D8. Architecture for vertical variants — ✅ Resolved

Roughly 60% of the current 80 skills are vertical-neutral, 30% keep their shape but need
vertical-specific content, and 10% would be genuinely new per vertical.

- (a) **Fork per vertical.** Simple to start; every core improvement must then be applied N times,
  and the copies diverge into unrelated repos within a quarter.
- **(b) Core plus thin overlays.** Core stays generic and single-copy. Each vertical is a small
  plugin holding (i) genuinely vertical-only skills and (ii) context files that core skills read
  when present, so `privacy-and-data-protection` stays one file and gains HIPAA behavior under the
  healthcare overlay. ← **recommended**
- (c) **Template plus generator.** A per-vertical config emits a standalone repo. Right if variants
  must ship without revealing the others; requires one-way generation and never hand-editing output.

**Recommendation: (b) if D7 is (a); (c) if D7 is (b).** This matches §11(B) of the
`executive:agent-hierarchy` playbook — publish-and-consume with a pinned core version — and its rule
that a core export is never removed because it looks unused applies from the second vertical onward.

**Suggested first step either way:** build one healthcare overlay against the current core and
measure how much of that middle 30% genuinely needs context files. A few hours, and it validates the
model before eight verticals depend on it.

**Resolution: (c) — template plus generator, built now.** Chosen over the recommended overlay model
because productization is planned (D7c) and this avoids migrating from overlays to a generator
later.

**What this commits to.** Generation must be one-way: the core plus a per-vertical config emits a
standalone repo, and generated output is **never hand-edited** — an edit made downstream is lost on
the next generation, silently. Every vertical change goes into the config or the core. This is
heavier up front than overlays and the discipline is the whole cost; a generator whose outputs get
edited is worse than a fork, because the divergence is invisible.

---

## D9. Security as its own department — ✅ Resolved

There are currently zero security skills. `legal-risk` covers governance, risk, and audit readiness
but no technical security work.

- (a) Add security skills under `technology`.
- **(b) Create a `security` department with its own CISO charter.** ← **recommended**
- (c) Extend `legal-risk` to cover technical security.

**Recommendation: (b).** At Fortune 500 scale the CISO reports independently precisely so security
can overrule engineering; modeling it under the CTO reproduces the conflict the role exists to
prevent. First skills: `threat-modeling`, `security-architecture-review`, `incident-response`,
`vulnerability-management`, `access-and-identity`.

**Resolution: (a).** A `security` department with its own CISO charter, reporting independently
rather than under the CTO.

---

## D10. Which department to deepen next — ✅ Resolved

Four departments have three specialists each; `administration` has none.

- (a) **Security** — the largest absolute gap. (Depends on D9.)
- (b) **Finance** — add procurement, investment analysis, cash management, revenue recognition,
  financial controls.
- (c) **People** — add performance management, employee relations, L&D, workforce planning.
- (d) **Legal** — add IP and licensing, regulatory compliance, audit readiness, corporate governance.
- (e) **Operations** — add supply-chain planning, quality management, capacity planning.

**Recommendation: (a) then (e).** Security is the biggest hole. Operations comes next because it is
the department your own businesses most immediately need — print, fulfillment, and production
work — and because it is the department most reused by the manufacturing and food verticals in D8.

**Resolution: all four, in this order — Security, Operations, Finance, People.** Security first as
the largest absolute gap; Operations second as the department your own businesses most need and the
one most reused by the manufacturing and food verticals.

---

## D11. Cross-org sweep of public repos — ✅ Resolved

`Keel-GRC` and `Drummond-IT` cannot be *attached* to this session (one-owner limit), but their
**public** repositories are readable here by anonymous clone. Verified against
`Keel-GRC/Claude-Skills-Governance-Risk-and-Compliance`.

Public and likely to hold material: `Claude-Skills-Governance-Risk-and-Compliance`,
`automotive-skills-suite`, `claude-grc-engineering`, `claude-grc-plugin`, `llm-iso27001`,
`evidence-fetchers`, and `Drummond-IT/enfocus-switch-script-skill`.

- (a) Sweep them now and propose a `compliance` department.
- **(b) Sweep and catalogue only** — report what is there, import nothing until D6 is settled. ←
  **recommended**
- (c) Defer entirely.
- (d) Also run the private/internal sweep via `docs/cross-org-sweep-prompt.md`.

**Recommendation: (b).** The catalogue is cheap and informs D8 and D10. Importing anything before D6
is resolved would repeat the exact mistake D3 and D4 were about — and these are forks of
third-party work, so the same licensing question applies to all of them.

**Resolution: (d).** Catalogue the public repos from this session, and additionally start a separate
session against `Keel-GRC` to sweep private and internal repos per `docs/cross-org-sweep-prompt.md`.

**Constraint carried forward:** catalogue only. Nothing from either sweep is imported until its
licensing is established, since these are forks of third-party work and D3 and D6 both turned on
exactly that question.

---

## D12. Administration department disposition — ✅ Resolved

`administration` holds one charter and no specialists. It exists so orphaned responsibilities have
an owner.

- (a) Keep as a placeholder.
- (b) Staff it — corporate records, board support, insurance and continuity, workplace.
- **(c) Fold into `legal-risk` and `executive`**, and delete the department. ← **recommended**

**Recommendation: (c) for now.** At your scale corporate governance sits naturally with Legal & Risk
and board support with the CEO's office. An empty department installed for one charter is overhead.
Revisit if the corporate-secretary function becomes real.

**Resolution: (c).** Fold corporate governance into `legal-risk` and board support into `executive`,
then delete the `administration` department.

---

## D13. Reviewer-class agents and audit independence — ✅ Resolved

The `executive:agent-hierarchy` skill requires that producer and auditor are never the same agent.
The current chart violates it: every department reviews its own work.

- (a) Accept it for now.
- **(b) Designate reviewer-class departments** — `legal-risk`, and `security` if D9 is (b) — whose
  charters explicitly cannot be overruled by the department they are reviewing. ← **recommended**
- (c) Add a separate `internal-audit` department reporting to a board/audit-committee construct
  rather than to the Chief Executive.

**Recommendation: (b) now, (c) later.** (b) is a charter edit and costs nothing. (c) matters once
there is real audit activity — and note that if it is ever added, placing it under `executive` would
reproduce the independence failure it exists to prevent.

**Resolution: (b).** Mark `legal-risk` and the new `security` department reviewer-class in their
charters — explicitly not overrulable by the department under review. Internal audit deferred until
there is real audit activity; if added, it must not report to the Chief Executive.

---

## D14. Enforcing the surface map in CI — ✅ Resolved

`executive:agent-hierarchy/scripts/agent-guard.mjs` is present and runs, but nothing invokes it and
no surface map exists. The playbook's own position is that an unenforced map is a suggestion.

- (a) Leave it as reference material.
- **(b) Write `docs/AGENT-SURFACES.md` mapping each department to its exclusive path glob, and run
  `agent-guard check` in CI.** ← **recommended**
- (c) Also run `agent-guard diff` per change.

**Recommendation: (b).** The department layout already is a surface map — each department owns
`plugins/<dept>/**` and nothing else — so writing it down is close to free, and it becomes load-bearing
the moment more than one session edits this repo. Note the repo has no CI workflows at all yet, so
this also means adding the first one.

**Resolution: (b).** Write `docs/AGENT-SURFACES.md` mapping each department to its exclusive glob and
run `agent-guard check` in CI. This adds the repository's first CI workflow.

---

## D15. PR #2 readiness and merge timing — ✅ Resolved

PR #2 is a draft: 80 skills, eleven departments, merges cleanly, no CI configured, no review threads.

- (a) Mark ready and merge now; treat D6 as follow-up work.
- **(b) Resolve D6 first**, then mark ready and merge. ← **recommended**
- (c) Keep as a draft while D7–D10 are decided, and merge one larger change.

**Recommendation: (b).** D6 is the only open item that changes files already in this PR's scope.
D7–D14 are all new work that belongs in later PRs — holding this one open for them means a
1,000-file review nobody can do properly.

**Resolution: (b).** Resolve D6 first, then mark ready and merge. D6 is the only open item touching
files already in this PR's scope.

---

## D16. Repo visibility versus marketplace distribution — ✅ Resolved

`cbrock84/agents-v1` is **private**, but the README instructs `/plugin marketplace add
cbrock84/agents-v1`. A private marketplace requires each installing machine to be authenticated to
this repository, which the instructions do not mention.

- (a) Keep private, and document the authentication requirement in the README.
- (b) Make the repository public. Note that this would publish the D6 skills, whose terms are
  unknown — do not choose this before D6 is resolved.
- **(c) Keep private now, decide visibility after D6 and D7.** ← **recommended**

**Recommendation: (c), with the README corrected immediately** either way, since it currently
documents an install path that will fail for anyone but you.

**Resolution: (c).** Stay private until the twelve rewritten skills land, then revisit. The README
already states the authentication requirement. Note that if D8's generator becomes the distribution
path, the per-vertical repos rather than this one may be the artifact that needs to be public.

---

# Work queue

Derived from the resolutions above, in dependency order. This is the execution plan, not a new set
of decisions.

| # | Work | From | Blocks | Status |
|---|---|---|---|---|
| 1 | Rewrite the 12 Drive-sourced skills from scratch | D6 | D15, D16 | ✅ done |
| 2 | Fold `administration` into `legal-risk` + `executive`; delete the department | D12 | — | ✅ done |
| 3 | Mark `legal-risk` reviewer-class in its charter | D13 | — | ✅ done |
| 4 | Write `docs/AGENT-SURFACES.md`; add first CI workflow running `agent-guard check` | D14 | — | ✅ done |
| 5 | Mark PR #2 ready; squash-merge; delete the branch | D5, D15 | 6+ |
| 6 | Build `security` department + CISO charter, marked reviewer-class | D9, D10, D13 | — |
| 7 | Deepen `operations`, then `finance`, then `people` | D10 | — |
| 8 | Catalogue public Keel-GRC and Drummond repos — no import | D11 | — |
| 9 | Start a separate session against Keel-GRC for the private sweep | D11 | — |
| 10 | Build the vertical generator: core, per-vertical config, one-way emit | D8 | — |
| 11 | Revisit repo visibility | D16 | after 1 |

Items 1–4 can proceed in parallel; all four land before item 5. Item 9 needs a session started
outside this one — see `docs/cross-org-sweep-prompt.md`.
