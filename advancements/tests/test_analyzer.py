from analyzer import Analyzer


def test_tool_registration():

    analyzer = Analyzer()

    assert analyzer.registry.list_tools() == [
        "generate_readme",
        "find_bugs",
        "review_repository"
    ]