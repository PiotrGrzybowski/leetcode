package algos

func mySqrt(x int) int {
	if x == 0 {
		return 0
	} else if x < 4 {
		return 1
	} else {
		left := 1
		right := x / 2
		result := 0

		for left <= right {
			middle := left + (right-left)/2

			if middle <= x/middle {
				left = middle + 1
				result = middle
			} else {
				right = middle - 1
			}
		}
		return result
	}
}
