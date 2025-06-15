from uv_agentic import PlanningState, ExecutionState, SummaryState


def test_state_instantiation():
    planning = PlanningState(goal="test goal", plan=["step1", "step2"])
    assert planning.goal == "test goal"
    exec_state = ExecutionState(goal="goal", plan=["step1"])  # minimal
    assert exec_state.steps_completed == []
    summary = SummaryState(goal="goal", plan=["step1"], summary="done")
    assert summary.summary == "done"
