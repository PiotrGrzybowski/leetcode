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
	return map[int]int{1: 2, 4: 4}
}

func abdcd() map[int][]int {
	return map[int][]int{1: {1, 2}, 2: {1, 2}}
}

func abdcdd() map[int][]string {
	return map[int][]string{1: {"2", "2", "3"}, 2: {"1", "2", "3"}}
}

func main() {
	fmt.Println("KOs")
	assert.Equal(&testing.T{}, 1, 2)
	fmt.Println(abdc())

}
