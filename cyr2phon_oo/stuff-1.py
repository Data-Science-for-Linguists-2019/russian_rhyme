import regex as re
from typing import Optional

# experiment with function factory to bind constants with function

"""
Create callable named function, bundling constants and callback with function code

Keyword parameters:
constants (dict; optional): name:value; e.g., for regex expressions and translation tables
callbacks (dict; optional): name:value; e.g., for re.sub() replacement functions
function (str; required): function body as (possibly multiline) string, with proper indentation

Returns:
str
"""


def make_f(constants: Optional[dict] = None, callbacks: Optional[dict] = None, function: str = None):
    # FIXME: getting "shadowing inner scope" and "unused local" warnings; is this a problem?
    def f(line: str, constants: Optional[dict] = constants, callbacks: Optional[dict] = callbacks,
          function=function) -> str:
        return eval(function)
    return f


# sample function, uses two constants, one of which is a compiled regex
a = make_f(constants={
    "pattern": re.compile(r"[AEIOU]"),
    "age": 33},
    function="""
constants["pattern"].sub('x', line.upper()), (constants["age"])
""")
print("Y", a("koala"), "Y")
print("Z", a("platypus"), "Z")
print(type(a))
print(dir(a))
