"""
TODO:

foo should accept an integer argument.
"""


def foo(x: int):
    pass


foo(10)

foo("10") # type: ignore # expect-type-error
