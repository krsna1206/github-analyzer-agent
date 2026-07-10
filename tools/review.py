from prompts import (
    README_SYSTEM_PROMPT,
    BUG_SYSTEM_PROMPT,
    REVIEW_SYSTEM_PROMPT,
)

from llm import stream_response
from .context_builder import build_llm_context
from .context_validator import validate_context
def review_repository(state):
    context = state.context
    user_prompt = state.user_prompt
    validate_context(context)
    user_message = f"""
{build_llm_context(context)}

User Request:

{user_prompt}
"""

    yield from stream_response(
        REVIEW_SYSTEM_PROMPT,
        user_message
    )
