from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_trees(first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
    if first is None and second is None:
        return True
    elif (first is None and second is not None) or (first is not None and second is None):
        return False
    else:
        return first.val == second.val and same_trees(first.left, second.left) and same_trees(first.right, second.right)


if __name__ == '__main__':
    assert same_trees(TreeNode(2), TreeNode(2))
    assert same_trees(TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(2, TreeNode(1), TreeNode(3)))
    assert not same_trees(TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(2, TreeNode(1), TreeNode(3)))
