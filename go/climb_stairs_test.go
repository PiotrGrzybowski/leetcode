package algos

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestClimb_Stairs(t *testing.T) {
    assert.Equal(t, 2, climbStairs(2))
    assert.Equal(t, 3, climbStairs(3))
    assert.Equal(t, 34, climbStairs(8))
    assert.Equal(t, 1597, climbStairs(16))
}
