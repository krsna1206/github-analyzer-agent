# from prompts import (
#     README_SYSTEM_PROMPT,
#     BUG_SYSTEM_PROMPT,
#     REVIEW_SYSTEM_PROMPT,
# )

# from llm import stream_response


# def build_llm_context(context):

#     tree = "\n".join(context["tree"][:100])   # first 100 entries only

#     dependencies = ""

#     for path, content in context["dependencies"].items():
#         dependencies += f"\n### {path}\n{content[:1000]}\n"

#     source_code = ""

#     count = 0
#     for path, content in context["source_files"].items():

#         source_code += f"""
# ### {path}

# {content[:2000]}
# """

#         count += 1
#         if count == 3:
#             break

#     return f"""
# Repository Name:
# {context['repo']}

# Owner:
# {context['owner']}

# Language:
# {context['language']}

# README:
# {context['readme'][:2000]}

# Folder Structure:
# {tree}

# Dependencies:
# {dependencies}

# Important Source Files:
# {source_code}
# """


# def generate_readme(context, user_prompt):

#     user_message = f"""
# {build_llm_context(context)}

# User Request:

# {user_prompt}
# """

#     yield from stream_response(
#         README_SYSTEM_PROMPT,
#         user_message
#     )

# def find_bugs(context, user_prompt):

#     user_message = f"""
# {build_llm_context(context)}

# User Request:

# {user_prompt}
# """

#     yield from stream_response(
#         BUG_SYSTEM_PROMPT,
#         user_message
#     )

# def review_repository(context, user_prompt):

#     user_message = f"""
# {build_llm_context(context)}

# User Request:

# {user_prompt}
# """

#     yield from stream_response(
#         REVIEW_SYSTEM_PROMPT,
#         user_message
#     )

from advancements.state import AgentState
from advancements.registry import ToolRegistry
from advancements.dispatcher import Dispatcher
from advancements.planner import Planner
from tools.repo_context import build_repository_context_tool
from tools.readme import generate_readme
from tools.bugs import find_bugs
from tools.review import review_repository
from advancements.logger import logger

class Analyzer:

    def __init__(self):

        # Create Registry
        self.registry = ToolRegistry()

        # Register Tools
        self.registry.register(
            "generate_readme",
            generate_readme
        )
        self.registry.register(
            "build_repository_context",
            build_repository_context_tool
        )
        self.registry.register(
            "find_bugs",
            find_bugs
        )

        self.registry.register(
            "review_repository",
            review_repository
        )

        # Create Dispatcher
        self.dispatcher = Dispatcher(self.registry)

        # Create Planner
        self.planner = Planner()
    # print(context)
    def analyze(self, repo_url, user_prompt):

        logger.info("Starting analysis...")

        # Create Agent State
        state = AgentState(
            repo_url=repo_url,
            user_prompt=user_prompt
        )

        iterations = 0

        while not state.finished:

            if iterations >= 10:
                raise RuntimeError(
                    "Maximum iterations reached."
                )

            iterations += 1

            logger.info("Planner selecting next tool...")

            tool_name = self.planner.next_tool(state)

            if tool_name is None:
                break

            logger.info(f"Planner selected: {tool_name}")

            state.current_tool = tool_name

            try:

                result = self.dispatcher.execute(
                    tool_name,
                    state
                )

                # Save only user-facing results
                if result is not None:
                    state.result = result

                state.completed_tools.add(tool_name)
                state.tool_history.append(tool_name)

            except Exception:

                logger.exception(
                    f"Error while executing '{tool_name}'"
                )

                state.finished = True
                raise

        logger.info("Analysis completed.")

        return state.result
