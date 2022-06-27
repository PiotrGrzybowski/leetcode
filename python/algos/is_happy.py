def digits_squared_sum(number: int) -> int:
    result = 0
    while number > 0:
        result += (number % 10) ** 2
        number //= 10
    return result


def is_happy(number: int) -> bool:
    seen = set()
    number = digits_squared_sum(number)
    while number != 1 and number not in seen:
        seen.add(number)
        number = digits_squared_sum(number)
    return number == 1


def test_is_happy():
    assert is_happy(19)
    assert not is_happy(2)
