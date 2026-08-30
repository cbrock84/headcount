# Headcount Organization for Antigravity and Codex

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
Copy-Item -Recurse "Codex/.agents" "C:\path\to\my-project\"
```

When you open `my-project` in Antigravity or run OpenAI Codex:
- All 143 skills are detected via progressive disclosure.
- All 19 subagent charters are available for delegation.
- Department rules and surface governance in `rules/AGENTS.md` guide the agents.
