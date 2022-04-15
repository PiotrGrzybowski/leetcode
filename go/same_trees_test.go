package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestSame_Trees(t *testing.T) {

	assert.True(t, isSameTree(&TreeNode{
		Val: 5,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:   7,
			Left:  nil,
			Right: nil,
		},
	}, &TreeNode{
		Val: 5,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:   7,
			Left:  nil,
			Right: nil,
		},
	}))

	assert.False(t, isSameTree(&TreeNode{
		Val: 5,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:   7,
			Left:  nil,
			Right: nil,
		},
	}, &TreeNode{
		Val: 5,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:  7,
			Left: nil,
			Right: &TreeNode{
				Val:   99,
				Left:  nil,
				Right: nil,
			},
		},
	}))
}
