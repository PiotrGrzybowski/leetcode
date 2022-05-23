package algos

func singleNumber(numbers []int) int {
	occurrences := make(map[int]int)
	for _, number := range numbers {
		if _, ok := occurrences[number]; ok {
			occurrences[number] += 1
		} else {
			occurrences[number] = 1
		}
	}
	for _, number := range numbers {
		if occurrences[number] == 1 {
			return number
		}
	}
	return 0
}
