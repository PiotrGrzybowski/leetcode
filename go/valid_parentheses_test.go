package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestValidParentheses(t *testing.T) {
	assert.True(t, validParentheses("{}{}"))
	assert.True(t, validParentheses("[[]]"))
	assert.False(t, validParentheses("{{{"))
}
