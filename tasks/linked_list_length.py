from generator.basics import *
from tasks.config import writer

function = "linked_list_length"
arguments = (
    Argument("node", Pointer[ListNode]),
)

cases = [
    # TestCase(function, [Null()], Int(0)),
    TestCase(function, [Pointer[ListNode](ListNode(Int(1), Pointer[ListNode](ListNode(Int(2), Pointer[ListNode](ListNode(3, Pointer[ListNode](ListNode(4, Null()))))))))], Int(4)),
]

signature = Signature(function, arguments, Int)
test = Test(function, cases)
writer.write_go(function, signature, test)
writer.write_python(function, signature, test)
