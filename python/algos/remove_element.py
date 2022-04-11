from typing import List


def remove_element(nums: List[int], value: int) -> int:
    """Removes value from nums in place."""
    i = 0
    for x in nums:
        if x != value:
            nums[i] = x
            i += 1
    return i


if __name__ == "__main__":
    assert remove_element([3, 2, 2, 3], 3) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
