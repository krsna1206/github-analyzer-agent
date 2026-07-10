import pytest

from tools.context_validator import validate_context


def test_empty_context():

    with pytest.raises(ValueError):
        validate_context({})

def test_missing_tree():

    context = {
        "repo": "demo",
        "owner": "me",
        "language": "Python",
        "readme": "",
        "dependencies": {},
        "source_files": {}
    }
    with pytest.raises(ValueError):
        validate_context(context)
def test_valid_context():

    context = {
        "repo": "demo",
        "owner": "me",
        "language": "Python",
        "readme": "",
        "tree": [],
        "dependencies": {},
        "source_files": {}
    }

    assert validate_context(context) is True
