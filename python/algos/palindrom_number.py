def is_palindrome(number: int) -> bool:
    """Given an integer x, return true if x is palindrome integer."""
    if number < 0 or (number % 10 == 0 and number != 0):
        return False
    elif number < 10:
        return True
    else:
        reversed_number = 0
        while number > reversed_number:
            reversed_number = reversed_number * 10 + number % 10
            number //= 10
        return reversed_number == number or number == reversed_number // 10


if __name__ == "__main__":
    assert is_palindrome(131)
    assert not is_palindrome(-131)
    assert not is_palindrome(1351)
    assert is_palindrome(139931)
