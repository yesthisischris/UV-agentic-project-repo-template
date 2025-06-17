from pydantic import BaseModel, ConfigDict


class PlanState(BaseModel):
    user_request: str
    plan: list[str] = []

    model_config = ConfigDict(extra="forbid")
