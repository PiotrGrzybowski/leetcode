"""

#!/bin/bash

touch go/$1.go
touch go/$1_test.go

touch python/algos/$1.py

touch rust/src/algos/$1.rs
touch rust/tests/test_$1.rs

"""
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import numpy as np


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
    ([(1, int)], ([1,3,2], list[int])),
]

python_script_path = Path("python", "algos", f"{filename}.py")
python_script_path.touch(exist_ok=True)

with open(python_script_path, 'w') as f:
    f.write(f"{python_signature(python_function_name, inputs, output)}\n\n\n")
    f.write(f"{PYTHON_MAIN}\n")
    for test in tests:
        f.write(f"    {python_test_case(python_function_name, test)}\n")

rust_script_path = Path("rust", "src", "algos", f"{filename}.rs")
rust_test_path = Path("rust", "tests", f"test_{filename}.rs")
rust_mod_path = Path("rust", "src", "algos", "mod.rs")
rust_script_path.touch(exist_ok=True)
rust_test_path.touch(exist_ok=True)

with open(rust_script_path, 'w') as f:
    f.write(f"{rust_signature(python_function_name, inputs, output)}\n\n\n")

with open(rust_test_path, 'w') as f:
    f.write(f"use rust::algos::{filename}::{filename};\n\n")
    f.write(f"#[test]\n")
    f.write(f"fn test_{filename}() {{\n")
    for test in tests:
        f.write(f"    {rust_test_case(python_function_name, test)}\n")
    f.write("}\n")

with open(rust_mod_path, "a") as f:
    f.write(f"pub mod {filename};\n")

go_script_path = Path("go", f"{filename}.go")
go_test_path = Path("go", f"{filename}_test.go")
go_script_path.touch(exist_ok=True)
go_test_path.touch(exist_ok=True)

with open(go_script_path, 'w') as f:
    f.write("package algos\n\n")
    f.write(f"{go_signature(python_function_name, inputs, output)}\n\n\n")

with open(go_test_path, 'w') as f:
    f.write("package algos\n\n")
    f.write("import (\n    \"github.com/stretchr/testify/assert\"\n    \"testing\"\n)\n\n")
    f.write(f"func Test{filename.title()}(t *testing.T) {{\n")
    for test in tests:
        f.write(f"    {go_test_case(python_function_name, test)}\n")
    f.write("}\n")

with open(rust_mod_path, "a") as f:
    f.write(f"pub mod {filename};\n")
