| Agent Name   | Entry-point                               | State Model                      | Purpose |
|--------------|-------------------------------------------|----------------------------------|---------|
| Developer    | `src/uv_agentic/agents/developer_agent.py`| `uv_agentic.state.PlanState`     | Plan / build / review orchestrator |
| CodeReviewer | `src/uv_agentic/agents/code_reviewer.py`  | n/a                              | LLM-powered diff review           |
