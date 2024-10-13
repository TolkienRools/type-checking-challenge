"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""
from typing import Any


def foo(argument: Any):
    """⬆️ Change me. No need to implement the function."""


foo(1)
foo("10")
foo(1, 2) # type: ignore # expect-type-error