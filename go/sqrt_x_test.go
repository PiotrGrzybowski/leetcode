package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMySqrt(t *testing.T) {
	assert.Equal(t, 0, mySqrt(0))
	assert.Equal(t, 1, mySqrt(1))
	assert.Equal(t, 1, mySqrt(3))
	assert.Equal(t, 2, mySqrt(4))
	assert.Equal(t, 2, mySqrt(8))
	assert.Equal(t, 4, mySqrt(16))
	assert.Equal(t, 46339, mySqrt(2147395599))
}
