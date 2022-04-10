package algos

func isLeft(sign byte) bool {
	return sign == '(' || sign == '[' || sign == '{'
}

func validParentheses(expression string) bool {
	mapping := map[byte]byte{')': '(', ']': '[', '}': '{'}
	var stack []byte

	for i := 0; i < len(expression); i++ {
		if isLeft(expression[i]) {
			stack = append(stack, expression[i])
		} else {
			if len(stack) == 0 || mapping[expression[i]] != stack[len(stack)-1] {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}

	return len(stack) == 0
}
