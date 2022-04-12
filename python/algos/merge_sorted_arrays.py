def merge(first: list[int], m: int, second: list[int], n: int) -> list[int]:
    first_index = m - 1
    second_index = n - 1
    target_index = m + n - 1

    while second_index >= 0:
        if first_index >= 0 and first[first_index] > second[second_index]:
            first[target_index] = first[first_index]
            target_index -= 1
            first_index -= 1
        else:
            first[target_index] = second[second_index]
            target_index -= 1
            second_index -= 1
    return first


if __name__ == '__main__':
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert merge([1, 2, 2, 3, 3, 4, 8, 0, 0, 0, 0, 0], 7, [2, 2, 3, 3, 5], 5) == [1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 8]
    assert merge([1], 1, [], 0) == [1]
    assert merge([0], 0, [1], 1) == [1]
    assert merge([2, 0], 1, [1], 1) == [1, 2]
