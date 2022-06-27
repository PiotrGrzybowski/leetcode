
from generator.basics import *
from tasks.config import writer

function = "two_sum"
arguments = (
    Argument("numbers", Vector[Int]),
    Argument("target", Int)
)

cases = [
    TestCase(function, [Vector[Int]([2, 7, 11, 15]), Int(9)], Vector[Int]([0, 1])),
    TestCase(function, [Vector[Int]([3, 2, 4]), Int(6)], Vector[Int]([1, 2]))
]

signature = Signature(function, arguments, Int)
test = Test(function, cases)
writer.write_go(function, signature, test)
writer.write_python(function, signature, test)
