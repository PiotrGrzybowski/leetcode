from typing import List


def max_sub_array(nums: List[int]) -> int:
    """Returns sum of max possible subarray."""
    best = float("-inf")
    current_max = 0

    for value in nums:
        current_max = max(value, current_max + value)
        best = max(best, current_max)

    return best


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
