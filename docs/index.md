# Welcome to this UV Agentic Project

This is the documentation site.

## Quick Start

Get started with building your AI agent:

```bash
# Create a new project from this template
gh repo create my-agent --template langgraph-mcp-template

# Navigate to your project
cd my-agent

# Set up the development environment
bash scripts/bootstrap.sh
```

## Architecture Overview

This template provides a solid foundation for building sophisticated AI agents using:

- **LangGraph**: For orchestrating complex agent workflows
- **Model Context Protocol**: For tool integration and external system access
- **Vector Memory**: For long-term memory and context retrieval
- **Modern Python Stack**: Hatch, Ruff, MyPy for development workflow

## Key Features

- **Rapid Development**: Get from idea to working agent quickly
- **Tool Integration**: Easy MCP server setup and tool binding
- **Memory Management**: Built-in vector store and state management
- **CI/CD Ready**: GitHub Actions workflows for testing and deployment
- **Observability**: LangSmith integration for monitoring and debugging

## Project Structure

```
my-agent/
├── src/my_agent_project/
│   ├── agents/          # Agent implementations
│   ├── graphs/          # LangGraph workflow definitions
│   ├── memory/          # Vector store and state schemas
│   └── prompts/         # System and user prompts
├── scripts/             # Development and deployment scripts
└── docs/               # Documentation (this site)
```

## Next Steps

- [Architecture Overview](architecture.md)
- [Contributing Guide](contributing.md)
- [API Reference](api/)

---
