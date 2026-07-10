REQUIRED_FIELDS = [
    "repo",
    "owner",
    "language",
    "readme",
    "tree",
    "dependencies",
    "source_files",
]


def validate_context(context: dict):

    if not context:
        raise ValueError("Repository context is empty.")

    for field in REQUIRED_FIELDS:

        if field not in context:
            raise ValueError(
                f"Repository context is missing required field: '{field}'"
            )

    return True