from advancements.state import AgentState
from advancements.logger import logger


class Planner:

    def next_tool(self, state: AgentState):

        logger.info("Planner selecting next tool...")

        # Step 1: Build repository context first
        if (
            not state.context
            and "build_repository_context" not in state.completed_tools
        ):
            logger.info("Planner selected: build_repository_context")
            return "build_repository_context"

        prompt = state.user_prompt.lower()

        # Step 2: README
        if (
            "readme" in prompt
            and "generate_readme" not in state.completed_tools
        ):
            logger.info("Planner selected: generate_readme")
            return "generate_readme"

        # Step 3: Bug Finder
        if (
            "bug" in prompt
            and "find_bugs" not in state.completed_tools
        ):
            logger.info("Planner selected: find_bugs")
            return "find_bugs"

        # Step 4: Repository Review
        if (
            "review" in prompt
            and "review_repository" not in state.completed_tools
        ):
            logger.info("Planner selected: review_repository")
            return "review_repository"

        logger.info("Planner finished. No more tools to execute.")

        state.finished = True
        return None