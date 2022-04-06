package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestIsPalindrome(t *testing.T) {
	assert.True(t, isPalindrome(121))
	assert.True(t, isPalindrome(11122111))
	assert.False(t, isPalindrome(-121))
	assert.False(t, isPalindrome(1321))
}
