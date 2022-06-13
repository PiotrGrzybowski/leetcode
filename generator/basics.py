import typing
from typing import TypeVar, Generic, get_args

T = TypeVar('T')
S = TypeVar('S')


class OwnGeneric(Generic[T]):
    def __init__(self):
        self.origin_class = None


class Vector(Generic[T]):
    def __init__(self, values: list[T]) -> None:
        super().__init__()
        self.values = values

    name = 'vector'


class PythonVector(Generic[T]):
    @staticmethod
    def default() -> str:
        return "[]"

class PythonMap(Generic[T]):
    pass


class GoVector(Vector[T]):
    @staticmethod
    def resolve():
        print("a")
    # def new(self) -> str:
    #     return f"[]{self.__dict__['__orig_class__'].__args__[0].name}{{}}"
    #
    # @staticmethod
    # def typename(generic) -> str:
    #     return f"[]{generic[0]}"
    #
    # def smartname(self):
    #     print(self.__dict__)
    #     # print(self.__dict__['__orig_class__'])


class RustVector(Vector[T]):
    pass


class GoMap(Generic[T, S]):
    def _resolve(self, generic):
        print(generic.__origin__)
        for a in generic.__args__:
            a._resolve()


class Int:
    def __init__(self, value: int) -> None:
        self.value = value

    def typename(self) -> str:
        return 'int'

    def val(self) -> str:
        return str(self.value)

    @staticmethod
    def resolve():
        return 'int'


def resolve_generic(generic):
    def help(generic):
        origin = generic.__origin__
        generics = []
        for a in generic.__args__:
            if hasattr(a, '__args__'):
                generics.append(help(a))
            else:
                generics.append(a.resolve())
        return origin.typename(generics)

    if hasattr(generic, '__orig_class__'):
        origin = generic.__dict__['__orig_class__']
        return help(origin)
    else:
        return generic.resolve()


if __name__ == '__main__':
    x = GoVector[GoVector[GoMap[Int, Int]]]#([[{1: 1}], [{2: 2}], [{3: 3}]])
    # print(resolve_generic(x))

    print(x.__dict__)
    # origin = x.__dict__['__orig_class__']
    # print(x.__dict__['__orig_class__'])
    print(x.__origin__)
    print(x.__args__)


