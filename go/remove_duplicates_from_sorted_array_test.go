package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRemoveDuplicatesFromSortedArray(t *testing.T) {
	assert.Equal(t, removeDuplicates([]int{1, 1, 2}), 2)
	assert.Equal(t, removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}), 5)
}
