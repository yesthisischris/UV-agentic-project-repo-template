from langsmith import trace
import structlog

log = structlog.get_logger()

class DevAgentState:
    def __init__(self, user_request: str, plan: list[str] | None = None):
        self.user_request = user_request
        self.plan = plan or []

    def copy(self, update: dict):
        new = DevAgentState(self.user_request, self.plan.copy())
        if 'plan' in update:
            new.plan = update['plan']
        return new

@trace(name="planner_node")
def planner_node(state: DevAgentState) -> DevAgentState:
    plan = ["task1", "task2"]
    log.info("planner.complete", task_count=len(plan))
    return state.copy(update={"plan": plan})
