from __future__ import annotations


class TreeNode:
    def __init__(self, value: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = value
        self.left = left
        self.right = right


def path_sum(node: TreeNode | None, target_sum: int) -> bool:
    if node is None:
        return False
    elif node.right is None and node.left is None:
        return node.val == target_sum
    else:
        return path_sum(node.left, target_sum - node.val) or path_sum(node.right, target_sum - node.val)
