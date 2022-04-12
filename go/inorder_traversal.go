package algos

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func help(root *TreeNode, result []int) []int {
	if root != nil {
		result = help(root.Left, result)
		result = append(result, root.Val)
		result = help(root.Right, result)
	}
	return result
}

func inorderTraversal(root *TreeNode) []int {
	var result []int
	return help(root, result)
}
