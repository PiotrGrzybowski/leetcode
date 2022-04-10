from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    """Removes duplicates from sorted list in place."""
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == '__main__':
    assert remove_duplicates_from_sorted_array([1, 1, 2]) == 2
    assert remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
