from advancements.planner import Planner
from advancements.state import AgentState


def test_first_tool():

    planner = Planner()

    state = AgentState("repo")

    assert planner.next_tool(state) == "clone_repo"

def test_second_tool():

    planner = Planner()

    state = AgentState("repo")

    state.completed_tools.add("clone_repo")

    assert planner.next_tool(state) == "detect_languages"
def test_third_tool():

    planner = Planner()

    state = AgentState("repo")

    state.completed_tools.update({
        "clone_repo",
        "detect_languages"
    })

    assert planner.next_tool(state) == "dependency_scan"
def test_finish():

    planner = Planner()

    state = AgentState("repo")

    state.completed_tools.update({
        "clone_repo",
        "detect_languages",
        "dependency_scan"
    })

    assert planner.next_tool(state) is None