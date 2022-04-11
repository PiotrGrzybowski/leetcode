package algos

import "math"

func max(x int, y int) int {
	if x < y {
		return y
	}
	return x
}

func maxSubArray(nums []int) int {
	best := math.MinInt64
	currentMax := 0
	for _, value := range nums {
		currentMax = max(value, currentMax+value)
		best = max(best, currentMax)
	}
	return best
}
