from pathlib import Path

TEMPLATES_PATH = Path('/Users/alphabrain/Workspace/Projects/algos/generator/templates')
s1 = "sorted_array_to_bst_ranged(nums: &mut Vec<i32>, left: usize, right: usize)"
s2 = "Option<Rc<RefCell<TreeNode>>>"


def extract_arguments(signature: str):
    index = signature.index("(")
    arguments = signature[index + 1: len(signature) - 1]
    print(arguments.split(', '))
    return arguments.split(', ')



generics_mapping = {
    'Vec': 0,
    'HashMap': 0
}

if __name__ == '__main__':
    arguments = extract_arguments(s1)
    for argument in arguments:
        name, argument_type = argument.split(": ")
        print(argument_type)
