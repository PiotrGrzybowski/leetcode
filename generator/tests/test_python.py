from generator.basics import resolve_type
from generator.python import (
    PythonBool,
    PythonInt,
    PythonListNode,
    PythonMap,
    PythonNone,
    PythonPointer,
    PythonString,
    PythonVector,
    single_linked_list_from_array,
)


def test_python_int():
    assert PythonInt.default() == "0"
    assert resolve_type(PythonInt) == "int"
    assert str(PythonInt(5).build()) == "5"


def test_python_none():
    assert PythonNone.default() == "None"
    assert resolve_type(PythonNone) == "None"
    assert str(PythonNone().build()) == "None"


def test_python_bool():
    assert PythonBool.default() == "True"
    assert resolve_type(PythonBool) == "bool"
    assert str(PythonBool(True).build()) == "True"


def test_python_string():
    assert PythonString.default() == '""'
    assert resolve_type(PythonString) == "str"
    assert str(PythonString("Piotr").build()) == '"Piotr"'


def test_python_vector():
    assert PythonVector[PythonInt].default() == "[]"
    assert resolve_type(PythonVector[PythonInt]) == "list[int]"
    assert str(PythonVector[PythonInt]([1, 2, 3]).build()) == "[1, 2, 3]"


def test_python_map():
    assert PythonMap[PythonInt, PythonInt].default() == "{}"
    assert resolve_type(PythonMap[PythonInt, PythonInt]) == "dict[int, int]"
    assert str(PythonMap[PythonInt, PythonInt]({1: 1, 2: 2, 3: 3}).build()) == "{1: 1, 2: 2, 3: 3}"


def test_python_nested_map_vector():
    assert PythonMap[PythonInt, PythonVector[PythonInt]].default() == "{}"
    assert resolve_type(PythonMap[PythonInt, PythonVector[PythonInt]]) == "dict[int, list[int]]"
    assert (
        str(PythonMap[PythonInt, PythonVector[PythonInt]]({1: [1], 2: [2], 3: [3]}).build())
        == "{1: [1], 2: [2], 3: [3]}"
    )


def test_python_pointer():
    assert resolve_type(PythonPointer[PythonInt]) == "int"
    assert PythonPointer[PythonInt].default() == "None"
    assert str(PythonPointer[PythonInt](5).build()) == "5"


def test_python_list_node():
    assert resolve_type(PythonListNode) == "ListNode"
    assert PythonListNode.default() == "None"
    assert str(PythonListNode(5, PythonNone())) == "ListNode(5, None)"
    assert (
        str(PythonListNode(5, PythonPointer[PythonListNode](PythonListNode(6, PythonNone()))))
        == "ListNode(5, ListNode(6, None))"
    )


def test_python_list_node_pointer():
    assert resolve_type(PythonPointer[PythonListNode]) == "ListNode"
    assert PythonPointer[PythonListNode].default() == "None"
    assert str(PythonPointer[PythonListNode](PythonListNode(5, PythonNone()))) == "ListNode(5, None)"
    assert (
        str(
            PythonPointer[PythonListNode](
                PythonListNode(5, PythonPointer[PythonListNode](PythonListNode(6, PythonNone())))
            )
        )
        == "ListNode(5, ListNode(6, None))"
    )


def test_single_linked_list_from_array():
    assert str(single_linked_list_from_array([])) == "None"
    assert str(single_linked_list_from_array([1])) == "ListNode(1, None)"
    assert str(single_linked_list_from_array([1, 2])) == "ListNode(1, ListNode(2, None))"
