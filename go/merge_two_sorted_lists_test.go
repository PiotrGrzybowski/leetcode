package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMergeTwoSortedListsBothEmpty(t *testing.T) {
	assert.Nil(t, mergeTwoLists(nil, nil))
}

func TestMergeTwoSortedListsBothNotEmpty(t *testing.T) {
	list1 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val:  4,
				Next: nil,
			},
		},
	}

	list2 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 3,
			Next: &ListNode{
				Val:  4,
				Next: nil,
			},
		},
	}

	result := mergeTwoLists(list1, list2)

	assert.Equal(t, result.Val, 1)
	assert.Equal(t, result.Next.Val, 1)
	assert.Equal(t, result.Next.Next.Val, 2)
	assert.Equal(t, result.Next.Next.Next.Val, 3)
	assert.Equal(t, result.Next.Next.Next.Next.Val, 4)
	assert.Equal(t, result.Next.Next.Next.Next.Next.Val, 4)
}
