#!/usr/bin/env python3
"""Build and sync the `Codex/.agents` directory with everything from the headcount repository.

Syncs:
1. Skills: All 143 skills flattened into `Codex/.agents/skills/`.
2. Agents: All 19 subagent charters from `.claude/agents/*.md` into `Codex/.agents/agents/`.
3. Plugins: All 16 department plugins from `plugins/*` into `Codex/.agents/plugins/`.
4. Docs: Governance and architecture documents into `Codex/.agents/docs/`.
5. Rules: Multi-agent organization guide in `Codex/.agents/rules/AGENTS.md`.
6. Scripts: Executable surface guard and utilities in `Codex/.agents/scripts/`.
7. Documentation: Comprehensive `Codex/.agents/README.md`.
"""
import glob
import json
import os
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODEX_DIR = os.path.join(REPO_ROOT, "Codex")
AGENTS_DIR = os.path.join(CODEX_DIR, ".agents")


README_CONTENT = """# Headcount Organization for Antigravity and Codex

This directory packages the complete headcount organization — 16 departments, 143 skills, 19
subagents, surface governance maps, and executable guards — adapted from the original repository
for **Google Antigravity** and **OpenAI Codex**.

---

## Directory Structure

```text
.agents/
├── skills/              # All 143 skills flattened for progressive disclosure
│   ├── code-review/
│   ├── systematic-debugging/
│   └── ...
├── agents/              # 19 subagent charters (technology, security, executive, etc.)
│   ├── executive.md
│   ├── technology.md
│   └── ...
├── plugins/             # 16 complete department packages
│   ├── technology/
│   ├── security/
│   └── ...
├── rules/               # Multi-agent coordination rules
│   └── AGENTS.md        # Organization roster, surface maps, and governance rules
├── docs/                # Architecture decisions, use cases, and surface maps
│   ├── AGENT-SURFACES.md
│   ├── DECISION-LOG.md
│   └── USE-CASES.md
└── scripts/             # Executable surface guard (agent-guard.mjs) and utilities
```

---

## How to Use in Your Projects

### Option 1: Use the Graphical Installer
Launch the GUI installer located in `Codex/`:
```powershell
python Codex/installer_gui.py
# or double-click Codex/install.bat in Windows Explorer
```
- **Sync from Original Repo**: Refreshes everything from the headcount tree.
- **Install Globally**: Installs skills and agents into user profile directories.
- **Install to Project Folder**: Copies the complete `.agents` organization to your project.

### Option 2: Copy Manually
Copy this entire `.agents` folder into any target project:
```powershell
Copy-Item -Recurse "Codex/.agents" "C:\\path\\to\\my-project\\"
```

When you open `my-project` in Antigravity or run OpenAI Codex:
- All 143 skills are detected via progressive disclosure.
- All 19 subagent charters are available for delegation.
- Department rules and surface governance in `rules/AGENTS.md` guide the agents.
"""

AGENTS_MD_TEMPLATE = """# Headcount Multi-Agent Organization

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
"""


def sync_all(repo_root=REPO_ROOT):
    """Synchronize everything from headcount into Codex/.agents."""
    os.chdir(repo_root)

    skills_dir = os.path.join(AGENTS_DIR, "skills")
    agents_dir = os.path.join(AGENTS_DIR, "agents")
    plugins_dir = os.path.join(AGENTS_DIR, "plugins")
    docs_dir = os.path.join(AGENTS_DIR, "docs")
    rules_dir = os.path.join(AGENTS_DIR, "rules")
    scripts_dir = os.path.join(AGENTS_DIR, "scripts")

    for d in [skills_dir, agents_dir, plugins_dir, docs_dir, rules_dir, scripts_dir]:
        os.makedirs(d, exist_ok=True)

    # 1. Sync Skills (flattened for direct progressive disclosure)
    skill_mds = sorted(glob.glob("plugins/*/skills/*/SKILL.md"))
    skills_count = 0
    for skill_md in skill_mds:
        src_dir = os.path.dirname(skill_md)
        name = os.path.basename(src_dir)
        dst_dir = os.path.join(skills_dir, name)
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        shutil.copytree(src_dir, dst_dir)
        skills_count += 1

    # 2. Sync Agent Charters (.claude/agents/*.md -> Codex/.agents/agents/)
    agent_files = sorted(glob.glob(".claude/agents/*.md"))
    agents_count = 0
    for agent_file in agent_files:
        dst_file = os.path.join(agents_dir, os.path.basename(agent_file))
        shutil.copy2(agent_file, dst_file)
        agents_count += 1

    # 3. Sync Department Plugins (plugins/* -> Codex/.agents/plugins/*)
    plugins_count = 0
    for dept_path in sorted(glob.glob("plugins/*")):
        if not os.path.isdir(dept_path):
            continue
        dept_name = os.path.basename(dept_path)
        dst_dept = os.path.join(plugins_dir, dept_name)
        if os.path.exists(dst_dept):
            shutil.rmtree(dst_dept)
        shutil.copytree(dept_path, dst_dept)

        # Standardize plugin.json at plugin root for Antigravity compatibility
        claude_manifest = os.path.join(dst_dept, ".claude-plugin", "plugin.json")
        root_manifest = os.path.join(dst_dept, "plugin.json")
        if os.path.exists(claude_manifest) and not os.path.exists(root_manifest):
            shutil.copy2(claude_manifest, root_manifest)

        plugins_count += 1

    # 4. Sync Documentation (docs/* -> Codex/.agents/docs/)
    docs_count = 0
    for doc in ["AGENT-SURFACES.md", "DECISION-LOG.md", "USE-CASES.md"]:
        src_doc = os.path.join("docs", doc)
        if os.path.exists(src_doc):
            shutil.copy2(src_doc, os.path.join(docs_dir, doc))
            docs_count += 1

    # 5. Sync Rules (Codex/.agents/rules/AGENTS.md & Codex/.agents/AGENTS.md)
    with open(os.path.join(rules_dir, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(AGENTS_MD_TEMPLATE.strip() + "\n")
    with open(os.path.join(AGENTS_DIR, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(AGENTS_MD_TEMPLATE.strip() + "\n")

    # 6. Sync Guard Scripts
    guard_src = os.path.join(
        "plugins", "executive", "skills", "agent-hierarchy", "scripts", "agent-guard.mjs"
    )
    if os.path.exists(guard_src):
        shutil.copy2(guard_src, os.path.join(scripts_dir, "agent-guard.mjs"))

    # 7. Write README.md
    with open(os.path.join(AGENTS_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(README_CONTENT.strip() + "\n")

    return {
        "skills": skills_count,
        "agents": agents_count,
        "plugins": plugins_count,
        "docs": docs_count,
    }


def main():
    res = sync_all()
    print(
        f"build-agents: synchronized {res['skills']} skills, {res['agents']} agent charters, "
        f"{res['plugins']} department plugins, and {res['docs']} docs into Codex/.agents/"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
