#!/usr/bin/env bash
set -euo pipefail

echo "Bootstrapping LangGraph MCP template development environment…"

# ---------------------------------------------------------------------------
# 1.  Sanity checks
# ---------------------------------------------------------------------------

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: Python 3.11+ is required but not found." >&2
    exit 1
fi

PY_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
echo "Found Python ${PY_VERSION}"

# ---------------------------------------------------------------------------
# 2.  Install build tooling (pip, hatch) – user-local to avoid sudo
# ---------------------------------------------------------------------------

python3 -m pip install --upgrade --user pip hatch

# Ensure the user-local bin directory is on PATH for this session
# shellcheck disable=SC2016
export PATH="$HOME/.local/bin:$PATH"

# ---------------------------------------------------------------------------
# 3.  Create Hatch environment (uses pyproject.toml)
# ---------------------------------------------------------------------------

echo "Creating Hatch virtual environment…"
hatch env create

# ---------------------------------------------------------------------------
# 4.  Pre-commit hooks
# ---------------------------------------------------------------------------

if ! command -v pre-commit >/dev/null 2>&1; then
    echo "Installing pre-commit…"
    python3 -m pip install --user pre-commit
fi

echo "Installing pre-commit hooks…"
pre-commit install
pre-commit install --hook-type commit-msg

# ---------------------------------------------------------------------------
# 5.  Environment template
# ---------------------------------------------------------------------------

if [[ ! -f .env ]]; then
    echo "Creating .env from template…"
    cp env.example .env
    echo "Edit .env and add your API keys before running the agent."
fi

# ---------------------------------------------------------------------------
# 6.  Quick smoke test (optional)
# ---------------------------------------------------------------------------

echo "Running initial test harness (will be skipped if none exist)…"
if hatch run test:pytest --version >/dev/null 2>&1; then
    echo "Tests discovered – run 'hatch run test:pytest' for full suite."
else
    echo "No tests implemented yet (that is fine for a fresh repo)."
fi

# ---------------------------------------------------------------------------
# 7.  Final message
# ---------------------------------------------------------------------------

cat <<'EOF'

Bootstrap complete.

Next steps:
  1. Populate .env with your API keys.
  2. Start coding your agent in src/uv_agentic/.
  3. Run 'hatch run test:pytest' to execute tests.
  4. Run 'hatch run dev' (or your preferred entry-point) to start a dev session.

Happy coding!
EOF
