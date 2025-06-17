# Welcome to this UV Agentic Project

This is the documentation site.

## Quick Start

Get started with the template:

```bash
# Create a new project from this template
gh repo create my-agent --template UV-agentic-project-repo-template

# Navigate to your project
cd my-agent

# Install the project in editable mode
python -m pip install -e .

# Run the unit tests
pytest -q
```

## Architecture Overview

This template provides a lightweight starting point for building AI agents. It uses a modern Python stack (Hatch, Ruff, MyPy) and can be extended with frameworks such as LangGraph or the Model Context Protocol if your project requires them.

## Key Features

- **Rapid Development**: Get from idea to working agent quickly
- **Clean Project Layout**: Straightforward structure for code, tests and docs
- **CI/CD Ready**: GitHub Actions workflow for testing and deployment
- **Customizable**: Integrate memory backends or external frameworks as needed

## Project Structure

```
my-agent/
├── src/            # project code
├── tests/          # unit tests
├── docs/           # documentation
└── .github/        # CI configuration

```

## Next Steps

- [Architecture Overview](architecture.md)
- [Contributing Guide](CONTRIBUTING.md)
- [API Reference](api/index.md)

---
