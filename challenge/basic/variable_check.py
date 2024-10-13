"""
TODO:

`a` should be an integer.
"""
from typing import Any


a: int

a = 2
a = "1"  # type: ignore # expect-type-error
