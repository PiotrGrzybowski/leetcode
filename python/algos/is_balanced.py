class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def depth(node: TreeNode | None, cache) -> int:
    if node in cache:
        return cache[node]
    else:
        if node is None:
            return 0
        else:
            result = 1 + max(depth(node.left, cache), depth(node.right, cache))
            cache[node] = result
            return result


def is_balanced(node: TreeNode | None, cache) -> bool:
    if node is None:
        return True
    else:
        return abs(depth(node.left, cache) - depth(node.right, cache)) <= 1 and is_balanced(node.left, cache) and is_balanced(node.right, cache)


if __name__ == '__main__':
    tree = TreeNode(2,
                    TreeNode(2,
                             TreeNode(3,
                                      TreeNode(4),
                                      TreeNode(4)),
                             TreeNode(3)),
                    TreeNode(2))
