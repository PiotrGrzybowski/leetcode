package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestLinked_List_Cycle(t *testing.T) {
	node := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val:  2,
			Next: nil,
		},
	}
	node.Next.Next = node
	assert.Equal(t, true, linkedListCycle(node))
}
