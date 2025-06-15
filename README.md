# Umbra Versa Agentic Project Template

> Production‑ready scaffold for **agentic developer bots** powered by
> LangChain + LangGraph and backed by MCP‑capable models (o3‑pro, Claude 4)
> and accessing external tools and databases

## Quick‑Start

```bash
git clone --template=gh:your‑org/langgraph‑mcp‑template my‑agent
cd my‑agent
scripts/bootstrap.sh          # sets venv, pre‑commit, prints next steps

cp env.example .env           # add your API keys
docker‑compose up -d          # spin up redis + pgvector

python -m my_agent_project    # run CLI entry
