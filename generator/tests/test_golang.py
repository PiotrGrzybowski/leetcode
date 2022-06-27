from generator.basics import resolve_type, Argument, Int, Vector, Signature
from generator.golang import (
    GoBool,
    GoInt,
    GoListNode,
    GoMap,
    GoNone,
    GoPointer,
    GoString,
    GoVector,
    single_linked_list_from_array,
)


def test_golang_int():
    assert resolve_type(GoInt) == "int"
    assert GoInt.default() == "0"
    assert str(GoInt(5).build()) == "5"


def test_golang_none():
    assert resolve_type(GoNone) == "nil"
    assert GoNone.default() == "nil"
    assert str(GoNone().build()) == "nil"


def test_golang_bool():
    assert resolve_type(GoBool) == "bool"
    assert GoBool.default() == "true"
    assert str(GoBool(True).build()) == "true"


def test_golang_string():
    assert resolve_type(GoString) == "string"
    assert GoString.default() == '""'
    assert str(GoString("Piotr").build()) == '"Piotr"'


def test_golang_vector():
    assert resolve_type(GoVector[GoInt]) == "[]int"
    assert GoVector[GoInt].default() == "nil"
    assert str(GoVector[GoInt]([1, 2, 3]).build()) == "{1, 2, 3}"


def test_golang_map():
    assert resolve_type(GoMap[GoInt, GoInt]) == "map[int]int"
    assert GoMap[GoInt, GoInt].default() == "nil"
    assert str(GoMap[GoInt, GoInt]({1: 1, 2: 2, 3: 3}).build()) == "{1: 1, 2: 2, 3: 3}"


def test_golang_nested_map_vector():
    assert resolve_type(GoMap[GoInt, GoVector[GoInt]]) == "map[int][]int"
    assert GoMap[GoInt, GoVector[GoInt]].default() == "nil"
    assert str(GoMap[GoInt, GoVector[GoInt]]({1: [1], 2: [2], 3: [3]}).build()) == "{1: {1}, 2: {2}, 3: {3}}"


def test_golang_pointer():
    assert resolve_type(GoPointer[GoInt]) == "*int"
    assert GoPointer[GoInt].default() == "nil"
    assert str(GoPointer[GoInt](5).build()) == "5"


def test_golang_list_node():
    assert resolve_type(GoListNode) == "ListNode"
    assert GoListNode.default() == "ListNode{}"
    assert str(GoListNode(5, GoNone())) == "ListNode{5, nil}"
    assert str(GoListNode(5, GoPointer[GoListNode](GoListNode(6, GoNone())))) == "ListNode{5, &ListNode{6, nil}}"


def test_golang_list_node_pointer():
    assert resolve_type(GoPointer[GoListNode]) == "*ListNode"
    assert GoPointer[GoListNode].default() == "nil"
    assert str(GoPointer[GoListNode](GoListNode(5, GoNone()))) == "&ListNode{5, nil}"
    assert (
            str(GoPointer[GoListNode](GoListNode(5, GoPointer[GoListNode](GoListNode(6, GoNone())))))
            == "&ListNode{5, &ListNode{6, nil}}"
    )


def test_single_linked_list_from_array():
    assert str(single_linked_list_from_array([])) == "nil"
    assert str(single_linked_list_from_array([1])) == "&ListNode{1, nil}"
    assert str(single_linked_list_from_array([1, 2])) == "&ListNode{1, &ListNode{2, nil}}"

#
# def test_signature_1():
#     arguments = (
#         Argument("numbers", Vector[Int]),
#         Argument("target", Int)
#     )
#     signature = Signature("two_sum", arguments, Int)
#     expected = "func two_sum(numbers []int, target int) int {\n    return 0\n}"
#
#     assert Go().resolve_signature(signature) == expected
