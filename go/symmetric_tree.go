package algos

func isSymmetric(first *TreeNode, second *TreeNode) bool {
	if first == nil && second == nil {
		return true
	} else if first == nil || second == nil {
		return false
	} else {
		return first.Val == second.Val && isSymmetric(first.Left, second.Right) && isSymmetric(first.Right, second.Left)
	}
}

func symmetric_tree(node *TreeNode) bool {
	if node == nil {
		return true
	} else {
		return isSymmetric(node.Left, node.Right)
	}
}
