import regex as re
from typing import Optional


# experiment with function factory to bind constants with function

class F:
    """
    Create named function, bundling constants and callback with name and function code

    Keyword parameters:
    name (str; required): function name
    constants (dict; optional): name:value; for regex expressions and translation tables
    callbacks (dict; optional): name:value; for re.sub() replacement functions
    function (str; required): function body as (possibly multiline) string, with proper indentation

    Returns:
    str (specific to this project; could be told to return other types)
    """
    def __init__(self, name: str, constants: Optional[dict] = None, callbacks: Optional[dict] = None,
                 function: str = None):
        self.__name__ = name
        self.constants = constants
        self.callbacks = callbacks
        self.function = function

    def __call__(self, line: str) -> str:
        exec(self.function)


# sample function; name is 'tuber', uses two constants, one of which is a regex
a = F('tuber',
      constants={
          "pattern": re.compile(r"[AEIOU]"),
          "age": 33},
      function="""
print(self.constants["pattern"].sub('x', line.upper()) + str(self.constants["age"]))
""")
a('spud')
