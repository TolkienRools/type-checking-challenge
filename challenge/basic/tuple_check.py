"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""
from typing import Tuple


def foo(x: Tuple[str, int]):
    pass


foo(("foo", 1))
foo((1, 2)) # type: ignore
foo(("foo", "bar")) # type: ignore
foo((1, "bar")) # type: ignore
