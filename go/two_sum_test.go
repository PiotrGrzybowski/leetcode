package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test1(t *testing.T) {
	assert.Equal(t, twoSum([]int{2, 7, 11, 15}, 9), []int{0, 1})
	assert.Equal(t, twoSum([]int{3, 2, 4}, 6), []int{1, 2})
	assert.Equal(t, twoSum([]int{3, 3, 6}, 6), []int{0, 1})
}
