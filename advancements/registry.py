from typing import Callable


class ToolRegistry:

    def __init__(self):
        self._tools = {}

    def register(self, name: str, func: Callable):
        self._tools[name] = func

    def get(self, name: str):
        return self._tools.get(name)

    def list_tools(self):
        return list(self._tools.keys())
    