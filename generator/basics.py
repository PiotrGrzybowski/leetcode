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


class Map(Generic[T, S]):
    def __init__(self, values: dict[T, S]) -> None:
        super().__init__()
        self.values = values


class PythonVector(Vector[T]):
    @staticmethod
    def resolve(generics) -> str:
        return f"list[{generics[0]}]"

    @staticmethod
    def default() -> str:
        return '[]'

    @staticmethod
    def new(generics, values):
        return f"[{values}]"

    @staticmethod
    def build(data, generics):
        return [build(generics[0], value) for value in data]


class PythonMap(Map[T, S]):
    @staticmethod
    def resolve(generics) -> str:
        return f"dict[{generics[0]}, {generics[1]}]"

    @staticmethod
    def default() -> str:
        return '{}'

    @staticmethod
    def build(data, generics):
        key_alias, value_alias = generics
        return {build(key_alias, key): build(value_alias, value) for key, value in data.items()}


def build(alias, value):
    if hasattr(alias, '__origin__'):
        return alias.__origin__.build(value, alias.__args__)
    else:
        return alias.new(value)


class GoVector(Vector[T]):
    @staticmethod
    def resolve(generics) -> str:
        return f"[]{generics[0]}"

    @staticmethod
    def default() -> str:
        return 'nil'


class RustVector(Vector[T]):
    pass


class GoMap(Map[T, S]):
    @staticmethod
    def resolve(generics) -> str:
        return f"map[{generics[0]}]{generics[1]}"

    @staticmethod
    def default() -> str:
        return 'nil'

    @staticmethod
    def build(data, generics):
        key_alias, value_alias = generics
        return {build(key_alias, key): build(value_alias, value) for key, value in data.items()}


class Int:
    def __init__(self, number: int) -> None:
        self.number = number

    @staticmethod
    def resolve():
        return 'int'

    @staticmethod
    def default() -> str:
        return '0'

    def value(self) -> str:
        return str(self.number)

    @staticmethod
    def new(value):
        return value


def resolve_type(alias):
    if hasattr(alias, '__origin__'):
        origin = alias.__origin__
        parameters = alias.__args__
        parameters = [resolve_type(p) for p in parameters]
        return origin.resolve(parameters)
    else:
        return alias.resolve()


def resolve_type2(alias, value):
    if hasattr(alias, '__origin__'):
        origin = alias.__origin__
        parameters = alias.__args__
        parameters = [resolve_type2(p, value) for p in parameters]
        return origin, parameters
    else:
        return alias


#
# def resolve_nested_value(alias, value):
#     if hasattr(alias, '__origin__'):
#         origin = alias.__origin__
#
#         parameters = alias.__args__
#         parameters = [resolve_nested_value(p, value) for p in parameters]
#
#         print(origin)
#         print(parameters)
#         # return origin.value(parameters)
#     else:
#         return alias.new(value)



def resolve_value(value):
    # print(value.__dict__)
    if hasattr(value, '__orig_class__'):
        # print(value.__orig_class__)
        # print(value.__orig_class__.__dict__)
        # print(value.__orig_class__.__origin__)
        # print(value.__orig_class__.__args__)
        alias = value.__orig_class__
        # resolved, generic = resolve_type2(alias, value)
        # print(alias)
        # print(resolved)
        # print(generic)
        ##resolvec -> []int{...}
        return build(alias, value.values)

    else:
        return str(value.number)



def map_resolver(d):
    elements = []
    for key, value in d.items():
        elements.append(f"{builo(key)}, {builo(value)}")


def builo(value):
    match type(value):
        case list():
            return "d"
        case dict():
            return "a"
    pass


if __name__ == '__main__':
    x = GoVector[GoVector[GoMap[Int, Int]]]
    y = PythonVector[PythonVector[PythonMap[Int, Int]]]
    # ([[{1: 1}], [{2: 2}], [{3: 3}]])
    #
    # print(resolve_type(x))
    # print(resolve_type2(y))
    # print(resolve_value(Int(5)))
    # print(resolve_value(Int(5)))
    # print(resolve_value(Vector[Int]([1, 25])))
    # print(resolve_value(PythonMap[Int, PythonVector[Int]]({2: [1, 2], 1: [2, 3]})))
    print(resolve_value(PythonMap[Int, PythonVector[Int]]({1: [2, 2, 3], 2: [1, 2, 3]})))
    # print(resolve_value(y([[{1: 1}], [{2: 2}], [{3: 3}]])))
    # print(resolve_type(PythonVector[PythonVector[PythonMap[PythonVector[Int], Int]]]))
    #
    # x = {2: [1, 2], 1: [2, 3]}
    # print(builo([]))


