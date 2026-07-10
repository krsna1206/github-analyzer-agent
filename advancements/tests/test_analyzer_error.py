import pytest

from analyzer import Analyzer


def test_unknown_request():

    analyzer = Analyzer()

    result = analyzer.analyze(
        "https://github.com/pallets/flask",
        "Do something impossible"
    )

    assert result is None