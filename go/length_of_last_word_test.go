package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestLengthOfLastWord(t *testing.T) {
	assert.Equal(t, 5, lengthOfLastWord("Hello World"))
	assert.Equal(t, 6, lengthOfLastWord("luffy is still joyboy"))
	assert.Equal(t, 4, lengthOfLastWord("   fly me   to   the moon  "))
	assert.Equal(t, 1, lengthOfLastWord("a"))
}
