package algos

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	} else {
		return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
	}
}
