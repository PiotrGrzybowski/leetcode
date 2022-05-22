from __future__ import annotations

from typing import Sequence


class TreeNode:
    def __init__(self, value: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = value
        self.left = left
        self.right = right


def sorted_array_to_bst_ranged(values: Sequence[int], left: int, right: int) -> TreeNode | None:
    if left > right:
        return None
    elif left == right:
        return TreeNode(values[left])
    else:
        middle = left + (right - left) // 2
        return TreeNode(
            values[middle],
            sorted_array_to_bst_ranged(values, left, middle - 1),
            sorted_array_to_bst_ranged(values, middle + 1, right),
        )


def sorted_array_to_bst(values: Sequence[int]) -> TreeNode | None:
    return sorted_array_to_bst_ranged(values, 0, len(values) - 1)


if __name__ == '__main__':
    sorted_array_to_bst([])
    sorted_array_to_bst([1])
    sorted_array_to_bst([-10, -3, 0, 5, 9])
