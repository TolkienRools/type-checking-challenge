"""
TODO:

foo should accept a empty tuple argument.
"""


def foo(x: tuple[()]):
    pass


foo(())
foo((1)) # type: ignore # expect-type-error
