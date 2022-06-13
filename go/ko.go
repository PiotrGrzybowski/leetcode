package main

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"testing"
)

func main() {
	fmt.Println("KOs")
	assert.Equal(&testing.T{}, 1, 2)
}
