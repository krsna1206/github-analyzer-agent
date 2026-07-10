from advancements.registry import ToolRegistry


def dummy_tool():
    return "Executed"


def test_register_tool():

    registry = ToolRegistry()

    registry.register("dummy", dummy_tool)

    assert registry.get("dummy") == dummy_tool

def test_list_tools():

    registry = ToolRegistry()

    registry.register("dummy", dummy_tool)

    assert registry.list_tools() == ["dummy"]

def test_unknown_tool():

    registry = ToolRegistry()

    assert registry.get("nothing") is None