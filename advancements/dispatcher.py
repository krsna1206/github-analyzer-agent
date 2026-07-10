from advancements.registry import ToolRegistry
from advancements.logger import logger


class Dispatcher:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, tool_name: str, state):

        tool = self.registry.get(tool_name)

        if tool is None:
            raise ValueError(
                f"Tool '{tool_name}' is not registered."
            )

        logger.info(f"Executing: {tool_name}")

        result = tool(state)

        logger.info(f"Completed: {tool_name}")

        return result