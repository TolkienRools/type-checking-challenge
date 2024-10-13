"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

import typing



class Foo:
    def return_self(self) -> typing.Self: # type: ignore
        ...


class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()

sf: SubclassOfFoo = Foo().return_self() # type: ignore # expect-type-error
