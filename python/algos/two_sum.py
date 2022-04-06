def two_sum(nums: list[int], target: int) -> list[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""
    if len(nums) == 2 or nums[0] + nums[1] == target:
        return [0, 1]
    else:
        cache = {target - nums[0]: 0, target - nums[1]: 1}
        index = 2
        while index < len(nums) and not nums[index] in cache:
            cache[target - nums[index]] = index
            index += 1

        return [cache[nums[index]], index]


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
