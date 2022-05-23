import string


def is_palindrome(text: str) -> bool:
    text = [char for char in text.lower() if char.isalnum()]
    if len(text) == 0:
        return True
    else:
        index = 0
        while index < len(text) // 2:
            if text[index] == text[len(text) - 1 - index]:
                index += 1
            else:
                return False
    return True


if __name__ == '__main__':
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("race a car")
    assert is_palindrome(" ")
