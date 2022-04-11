def my_sqrt(x: int) -> int:
    """Calculates integer sqrt."""
    if x == 0:
        return 0
    elif x < 4:
        return 1
    else:
        left = 2
        right = x // 2
        result = 2

        while left <= right:
            middle = left + (right - left) // 2
            if middle <= x / middle:
                left = middle + 1
                result = middle
            else:
                right = middle - 1

        return result


if __name__ == '__main__':
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(3) == 1
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2
    assert my_sqrt(16) == 4
    assert my_sqrt(2147395599) == 46339
