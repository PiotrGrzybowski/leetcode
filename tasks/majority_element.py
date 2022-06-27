from generator.basics import *
from tasks.config import writer

function = "majority_element"
arguments = (
    Argument("numbers", Vector[Int]),
)

cases = [
    TestCase(function, [Vector[Int]([3, 2, 3])], Int(3)),
    TestCase(function, [Vector[Int]([2, 2, 1, 1, 1, 2, 2])], Int(2))
]

signature = Signature(function, arguments, Int)
test = Test(function, cases)
writer.write_go(function, signature, test)
writer.write_python(function, signature, test)
