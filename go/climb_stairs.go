package algos

func climbStairs(stairs int) int {
	if stairs == 1 {
		return 1
	} else if stairs == 2 {
		return 2
	} else {
		earlier := 1
		last := 2
		answer := 0
		for stairs > 2 {
			answer = earlier + last
			earlier = last
			last = answer
			stairs -= 1
		}
		return answer
	}
}
