def majority_element(numbers: list[int]) -> int:
    score = 0
    candidate = None
    for value in numbers:
        if score == 0:
            candidate = value
            score = 1
        elif value == candidate:
            score += 1
        else:
            score -= 1
    return candidate


def test_majority_element():
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
