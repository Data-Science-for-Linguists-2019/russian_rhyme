import regex as re
from typing import Optional

# experiment with function factory to bind constants with function

class f:
    def __init__(self, name: str, constants: Optional[dict] = {}, callbacks: Optional[dict] = {}, function:str = ""):
        self.__name__ = name
        self.constants = constants
        self.callbacks = callbacks
        self.function = function

    def __call__(self, line):
        exec(self.function)
