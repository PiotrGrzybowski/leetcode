package algos

import (
	"fmt"
	"testing"
)

func TestInorder_Traversal(t *testing.T) {
	r := &TreeNode{
		Val:  1,
		Left: nil,
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val:   3,
				Left:  nil,
				Right: nil,
			},
		},
	}
	ans := inorderTraversal(r)
	fmt.Println(ans)
	//assert.Equal(t, []int{[1, 3, 2]}, inorderTraversal(1))
}
