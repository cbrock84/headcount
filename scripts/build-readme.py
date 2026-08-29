#!/usr/bin/env python3
"""Regenerate README.md from the plugin tree. Run via ./scripts/check-all.sh --fix-readme,
and verified in CI so the README can never drift from what the repo actually contains."""
import glob, os, re, json, sys

ORDER = [
    ("executive",         "Office of the CEO",  "Chief Executive"),
    ("technology",        "Technology",         "CTO / CIO"),
    ("security",          "Security",           "CISO"),
    ("product",           "Product",            "CPO"),
    ("marketing",         "Marketing",          "CMO"),
    ("demand-generation", "Demand Generation",  "CMO"),
    ("revenue",           "Revenue",            "CRO"),
    ("finance",           "Finance",            "CFO"),
    ("operations",        "Operations",         "COO"),
    ("customer-experience","Customer Experience","CCO"),
    ("data-analytics",    "Data & Analytics",   "CDO"),
    ("corporate-strategy","Corporate Strategy", "CSO"),
    ("people",            "People",             "CHRO"),
    ("legal-risk",        "Legal & Risk",       "CLO / CCO"),
]
REVIEWER = {"security", "legal-risk"}


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
out = [
    "# agents-v1",
    "",
    "An agent organization for [Claude Code](https://claude.com/claude-code), structured as a company:",
    f"a chief executive over {len(ORDER)} departments, {total} skills in total.",
    "",
    "Every department is an independently installable plugin, so a project loads only the functions it",
    "needs rather than all of them at once.",
    "",
    "## Install",
    "",
    "```",
    "/plugin marketplace add cbrock84/agents-v1",
    "/plugin install security@agents-v1",
    "```",
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
    "## How it is organized",
    "",
    "```",
    "plugins/<department>/",
    "  .claude-plugin/plugin.json   department manifest",
    "  skills/<skill>/SKILL.md      frontmatter name equals the directory name",
    ".claude/agents/<id>.md         one charter per department",
    "docs/AGENT-SURFACES.md         every path has exactly one owner, enforced in CI",
    "docs/DECISION-LOG.md           numbered decisions with options and recommendations",
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
    "Verifies the surface map is coherent, every skill's frontmatter is valid and unique, no third-party",
    "licence text has appeared, and every manifest parses. CI runs the same script.",
    "",
    "A new department needs its roster row in `docs/AGENT-SURFACES.md`, a surface block, a charter in",
    "`.claude/agents/`, and an entry in `.claude-plugin/marketplace.json` — all in the same change, or",
    "the check fails.",
    "",
    "## Licence",
    "",
    "MIT — see [LICENSE](LICENSE). Every skill here was written for this repository.",
    "",
    "---",
    "",
    "<sub>README generated by `scripts/build-readme.py` — edit that, not this file.</sub>",
    "",
]
content = "\n".join(out)

if "--check" in sys.argv:
    current = open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else ""
    if current != content:
        print("  README.md is stale — run: python3 scripts/build-readme.py")
        sys.exit(1)
    print("README is current")
    sys.exit(0)

open("README.md", "w", encoding="utf-8").write(content)
print(f"README.md regenerated — {len(ORDER)} departments, {total} skills")
