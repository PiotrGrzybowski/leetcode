package algos

func isSameTree(first *TreeNode, second *TreeNode) bool {
	if first == nil && second == nil {
		return true
	} else if (first == nil && second != nil) || (first != nil && second == nil) {
		return false
	} else {
		return first.Val == second.Val && isSameTree(first.Left, second.Left) && isSameTree(first.Right, second.Right)
	}
}
