package algos

func minimumDepthOfBst(root *TreeNode) int {
	if root == nil {
		return 0
	} else if root.Right == nil && root.Left == nil {
		return 1
	} else if root.Left == nil {
		return 1 + minimumDepthOfBst(root.Right)
	} else if root.Right == nil {
		return 1 + minimumDepthOfBst(root.Left)
	} else {
		return 1 + min(minimumDepthOfBst(root.Left), minimumDepthOfBst(root.Right))
	}
}
