package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMerge_Sorted_Arrays(t *testing.T) {
	assert.Equal(t, []int{1, 2, 2, 3, 5, 6}, merge([]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3))
	assert.Equal(t, []int{1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 8}, merge([]int{1, 2, 2, 3, 3, 4, 8, 0, 0, 0, 0, 0}, 7, []int{2, 2, 3, 3, 5}, 5))
	assert.Equal(t, []int{1}, merge([]int{1}, 1, []int{}, 0))
	assert.Equal(t, []int{1}, merge([]int{0}, 0, []int{1}, 1))
}
