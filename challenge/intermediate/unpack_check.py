"""
TODO:

`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""

from typing import TypedDict, Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    ...


person: Person = {"name": "The Meaning of Life",
                  "age": 1983}
foo(**person)
foo(**{"name": "Brian", "age": 30}) # type: ignore

foo(**{"name": "Brain"}) # type: ignore # expect-type-error
person2: dict[str, object] = {"name": "Brain",
                              "age": 20}
foo(**person2) # type: ignore # expect-type-error
foo(**{"name": "Brain", "age": "1979"}) # type: ignore # expect-type-error
