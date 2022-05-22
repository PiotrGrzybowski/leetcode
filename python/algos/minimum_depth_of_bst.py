from __future__ import annotations


class TreeNode:
    def __init__(self, value: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = value
        self.left = left
        self.right = right


def minimum_depth_of_bst(node: TreeNode | None) -> int:
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    elif node.left is None:
        return 1 + minimum_depth_of_bst(node.right)
    elif node.right is None:
        return 1 + minimum_depth_of_bst(node.left)
    else:
        return 1 + min(minimum_depth_of_bst(node.left), minimum_depth_of_bst(node.right))


if __name__ == '__main__':
    assert minimum_depth_of_bst(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15, TreeNode(8)), TreeNode(7)))) == 2

    assert minimum_depth_of_bst(TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))) == 5
    assert minimum_depth_of_bst(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 2
