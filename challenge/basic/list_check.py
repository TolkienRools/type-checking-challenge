"""
TODO:

foo should accept a list argument, whose elements are string.
"""
from typing import Sequence


def foo(x: Sequence[str]):
    pass


foo(["foo", "bar"])
foo(["foo", 1]) # type: ignore
