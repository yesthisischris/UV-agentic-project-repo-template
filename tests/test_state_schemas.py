from uv_agentic import PlanningState, ExecutionState, SummaryState


def test_state_instantiation():
    planning = PlanningState(goal="test goal", plan=["step1", "step2"])
    assert planning.goal == "test goal"
    exec_state = ExecutionState(goal="goal", plan=["step1"])  # minimal
    assert exec_state.steps_completed == []
    summary = SummaryState(goal="goal", plan=["step1"], summary="done")
    assert summary.summary == "done"


def test_extra_keys_forbidden():
    try:
        PlanningState(goal="x", plan=[], junk=1)
    except Exception as exc:  # Pydantic ValidationError
        assert "Extra inputs are not permitted" in str(exc)
    else:
        raise AssertionError("extra keys not forbidden")


def test_str_shows_diff():
    state = ExecutionState(goal="g", plan=["a"], last_step=None)
    assert str(state) == "ExecutionState({'goal': 'g', 'plan': ['a']})"
