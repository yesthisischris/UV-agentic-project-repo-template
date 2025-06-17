import structlog

log = structlog.get_logger()

class DeveloperAgent:
    def __init__(self, state):
        self.state = state

    def display_plan(self):
        # old
        # console.print(Panel("Generated plan", ...))
        # new
        log.info("plan_generated", tasks=len(self.state.plan))
