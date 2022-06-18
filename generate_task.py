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
from typing import Any, Callable, Optional, Sequence, TypeVar


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
        return f'"{value}"'

    @staticmethod
    def default_value() -> str:
        return f'""'


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
        return f'String::from("{value}")'

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

    def __str__(self):
        return "bool"

    @staticmethod
    def name() -> str:
        return "bool"


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
        return "True" if value else "False"

    @staticmethod
    def default_value() -> str:
        return "True"

    def __str__(self):
        return "bool"

    @staticmethod
    def name() -> str:
        return "bool"


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

    def __str__(self):
        return "bool"

    @staticmethod
    def name() -> str:
        return "bool"


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
        return cls(pointer.target)


class Custom:
    def __init__(self, target) -> None:
        self.target = target

    def __str__(self) -> str:
        return str(self.target)[1:]

    def value(self, value):
        return self.target.test(value)


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
        return self.target.test(value)


class PythonReference(Reference):
    def __str__(self):
        return str(self.target)


class RustPointer(Pointer):
    def __str__(self):
        return f"Option<Box<{self.target}>>"

    def value(self, value):
        return f"&{self.target.test(value)}"


class GoPointer(Pointer):
    def __str__(self):
        return f"*{self.target}"

    def value(self, value):
        return f"{self.target.test(value)}"


class PythonPointer(Pointer):
    def __str__(self):
        return f"Optional[{self.target}]"

    def value(self, value):
        return self.target.test(value)


class Language:
    def __init__(self, types, mappings):
        self.types = types
        self.mappings = mappings

        self.resolvers: dict[Any, Callable] = {
            Reference: self.resolve_reference,
            Vector: self.resolve_vector,
            Pointer: self.resolve_pointer,
            Custom: self.resolve_custom,
        }

    def resolve_type(self, kind):
        if isinstance(kind, type):
            return self.types[kind]
        else:
            return self.resolvers[type(kind)](kind)

    def resolve_reference(self, reference):
        return self.mappings[Reference](
            self.resolve_type(reference.target), reference.mutable
        )

    def resolve_pointer(self, pointer):
        return self.mappings[Pointer](self.resolve_type(pointer.target))

    def resolve_vector(self, vector):
        return self.mappings[Vector](self.resolve_type(vector.generic))

    def resolve_custom(self, custom):
        return custom.target()

    def resolve_arguments(self, arguments: list[Argument]) -> str:
        return ", ".join([self.resolve_argument(argument) for argument in arguments])

    def resolve_value(self, value: Value) -> str:
        reso = self.resolve_type(value.kind)
        return str(reso.test(value.value))

    def resolve_values(self, values: list[Value]):
        return ", ".join([self.resolve_value(value) for value in values])

    def resolve_default_result(self, output):
        if isinstance(output, type):
            return self.types[output].default_value()
        else:
            return self.types[type(output)].cast(output).default_value()

    def resolve_argument(self, argument) -> str:
        pass

    def function_signature(
            self, function: str, arguments: list[Argument], output=None
    ) -> str:
        pass

    def test_case(self, filename, param, param1):
        pass


class Rust(Language):
    def resolve_argument(self, argument: Argument) -> str:
        return f"{argument.name}: {self.resolve_type(argument.kind)}"

    def resolve_output_type(self, output) -> str:
        return f"-> {self.resolve_type(output).name()}" if output else ""

    def function_signature(
            self, function: str, arguments: list[Argument], output=None
    ) -> str:
        arguments = self.resolve_arguments(arguments)
        default_value = self.resolve_default_result(output)
        output_type = self.resolve_output_type(output)
        return (
            f"pub fn {function}({arguments}) {output_type} {{\n    {default_value}\n}}"
        )

    def test_case(self, function: str, arguments, expected) -> str:
        return f"assert_eq!({self.resolve_value(expected)}, {function}({self.resolve_values(arguments)})"


class Go(Language):
    def resolve_argument(self, argument: Argument) -> str:
        return f"{argument.name} {self.resolve_type(argument.kind)}"

    def resolve_output_type(self, output) -> str:
        return f"{self.resolve_type(output).name()}" if output else ""

    def function_signature(
            self, function: str, arguments: list[Argument], output=None
    ) -> str:
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
        return f"-> {self.resolve_type(output).name()}" if output else ""

    def function_signature(
            self, function: str, arguments: list[Argument], output=None
    ) -> str:
        arguments = self.resolve_arguments(arguments)
        default_value = self.resolve_default_result(output)
        output_type = self.resolve_output_type(output)
        return f"def {function}({arguments}) {output_type}:\n    {default_value}\n"

    def test_case(self, function: str, arguments, expected) -> str:
        return f"assert {function}({self.resolve_values(arguments)}) == {self.resolve_value(expected)}"

    # def test_cases(self, function, arguments_sequence, expected_sequence):
    #     return '\n'.join


class TreeNode:
    def __str__(self):
        return "TreeNode"

    @staticmethod
    def name():
        return "TreeNode"

    @staticmethod
    def default_value():
        return "TreeNode()"

    @staticmethod
    def value(value):
        return f"TreeNode({value})"


class ListNode:
    def __str__(self):
        return "ListNode"

    @staticmethod
    def name():
        return "ListNode"

    @staticmethod
    def default_value():
        return "ListNode()"

    @staticmethod
    def value(value):
        return f"ListNode({value})"


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
        {
            String: RustString(),
            Int: RustInt(),
            None: RustNone(),
            Vector: RustVector,
            Reference: RustReference,
            Bool: RustBool,
            Pointer: RustPointer,
        },
        {Reference: RustReference, Vector: RustVector, Pointer: RustPointer},
    )
    return r


def create_go():
    r = Go(
        {
            String: GoString(),
            Int: GoInt(),
            None: GoNone(),
            Vector: GoVector,
            Reference: GoReference,
            Bool: GoBool,
            Pointer: GoPointer,
        },
        {Reference: GoReference, Vector: GoVector, Pointer: GoPointer},
    )
    return r


def create_python():
    r = Python(
        {
            String: PythonString(),
            Int: Int(),
            None: PythonNone(),
            Vector: PythonVector,
            Reference: PythonReference,
            Bool: PythonBool,
            Pointer: PythonPointer,
        },
        {Reference: PythonReference, Vector: PythonVector, Pointer: PythonPointer},
    )
    return r


class Script:
    def __init__(self, language: Language, path: Path) -> None:
        self.language = language
        self.path = path

    def create(
            self,
            filename: str,
            function: str,
            arguments: list[Argument],
            test_inputs: list[Value],
            test_expected: list[Value],
    ):
        pass


class PythonScript(Script):
    python_main = "if __name__ == '__main__':\n"

    def generate_imports(self):
        return "from typing import Optional"

    def create(
            self,
            filename: str,
            arguments: list[Argument],
            output: Any,
            test_inputs: list[list[Value]],
            test_expected: list[Value],
    ) -> None:
        self.touch(filename)

        with open(self.filename(filename), "w") as f:
            f.write(self.generate_imports())
            self.write_lines(f, 3)
            f.write(self.language.function_signature(filename, arguments, output))
            self.write_lines(f, 2)
            f.write(self.python_main)
            self.write_test_cases(f, filename, test_expected, test_inputs)

    def write_test_cases(self, f, filename, test_expected, test_inputs):
        for inputs, expected in zip(test_inputs, test_expected):
            f.write(f"    {self.language.test_case(filename, inputs, expected)}\n")

    def write_lines(self, f, n):
        for i in range(n):
            f.write("\n")

    def touch(self, filename: str) -> None:
        (self.path / f"{filename}.py").touch(exist_ok=True)

    def filename(self, filename: str) -> Path:
        return self.path / f"{filename}.py"


class RustScript(Script):
    def __init__(self, language: Language, script_path: Path, test_path: Path):
        super().__init__(language, script_path)
        self.test_path = test_path

    def create(
            self,
            filename: str,
            arguments: list[Argument],
            output: Any,
            test_inputs: list[list[Value]],
            test_expected: list[Value],
    ) -> None:
        self.touch(filename)

        with open(self.filename(filename), "w") as f:
            f.write(self.language.function_signature(filename, arguments, output))

        with open(self.test_filename(filename), "w") as f:
            f.write(f"use rust::algos::{filename}::{filename};\n\n")
            f.write(f"#[test]\n")
            f.write(f"fn test_{filename}() {{\n")
            for inputs, expected in zip(test_inputs, test_expected):
                f.write(f"    {self.language.test_case(filename, inputs, expected)}\n")
            f.write("}\n")

        with open(self.path / "mod.rs", "a") as f:
            f.write(f"pub mod {filename};\n")

    def write_lines(self, f, n):
        for i in range(n):
            f.write("\n")

    def touch(self, filename: str) -> None:
        (self.path / f"{filename}.rs").touch(exist_ok=True)

    def filename(self, filename: str) -> Path:
        return self.path / f"{filename}.rs"

    def test_filename(self, filename: str) -> Path:
        return self.test_path / f"test_{filename}.rs"


class GoScript(Script):
    def create(
            self,
            filename: str,
            arguments: list[Argument],
            output: Any,
            test_inputs: list[list[Value]],
            test_expected: list[Value],
    ) -> None:
        self.touch(filename)

        with open(self.filename(filename), "w") as f:
            f.write("package algos\n\n")
            f.write(self.language.function_signature(filename, arguments, output))

        with open(self.test_filename(filename), "w") as f:
            f.write("package algos\n\n")
            f.write(
                'import (\n    "github.com/stretchr/testify/assert"\n    "testing"\n)\n\n'
            )
            f.write(f"func Test{filename.title()}(t *testing.T) {{\n")
            for inputs, expected in zip(test_inputs, test_expected):
                f.write(f"    {self.language.test_case(filename, inputs, expected)}\n")
            f.write("}\n")

    def touch(self, filename: str) -> None:
        (self.path / f"{filename}.go").touch(exist_ok=True)

    def filename(self, filename: str) -> Path:
        return self.path / f"{filename}.go"

    def test_filename(self, filename: str) -> Path:
        return self.path / f"{filename}_test.go"


inputs = [
    Argument("node", Reference(Custom(ListNode), False)),
]

output = Bool

rust = create_rust()
go = create_go()
python = create_python()

test_inputs = [
    # [Value([2, 2, 1], Vector(Int))],
    # [Value([4, 1, 2, 1, 2], Vector(Int))],
    # [Value([1], Vector(Int))],

]
test_expected = [
    # Value(1, Int),
    # Value(4, Int),
    # Value(1, Int),
]

python_script = PythonScript(python, Path("python", "algos"))
rust_script = RustScript(rust, Path("rust", "src", "algos"), Path("rust", "tests"))
go_script = GoScript(go, Path("go"))
# python_script = PythonScript(python, Path("python", "algos"))
filename = "linked_list_cycle"
python_script.create(filename, inputs, output, test_inputs, test_expected)
rust_script.create(filename, inputs, output, test_inputs, test_expected)
go_script.create(filename, inputs, output, test_inputs, test_expected)
