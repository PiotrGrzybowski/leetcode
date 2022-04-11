package algos

func lengthOfLastWord(s string) int {
	i := len(s) - 1
	for s[i] == ' ' {
		i -= 1
	}
	pointer := i
	for i >= 0 && s[i] != ' ' {
		i -= 1
	}
	return pointer - i
}
