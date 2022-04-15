from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_bst(tree: Optional[TreeNode]) -> bool:
    return 0 if tree is None else 1 + max(max_depth_bst(tree.left), max_depth_bst(tree.right))


if __name__ == '__main__':
    assert max_depth_bst(TreeNode(2)) == 3
