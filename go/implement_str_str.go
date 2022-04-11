package algos

func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	} else {
		index := 0
		for index <= len(haystack) - len(needle) {
			i := 0
			for i < len(needle) && haystack[index + i] == needle[i] {
				i += 1
			}
			if i == len(needle) {
				return index
			}
			index += 1
		}
		return -1
	}
}