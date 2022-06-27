from generator.basics import *
from tasks.config import writer

function = "is_happy"
arguments = (
    Argument("number", Bool),
)

cases = [

    TestCase(function, [Int(19)], Bool(True)),
    TestCase(function, [Int(2)], Bool(False)),
]

signature = Signature(function, arguments, Int)
test = Test(function, cases)
writer.write_go(function, signature, test)
writer.write_python(function, signature, test)
