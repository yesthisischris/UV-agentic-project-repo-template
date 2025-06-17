# Contributor Guidelines

This repository demonstrates a light-weight LangGraph/MCP workflow for building modules. Changes should follow these conventions:

- Follow PEP8 style with 4-space indentation and type hints.
- Keep the workflow modular. Each LangGraph node should be a small function that accepts and returns a dictionary of state.
- Never use emojis
- Document public classes and functions with docstrings.
- Code should be well documented with explanations for major sections.
- Add a descriptive comment block at the top of every Python file explaining its
  purpose and overall structure.
- Prefer simple, easily testable functions. If logic grows, factor it into
  helpers under `src/lmb_agent`.
- Run `ruff --fix` and `pytest` before committing when tests exist.
- Document new commands or examples in `README.md`.
- Security, modularity, and agent action traceability are paramount.
- Pull Request Summaries should briefly explain the rationale for changes and mention updated
  files.
