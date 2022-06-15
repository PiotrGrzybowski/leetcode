package main

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"testing"
)

func abc() [][]map[int]int {
	return nil
}

func abdc() map[int]int {
	return nil
}

func main() {
	fmt.Println("KOs")
	assert.Equal(&testing.T{}, 1, 2)
	fmt.Println(abdc())

}
