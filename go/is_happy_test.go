package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)



func TestIsHappy(t *testing.T) {
    assert.Equal(t, isHappy(19), true)
    assert.Equal(t, isHappy(2), false)
}
