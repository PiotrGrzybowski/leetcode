from typing import Optional


def single_number(numbers: list[int]) -> int:
    occurrences = {}
    for value in numbers:
        occurrences[value] = 1 + occurrences.get(value, 0)
    for value in numbers:
        if occurrences[value] == 1:
            return value


if __name__ == '__main__':
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
