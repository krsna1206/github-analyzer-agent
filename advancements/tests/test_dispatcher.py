from advancements.dispatcher import Dispatcher
from advancements.registry import ToolRegistry
from advancements.state import AgentState


def dummy_tool(state):
    state.context["status"] = "executed"

def test_dispatcher_executes_tool():

    registry = ToolRegistry()
    registry.register("dummy", dummy_tool)

    dispatcher = Dispatcher(registry)

    state = AgentState("https://github.com/test/repo")

    dispatcher.execute("dummy", state)

    assert state.context["status"] == "executed"

import pytest


def test_unknown_tool():

    registry = ToolRegistry()

    dispatcher = Dispatcher(registry)

    state = AgentState("repo")

    with pytest.raises(ValueError):
        dispatcher.execute("unknown", state)