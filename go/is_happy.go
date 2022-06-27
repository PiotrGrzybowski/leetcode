package algos

func digitsSquaredSum(number int) int {
	result := 0
	for number > 0 {
		result += (number % 10) * (number % 10)
		number = number / 10
	}

	return result
}

func isHappy(number int) bool {
	seen := make(map[int]bool)
	for number != 1 {
		if _, ok := seen[number]; ok {
			break
		} else {
			seen[number] = true
			number = digitsSquaredSum(number)
		}
	}
	return number == 1
}
