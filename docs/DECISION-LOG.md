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

The first execution of D3 deleted the originals and then wrote replacements from a catalog of
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

**Resolution: (a) — done.** PR #2 squash-merged as `cc77e22`; branch deleted. `main` carries a single
clean commit, and no licensed path was ever added on `main` across its whole history. The three
commits carrying the vendored tree are unreachable.

---

## D6. Provenance of the 12 Drive-sourced skills — ✅ Resolved

Twelve skills came from the shared Drive folder "12 ready-to-use Claude Skills that turn Claude into
your own AI team," owned by an unfamiliar Gmail account. They carry **no license and no stated terms**,
and they were never rewritten — they are the only skills in the repository that are not original work.

They are already merged to `main` via PR #1, and they sit in six departments: `ceo-advisor`,
`business-growth-consultant`, `saas-idea-validator`, `ai-research-analyst`, `ai-workflow-architect`,
`prompt-optimizer`, `chief-content-officer`, `marketing-campaign-planner`, `newsletter-writer`,
`landing-page-cro-expert`, `youtube-producer`, `ux-product-auditor`.

This matters because the whole point of D3 was to remove third-party licensed content. No license is
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

Two other organizations I have access to cannot be *attached* to this session (one-owner limit), but their
**public** repositories are readable here by anonymous clone. Verified against
`one of their public repositories`.

Public and likely to hold material: `a governance and compliance skill set`,
`an industry skills suite`, `GRC engineering`, `a GRC plugin`, `ISO 27001 tooling`,
`evidence collection`, and `a workflow-automation script skill`.

- (a) Sweep them now and propose a `compliance` department.
- **(b) Sweep and catalog only** — report what is there, import nothing until D6 is settled. ←
  **recommended**
- (c) Defer entirely.
- (d) Also run the private/internal sweep via `docs/cross-org-sweep-prompt.md`.

**Recommendation: (b).** The catalog is cheap and informs D8 and D10. Importing anything before D6
is resolved would repeat the exact mistake D3 and D4 were about — and these are forks of
third-party work, so the same licensing question applies to all of them.

**Resolution: (d).** Catalog the public repos from this session, and additionally start a separate
separate session to sweep private and internal repositories per `docs/cross-org-sweep-prompt.md`.

**Constraint carried forward:** catalog only. Nothing from either sweep is imported until its
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

`cbrock84/headcount` is **private**, but the README instructs `/plugin marketplace add
cbrock84/headcount`. A private marketplace requires each installing machine to be authenticated to
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
| 5 | Mark PR #2 ready; squash-merge; delete the branch | D5, D15 | 6+ | ✅ done |
| 6 | Build `security` department + CISO charter, marked reviewer-class | D9, D10, D13 | — | ✅ done |
| 7 | Deepen `operations`, then `finance`, then `people` | D10 | — | |
| 8 | Catalog the other organizations' public repos — no import | D11 | — | |
| 9 | Start a separate session for the private sweep | D11 | — | |
| 10 | Build the vertical generator: core, per-vertical config, one-way emit | D8 | — | |
| 11 | Revisit repo visibility | D16 | after 1 | ✅ done |

Items 1–4 can proceed in parallel; all four land before item 5. Item 9 needs a session started
outside this one — see `docs/cross-org-sweep-prompt.md`.

---

# Open decisions

Raised after the first sixteen were resolved. Same convention: numbers are addresses, assigned when
asked.

## D17. Which department is the next real gap — ✅ Resolved

With `security` built, the catalog covers eleven departments. Three functions a Fortune 500 has
that this does not:

- **(a) Customer Experience / Support.** Every business has support; the catalog has none.
  `revenue:retention` is the only adjacent skill. Needed: support operations, escalation handling,
  voice-of-customer, service-level design. ← **recommended**
- (b) **Data & Analytics (CDO).** `demand-generation:marketing-analytics` covers marketing
  measurement only. No data governance, warehouse modeling, BI, or AI/ML governance — the last is
  increasingly a board obligation.
- (c) **Corporate Strategy / Corp Dev.** M&A, diligence, scenario planning, competitive war-gaming.
- (d) None — deepen the eleven that exist instead.

**Recommendation: (a), then (b).** Support is the most conspicuous absence to anyone reading the
catalog — it is the department every company has and this one does not. Data & Analytics is the
one most likely to be expected of a modern org chart. Corp Dev is real but only bites at a scale
this repo's likely users have not reached.

**Resolution: all three, treated as equally important.** `customer-experience`, `data-analytics`,
and `corporate-strategy` built together, five skills each. Fourteen departments, 101 skills.

## D18. Repository visibility, now that all content is original — ✅ Resolved

D16 deferred this until the rewrite landed. It has. Nothing in the repository now carries a
third-party obligation, and `scripts/check-provenance.py` fails the build if that changes.

- **(a) Make it public under MIT.** The install path in the README then works for anyone. ←
  **recommended**
- (b) Stay private and document the authentication requirement.
- (c) Public, but wait until the vertical generator (D8) decides whether per-vertical repos are the
  distributed artifact instead.

**Recommendation: (a).** The blocker was provenance and it is resolved. Publishing does not commit
you on D8 — a generator can emit per-vertical repos later regardless of whether this one is public.

**Resolution: (a).** `cbrock84/headcount` is public under MIT as of 29 August 2026, confirmed via the
API (`visibility: public`). This also closes work-queue item 11, which existed only to revisit this.

**What publishing actually changed.** The install path in the README now resolves for anyone — under
D16 it required every installing machine to be authenticated to the account, which made the
documented instructions untrue for everybody except the owner. That gap is closed.

**Still unverified.** Nothing in this session can run `/plugin marketplace add` against a clean
client, so the manifest is verified only up to "it parses and every referenced path exists". The
first genuine test is an install from a machine that has never seen this repository.

## D19. README drift — ✅ Resolved

`scripts/build-readme.py` regenerates the README from the tree, and `check-all.sh` fails if it is
stale. This works but means the README cannot be hand-edited.

- **(a) Keep generation, edit the generator.** ← **recommended**
- (b) Generate only the tables, hand-write the prose around them.
- (c) Drop generation; accept that counts drift.

**Recommendation: (a) for now, (b) if the prose starts wanting per-section nuance the generator makes
awkward.** The failure this prevents is real: the README claimed eleven departments and listed a
deleted one for two commits before it was caught by hand.

**Resolution: (a), and the scope of generation has since widened twice.** The org chart's department
table was moved inside generated markers after it drifted the same way, and the badge counts in the
README header are now emitted from the same tree walk that builds the tables — so a wrong count is a
CI failure rather than something a reader has to notice.

The generator was also hardened after review: it discovers departments from the plugin tree instead
of a hand-maintained list, and refuses to run when a department on disk has no display metadata. The
earlier design would have omitted a new department from both documents while `--check` still passed,
because it compared the files against output from the same incomplete list.

**(b) remains the fallback** if the prose ever wants per-section nuance that the generator makes
awkward. Nothing about that has changed.

## D20. Publishing steps that need your hands — ✅ Resolved

Repository settings are not reachable from this session — no tool exposes topics, description, or
merge defaults, and the git proxy blocks branch deletion. These are yours to click.

- (a) Do them all now, before going public.
- **(b) Do the four that affect discoverability and hygiene now; treat the profile README as
  optional.** ← **recommended**
- (c) Publish first, tidy later.

The list, in order of value:

1. **Topics** — `claude-code`, `claude-skills`, `ai-agents`, `agent-marketplace`, `claude-plugins`.
   This is how anyone finds it, and it is the step most often skipped.
2. **About** — one line plus the repo URL. Suggested: *"An agent organization for Claude Code: a
   C-suite of 14 departments and 101 skills, installable per department."*
3. **Settings → General → Automatically delete head branches.** Three merged branches have needed
   manual deletion so far.
4. **Default merge to squash**, if you want one commit per change on `main`. #3 came in as a merge
   commit.
5. *Optional:* pin the repo on your profile, and a `cbrock84/cbrock84` profile README featuring it.

**Recommendation: (b).** 1–3 matter; 4 is preference; 5 is worth doing only if you want the profile
to lead with this.

**Resolution: (b), executed 29 August 2026.** Repository renamed to `headcount` (D22), made public,
description set, automatic head-branch deletion enabled, and the four stale merged branches deleted.
`origin/main` is now the only remote branch.

**One item outstanding, carried to D23:** topics are still empty. Verified via the API — the
repository returns no topics array. This is the item the entry above called "the step most often
skipped", and it was skipped, for a findable reason: **topics are not in Settings.** They live behind
the gear icon on the About panel of the repository home page, which is where nobody looks for a
setting. Noted here because the same confusion will recur on every vertical repo D8 emits.

## D21. MIT or Apache-2.0 for the long term — ✅ Resolved

Raised while preparing to publish. Apache-2.0 is the usual alternative to MIT for a project intended
for wide reuse.

**What Apache-2.0 adds over MIT:** an explicit patent grant with a retaliation clause, an explicit
trademark carve-out, a requirement that modified files carry a notice of change, and automatic terms
for inbound contributions.

- **(a) MIT.** ← **chosen**
- (b) Apache-2.0.
- (c) A content license such as CC-BY-4.0.
- (d) Dual — CC-BY for the prose, MIT for the scripts.

**Resolution: (a).** The reasoning, recorded so it is not re-litigated:

- **The patent grant is Apache's headline feature and is near-irrelevant here.** This repository is
  markdown. Instructions for running a threat model or a CRO audit are not patentable subject matter
  in any practical sense, so the protection Apache exists to provide has almost nothing to attach to.
- **Apache §4(b) is active friction for the intended use.** It requires modified files to carry
  prominent change notices. The whole design is people installing a department and adapting it; MIT
  lets them, Apache asks them to annotate every file they touch.
- **MIT is the ecosystem norm.** Every collection this repository originally drew from was MIT, and
  the Claude skills and plugins ecosystem is MIT by convention. Lower friction, fewer legal reviews.
- **Short licenses get complied with.** Two hundred lines of license on a prose repository invites
  the question of whether anyone read it.
- **(c) and (d) rejected:** Creative Commons explicitly advises against using CC for software, this
  repository contains executable scripts alongside the prose, and a split license confuses tooling
  and adopters for no practical gain.

**The one real gap MIT leaves** — what license inbound contributions carry — is closed by
`CONTRIBUTING.md` stating that contributions are accepted under MIT, rather than by changing the
license.

**Timing note, which is the part that matters later.** Relicensing is clean only while there is a
single copyright holder. Once outside contributions land under MIT, you cannot retroactively un-MIT
what has been published; you would be layering Apache over MIT-licensed parts, which is lawful but
messy. So this decision is cheap to reverse **today** and expensive to reverse after the first
external pull request.

**Revisit if** the repository grows substantial executable code — the vertical generator in D8 is the
plausible candidate — or if a corporate adopter's legal team specifically asks for the patent grant.
Neither is true now.

**Not legal advice.** For the productized vertical variants contemplated in D8, where money and
third-party distribution are involved, this is worth qualified counsel rather than a decision log.

---

## D22. What to call this — ✅ Resolved

`agents-v1` was a working title. It describes the mechanism (agents) and a version number, neither of
which is a name, and it was about to be published — at which point the name stops being free to
change.

The binding constraint is not aesthetics. It is that the brand appears **after an `@` in every
install command**:

```
/plugin marketplace add cbrock84/NAME
/plugin install security@NAME
```

`security@NAME` renders as a corporate email address. That is free explanation of the whole product,
but only for a name that reads like a company. It rules out descriptive multi-word names.

- **(a) `headcount`.** ← **chosen**
- (b) `holdco` — a holding company holds operating subsidiaries; this holds installable departments.
  Structurally exact, and less likely to collide with an existing product.
- (c) `boardroom`, `roster`, `charter`, `quorum` — all read as companies; each is either semantically
  off (a boardroom is the board, not the operating org) or heavily used elsewhere.
- (d) `company-in-a-box` and relatives — say exactly what it is, but are not distinctive and destroy
  the `@` construction.
- (e) Keep `agents-v1`.

**Resolution: (a).**

- **It names the benefit, not the mechanism.** "101 markdown skills in a plugin marketplace" is what
  it is made of. "Headcount" is what someone wants: a CISO, a CFO, a growth lead, without the req.
- **The install string becomes the tagline.** `/plugin install security@headcount` reads as hiring a
  security department. Nothing further needs explaining.
- **It survives D8.** Generated verticals are `headcount-health`, `headcount-retail`,
  `headcount-industrial` — which parse as staffing firms with a specialty. The metaphor strengthens
  as it is cloned, which is unusual and worth the points.

**This sets the vertical naming convention for D8**, whose resolution (c) emits standalone repos:
each generated vertical is `headcount-<vertical>`, and the generator's per-vertical config carries
the suffix. Recorded here so the generator is not built against a different scheme.

**Name-collision caveat, not resolved by this entry.** `headcount` is a common noun in HR software
and this log is not a trademark search. The check is worth doing before any commercial use of the
D7/D8 productized variants; for an MIT repository under a personal account the exposure is low.
`holdco` (b) remains the fallback if a conflict surfaces, and is a cheap swap while the name is
young — the same timing logic as D21.

**Timing.** Renaming cost one commit here. After publication the install string gets copied into
config files, posts and screenshots that never update — GitHub redirects renamed repositories, but
it cannot rewrite what people have already pasted elsewhere. This was the last moment it was free.

---

## D23. Buttoning up the repository now that it is public — ✅ Resolved

Going public changes the threat model and the audience. Anyone can now fork, open a pull request
that runs CI, and judge the project in about four seconds of looking at the landing page.

- **(a) Presentation and hardening together, now.** ← **chosen**
- (b) Presentation now, hardening when there is actual traffic.
- (c) Neither; the repository is fine as it is.

**Resolution: (a).** Both are cheap, and the hardening items are the kind that are embarrassing to
add after an incident rather than before one.

**Presentation — done in this change.**

The README now opens with a centered title, the tagline, and a badge row: built-for Claude Code,
department count, skill count, license, and PRs-welcome. **The counts are generated from the same
tree walk that builds the tables**, so they are covered by the existing staleness check — a badge
claiming the wrong number fails CI. A hand-typed badge would have become a lie on the next
department, which is precisely the D19 failure in a more visible place.

**`.gitattributes` added.** GitHub labeled the repository *JavaScript* on the strength of a single
`.mjs` guard script, against 101 markdown skills that are the actual product. Linguist counts bytes
of code and does not know what a repository is for. The attributes file marks tooling as vendored
and generated documents as generated, so the language bar reflects the deliverable.

**Hardening — done in this change.**

- **Explicit `permissions: contents: read` on the workflow.** It only reads the tree and runs
  checks. Public repositories accept pull requests from forks, and being explicit means a permissive
  account-level default cannot hand a write-scoped token to a workflow triggered by a stranger.
- **Push trigger narrowed from `["**"]` to `[main]`.** Every push was running the workflow twice —
  once for the push, once for the pull request, on the same commit. Pure waste either way.
- **Deprecated actions bumped.** The first green run warned that `actions/checkout@v4` and
  `actions/setup-node@v4` run on Node 20, which is being force-migrated to Node 24. Both are now at
  v7, with `node-version` at 24. Versions were checked against the actions' own release pages rather
  than assumed — the guess would have been v5, and both are three majors further on than that.

**The CI blackout ended, and not for the reason recorded.** Every run from 28 August onward failed in
three to four seconds with no steps and empty output, on this repository and on `main` alike. That
was diagnosed as exhausted Actions minutes, with the fix being the 1 September quota reset. The
minutes were genuinely exhausted, but the reset was never the fix: **GitHub Actions is free and
unlimited for public repositories on standard runners** (GitHub's own billing documentation:
"GitHub Actions usage is free for self-hosted runners and for public repositories that use standard
GitHub-hosted runners"). Making the repository public under D18 ended the blackout immediately —
the first run after publishing went green in eight seconds, executing all five checks.

Worth recording because the wrong lesson was nearly banked. The blackout was treated as an external
constraint to wait out, and `scripts/check-all.sh` was built to decouple verification from CI while
it lasted. That script earns its place regardless. But the constraint was a consequence of a setting
this project had already decided to change, and nobody connected the two for a full day.

**Deliberately not done.**

- **Dependabot.** There are no dependency manifests — no `package.json`, no `requirements.txt`.
  It would have nothing to scan, and enabling it would only add a quiet integration that never fires.
- **Branch protection requiring approvals.** With a single maintainer, required approvals block the
  only person who can approve. A ruleset requiring a pull request into `main`, with the owner as a
  bypass actor, is the right shape if drive-by pushes ever become a concern; it is not one yet.

**Left to the owner** (settings are not reachable from an agent session — see D20): topics, secret
scanning with push protection, and turning off the unused Wiki and Projects tabs.

---

## D24. Whether to add sponsorship — ✅ Resolved

GitHub Sponsors would put a **Sponsor** button on the repository, driven by `.github/FUNDING.yml`.

- (a) Enrol and add `FUNDING.yml` now, with the repository.
- **(b) Not yet — revisit at a real usage signal.** ← **chosen**
- (c) Never; keep it a pure gift.

**Resolution: (b).** Not on principle — the timing is simply wrong, and the cost of asking early is
not zero.

- **There is nothing to sponsor yet.** One star, no external installs, no issues, published today.
  A funding ask is a claim that ongoing maintenance has value to someone; that claim is currently
  unevidenced, and a reader can tell.
- **It changes how the first impression reads.** A brand-new repository leading with a payment link
  invites the question of whether the catalog was assembled to be monetised. That is a costly
  question to raise while the provenance story — 101 skills written from scratch after removing
  every vendored collection — is the thing worth the reader's attention.
- **It is thirty seconds whenever you want it.** Enrol at `github.com/sponsors`, then a two-line
  `.github/FUNDING.yml` with `github: [cbrock84]`. Nothing about deferring makes it harder later.

**The signal to revisit:** external installs, inbound issues from people who are not you, or a fork
that gets used. Any one of those makes the ask legible. **Revisit sooner** if the D7/D8 vertical
variants become a commercial product — that is a different question (pricing, not donations) and
deserves its own entry rather than a sponsor button.

---

## D25. Whether to register a domain for the About field — ✅ Resolved

GitHub's About panel has a Website field. The available domains were `headcount.biz`,
`headcount.info` and similar — the short, conventional ones are gone.

- (a) Register a cheap available TLD (`.biz`, `.info`) and link it now.
- **(b) Leave the Website field empty; revisit when there is something to point at.** ←
  **chosen**
- (c) Register `headcount.dev` if free and hold it unused against later need.
- (d) Point the Website field at a GitHub Pages site built from this repository.

**Resolution: (b), with (c) as a cheap optional hedge.**

- **`.biz` and `.info` are negative signals to this audience.** They are the TLDs of parked
  pages and expired-domain farms. Someone deciding whether to install 101 skills into their
  agent is making a trust judgment, and that domain in the About field reads worse than a blank
  field. A rare case where the cheap option is worse than nothing rather than merely weaker.
- **A domain does not serve this product yet.** Installation is `/plugin marketplace add
  cbrock84/headcount`, typed inside Claude Code. Discovery runs through repository topics, the
  plugin ecosystem, and word of mouth — none of which route through a domain. Nobody searches
  the web for "headcount" and finds an agent marketplace; they find HR software.
- **A link has to point at something.** A redirect to the repository adds a hop for no gain, and
  a parked domain is a worse signal than an empty field. (d) has the same problem until there is
  documentation that does not fit in the README.

**The part worth keeping.** That the short TLDs are gone is *evidence for the collision caveat
already recorded in D22*, discovered by accident. `headcount` is a common noun in HR software,
and the domain market is confirming how crowded that space is. The name remains right for a
repository, where the namespace is `cbrock84/headcount` and collision costs nothing — but **do
not build an identity that depends on owning the word.** Accepting a degraded TLD would be
exactly that mistake in miniature.

**Revisit when** the D7/D8 vertical variants become something distributed or sold. That is a real
product with a reason for a hub, and it is the same moment the trademark question in D22 needs a
proper answer rather than a caveat. Prefer `.dev` then — correct signal for developer tooling and
HTTPS-only — or a modified name over a degraded TLD.

---

## D26. Where project management lives — ✅ Resolved

Project management existed only as a single `program-management` skill inside `operations`. The
question raised was whether
discipline belongs in silos inside each department or as an enterprise function.

- (a) **Siloed.** Each department carries its own project management guidance.
- (b) **Inside `operations`.** Expand the COO's department to hold the discipline.
- **(c) A separate `pmo` department reporting to the COO.** ← **chosen**

**Resolution: (c).**

- **(a) fails this repository's founding rule.** `executive:agent-hierarchy` splits by exclusive
  write surface, not by topic. Project management is a topic crossing all sixteen departments, so
  siloing it produces sixteen near-identical skills — precisely the duplication that forced the
  earlier consolidation.
- **(c) over (b) on installability.** The premise of the marketplace is installing only what you
  need. Someone who wants portfolio governance and stage gates should not have to take
  `supply-chain-and-logistics` and `vendor-management` with it. An EPMO is also a distinct function
  in practice, with its own head, rather than a subset of operations.

**The `program-management` skill moved from `operations` to `pmo:program-management`.** Worth doing
at this moment specifically: the repository published today with no external installs, so the
address is still free
to change. Once someone has the department installed and the address referenced, it is not — the same
timing logic as the rename in D22 and the license in D21. Verified no reference to the old address
survives anywhere in the tree.

**Reporting line: the COO**, reflected in the org chart. The EPMO governs delivery across the
organization; it does not own the functions whose work it governs.

**Boundaries stated in the skills rather than left to collide.** `pmo:portfolio-governance` handles
resource contention across projects while `operations:capacity-and-demand-planning` handles
operational throughput; `pmo:dependency-and-risk-management` handles delivery risk while
`legal-risk:enterprise-risk` owns the enterprise framework.

---

## D27. Splitting CIO-side IT operations out of `technology` — ✅ Resolved

`technology` was labeled "CTO / CIO" and held twelve skills, all of them software development
workflow. The request to add help desk, network administration and system administration forced the
question of whether those belong in the same department.

- (a) **Add them to `technology`.** One department, around twenty-five skills.
- **(b) Split: `technology` for the CTO side, a new `it-operations` for the CIO side.** ← **chosen**
- (c) Leave corporate IT out of the catalog.

**Resolution: (b).**

- **They are different functions with different audiences.** Product engineering and corporate IT
  share a reporting line in some organizations and almost nothing else. Bundled, a SaaS engineering
  team installing `technology` receives deskside support skills it will never open, and an IT
  director receives worktree workflow they will never open. The split is what makes both installable
  without noise.
- **The combined "CTO / CIO" label was papering over a real division**, and the catalog was
  honest about only one half of it.

**What moved where.** `technology` gained `solution-architecture`, `api-design`,
`technical-debt-management`, `cloud-infrastructure`, `observability-and-reliability` and
`release-and-deployment`, reaching eighteen. `it-operations` is new with seven. `data-engineering`
went to `data-analytics` rather than `technology`, because pipelines belong beside `data-modeling`
and `data-governance` under the CDO.

**Overlaps resolved explicitly inside the skills**, since unstated boundaries are what forced the
earlier consolidation:

- `security:access-and-identity` owns access **policy**;
  `it-operations:identity-lifecycle-administration` owns **execution** of joiner-mover-leaver.
- `operations:business-continuity-and-resilience` owns recovery objectives and the business process;
  `it-operations:backup-and-recovery` owns the technical restore that delivers against them.
- `technology:cloud-infrastructure` owns cloud environment design;
  `it-operations:systems-administration` owns operating the systems the company runs on.
- `security:vulnerability-management` decides what is urgent to patch;
  `it-operations:systems-administration` executes the cadence.

**Also fixed here.** Every agent charter carried a hardcoded skill count — `finance` claimed four
while holding nine. The count added nothing and rotted silently, so it was removed rather than
updated to a number that would rot again.

---

## D28. US English as house style — ✅ Resolved

The catalog had drifted into British spelling across 178 occurrences in 49 files — the British
forms of *license*, *program*, *catalog*, *behavior*, *prioritize* and *center*, among others. The
author is in Georgia and writes in US English, so the repository was not speaking in his voice.

- (a) **Fix the current occurrences.** A one-time rewrite.
- **(b) Fix them and enforce it.** ← **chosen**
- (c) Accept mixed spelling as unimportant.

**Resolution: (b).** The one-time fix is the smaller half. Spelling drift is invisible to review and
returns with the next contribution, and a repository of original work reading as though it came from
somewhere else is precisely the wrong impression. `scripts/check-us-english.py` fails the build on
British spellings and rewrites them under `--fix`; it is the ninth check.

**Exact word forms, never stems.** This is the trap the check is built around: *analysis*,
*analyst*, *specialist* and *realistic* are all correct US English already. A rewrite keyed on the
stems those words share with their British-spelled cousins would have mangled all four across the
catalog. The pairs list holds exact forms only, and those four words were confirmed unflagged before
the rewrite was run.

**`LICENSE` is never rewritten.** It carries the canonical MIT text, which is not ours to edit.

**It exposed a latent bug rather than creating one.** Converting `CONTRIBUTING.md` to the US
spelling of *license* immediately failed `check-provenance.py`, whose `\bMIT License\b` marker had
never matched the British form. The provenance check had been passing that file **by accident** —
anyone
writing it the American way would have failed the build, for a reason that would have been
baffling.

Fixed with a deliberately narrow waiver: the `MIT License` marker alone is waived, in
`CONTRIBUTING.md` and `README.md` alone, because naming our own license in our own documentation is
expected. Every other marker still applies to those files, verified by planting a third-party
copyright notice in one and Apache text in the other — both still caught.

**The naming consequence.** The PMO department's display title becomes *Program Management Office*.
The slug `pmo` and the skill addresses are unaffected, so nothing anyone could have installed
changes.

---

## D29. Publishing the org chart so the README can link to it — 🔵 Open (needs your hands)

The README now leads with a screenshot of the org chart. The screenshot is honest but static; the
value is in the live page, and **GitHub does not render HTML from a repository** — a link to
`docs/org-chart.html` shows a reader the source, not the chart.

- **(a) GitHub Pages, serving `/docs` from `main`.** ← **recommended**
- (b) A third-party HTML preview proxy.
- (c) Screenshot only, no link.
- (d) A hosted site on a purchased domain.

**Recommendation: (a).** Free on public repositories, one setting, and it republishes on every push
— so the live chart tracks the generator with no extra step. The URL becomes
`https://cbrock84.github.io/headcount/org-chart.html`, which is what the README already points at.

- **(b) rejected.** Depends on someone else's service staying up, and the URL is unpresentable.
- **(c) rejected** as the default, though it is what you get until (a) is enabled: the screenshot is
  the flair, the live page is the substance.
- **(d) is D25 revisited and still premature** — Pages costs nothing and needs no domain.

**Two consequences worth knowing before enabling it.**

1. Pages serves everything in `/docs`, so the decision log and use cases become browsable as raw
   files. The repository is already public, so nothing is newly exposed; it is only more visible.
2. `docs/index.html` redirects the site root to the chart, so
   `https://cbrock84.github.io/headcount` works rather than presenting a directory listing.

**This also reopens the Website field from D25**, which was left empty for want of anything worth
pointing at. A live, self-updating org chart is exactly that, at no cost and with none of the
credibility risk of a degraded TLD. If Pages is enabled, the Website field should be set to the
Pages URL. D25's reasoning about domains is unchanged: still not worth buying one.

**Until enabled**, the README's two links to the Pages URL are dead. That is the one cost of
shipping this before the setting is flipped, and it is a single line to revert if you would rather
not publish a site.

**To enable:** Settings → Pages → Source: *Deploy from a branch* → Branch: `main`, folder `/docs`.
