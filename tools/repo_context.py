from repo_parser import build_repository_context


def build_repository_context_tool(state):

    context = build_repository_context(
        state.repo_url
    )

    # Store the repository context in the shared state
    state.context = context

    # Infrastructure tools don't return user-facing results
    return None