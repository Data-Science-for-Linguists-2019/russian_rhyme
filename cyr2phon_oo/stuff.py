import regex as re
from typing import Optional


# experiment with function factory to bind constants with function
# can we return, instead of printing explicitly?

class F:
    """
    Create callable named function, bundling constants and callback with function code

    Keyword parameters:
    constants (dict; optional): name:value; e.g., for regex expressions and translation tables
    callbacks (dict; optional): name:value; e.g., for re.sub() replacement functions
    function (str; required): function body as (possibly multiline) string, with proper indentation

    Returns:
    str

    TODO: Can we use return, instead of print, to get the result
    """
    def __init__(self, constants: Optional[dict] = None, callbacks: Optional[dict] = None,
                 function: str = None):
        self.constants = constants
        self.callbacks = callbacks
        self.function = function

    def __call__(self, line: str) -> str:
        exec(self.function)


# sample function, uses two constants, one of which is a compiled regex
a = F(constants={
          "pattern": re.compile(r"[AEIOU]"),
          "age": 33},
      function="""
print(self.constants["pattern"].sub('x', line.upper()), (self.constants["age"]))
""")
a('spud') # returns >>> SPxD 33
