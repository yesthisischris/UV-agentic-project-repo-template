"""Pydantic state models for LangGraph stages."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class PlanningState(BaseModel):
    """State for the planning stage."""

    goal: str = Field(..., description="Overall goal the agent is pursuing")
    plan: Optional[List[str]] = Field(
        default=None, description="List of planned actions to achieve the goal"
    )


class ExecutionState(BaseModel):
    """State while executing a plan."""

    goal: str = Field(..., description="Overall goal the agent is pursuing")
    plan: List[str] = Field(..., description="List of actions to execute")
    last_step: Optional[str] = Field(
        default=None, description="The action most recently executed"
    )
    steps_completed: List[str] = Field(
        default_factory=list, description="Actions completed so far"
    )


class SummaryState(BaseModel):
    """State for summarization after execution."""

    goal: str = Field(..., description="Overall goal the agent was pursuing")
    plan: List[str] = Field(..., description="Executed plan")
    summary: Optional[str] = Field(
        default=None, description="Final summary of execution"
    )

