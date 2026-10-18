#!/usr/bin/env python3
"""Graphical installer for Headcount Organization (Codex & Antigravity).

Cross-platform: Windows, macOS, and Linux.
Automatically synchronizes the latest skills, agents, plugins, docs, and rules from the
repository before installing.

Options:
1. Install Globally: Syncs and installs into user profile (~/.agents and ~/.codex).
2. Install to Project: Syncs and copies the complete organization to a chosen project folder.
"""
import glob
import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(BASE_DIR)
SOURCE_AGENTS_DIR = os.path.join(BASE_DIR, ".agents")


def perform_sync(repo_root=REPO_ROOT) -> dict:
    """Synchronizes all skills, agent charters, plugins, docs, and rules from headcount."""
    sys.path.insert(0, os.path.join(repo_root, "scripts"))
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "build_agents", os.path.join(repo_root, "scripts", "build-agents.py")
    )
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    return builder.sync_all(repo_root)


def run_cli_fallback():
    """Interactive CLI menu for headless Linux environments or terminal use."""
    print("\n" + "=" * 52)
    print(" Headcount Organization Installer (Terminal Mode)   ")
    print("=" * 52 + "\n")
    print("1. Install Globally (User Profile: ~/.agents & ~/.codex)")
    print("2. Install to Specific Project Folder")
    print("3. Exit\n")

    choice = input("Select an option [1-3]: ").strip()

    if choice == "1":
        print("\n[SYNC] Synchronizing latest repository files...")
        res = perform_sync(REPO_ROOT)
        print(f"[SYNC] Synced {res['skills']} skills, {res['agents']} agents, {res['plugins']} plugins.")

        src_skills = os.path.join(SOURCE_AGENTS_DIR, "skills")
        src_agents = os.path.join(SOURCE_AGENTS_DIR, "agents")
        for target_base in ["~/.agents", "~/.codex"]:
            dst_skills = os.path.expanduser(os.path.join(target_base, "skills"))
            os.makedirs(dst_skills, exist_ok=True)
            for item in os.listdir(src_skills):
                s = os.path.join(src_skills, item)
                d = os.path.join(dst_skills, item)
                if os.path.isdir(s):
                    if os.path.exists(d):
                        shutil.rmtree(d)
                    shutil.copytree(s, d)

            if os.path.isdir(src_agents):
                dst_agents = os.path.expanduser(os.path.join(target_base, "agents"))
                os.makedirs(dst_agents, exist_ok=True)
                for item in os.listdir(src_agents):
                    s = os.path.join(src_agents, item)
                    d = os.path.join(dst_agents, item)
                    if os.path.isfile(s):
                        shutil.copy2(s, d)
        print("\n[SUCCESS] Installed skills and agent charters to ~/.agents and ~/.codex")

    elif choice == "2":
        target = input("Enter target project root path: ").strip().strip('"').strip("'")
        if not target or not os.path.isdir(target):
            print(f"\n[ERROR] Directory not found: {target}")
            return

        print("\n[SYNC] Synchronizing latest repository files...")
        res = perform_sync(REPO_ROOT)
        print(f"[SYNC] Synced {res['skills']} skills, {res['agents']} agents, {res['plugins']} plugins.")

        dst_agents = os.path.join(target, ".agents")
        if os.path.exists(dst_agents):
            shutil.rmtree(dst_agents)
        shutil.copytree(SOURCE_AGENTS_DIR, dst_agents)
        print(f"\n[SUCCESS] Installed complete organization to {dst_agents}")

    elif choice == "3":
        print("Exiting.")
    else:
        print("Invalid choice.")


def run_gui():
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk

    class SkillsInstallerApp:
        def __init__(self, root: tk.Tk):
            self.root = root
            self.root.title("Headcount Organization Installer")
            self.root.geometry("600x460")
            self.root.minsize(540, 400)

            # Cross-platform theme selection
            self.style = ttk.Style()
            try:
                available = self.style.theme_names()
                if "aqua" in available:
                    self.style.theme_use("aqua")
                elif "vista" in available:
                    self.style.theme_use("vista")
                elif "clam" in available:
                    self.style.theme_use("clam")
            except Exception:
                pass

            self._build_ui()
            self._check_source()

        def _build_ui(self):
            main_frame = ttk.Frame(self.root, padding="20")
            main_frame.pack(fill=tk.BOTH, expand=True)

            # Header
            title_label = ttk.Label(
                main_frame,
                text="Headcount Organization Installer",
                font=("Segoe UI", 16, "bold"),
            )
            title_label.pack(anchor="w", pady=(0, 4))

            subtitle_label = ttk.Label(
                main_frame,
                text="Installs the 16-department organization for Google Antigravity & OpenAI Codex.\n"
                "Automatically synchronizes the latest changes from the repository before installing.",
                font=("Segoe UI", 9),
                foreground="#555555",
            )
            subtitle_label.pack(anchor="w", pady=(0, 14))

            # Actions Card
            actions_frame = ttk.LabelFrame(main_frame, text=" Installation Options ", padding="15")
            actions_frame.pack(fill=tk.X, pady=(0, 14))

            # Button 1: Global install
            btn_global = ttk.Button(
                actions_frame,
                text="Install Globally (User Profile)",
                command=self.install_globally,
            )
            btn_global.pack(fill=tk.X, pady=(0, 4))

            desc_global = ttk.Label(
                actions_frame,
                text="Syncs and installs skills and agent charters into ~/.agents and ~/.codex.",
                font=("Segoe UI", 8),
                foreground="#666666",
            )
            desc_global.pack(anchor="w", pady=(0, 12))

            # Button 2: Project install
            btn_project = ttk.Button(
                actions_frame,
                text="Install to Specific Project Folder...",
                command=self.install_to_project,
            )
            btn_project.pack(fill=tk.X, pady=(0, 4))

            desc_project = ttk.Label(
                actions_frame,
                text="Syncs and copies the full .agents organization (skills, agents, plugins, docs, rules) into a project.",
                font=("Segoe UI", 8),
                foreground="#666666",
            )
            desc_project.pack(anchor="w", pady=(0, 2))

            # Status / Log Area
            log_frame = ttk.LabelFrame(main_frame, text=" Log Output ", padding="10")
            log_frame.pack(fill=tk.BOTH, expand=True)

            self.log_text = tk.Text(
                log_frame,
                height=6,
                wrap=tk.WORD,
                font=("Consolas", 9),
                state=tk.DISABLED,
                bg="#f8f9fa",
                relief=tk.FLAT,
            )
            self.log_text.pack(fill=tk.BOTH, expand=True)

        def log(self, message: str):
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, message + "\n")
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)

        def _check_source(self):
            skills_dir = os.path.join(SOURCE_AGENTS_DIR, "skills")
            if os.path.isdir(skills_dir):
                count = len([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
                self.log(f"[READY] Ready to install {count} skills and 19 subagent charters.")
            else:
                self.log("[READY] Ready to sync and install.")

        def install_globally(self):
            confirm = messagebox.askyesno(
                "Confirm Global Installation",
                "This will synchronize the latest files and install them into your user profile:\n\n"
                f"• {os.path.expanduser('~/.agents/skills')}\n"
                f"• {os.path.expanduser('~/.codex/skills')}\n"
                f"• {os.path.expanduser('~/.agents/agents')}\n"
                f"• {os.path.expanduser('~/.codex/agents')}\n\n"
                "Do you wish to proceed?",
            )
            if not confirm:
                return

            try:
                self.log("[SYNC] Synchronizing latest repository files before installation...")
                res = perform_sync(REPO_ROOT)
                self.log(
                    f"[SYNC] Synced {res['skills']} skills, {res['agents']} agents, "
                    f"{res['plugins']} plugins, {res['docs']} docs."
                )

                src_skills = os.path.join(SOURCE_AGENTS_DIR, "skills")
                src_agents = os.path.join(SOURCE_AGENTS_DIR, "agents")

                for target_base in ["~/.agents", "~/.codex"]:
                    dst_skills = os.path.expanduser(os.path.join(target_base, "skills"))
                    os.makedirs(dst_skills, exist_ok=True)
                    for item in os.listdir(src_skills):
                        s = os.path.join(src_skills, item)
                        d = os.path.join(dst_skills, item)
                        if os.path.isdir(s):
                            if os.path.exists(d):
                                shutil.rmtree(d)
                            shutil.copytree(s, d)

                    if os.path.isdir(src_agents):
                        dst_agents = os.path.expanduser(os.path.join(target_base, "agents"))
                        os.makedirs(dst_agents, exist_ok=True)
                        for item in os.listdir(src_agents):
                            s = os.path.join(src_agents, item)
                            d = os.path.join(dst_agents, item)
                            if os.path.isfile(s):
                                shutil.copy2(s, d)

                self.log("[GLOBAL] Successfully installed skills and agent charters globally.")
                messagebox.showinfo(
                    "Installation Complete",
                    f"Synchronized and installed {res['skills']} skills and {res['agents']} subagent charters globally!\n\n"
                    "Antigravity and Codex can now use them across all workspaces.",
                )
            except Exception as e:
                self.log(f"[ERROR] Global install failed: {e}")
                messagebox.showerror("Error", f"Failed to install globally:\n{e}")

        def install_to_project(self):
            selected_dir = filedialog.askdirectory(
                title="Select Target Project Root Folder",
                mustexist=True,
            )
            if not selected_dir:
                return

            target_agents_dir = os.path.join(selected_dir, ".agents")

            try:
                self.log("[SYNC] Synchronizing latest repository files before installation...")
                res = perform_sync(REPO_ROOT)
                self.log(
                    f"[SYNC] Synced {res['skills']} skills, {res['agents']} agents, "
                    f"{res['plugins']} plugins, {res['docs']} docs."
                )

                if os.path.exists(target_agents_dir):
                    shutil.rmtree(target_agents_dir)
                shutil.copytree(SOURCE_AGENTS_DIR, target_agents_dir)

                self.log(f"[PROJECT] Successfully installed complete organization to {target_agents_dir}")
                messagebox.showinfo(
                    "Installation Complete",
                    f"Successfully synchronized and installed the complete headcount organization into:\n{target_agents_dir}\n\n"
                    f"Includes:\n"
                    f"• All {res['skills']} Skills (.agents/skills)\n"
                    f"• {res['agents']} Subagent Charters (.agents/agents)\n"
                    f"• {res['plugins']} Department Plugins (.agents/plugins)\n"
                    f"• Multi-Agent Rules & Surface Maps (.agents/rules)\n\n"
                    "Open this project in Antigravity or Codex to use them!",
                )
            except Exception as e:
                self.log(f"[ERROR] Project install failed: {e}")
                messagebox.showerror("Error", f"Failed to install to project:\n{e}")

    root = tk.Tk()
    app = SkillsInstallerApp(root)
    root.mainloop()


def main():
    if "--cli" in sys.argv:
        run_cli_fallback()
        return

    try:
        run_gui()
    except Exception as e:
        print(f"GUI not available ({e}). Starting interactive terminal mode...")
        run_cli_fallback()


if __name__ == "__main__":
    main()
