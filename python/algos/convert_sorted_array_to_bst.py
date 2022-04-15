from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


def sorted_array_to_bst(nums: list[int], left: int, right: int) -> Optional[TreeNode]:
    if left > right:
        return None
    elif left == right:
        return TreeNode(nums[left])
    elif right - left == 1:
        return TreeNode(nums[right], TreeNode(nums[left]))
    elif right - left == 2:
        return TreeNode(nums[left + 1], TreeNode(nums[left]), TreeNode(nums[right]))
    else:
        middle = left + (right - left) // 2
        return TreeNode(nums[middle], sorted_array_to_bst(nums, left, middle - 1), sorted_array_to_bst(nums, middle + 1, right))


if __name__ == '__main__':
    array = [-10, -3, 0, 5, 9]
    result = sorted_array_to_bst(array, 0, len(array) - 1)
