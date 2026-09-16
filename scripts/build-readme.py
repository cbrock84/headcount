#!/usr/bin/env python3
"""Regenerate README.md from the plugin tree. Run via ./scripts/check-all.sh --fix-readme,
and verified in CI so the README can never drift from what the repo actually contains."""
import glob, os, re, json, sys

# Display metadata per department. The department list itself comes from the plugin tree — see
# load_departments() — so a department cannot be added to disk and silently omitted from the docs.
# The rank fixes reporting order: the chief executive first, then the functions beneath.
META = {
    "executive":          (10, "Office of the CEO",   "Chief Executive"),
    "technology":         (20, "Technology",          "CTO / CIO"),
    "security":           (30, "Security",            "CISO"),
    "it-operations":      (35, "IT Operations",       "CIO"),
    "product":            (40, "Product",             "CPO"),
    "marketing":          (50, "Marketing",           "CMO"),
    "demand-generation":  (60, "Demand Generation",   "CMO"),
    "revenue":            (70, "Revenue",             "CRO"),
    "finance":            (80, "Finance",             "CFO"),
    "operations":         (90, "Operations",          "COO"),
    "pmo":                (95, "Program Management Office", "EPMO / COO"),
    "customer-experience": (100, "Customer Experience", "CCO"),
    "data-analytics":     (110, "Data & Analytics",   "CDO"),
    "corporate-strategy": (120, "Corporate Strategy", "CSO"),
    "people":             (130, "People",             "CHRO"),
    "legal-risk":         (140, "Legal & Risk",       "CLO / CCO"),
}
REVIEWER = {"security", "legal-risk"}


def load_departments():
    """Departments come from disk, not from a list someone has to remember to update. A department
    present on disk but missing from META is a hard error rather than a silent omission — the same
    mistake used to drop a department out of both generated docs while --check still passed."""
    found = {os.path.basename(os.path.dirname(os.path.dirname(m)))
             for m in glob.glob("plugins/*/.claude-plugin/plugin.json")}
    missing = sorted(found - set(META))
    if missing:
        sys.exit("build-readme: no display metadata for department(s) "
                 + ", ".join(missing)
                 + "\n  add a (rank, title, executive) entry to META in scripts/build-readme.py")
    stale = sorted(set(META) - found)
    if stale:
        sys.exit("build-readme: META names department(s) that are not on disk: "
                 + ", ".join(stale)
                 + "\n  remove them from META in scripts/build-readme.py")
    return [(d, META[d][1], META[d][2]) for d in sorted(found, key=lambda d: META[d][0])]


ORDER = load_departments()


def _catalog_counts():
    """Catalog totals, read from the catalog so the README cannot claim a number it does not hold."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_sources", "scripts/check-sources.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    entries = module.load()
    skills = {ref for _, e in entries for ref in e.get("skills", [])}
    quotable = {"public-domain-usgov", "public-domain", "cc0", "cc-by", "open-data",
                "attribution-required"}
    return len(entries), len(skills), sum(1 for _, e in entries if e["license"] in quotable)


SOURCE_COUNT, SOURCE_SKILLS, SOURCE_QUOTABLE = _catalog_counts()


def summarize(path, limit=165):
    text = open(path, encoding="utf-8").read()
    front = re.match(r"^---\s*\n(.*?)\n---", text, re.S).group(1)
    desc = re.search(r"^description:\s*(.*)$", front, re.M).group(1).strip()
    cut = re.split(r"(?:\.\s+)(?:Also )?[Uu]se (?:this|it)\b", desc)[0]
    if len(cut) < 40:
        cut = desc
    cut = cut.rstrip(" .,—-")
    return cut[: limit - 1].rstrip() + "…" if len(cut) > limit else cut


def skills(dept):
    return sorted(glob.glob(f"plugins/{dept}/skills/*/SKILL.md"))


total = sum(len(skills(d)) for d, _, _ in ORDER)
# Badge counts come from the same tree walk as the tables below, so they cannot drift from
# reality — a wrong count fails `build-readme.py --check` in CI like any other staleness.
# Two bases, and the difference matters: the static `/badge/` endpoint takes a literal
# label-message-color triple, while the live endpoints hang off the root. Interpolating the
# `/badge` base into a `github/...` path produces a URL that returns a picture of itself.
SHIELDS = "https://img.shields.io"
B = f"{SHIELDS}/badge"
REPO = "cbrock84/headcount"
out = [
    '<h1 align="center">headcount</h1>',
    "",
    '<p align="center"><b>Add a department, not a prompt.</b></p>',
    "",
    '<p align="center">',
    # "Built for Claude Code" stopped being true when the ChatGPT manifests landed. Both tools read
    # the same skills from this tree, and the badge is the first thing anyone reads.
    f'  <a href="AGENTS.md"><img alt="Runs in Claude Code and ChatGPT"'
    f' src="{B}/runs%20in-Claude%20Code%20%C2%B7%20ChatGPT-D97757?style=flat-square"></a>',
    f'  <img alt="{len(ORDER)} departments" src="{B}/departments-{len(ORDER)}-3F4B5B?style=flat-square">',
    f'  <img alt="{total} skills" src="{B}/skills-{total}-3F4B5B?style=flat-square">',
    f'  <a href="docs/SOURCES.md"><img alt="{SOURCE_COUNT} cited sources"'
    f' src="{B}/cited%20sources-{SOURCE_COUNT}-3F4B5B?style=flat-square"></a>',
    f'  <a href="LICENSE"><img alt="MIT licensed" src="{B}/license-MIT-3F4B5B?style=flat-square"></a>',
    "</p>",
    "",
    # A second row, live rather than generated. The first row says what this is and is computed
    # from the tree; this one says how it is doing and is fetched when someone loads the page.
    # The build badge is the one that earns its place: fourteen checks run on every push, and a
    # reader has no other way to know they pass.
    '<p align="center">',
    f'  <a href="https://github.com/{REPO}/actions/workflows/checks.yml"><img alt="Checks"'
    f' src="{SHIELDS}/github/actions/workflow/status/{REPO}/checks.yml?style=flat-square&label=checks"></a>',
    f'  <a href="https://github.com/{REPO}/stargazers"><img alt="Stars"'
    f' src="{SHIELDS}/github/stars/{REPO}?style=flat-square&color=3F4B5B"></a>',
    f'  <a href="https://github.com/{REPO}/graphs/contributors"><img alt="Contributors"'
    f' src="{SHIELDS}/github/contributors/{REPO}?style=flat-square&color=3F4B5B"></a>',
    f'  <img alt="Last commit" src="{SHIELDS}/github/last-commit/{REPO}?style=flat-square&color=3F4B5B">',
    f'  <img alt="Visitors" src="https://visitor-badge.laobi.icu/badge?page_id={REPO.replace("/", ".")}&title=visitors&color=3F4B5B">',
    f'  <a href="CONTRIBUTING.md"><img alt="PRs welcome" src="{B}/PRs-welcome-2EA043?style=flat-square"></a>',
    "</p>",
    "",
    # The chart is the clearest single statement of what this is, so it leads. GitHub does not
    # render HTML from a repository, so the image links to the Pages copy, which does.
    '<p align="center">',
    '  <a href="https://cbrock84.github.io/headcount/org-chart.html">',
    "    <picture>",
    '      <source media="(prefers-color-scheme: dark)" srcset="docs/assets/org-chart-dark.png">',
    f'      <img alt="The headcount org chart — {len(ORDER)} departments, {total} skills, searchable"'
    ' src="docs/assets/org-chart-light.png" width="840">',
    "    </picture>",
    "  </a>",
    "</p>",
    "",
    '<p align="center">',
    '  <a href="https://cbrock84.github.io/headcount/org-chart.html"><b>Open the interactive org'
    " chart</b></a> — search every skill, open a department, jump to the source.",
    "</p>",
    "",
    "An agent organization structured as a company: a chief executive over",
    f"{len(ORDER)} departments, {total} skills in total.",
    "",
    "Every department is an independently installable plugin, so a project loads only the functions it",
    "needs rather than all of them at once.",
    "",
    "## Install",
    "",
    "**[Claude Code](https://claude.com/claude-code)**",
    "",
    "```",
    "/plugin marketplace add cbrock84/headcount",
    "/plugin install security@headcount",
    "```",
    "",
    "**ChatGPT and Codex** — the same repository. Add it as a plugin marketplace, or drop the",
    "department you want into `.agents/skills/` in your own project.",
    "",
    "The skills are identical in both; only the manifests differ, and both sets are generated from",
    "this tree, so a fix reaches both at once. See `AGENTS.md`.",
    "",
    "Install as many departments as the project needs. Skills are addressed as `department:skill` —",
    "`security:threat-modeling`, `finance:unit-economics` — so names never collide.",
    "",
    "## Use",
    "",
    "Skills load themselves when a request matches. Ask a question in the department's territory and the",
    "right specialist engages:",
    "",
    "| You ask | What loads |",
    "|---|---|",
    "| \"why isn't this landing page converting?\" | `demand-generation:landing-page-cro-expert` |",
    "| \"review this design before we build it\" | `security:threat-modeling` |",
    "| \"can we afford this hire?\" | `finance:unit-economics` |",
    "| \"our growth has stalled\" | `executive:business-growth-consultant` |",
    "",
    "Invoke one directly by name when you want a specific lens: `/finance:financial-modeling`.",
    "",
    "New to this? [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) covers which departments to",
    "install first, the three ways to invoke a skill, and what reviewer-class departments do",
    "differently.",
    "",
    "Eleven situations that cross departments — a SOC 2 demand from an enterprise prospect, a link",
    "down between two sites, a renewal that auto-renewed because nobody owned the date — are worked",
    "through end to end in [docs/USE-CASES.md](docs/USE-CASES.md), including what comes back and",
    "where a reviewer-class department stops the work rather than adding an opinion.",
    "",
    "Each department also ships an agent charter in `.claude/agents/`, so a department can be delegated",
    "to as a subagent with its own exclusive write surface.",
    "",
    "## Departments",
    "",
]
for dept, title, exec_role in ORDER:
    paths = skills(dept)
    tag = " · **reviewer-class**" if dept in REVIEWER else ""
    out += [f"<details>", f"<summary><b>{title}</b> ({exec_role}) — {len(paths)} skills{tag}</summary>", "",
            "| Skill | What it does |", "|---|---|"]
    for p in paths:
        out.append(f"| `{os.path.basename(os.path.dirname(p))}` | {summarize(p)}. |")
    out += ["", "</details>", ""]

out += [
    "**Reviewer-class departments** (`security`, `legal-risk`) review what other departments build, and",
    "their blocking findings are not overrulable by the department under review. That is why the CISO",
    "and the CLO report to the chief executive rather than into the function they oversee.",
    "",
    "## Sources",
    "",
    "A skill states what a competent practitioner knows. It cannot state what the regulator",
    "published last month — it is written once and the obligation moves. So skills that answer",
    "questions an outside authority settles carry a list of those authorities, in",
    "`references/sources.md` inside the skill, which is where an agent reads it while answering.",
    "",
    f"{SOURCE_COUNT} sources across {SOURCE_SKILLS} skills so far — tax and accounting, law and",
    "employment, security and controls frameworks, education standards.",
    "[The full index is in `docs/SOURCES.md`](docs/SOURCES.md).",
    "",
    "**References, never copies**, and every entry carries what you may actually do with it. That",
    "second part is the point: most of what a professional must cite is not open. ISO standards are",
    "sold, SANS papers are copyrighted, the FASB Codification needs an account — while US federal",
    "works are public domain by statute and EU legal texts are reusable with attribution.",
    f"{SOURCE_QUOTABLE} of the {SOURCE_COUNT} are quotable; the rest are read-and-cite, and the entry",
    "says so in the imperative next to the link.",
    "",
    "Links are re-checked weekly by their own workflow rather than on every push, because a",
    "publisher being briefly down is not a reason to fail an unrelated pull request.",
    "",
    "## How it is organized",
    "",
    "```",
    "plugins/<department>/",
    "  .claude-plugin/plugin.json   department manifest, Claude Code",
    "  .codex-plugin/plugin.json    the same department, ChatGPT and Codex",
    "  skills/<skill>/SKILL.md      frontmatter name equals the directory name",
    "  skills/<skill>/references/   supporting files, including the skill's sources",
    ".claude-plugin/marketplace.json  the marketplace Claude Code reads",
    ".agents/plugins/marketplace.json the same departments, for ChatGPT and Codex",
    "sources/*.toml                 the source catalog, mapped to the skills it serves",
    "verticals/<name>/              industry packs, emitted as standalone repositories",
    ".claude/agents/<id>.md         one charter per department",
    "AGENTS.md                      repository context for any agent working on this repo",
    "docs/AGENT-SURFACES.md         every path has exactly one owner, enforced in CI",
    "docs/DECISION-LOG.md           numbered decisions with options and recommendations",
    "docs/GETTING-STARTED.md        install, what to take first, and how to invoke a skill",
    "docs/SOURCES.md                every source in the catalog, and what may be done with it",
    "docs/USE-CASES.md              situations worked end to end across departments",
    "docs/org-chart.html            interactive org chart, searchable across every skill",
    "docs/index.html                GitHub Pages entry point, redirects to the chart",
    "```",
    "",
    "Agents split by **exclusive write surface**, not by topic — a topic split has no checkable",
    "boundary, and two agents working on \"SEO\" and \"UI\" both end up in the same file. See",
    "`executive:agent-hierarchy` for the method.",
    "",
    "## Contributing",
    "",
    "```",
    "./scripts/check-all.sh",
    "```",
    "",
    "Every check CI runs, in one script. The surface map is coherent; every skill's frontmatter is",
    "valid and unique; no third-party license text has appeared; the README, social card and org",
    "chart are current; every `department:skill` reference resolves; spelling is US English; no",
    "`## Never` block mixes two styles; the source catalog is valid and every skill's source file",
    "matches it; the ChatGPT manifests match the Claude ones; every vertical emits a repository that",
    "passes its own checks; and every manifest parses. CI calls this same script, so local and CI",
    "cannot drift.",
    "",
    "A new department needs its roster row in `docs/AGENT-SURFACES.md`, a surface block, a charter in",
    "`.claude/agents/`, and an entry in `.claude-plugin/marketplace.json` — all in the same change, or",
    "the check fails.",
    "",
    "## Contributors",
    "",
    # Both images are fetched when the page loads rather than committed, so neither can go stale
    # and neither adds a binary to the tree. The star chart carries a dark variant because the
    # plotted line is drawn on a light canvas by default and disappears on GitHub's dark theme.
    f'<a href="https://github.com/{REPO}/graphs/contributors">',
    f'  <img alt="Contributors to headcount" src="https://contrib.rocks/image?repo={REPO}">',
    "</a>",
    "",
    "The ChatGPT and Codex support in this repository started as a contribution from",
    "[@adi-dibra](https://github.com/adi-dibra), who worked out that the same `SKILL.md` files load",
    "in both tools and that only the manifests differ.",
    "",
    "<picture>",
    f'  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos={REPO}&type=Date&theme=dark">',
    f'  <img alt="Star history" src="https://api.star-history.com/svg?repos={REPO}&type=Date" width="600">',
    "</picture>",
    "",
    "## Writing",
    "",
    "Notes from building and running this, and from the day job — technology, security, AI, and the",
    "operating side of all three — go out at [cbrock84.substack.com](https://cbrock84.substack.com).",
    "",
    "The piece on why this is shaped like an org chart at all, and what broke before it was:",
    "[Giving AI agents an org chart]"
    "(https://cbrock84.substack.com/p/giving-ai-agents-an-org-chart).",
    "",
    "## License",
    "",
    "MIT — see [LICENSE](LICENSE). Every skill here was written for this repository.",
    "",
    "Built by [Chris Brock](https://chrisbrock.io).",
    "",
    "---",
    "",
    "<sub>README generated by `scripts/build-readme.py` — edit that, not this file.</sub>",
    "",
]
content = "\n".join(out)

# The org chart's department table drifts the same way the README did. Generate it between
# markers so the two cannot disagree; the analysis prose around it stays hand-written.
chart_rows = "\n".join(
    f"| `{d}` | {t} | {e} | {len(skills(d))}"
    + (" · reviewer-class |" if d in REVIEWER else " |")
    for d, t, e in ORDER
)
chart_block = (
    "<!-- BEGIN GENERATED: departments -->\n"
    f"| Department | Function | Executive | Skills |\n|---|---|---|---|\n{chart_rows}\n"
    f"\n{len(ORDER)} departments, {total} skills.\n"
    "<!-- END GENERATED: departments -->"
)
chart_path = "docs/org-chart.md"
chart_current = open(chart_path, encoding="utf-8").read()
chart_new = re.sub(
    r"<!-- BEGIN GENERATED: departments -->.*?<!-- END GENERATED: departments -->",
    lambda _: chart_block,
    chart_current,
    flags=re.S,
)

if "--check" in sys.argv:
    if chart_current != chart_new:
        print("  docs/org-chart.md department table is stale — run: python3 scripts/build-readme.py")
        sys.exit(1)
    current = open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else ""
    if current != content:
        print("  README.md is stale — run: python3 scripts/build-readme.py")
        sys.exit(1)
    print("README is current")
    sys.exit(0)

open("README.md", "w", encoding="utf-8").write(content)
open(chart_path, "w", encoding="utf-8").write(chart_new)
print(f"README.md and org-chart.md regenerated — {len(ORDER)} departments, {total} skills")
