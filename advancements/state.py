from dataclasses import dataclass, field

# @dataclass
# class AgentState:
#     repo_url: str

#     context: dict = field(default_factory=dict)

#     observations: list = field(default_factory=list)

#     completed_tools: set = field(default_factory=set)

#     next_tool: str | None = None

#     finished: bool = False
from advancements.logger import logger
@dataclass
class AgentState:
    # logger.info("Starting analysis")
    # User Input
    repo_url: str
    user_prompt: str

    # Repository Information
    context: dict = field(default_factory=dict)

    # Agent Execution
    current_tool: str | None = None
    completed_tools: set = field(default_factory=set)
    tool_history: list = field(default_factory=list)

    # Final Output
    result = None

    # Agent Control
    finished: bool = False
    def __post_init__(self):
        logger.info(f"Starting analysis for {self.repo_url}")