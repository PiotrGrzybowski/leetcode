package algos

func romanToInt(s string) int {
	digits := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	previous := 0
	result := 0
	for i := len(s) - 1; i >= 0; i-- {
		digit := digits[s[i]]
		if digits[s[i]] >= previous {
			result += digit
		} else {
			result -= digit
		}
		previous = digit
	}
	return result
}
