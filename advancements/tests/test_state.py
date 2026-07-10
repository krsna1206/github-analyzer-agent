from advancements.state import AgentState

def test_state_initialization():

    state = AgentState("https://github.com/test/repo")

    assert state.repo_url.endswith("repo")
    assert state.context == {}
    assert state.observations == []
    assert state.completed_tools == set()
    assert state.finished is False