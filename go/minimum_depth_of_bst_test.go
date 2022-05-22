package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMinimum_Depth_Of_Bst(t *testing.T) {
	tree := &TreeNode{
		Val: 6,
		Left: &TreeNode{
			Val: 1,
			Left: &TreeNode{
				Val:   3,
				Left:  nil,
				Right: nil,
			},
			Right: nil,
		},
		Right: nil,
	}
	assert.Equal(t, 1, minimumDepthOfBst(tree))
}
