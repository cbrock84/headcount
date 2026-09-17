#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Detect python3 or python
if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "Error: Python is required but not found in PATH." >&2
    exit 1
fi

exec "$PYTHON_BIN" "$DIR/installer_gui.py" "$@"
