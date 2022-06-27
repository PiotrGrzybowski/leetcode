from generator.basics import *


class PythonVector(Vector[T]):
    @staticmethod
    def resolve(generic: Any) -> str:
        return f"list[{generic}]"

    @staticmethod
    def default() -> str:
        return "[]"

    def __str__(self):
        return f"[{str(super().__str__())}]"


class PythonMap(Map[T, S]):
    @staticmethod
    def resolve(key: Any, value: Any) -> str:
        return f"dict[{key}, {value}]"

    @staticmethod
    def default() -> str:
        return "{}"


class PythonString(String):
    @staticmethod
    def resolve():
        return "str"


class PythonInt(Int):
    @staticmethod
    def resolve():
        return "int"


class PythonBool(Bool):
    @staticmethod
    def resolve():
        return "bool"

    @staticmethod
    def default() -> str:
        return "True"

    def __str__(self) -> str:
        return str(self.data)


class PythonNone(Null):
    @staticmethod
    def resolve():
        return "None"

    def __str__(self):
        return PythonNone.resolve()


class PythonPointer(Pointer[T]):
    @staticmethod
    def resolve(generic: Any) -> str:
        return str(generic)

    @staticmethod
    def default() -> str:
        return "None"

    def __str__(self):
        return f"{str(self.data)}"


class PythonListNode(ListNode):
    @staticmethod
    def resolve():
        return "ListNode"

    @staticmethod
    def default() -> str:
        return "None"

    def __str__(self):
        return f"ListNode({str(self.data)}, {str(self.next)})"


def single_linked_list_from_array(values: list) -> PythonPointer | PythonNone:
    if values:
        head = PythonPointer(PythonListNode(values[0], PythonNone()))
        pointer = head
        for value in values[1:]:
            p = PythonPointer(PythonListNode(value, PythonNone()))
            pointer.data.next = p
            pointer = pointer.data.next
        return head
    else:
        return PythonNone()


class PythonSignature(Signature):
    def resolve(self) -> str:
        return f"{self._keyword()} {self.function}({self._arguments()}) -> {self._result_type()}: {self._body()}"

    def _keyword(self) -> str:
        return "def"

    def _arguments(self) -> str:
        return ", ".join([f"{argument.name}: {resolve_type(argument.argument_type)}" for argument in self.arguments])

    def _result_type(self) -> str:
        return resolve_type(self.result_type)

    def _body(self) -> str:
        return f"\n    return {self.result_type.default()}\n"


class PythonTestCase(TestCase):
    def __str__(self) -> str:
        return f"assert {self.function}({', '.join(self.resolve_inputs())}) == {self.resolve_expected()}"

    @staticmethod
    def _resolve_value(value):
        if hasattr(value, "__orig_class__"):
            return f"{value.build()}"
        else:
            return str(value.build())


class PythonTest(Test):
    def _resolve_test_signature(self) -> str:
        return f"def test_{self.function}():"

    def _resolve_test_body(self) -> str:
        return '\n    ' + '\n    '.join([str(case) for case in self.cases])

    def resolve(self) -> str:
        return self._resolve_test_signature() + self._resolve_test_body()


PYTHON_MAPPING = {
    Int: PythonInt,
    String: PythonString,
    Bool: PythonBool,
    Vector: PythonVector,
    Map: PythonMap,
    Null: PythonNone,
    Pointer: PythonPointer,
    ListNode: PythonListNode,
    Test: PythonTest,
    TestCase: PythonTestCase,
    Signature: PythonSignature
}
