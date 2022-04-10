def is_left(sign: str) -> bool:
    """Checks if the given sign is left parentheses."""
    return sign == "(" or sign == "{" or sign == "["


def valid_parentheses(expression: str) -> bool:
    """Checks if given expression parentheses are correct."""
    mapping = {")": "(", "]": "[", "}": "{"}
    stack = []
    for sign in expression:
        if is_left(sign):
            stack.append(sign)
        else:
            if not stack or stack[-1] != mapping[sign]:
                return False
            else:
                stack.pop()
    return True


if __name__ == "__main__":
    assert valid_parentheses("()")
    assert valid_parentheses("([][]{}")
    assert not valid_parentheses("([)")
