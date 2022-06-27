from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generic, TypeVar

T = TypeVar("T")
S = TypeVar("S")


class Vector(Generic[T]):
    def __init__(self, values: list[T]) -> None:
        super().__init__()
        self.data = values
        self.__orig_class__ = None

    def build(self):
        self.data = [self.generic(value).build() for value in self.data]
        return self

    @property
    def generic(self):
        return self.__orig_class__.__args__[0]

    def __str__(self) -> str:
        return ", ".join(map(str, self.data))


class Pointer(Generic[T]):
    def __init__(self, target: T) -> None:
        super().__init__()
        self.data = target
        self.__orig_class__ = None

    def build(self):
        self.data = self.generic(self.data.data, self.data.next).build()
        return self

    @property
    def generic(self):
        return self.__orig_class__.__args__[0]


class Map(Generic[T, S]):
    def __init__(self, values: dict[T, S]) -> None:
        super().__init__()
        self.data = values
        self.__orig_class__ = None

    def build(self):
        self.data = {self.key_generic(key).build(): self.value_generics(value).build() for key, value in self.data.items()}
        return self

    @property
    def key_generic(self):
        return self.__orig_class__.__args__[0]

    @property
    def value_generics(self):
        return self.__orig_class__.__args__[1]

    def __str__(self):
        return f'{{{", ".join([f"{key}: {value}" for key, value in self.data.items()])}}}'


class Basic:
    def build(self):
        return self


class Int(Basic):
    def __init__(self, value: int) -> None:
        self.data = value

    @staticmethod
    def default() -> str:
        return "0"

    def __str__(self):
        return str(self.data)


class Bool(Basic):
    def __init__(self, value: bool) -> None:
        self.data = value


class String(Basic):
    def __init__(self, value: str) -> None:
        self.data = value

    @staticmethod
    def default() -> str:
        return '""'

    def __str__(self):
        return f'"{self.data}"'


class Null(Basic):
    @classmethod
    def default(cls) -> str:
        return cls.resolve()

    @staticmethod
    def resolve():
        raise NotImplementedError()

    def __str__(self):
        return self.resolve()


class ListNode:
    def __init__(self, value: Any, next: Pointer[ListNode] | Null) -> None:
        self.data = value
        self.next = next

    def build(self):
        self.data = self.data.build()
        self.next = self.next.build()
        return self


# def single_linked_list_from_array(values: list) -> Pointer | Null:
#     if values:
#         head = Pointer[ListNode](ListNode(values[0], Null()))
#         pointer = head
#         for value in values[1:]:
#             p = Pointer[ListNode](ListNode(value, Null()))
#             pointer.data.next = p
#             pointer = pointer.data.next
#         return head
#     else:
#         return Null()


class Signature:
    def __init__(self, function: str, arguments: tuple, result_type: Any) -> None:
        self.function = function
        self.arguments = arguments
        self.result_type = result_type

    def cast(self, mapping):
        arguments = [Argument(argument.name, cast_type(argument.argument_type, mapping)) for argument in self.arguments]
        return mapping[type(self)](self.function, arguments, cast_type(self.result_type, mapping))

    def resolve(self) -> str:
        raise NotImplementedError()

    def _keyword(self) -> str:
        raise NotImplementedError()

    def _arguments(self) -> str:
        raise NotImplementedError()

    def _result_type(self) -> str:
        raise NotImplementedError()

    def _body(self) -> str:
        raise NotImplementedError()


class Argument:
    def __init__(self, name: str, argument_type: Any) -> None:
        self.name = name
        self.argument_type = argument_type

    def __repr__(self) -> str:
        return f"Argument({self.name}, {self.argument_type})"


class TestCase:
    def __init__(self, function: str, inputs, expected) -> None:
        self.function = function
        self.inputs = inputs
        self.expected = expected

    def cast(self, mapping: dict) -> None:
        inputs = [cast_value(value, mapping) for value in self.inputs]
        expected = cast_value(self.expected, mapping)
        return mapping[type(self)](self.function, inputs, expected)

    def resolve_inputs(self):
        return [self._resolve_value(i) for i in self.inputs]

    def resolve_expected(self):
        return self._resolve_value(self.expected)

    @staticmethod
    def _resolve_value(value) -> str:
        raise NotImplementedError()


class Test:
    def __init__(self, function: str, cases: list[TestCase]):
        self.function = function
        self.cases = cases

    def cast(self, mapping):
        return mapping[type(self)](self.function, [case.cast(mapping) for case in self.cases])

    def resolve(self) -> str:
        raise NotImplementedError()


@dataclass
class Config:
    templates_path: Path
    python_path: Path
    go_path: Path
    python_mapping: dict
    go_mapping: dict


class Writer:
    def __init__(self, config: Config):
        self.config = config

    @staticmethod
    def _write_signature(filename: Path, signature: Signature):
        with open(filename, 'a') as f:
            f.write(signature.resolve())

    @staticmethod
    def _write_test(filename: Path, test: Test):
        with open(filename, 'a') as f:
            f.write('\n\n')
            f.write(test.resolve())
            f.write('\n')

    def write_python(self, name: str, signature: Signature, test: Test):
        filename = self.config.python_path / f"{name}.py"
        shutil.copy(self.config.templates_path / "template.py", filename)

        signature = signature.cast(self.config.python_mapping)
        test = test.cast(self.config.python_mapping)
        self._write_signature(filename, signature)
        self._write_test(filename, test)

    def write_go(self, name: str, signature: Signature, test: Test) -> None:
        signature = signature.cast(self.config.go_mapping)
        test = test.cast(self.config.go_mapping)

        filename = self.config.go_path / f"{name}.go"
        test_filename = self.config.go_path / f"{name}_test.go"
        shutil.copy(self.config.templates_path / "template.go", filename)
        shutil.copy(self.config.templates_path / "template_test.go", test_filename)

        self._write_signature(filename, signature)
        self._write_test(test_filename, test)


def resolve_type(alias):
    if hasattr(alias, "__origin__"):
        origin = alias.__origin__
        parameters = alias.__args__
        parameters = tuple(resolve_type(p) for p in parameters)
        return origin.resolve(*parameters)
    else:
        return alias.resolve()


def cast_type(alias, mapping):
    if hasattr(alias, "__origin__"):
        origin = alias.__origin__
        parameters = alias.__args__
        parameters = tuple(cast_type(p, mapping) for p in parameters)
        return mapping[origin][parameters]
    else:
        return mapping[alias]


def cast_value(value, mapping):
    if hasattr(value, "__orig_class__"):
        return cast_type(value.__orig_class__, mapping)(value.data)
    else:
        if type(value) is not Null:
            return mapping[type(value)](value.data)
        else:
            return mapping[type(value)]


def snake_case_to_camel_case(text: str) -> str:
    return ''.join(word.title() for word in text.split('_'))


def snake_case_to_semi_camel_case(text: str) -> str:
    words = [word.title() for word in text.split('_')]
    words[0] = words[0].lower()
    return ''.join(words)
