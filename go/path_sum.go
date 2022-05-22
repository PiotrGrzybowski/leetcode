package algos

func pathSum(node *TreeNode, targetSum int) bool {
	if node == nil {
		return false
	} else if node.Left == nil && node.Right == nil {
		return node.Val == targetSum
	} else {
		return pathSum(node.Left, targetSum-node.Val) || pathSum(node.Right, targetSum-node.Val)
	}
}
