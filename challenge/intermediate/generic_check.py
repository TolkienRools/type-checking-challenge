"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""
from typing import TypeVar
from typing import List, assert_type


T = TypeVar('T')

def add(a: T, b: T) -> T: # type: ignore
    # type: ignore
    ...


assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
# type: ignore
assert_type(add(1, "2"), int) # type: ignore # expect-type-error
