from pathlib import Path
import shutil
from generator.basics import *
from generator.utils import TEMPLATES_PATH


class GoVector(Vector[T]):
    @staticmethod
    def resolve(generic: Any) -> str:
        return f"[]{generic}"

    @staticmethod
    def default() -> str:
        return "nil"

    def __str__(self):
        return f"{{{str(super().__str__())}}}"


class GoMap(Map[T, S]):
    @staticmethod
    def resolve(key: Any, value: Any) -> str:
        return f"map[{key}]{value}"

    @staticmethod
    def default() -> str:
        return "nil"


class GoPointer(Pointer[T]):
    @staticmethod
    def resolve(generic: Any) -> str:
        return f"*{generic}"

    @staticmethod
    def default() -> str:
        return "nil"

    def __str__(self):
        if isinstance(self.data, Basic):
            return f"{str(self.data)}"
        else:
            return f"&{str(self.data)}"


class GoString(String):
    @staticmethod
    def resolve():
        return "string"


class GoInt(Int):
    @staticmethod
    def resolve():
        return "int"


class GoBool(Bool):
    @staticmethod
    def resolve():
        return "bool"

    @staticmethod
    def default() -> str:
        return "true"

    def __str__(self):
        return str(self.data).lower()


class GoNone(Null):
    @staticmethod
    def resolve():
        return "nil"


class GoListNode(ListNode):
    @staticmethod
    def resolve():
        return "ListNode"

    @staticmethod
    def default() -> str:
        return "ListNode{}"

    def __str__(self):
        return f"ListNode{{{str(self.data)}, {str(self.next)}}}"


def single_linked_list_from_array(values: list) -> GoPointer | GoNone:
    if values:
        head = GoPointer(GoListNode(values[0], GoNone()))
        pointer = head
        for value in values[1:]:
            p = GoPointer(GoListNode(value, GoNone()))
            pointer.data.next = p
            pointer = pointer.data.next
        return head
    else:
        return GoNone()


class GoSignature(Signature):
    def __init__(self, function: str, arguments: tuple, result_type: Any) -> None:
        super().__init__(snake_case_to_semi_camel_case(function), arguments, result_type)

    def resolve(self) -> str:
        return f"{self._keyword()} {self.function}({self._arguments()}) {self._result_type()} {self._body()}"

    def _keyword(self) -> str:
        return "func"

    def _arguments(self) -> str:
        return ", ".join([f"{argument.name} {resolve_type(argument.argument_type)}" for argument in self.arguments])

    def _result_type(self) -> str:
        return resolve_type(self.result_type)

    def _body(self) -> str:
        return f"{{\n    return {self.result_type.default()}\n}}"


class GoTestCase(TestCase):
    def __init__(self, function: str, inputs, expected) -> None:
        super().__init__(snake_case_to_semi_camel_case(function), inputs, expected)

    def __str__(self) -> str:
        return f"assert.Equal(t, {self.function}({', '.join(self.resolve_inputs())}), {self.resolve_expected()})"

    @staticmethod
    def _resolve_value(value):
        if hasattr(value, "__orig_class__"):
            return f"{resolve_type(value.__orig_class__)}{value.build()}"
        else:
            return str(value.build())


class GoTest(Test):
    def __init__(self, function: str, cases: list[TestCase]) -> None:
        super().__init__(snake_case_to_camel_case(function), cases)

    def _resolve_test_signature(self) -> str:
        return f"func Test{self.function}(t *testing.T) "

    def _resolve_test_body(self) -> str:
        return "{{\n    {}\n}}".format('\n    '.join([str(case) for case in self.cases]))

    def resolve(self) -> str:
        return self._resolve_test_signature() + self._resolve_test_body()


GO_MAPPING = {
    Int: GoInt,
    String: GoString,
    Bool: GoBool,
    Vector: GoVector,
    Map: GoMap,
    Null: GoNone,
    Pointer: GoPointer,
    ListNode: GoListNode,
    Test: GoTest,
    TestCase: GoTestCase,
    Signature: GoSignature,
}

if __name__ == '__main__':
    l = Pointer[ListNode](ListNode(Int(5), Null())).build()
    print(resolve_type(cast_type(Pointer[ListNode], GO_MAPPING)))
    print(l)

    print(cast_value(l, GO_MAPPING))
    print(cast_type(Pointer[ListNode], GO_MAPPING))
#     # a = Vector[Int]
#     # print(cast(a, MAPPING))
#     # b = Vector[Vector[Int]]([[2], [7], [11], [15]]).build()
#     # print(b)
#     # print(cast(b.__orig_class__, MAPPING))
#     # print(GoVector[GoVector[GoInt]]([[2], [7], [11], [15]]).build())
#     print(type(Int(5)))
#     print(type(Int(5)) in GO_MAPPING)
#     for k, v in GO_MAPPING.items():
#         print(k)
#
#     print(type(Int(5)) == Int)
#     print(type(Int(5)) in GO_MAPPING)
#
#     print(Vector[Int]([1, 2, 3]).__dict__)
#     # print(cc(Vector[Int]([1, 2, 3]), MAPPING).__dict__)
#     value = Vector[Int]([1, 2, 3])
#     value_type = value.__orig_class__
#     print(value_type.__dict__)
#     # cc(Vector[Int]([1, 2, 3]), MAPPING)
#
#     print(cast_type(Vector[Int], GO_MAPPING))
#     """cast origin do nowego"""
#     c = TestCase("two_sum", [Vector[Int]([2, 7, 11, 15]), Int(9)], Vector[Int]([0, 1]))
#     # v = Vector[Int]([2, 7, 11, 15])
#     # print(cast_type(type(v), MAPPING))
#     #
#     # print(cast_value(Int(5), MAPPING))
#     # print(cast_value(Vector[Int]([1, 2, 3]), MAPPING))
