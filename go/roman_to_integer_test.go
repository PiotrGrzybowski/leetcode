package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRomanToInteger(t *testing.T) {
	assert.Equal(t, 3, romanToInt("III"))
	assert.Equal(t, 58, romanToInt("LVIII"))
	assert.Equal(t, 1994, romanToInt("MCMXCIV"))
}
