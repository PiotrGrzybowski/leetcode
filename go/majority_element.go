package algos

func majorityElement(numbers []int) int {
	score := 0
	var candidate int

	for i := 0; i < len(numbers); i++ {
		if score == 0 {
			score = 1
			candidate = numbers[i]
		} else if numbers[i] == candidate {
			score += 1
		} else {
			score -= 1
		}
	}
	return candidate
}
