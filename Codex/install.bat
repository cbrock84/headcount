@echo off
start "" pythonw "%~dp0installer_gui.py"
if %errorlevel% neq 0 (
    python "%~dp0installer_gui.py"
)
