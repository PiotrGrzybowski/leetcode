"""

#!/bin/bash

touch go/$1.go
touch go/$1_test.go

touch python/algos/$1.py

touch rust/src/algos/$1.rs
touch rust/tests/test_$1.rs

"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Sequence, TypeVar, Callable


class Type:
    def __str__(self) -> str:
        return self.name()

    @staticmethod
    def name() -> str:
        pass


class Int(Type):
    @staticmethod
    def name() -> str:
        return "int"

    @staticmethod
    def value(value: int) -> str:
        return str(value)

    @staticmethod
    def default_value() -> str:
        return "0"


class String(Type):
    @staticmethod
    def value(value: str) -> str:
        return f"\"{value}\""

    @staticmethod
    def default_value() -> str:
        return f"\"\""


class Bool(Type):
    @staticmethod
    def name() -> str:
        return "bool"


class Vector:
    def __init__(self, generic) -> None:
        self.generic = generic

    @classmethod
    def cast(cls, vector):
        return cls(vector.generic)


class RustInt(Int):
    @staticmethod
    def name() -> str:
        return "i32"


class RustString:
    @staticmethod
    def name() -> str:
        return "String"

    @staticmethod
    def value(value) -> str:
        return f"String::from(\"{value}\")"

    @staticmethod
    def default_value() -> str:
        return f"String::new()"


class RustBool(Bool):
    @staticmethod
    def value(value: bool) -> str:
        return "true" if value else "false"

    @staticmethod
    def default_value() -> str:
        return "true"


class RustNone:
    @staticmethod
    def default_value() -> str:
        return ""


class RustVector(Vector):
    def __str__(self) -> str:
        return f"Vec<{self.generic}>"

    @staticmethod
    def default_value() -> str:
        return "Vec::new()"

    def value(self, value) -> str:
        return f"Vec::from({value})"



class GoInt(Int):
    @staticmethod
    def name() -> str:
        return "int"


class GoString(String):
    @staticmethod
    def name() -> str:
        return "string"


class GoBool(Bool):
    @staticmethod
    def value(value: bool) -> str:
        return "true" if value else "false"

    @staticmethod
    def default_value() -> str:
        return "true"


class GoVector(Vector):
    def __str__(self) -> str:
        return f"[]{self.generic}"

    def default_value(self) -> str:
        return f"return []{self.generic.name()}{{}}"

    def value(self, value) -> str:
        return f"return []{self.generic.name()}{{{str(value)[1:-1]}}}"


class GoNone:
    @staticmethod
    def default_value() -> str:
        return ""


class PythonString(String):
    @staticmethod
    def name() -> str:
        return "str"


class PythonBool(Bool):
    @staticmethod
    def value(value: bool) -> str:
        return "True" if value else "False"

    @staticmethod
    def default_value() -> str:
        return "True"


class PythonVector(Vector):
    def __str__(self) -> str:
        return f"list[{self.generic}]"

    @staticmethod
    def default_value() -> str:
        return "return []"

    def value(self, value) -> str:
        return str(value)


class PythonNone:
    @staticmethod
    def default_value() -> str:
        return "None"


class Reference:
    def __init__(self, target, mutable) -> None:
        self.target = target
        self.mutable = mutable

    @classmethod
    def cast(cls, reference):
        return cls(reference.target, reference.mutable)

    def value(self, value):
        return str(value)


class Pointer:
    def __init__(self, target) -> None:
        self.target = target

    @classmethod
    def cast(cls, pointer):
        return cls(pointer.generic)


class Custom:
    def __init__(self, target) -> None:
        self.target = target

    def __str__(self) -> str:
        return str(self.target)[1:]


class RustReference(Reference):
    def __str__(self):
        if self.mutable:
            return f"&mut {self.target}"
        else:
            return f"&{self.target}"

    def value(self, value):
        return f"&{value}"


class GoReference(Reference):
    def __str__(self):
        return str(self.target)

    def value(self, value):
        return self.target.value(value)


class PythonReference(Reference):
    def __str__(self):
        return str(self.target)


class RustPointer(Pointer):
    def __str__(self):
        return f"Optional<Box<{self.target}>>"


class GoPointer(Pointer):
    def __str__(self):
        return f"*{self.target}"


class PythonPointer(Pointer):
    def __str__(self):
        return str(self.target)


class Language:
    def __init__(self, types, mappings):
        self.types = types
        self.mappings = mappings

        self.resolvers: dict[Any, Callable] = {
            Reference: self.resolve_reference,
            Vector: self.resolve_vector,
            Pointer: self.resolve_pointer,
            Custom: self.resolve_custom
        }

    def resolve_type(self, kind):
        if isinstance(kind, type):
            return self.types[kind]
        else:
            return self.resolvers[type(kind)](kind)

    def resolve_reference(self, reference):
        return self.mappings[Reference](self.resolve_type(reference.target), reference.mutable)

    def resolve_pointer(self, pointer):
        return self.mappings[Pointer](self.resolve_type(pointer.target))

    def resolve_vector(self, vector):
        return self.mappings[Vector](self.resolve_type(vector.generic))

    def resolve_custom(self, custom):
        return custom

    def resolve_arguments(self, arguments: list[Argument]) -> str:
        return ', '.join([self.resolve_argument(argument) for argument in arguments])

    def resolve_value(self, value: Value) -> str:
        reso = self.resolve_type(value.kind)
        return str(reso.value(value.value))

    def resolve_values(self, values: list[Value]):
        return ', '.join([self.resolve_value(value) for value in values])

    def resolve_default_result(self, output):
        if isinstance(output, type):
            return self.types[output].default_value()
        else:
            return self.types[type(output)].cast(output).default_value()

    def resolve_argument(self, argument) -> str:
        pass


class Rust(Language):
    def resolve_argument(self, argument: Argument) -> str:
        return f"{argument.name}: {self.resolve_type(argument.kind)}"

    def resolve_output_type(self, output) -> str:
        return f"-> {self.resolve_type(output)}" if output else ""

    def function_signature(self, function: str, arguments: list[Argument], output=None) -> str:
        arguments = self.resolve_arguments(arguments)
        default_value = self.resolve_default_result(output)
        output_type = self.resolve_output_type(output)
        return f"pub fn {function}({arguments}) {output_type} {{\n    {default_value}\n}}"

    def test_case(self, function: str, arguments, expected) -> str:
        return f"assert.Equal(t, {self.resolve_value(expected)}, {function}({self.resolve_values(arguments)}))"

    def rust_test_case(function: str, case: tuple[Any, Any]) -> str:
        arguments, target = case
        arguments = ", ".join(
            [crate_rust_input_value(argument, typing) for argument, typing in arguments]
        )
        target = crate_rust_input_value(target[0], target[1])
        return f"assert_eq!({function}({arguments}), {target});"


class Go(Language):
    def resolve_argument(self, argument: Argument) -> str:
        return f"{argument.name} {self.resolve_type(argument.kind)}"

    def resolve_output_type(self, output) -> str:
        return f"{self.resolve_type(output)}" if output else ""

    def function_signature(self, function: str, arguments: list[Argument], output=None) -> str:
        arguments = self.resolve_arguments(arguments)
        default_value = self.resolve_default_result(output)
        output_type = self.resolve_output_type(output)
        return f"func {function}({arguments}) {output_type} {{\n    {default_value}\n}}"

    def test_case(self, function: str, arguments, expected) -> str:
        return f"assert.Equal(t, {self.resolve_value(expected)}, {function}({self.resolve_values(arguments)}))"


class Python(Language):
    def resolve_argument(self, argument: Argument) -> str:
        return f"{argument.name}: {self.resolve_type(argument.kind)}"

    def resolve_output_type(self, output) -> str:
        return f"-> {self.resolve_type(output)}" if output else ""

    def function_signature(self, function: str, arguments: list[Argument], output=None) -> str:
        arguments = self.resolve_arguments(arguments)
        default_value = self.resolve_default_result(output)
        output_type = self.resolve_output_type(output)
        return f"def {function}({arguments}) {output_type}:\n    {default_value}\n"

    def test_case(self, function: str, arguments, expected) -> str:
        return f"assert {function}({self.resolve_values(arguments)}) == {self.resolve_value(expected)}"

    # def test_cases(self, function, arguments_sequence, expected_sequence):
    #     return '\n'.join

TreeNode = TypeVar('TreeNode')


class Value:
    def __init__(self, value: Any, kind) -> None:
        self.value = value
        self.kind = kind


class Argument:
    def __init__(self, name: str, kind) -> None:
        self.name = name
        self.kind = kind


def create_rust():
    r = Rust(
        {String: RustString(), Int: RustInt(), None: RustNone(), Vector: RustVector, Reference: RustReference},
        {Reference: RustReference, Vector: RustVector, Pointer: RustPointer}
    )
    return r


def create_go():
    r = Go(
        {String: GoString(), Int: GoInt(), None: GoNone(), Vector: GoVector, Reference: GoReference},
        {Reference: GoReference, Vector: GoVector, Pointer: GoPointer}
    )
    return r


def create_python():
    r = Python(
        {String: PythonString(), Int: Int(), None: PythonNone(), Vector: PythonVector, Reference: PythonReference},
        {Reference: PythonReference, Vector: PythonVector, Pointer: PythonPointer}
    )
    return r


inputs = [
    Argument("nums1", Reference(Vector(Int), True)),
    Argument("m", Int),
    Argument("nums2", Reference(Vector(Int), True)),
    Argument("n", Int),
]

output = Vector(Int)

rust = create_rust()
go = create_go()
python = create_python()

print(rust.function_signature('merge', inputs, output))
print(go.function_signature('merge', inputs, output))
print(python.function_signature('merge', inputs, output))

test_inputs = [
    [
        Value([2, 3, 4], Reference(Vector(Int), True)),
        Value(3, Int),
        Value([1, 2, 3, 4], Reference(Vector(Int), True)),
        Value(4, Int)
    ]
]

test_expected = [
    Value([1, 2, 3, 4], Vector(Int))
]

print(python.test_case('merge', test_inputs[0], test_expected[0]))
print(go.test_case('merge', test_inputs[0], test_expected[0]))


@dataclass
class InputArgument:
    name: str
    argument_type: str


PYTHON = "python"
RUST = "rust"
GO = "go"

PYTHON_MAIN = "if __name__ == '__main__':"
types = {
    PYTHON: {
        int: "int",
        str: "str",
        float: "float",
        list[str]: "list[str]",
        list[int]: "list[int]",
        "None": "None"
    },
    RUST: {
        int: "i32",
        str: "String",
        list[str]: "Vec<String>",
        list[int]: "Vec<i32>",
        "None": ""
    },
    GO: {int: "int", str: "string", list[str]: "[]string", list[int]: "[]int", "None": ""},
}


def crate_rust_input_value(value: Any, typing: type) -> Any:
    if typing == int:
        return str(value)
    elif typing == str:
        return f'String::from("{value}")'
    elif typing == list[str]:
        return f"vec!{value}"
    elif typing == list[int]:
        return f"vec!{value}"
    else:
        return ""


def crate_go_input_value(value: Any, typing: type) -> Any:
    if typing == int:
        return str(value)
    elif typing == str:
        return f'"{value}"'
    elif typing == list[str]:
        return f"[]string{{{value}}}"
    elif typing == list[int]:
        return f"[]int{{{value}}}"
    else:
        return ""


def crate_python_input_value(value: Any, typing: type) -> Any:
    if typing == int:
        return str(value)
    elif typing == str:
        return f'"{value}"'
    elif typing == list[str]:
        return f"{value}"
    elif typing == list[int]:
        return f"{value}"
    else:
        return ""


def python_test_case(function: str, case: tuple[Any, Any]) -> str:
    arguments, target = case
    arguments = ", ".join(
        [crate_python_input_value(argument, typing) for argument, typing in arguments]
    )
    target = crate_python_input_value(target[0], target[1])
    return f"assert {function}({arguments}) == {target}"


def rust_test_case(function: str, case: tuple[Any, Any]) -> str:
    arguments, target = case
    arguments = ", ".join(
        [crate_rust_input_value(argument, typing) for argument, typing in arguments]
    )
    target = crate_rust_input_value(target[0], target[1])
    return f"assert_eq!({function}({arguments}), {target});"


def go_test_case(function: str, case: tuple[Any, Any]) -> str:
    arguments, target = case
    arguments = ", ".join(
        [crate_go_input_value(argument, typing) for argument, typing in arguments]
    )
    target = crate_go_input_value(target[0], target[1])
    init, *temp = function.split("_")
    function = "".join([init.lower(), *map(str.title, temp)])
    return f"assert.Equal(t, {target}, {function}({arguments}))"


def python_signature(filename, inputs, output):
    return f"def {filename}({', '.join([f'{argument[0]}: {types[PYTHON][argument[1]]}' for argument in inputs])}) -> {types[PYTHON][output]}:\n    return {python_default_output(output)}"


def rust_signature(filename, inputs, output):
    return f"pub fn {filename}({', '.join([f'{argument[0]}: {types[RUST][argument[1]]}' for argument in inputs])}) -> {types[RUST][output]} {{\n    {rust_default_output(output)}\n}}"


def go_signature(filename, inputs, output):
    init, *temp = filename.split("_")
    filename = "".join([init.lower(), *map(str.title, temp)])

    return f"func {filename}({', '.join([f'{argument[0]} {types[GO][argument[1]]}' for argument in inputs])}) {types[GO][output]} {{\n    return {go_default_output(output)}\n}}"


def python_default_output(typing) -> Any:
    if typing == int:
        return 0
    elif typing == str:
        return f'""'
    elif typing == list[str]:
        return f"[]"
    elif typing == list[int]:
        return f"[]"
    else:
        return ""


def rust_default_output(typing) -> Any:
    if typing == int:
        return 0
    elif typing == str:
        return f'String::from("")'
    elif typing == list[str]:
        return f"vec![]"
    elif typing == list[int]:
        return f"vec![]"
    else:
        return ""


def go_default_output(typing) -> Any:
    if typing == int:
        return 0
    elif typing == str:
        return f'""'
    elif typing == list[str]:
        return f"[]string{{}}"
    elif typing == list[int]:
        return f"[]int{{}}"
    else:
        return ""


filename = "inorder_traversal"

python_function_name = 'inorder_traversal'

inputs = [("root", int)]
output = list[int]
tests = [
    # ([([1, 2, 3, 0, 0, 0], list[int]), (3, int), ([2, 5, 6], list[int]), (2, int)], ([1, 2, 2, 3, 5, 6], list[int])),
    # ([([1, 2, 2, 3, 3, 4, 8, 0, 0, 0, 0, 0], list[int]), (7, int), ([2, 2, 3, 3, 5], list[int]), (5, int)],
    #  ([1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 8], list[int])),
    # ([([1], list[int]), (1, int), ([], list[int]), (0, int)], ([1], list[int])),
    ([(1, int)], ([1, 3, 2], list[int])),
]

# python_script_path = Path("python", "algos", f"{filename}.py")
# python_script_path.touch(exist_ok=True)
#
# with open(python_script_path, 'w') as f:
#     f.write(f"{python_signature(python_function_name, inputs, output)}\n\n\n")
#     f.write(f"{PYTHON_MAIN}\n")
#     for test in tests:
#         f.write(f"    {python_test_case(python_function_name, test)}\n")
#
# rust_script_path = Path("rust", "src", "algos", f"{filename}.rs")
# rust_test_path = Path("rust", "tests", f"test_{filename}.rs")
# rust_mod_path = Path("rust", "src", "algos", "mod.rs")
# rust_script_path.touch(exist_ok=True)
# rust_test_path.touch(exist_ok=True)
#
# with open(rust_script_path, 'w') as f:
#     f.write(f"{rust_signature(python_function_name, inputs, output)}\n\n\n")
#
# with open(rust_test_path, 'w') as f:
#     f.write(f"use rust::algos::{filename}::{filename};\n\n")
#     f.write(f"#[test]\n")
#     f.write(f"fn test_{filename}() {{\n")
#     for test in tests:
#         f.write(f"    {rust_test_case(python_function_name, test)}\n")
#     f.write("}\n")
#
# with open(rust_mod_path, "a") as f:
#     f.write(f"pub mod {filename};\n")
#
# go_script_path = Path("go", f"{filename}.go")
# go_test_path = Path("go", f"{filename}_test.go")
# go_script_path.touch(exist_ok=True)
# go_test_path.touch(exist_ok=True)
#
# with open(go_script_path, 'w') as f:
#     f.write("package algos\n\n")
#     f.write(f"{go_signature(python_function_name, inputs, output)}\n\n\n")
#
# with open(go_test_path, 'w') as f:
#     f.write("package algos\n\n")
#     f.write("import (\n    \"github.com/stretchr/testify/assert\"\n    \"testing\"\n)\n\n")
#     f.write(f"func Test{filename.title()}(t *testing.T) {{\n")
#     for test in tests:
#         f.write(f"    {go_test_case(python_function_name, test)}\n")
#     f.write("}\n")
#
# with open(rust_mod_path, "a") as f:
#     f.write(f"pub mod {filename};\n")
