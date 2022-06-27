package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)



func TestMajorityElement(t *testing.T) {
    assert.Equal(t, majorityElement([]int{3, 2, 3}), 3)
    assert.Equal(t, majorityElement([]int{2, 2, 1, 1, 1, 2, 2}), 2)
}
