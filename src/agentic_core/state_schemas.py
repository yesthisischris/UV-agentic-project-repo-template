"""Pydantic state models for LangGraph stages."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class PlanningState(BaseModel):
    """State for the planning stage."""

    model_config = ConfigDict(extra="forbid")

    goal: str = Field(..., description="Overall goal the agent is pursuing")
    plan: Optional[List[str]] = Field(
        default=None, description="List of planned actions to achieve the goal"
    )

    def __str__(self) -> str:
        diff = self.model_dump(exclude_none=True, exclude_defaults=True)
        return f"PlanningState({diff})"


class ExecutionState(BaseModel):
    """State while executing a plan."""

    model_config = ConfigDict(extra="forbid")

    goal: str = Field(..., description="Overall goal the agent is pursuing")
    plan: List[str] = Field(..., description="List of actions to execute")
    last_step: Optional[str] = Field(
        default=None, description="The action most recently executed"
    )
    steps_completed: List[str] = Field(
        default_factory=list, description="Actions completed so far"
    )

    def __str__(self) -> str:
        diff = self.model_dump(exclude_none=True, exclude_defaults=True)
        return f"ExecutionState({diff})"


class SummaryState(BaseModel):
    """State for summarization after execution."""

    model_config = ConfigDict(extra="forbid")

    goal: str = Field(..., description="Overall goal the agent was pursuing")
    plan: List[str] = Field(..., description="Executed plan")
    summary: Optional[str] = Field(
        default=None, description="Final summary of execution"
    )

    def __str__(self) -> str:
        diff = self.model_dump(exclude_none=True, exclude_defaults=True)
        return f"SummaryState({diff})"

