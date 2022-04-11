package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRemoveElement(t *testing.T) {
	assert.Equal(t, removeElement([]int{3, 2, 2, 3}, 2), 2)
	assert.Equal(t, removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2), 5)
}
