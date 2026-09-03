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
| D17 | Which department is the next real gap | ✅ Resolved |
| D18 | Repository visibility, now that all content is original | ✅ Resolved |
| D19 | README drift | ✅ Resolved |
| D20 | Publishing steps that need your hands | ✅ Resolved |
| D21 | MIT or Apache-2.0 for the long term | ✅ Resolved |
| D22 | What to call this | ✅ Resolved |
| D23 | Buttoning up the repository now that it is public | ✅ Resolved |
| D24 | Whether to add sponsorship | ✅ Resolved |
| D25 | Whether to register a domain for the About field | ✅ Resolved |
| D26 | Where project management lives | ✅ Resolved |
| D27 | Splitting CIO-side IT operations out of `technology` | ✅ Resolved |
| D28 | US English as house style | ✅ Resolved |
| D29 | Publishing the org chart so the README can link to it | ✅ Resolved |
| D30 | Coverage QC against public occupational taxonomies | ✅ Resolved |
| D31 | Authority as a second axis on the surface map | ✅ Resolved |
| D32 | Extending the skill-reference checker to skill bodies | ✅ Resolved |
| D33 | US English check rejects the plural of "analysis" | ✅ Resolved |
| D34 | Two skills claim social graphics | ✅ Resolved |
| D35 | Whether description shape is a checkable convention | ✅ Resolved |

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

Two other organizations I have access to cannot be *attached* to this session (one-owner limit),
but their **public** repositories are readable here by anonymous clone, which I verified against
one of them.

What looked likely to hold material: a set of governance, risk and compliance skill repositories,
some ISO 27001 tooling and evidence-collection work, and one workflow-automation script skill.

- (a) Sweep them now and propose a `compliance` department.
- **(b) Sweep and catalog only** — report what is there, import nothing until D6 is settled. ←
  **recommended**
- (c) Defer entirely.
- (d) Also run the private and internal sweep from a session rooted in the other organization.

**Recommendation: (b).** The catalog is cheap and informs D8 and D10. Importing anything before D6
is resolved would repeat the exact mistake D3 and D4 were about — and these are forks of
third-party work, so the same licensing question applies to all of them.

**Resolution: (d).** Catalog the public repos from this session, and additionally start a separate
session rooted in the other organization to sweep its private and internal repositories.

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
| 7 | Deepen `operations`, then `finance`, then `people` | D10 | — | ✅ done |
| 8 | Catalog the other organizations' public repos — no import | D11 | — | ✂️ dropped, D30 |
| 9 | ~~Separate session for the private sweep~~ | D11 | — | ✂️ dropped, D30 |
| 10 | Build the vertical generator: core, per-vertical config, one-way emit | D8 | — | |
| 11 | Revisit repo visibility | D16 | after 1 | ✅ done |

Items 1–4 can proceed in parallel; all four land before item 5. Items 8 and 9 were dropped in D30.

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

## D29. Publishing the org chart so the README can link to it — ✅ Resolved

The README now leads with a screenshot of the org chart. The screenshot is honest but static; the
value is in the live page, and **GitHub does not render HTML from a repository** — a link to
`docs/org-chart.html` shows a reader the source, not the chart.

- **(a) GitHub Pages, serving `/docs` from `main`.** ← **chosen**
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

**Resolution: (a), enabled before the repository was made public.** Verified live rather than
assumed: `/org-chart.html`, the site root and `/USE-CASES.md` all return 200, and the published
chart reads 172 skills — the current count — so Pages is republishing on push as (a) predicted.
The README's two links are live, not dead.

**This entry sat open long after the work was done**, and was read back as current state. An open
decision that is not open is worse than no entry, because it is trusted. Close a decision when the
thing is done, not when someone next reads the log.

---

## D30. Coverage QC against public occupational taxonomies — ✅ Resolved

Two questions, settled together: whether the cross-organization repository sweep was worth running,
and whether the catalog covers what a medium-to-large business actually contains.

**The sweep is dropped.** A manual pass over those repositories found little beyond
overlap with GRC roles already covered by `legal-risk` and `security`. Work-queue items 8 and 9 are
closed rather than deferred — a deferred item nobody intends to do is worse than a closed one,
because it keeps appearing in every review.

**Coverage was validated against external taxonomies rather than intuition.** Judging one's own
catalog complete by inspection reliably finds the functions the author already thought of. The
references used were the **BLS Standard Occupational Classification** major groups 11-0000
(Management Occupations) and 13-0000 (Business and Financial Operations Occupations) — public,
cross-industry, and the standard instrument for exactly this question.

**Eight gaps found, all built.** Six were functions the taxonomy names and the catalog did not
cover:

| Function | SOC codes | Why it was missed |
|---|---|---|
| `operations:procurement-and-sourcing` | 11-3061, 13-1023 | Judged covered by `vendor-management`, which is post-contract only. Two separate SOC codes point at the pre-contract discipline; that judgment was wrong. |
| `finance:tax` | 13-2081, 13-2082 | Zero coverage across nine finance skills. |
| `people:benefits-and-leave` | 11-3111, 13-1141 | `compensation-and-leveling` covers pay bands, not health, retirement or leave. |
| `legal-risk:regulatory-compliance` | 13-1041 | Already named as a gap; the taxonomy confirmed it. |
| `operations:facilities-and-workplace` | 11-3013, 11-9141 | Zero coverage. Also absorbs the administrative-services function from 11-3012, so D12's dissolution of the `administration` department stands. |
| `marketing:events-and-field-marketing` | 13-1121 | Seventeen marketing skills and no events. |

**Two more were internal inconsistencies the taxonomy did not find and a structural check did.**
Every department carried a department-head skill except `it-operations` and `pmo` — the two added
most recently. Their charters had been written to anchor on an arbitrary skill instead, which is a
workaround I introduced rather than a gap I reported. Fixed with
`it-operations:chief-information-officer` and `pmo:head-of-pmo`, and both charters now anchor on
their head like every other.

The CIO skill also states the CTO/CIO boundary explicitly, which D27 split but never wrote down in
a skill: the CIO runs the technology the company works *on*, the CTO the technology it *sells*.

**What was deliberately not built.** The industry-specific management occupations in SOC 11-9000 —
education, medical, food service, lodging, gambling, funeral, agricultural and construction — are
correctly absent from a cross-industry core and belong to the vertical variants in D8. Labor and
union relations (13-1075) and industrial production management (11-3051) are real but weighted
toward manufacturing, logistics and retail, so they go to the verticals too.

**Remaining Tier 1**, recorded in the org chart's gaps section: customer experience depth, legal
depth, corporate strategy depth, and product discovery and prioritization. None is a missing
function; all are thin coverage of a function already present.

---

## D31. Authority as a second axis on the surface map — ✅ Resolved

The surface map answers where an agent may write. It has never answered whether that write may
land without a decision, and the two are not the same question. In practice the second one was
settled per dispatch, from memory, by whoever happened to be driving — which is the condition the
surface map itself exists to eliminate.

- **(a) A fourth roster column, checked by the guard.** ← **chosen**
- (b) State it in each charter. Prose inside the agent being governed; nothing checks it, and it is
  invisible at the moment it matters, which is the dispatch.
- (c) Infer it from class. Conflates "cannot write" with "may not land unreviewed" — a reviewer is
  ungated precisely because it cannot write, and a builder's blast radius has nothing to do with
  its class.
- (d) Leave it implicit. The status quo, and the reason this was raised.

**Resolution:** (a). Three values — `autonomous` (dispatch it and take the result), `proposes` (the
orchestrator surfaces the diff before landing it), `escalates` (do not dispatch it unasked; the
work itself is the decision).

**Eighteen of nineteen rows are `autonomous`, and that is the honest answer rather than a
placeholder.** A department writes only inside its own plugin directory, where the worst outcome is
a bad skill in one department. Marking rows gated to make the column look load-bearing would be the
decoration this repository rejects everywhere else.

**The one exception is `repo-meta`, and it is a real one.** It owns the CI workflows, the check
scripts, every generator the documents are built from, and the surface map itself. A wrong change
under `plugins/finance/**` is wrong in one department. A wrong change to `scripts/check-all.sh` can
make every other check stop reporting, and nothing downstream would fail to say so. That is the
shape of thing worth a checkpoint.

**Two invariants are enforced rather than described**, both catching a row that reads as governed
while governing nothing: a reviewer may not be gated, because it holds no write surface to gate;
and a gated builder must own a surface. Both were verified against deliberately broken maps rather
than assumed — an unproven guard is a comment claiming to be a guard.

**Existing maps keep working.** The column is optional and omission means `autonomous`, but `check`
reports which rows defaulted, so a map that never considered the question stays distinguishable
from one that answered it. The value here is not the single gated row; it is that the axis is now
expressible and checked instead of remembered — the same argument that justified the surface map.

## D32. Extending the skill-reference checker to skill bodies — ✅ Resolved

`scripts/check-skill-refs.py` verifies that every `` `department:skill` `` reference resolves. It
scans `README.md`, `CONTRIBUTING.md` and `docs/**` — and nothing else. Skill files themselves are
not scanned, so the 131 cross-references inside `plugins/**/SKILL.md` have never been checked.

**Four of them were broken**, found by running the checker's own logic over the skill tree:

| Reference | In | Actual problem |
|---|---|---|
| revenue:revenue-recognition | `finance:tax` | Wrong department prefix |
| legal-risk:risk-and-controls | `legal-risk:chief-legal-and-risk-officer` | Skill never existed |
| customer-experience:churn | `revenue:chief-revenue-officer` | Skill never existed |
| operations:incident-management | `operations:chief-operating-officer` | Skill never existed |

All four are fixed on this branch. The first three were retargeted; the fourth was a genuine
capability gap and `operations:incident-management` now exists, which is what the reference always
promised a reader.

That leaves the checker itself, which is `repo-meta` — the one row on the surface map carrying
`proposes` under D31, so the change is surfaced here rather than made.

- **(a) Extend the checker to scan `plugins/**/SKILL.md` as well.** ← **chosen**
- (b) Leave it. Skill-to-skill references stay unchecked, and the next broken one is found by a
  reader rather than by CI.
- (c) Extend it, but as a warning rather than a failure. Keeps CI green while surfacing rot; also
  means nothing ever forces the fix, which is how the four above accumulated.

**Recommendation: (a).** The checker's own docstring says a reference to a skill that no longer
exists is a broken promise to a reader and that nothing else in the tree catches it. That argument
does not weaken inside a skill file — it strengthens, because that is where readers follow
references from. The measured cost is zero: 131 references, four failures, all now fixed, no
false positives from ordinary prose.

**Why it is not simply done here.** The argument that a draft pull request is itself the surfacing
`proposes` calls for does not hold up. It would license any `repo-meta` change made overnight,
which collapses `proposes` into `autonomous` and makes the single non-default row on the roster
decorative — precisely what D31 refused. Note the contrast with this log entry, which is also a
`repo-meta` write under `docs/**` and is fine because it was explicitly asked for. Same surface,
different authorization.

**One consequence worth knowing before choosing (a).** CI runs `check-all.sh` on every pull
request, so the extension turns any unresolved reference into a red build immediately — including a
forward reference written to a skill that has not been created yet. That is the intended behavior,
but it changes what writing a cross-reference costs.


**Resolution: (a).** The checker now scans `plugins/**/SKILL.md` alongside the documentation.
Coverage went from 99 references to 244, and the tree is clean at the point of the change because
the four broken ones were fixed when they were found.

The cost named in this entry is now live: a reference written to a skill that does not exist yet
fails CI immediately. That is the intended behavior, and it means a forward reference has to be
written after the skill it points at, not before.

## D33. US English check rejects the plural of "analysis" — ✅ Resolved

`scripts/check-us-english.py` maps the British spelling of the verb *analyze* and its inflections to
the American forms. One of those inflections collides with the plural of *analysis*, which is spelled
identically in both dialects and is ordinary American English. Writing a sentence about several
pieces of analysis therefore fails the check, and `--fix` rewrites the noun into the third-person
verb form, producing a sentence that is not English in any dialect.

Caught while writing `data-analytics:quantitative-analysis`, where that plural is the natural word
in the opening line. Worked around by rephrasing, so nothing fails today.

**Two things make this worth more than a shrug.** The `--fix` path corrupts correct text rather
than merely flagging it, which is worse than a plain false positive. And the check has no exemption
for code spans or quoted text, so the defect cannot be described in any file the check scans —
this entry has to talk around the word rather than name it, which is the clearest demonstration of
the problem available.

The same noun/verb collision exists in principle for the *practice* and *license* families, where
British English splits the spelling by part of speech. Both British forms are in the word list, so
the same trap is set for anyone writing about either.

- **(a) Drop the colliding inflection from the word list.** ← **chosen.** A one-line change.
  The British verb is rare in this library's register; the noun plural is common.
- (b) Skip matches inside backticks and block quotes. Fixes the describability problem for every
  word at once, and leaves the false positive in ordinary prose where it actually bites.
- (c) Make the rule context-sensitive on the preceding word. More precise, and more machinery than
  a spelling check should carry.
- (d) Leave it and rephrase around it, as was done here. Costs nothing today and quietly shapes
  what people are able to write.

**Recommendation: (a), and consider (b) alongside it** — they solve different halves and neither
excludes the other. This is repo-meta and carries `proposes` under D31, which is why it is logged
rather than fixed. It is independent of D32; either can be taken alone.


**Resolution: (a).** The colliding inflection is gone from the word list; the British verb and its
past form remain. Verified both directions — a sentence using the plural noun passes, and one using
the British verb is still caught.

(b), the code-span exemption, was not taken. It solves a narrower problem than it appears to: the
reason this entry could not name the word was that the whole file is scanned, and (a) removes that
constraint for this word without adding machinery. The exemption is worth revisiting if a second
word hits the same wall.

## D34. Two skills claim social graphics — ✅ Resolved

Found by a promise-versus-coverage sweep of all 172 descriptions. `product:presentation-design`
says "to design a banner, social graphic, or one-pager". `marketing:visual-content` says "create
social graphics" and covers carousels, infographics, quote graphics and social imagery in depth.

Both are legitimately scoped — one is about carrying an argument in a laid-out artifact, the other
about visual assets that carry content — but they compete for the same trigger, which is the
failure `technology:skill-authoring` calls the silent killer. A request to design a social graphic
can load either, and they give different advice.

The two sit in different departments, so resolving it moves work across surfaces rather than within
one. That is why it is logged rather than decided.

- **(a) Narrow `presentation-design` to decks and one-pagers**, and drop the social and banner
  claim from its description. ← **chosen.** `visual-content` is substantially deeper on that
  material — it covers format selection, carousels, infographics and generation prompts, where
  `presentation-design` gives it two paragraphs. The narrower skill also matches its own body,
  which is organized as decks first and everything else second.
- (b) Narrow `visual-content` instead, leaving all static graphic design in product. Inverts the
  depth: the shallower treatment would own the topic.
- (c) Merge them. They are genuinely different jobs — an argument in slides versus an asset in a
  feed — and merging produces one skill that triggers on both and serves neither well.
- (d) Leave both. The overlap keeps costing a wrong load occasionally, at no fix cost.

**Recommendation: (a).** It is a description change in one skill, no content moves, and it aligns
each skill's trigger with where its depth actually is.

**One adjacent overlap was fixed rather than logged**, because it sat inside a single department
and was introduced by this branch: `corporate-strategy:portfolio-strategy` claimed "decide market
entry or exit" while the new `corporate-strategy:market-entry` covers entry properly. The
portfolio skill's description now says exit only, which is what its body is about.


**Resolution: (a).** `presentation-design` now covers decks and one-pagers, and points at
`marketing:visual-content` for social graphics, carousels and infographics. The description and the
body both moved, so the trigger and the content agree.

The one-pager section kept its last bullet in changed form. It had been about a social graphic at
thumbnail size; it is now about a one-pager's real reading contexts — printed, attached, projected —
which is the same lesson applied to the surface this skill actually keeps.

---

## D35. Whether description shape is a checkable convention — ✅ Resolved

An outside read of all 172 skills reported that descriptions do not follow one pattern. Some open
with a capability sentence and then a `Use this to…` trigger sentence; some run the two together;
some name a sibling skill to route away from, most do not. Two checks already constrain
descriptions — a minimum length, and the promise-versus-coverage relationship that D34 came out of
— but nothing constrains their shape.

This is a convention question rather than a defect, and it touches every skill in the tree, so it
is logged rather than decided.

- **(a) Leave shape unconstrained.** ← **chosen.** The two checks that exist catch the
  failures that actually cost something: a description too thin to route on, and a description
  that promises what the body does not cover. Shape is not one of those. Normalizing 172
  descriptions to a template would be a large diff whose only beneficiary is the reader of the
  diff.
- (b) Fix a two-sentence template — capability, then trigger — and normalize all 172, with a check
  to hold it. Consistent, and the check is easy to write. It is also 172 files of churn for a
  problem no one has reported hitting.
- (c) Require only the trigger sentence, leaving the rest free. Half the discipline for a third of
  the churn, but "a sentence beginning `Use this`" is the part a checker can verify and the part
  that matters least — the trigger's *content* is what routes, and no check can read that.

**Recommendation: (a).**

**Resolution: (a).** Nothing changes in the tree. The two checks that exist stay the whole of what
is enforced about a description: it must be substantial enough to route on, and it must not promise
what the body does not cover. Shape is left to whoever writes the skill.

Recorded so the next full read does not re-raise it as a defect: the variation is deliberate, not
drift. A description that names a sibling skill does so because that pair actually collides; one
that runs capability and trigger together does so because the sentence reads better that way. A
template would flatten both, and the part a checker can verify — that a sentence beginning `Use
this` exists — is the part that matters least. What routes a request is the trigger's content, and
no check can read that.

**One item in the same report needs no decision, recorded here so the next read does not re-raise
it.** The figure "~24 agents over a 1,500-file monorepo" in `executive:agent-hierarchy` was read as
a claim about this roster, which currently runs 17 builders and 2 reviewers. It is not: both
instances say the method was *extracted from* a working implementation of that size. The sentence
describes the source the method came from, and changing the number would make it wrong.
