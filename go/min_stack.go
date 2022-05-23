package algos

type StackNode struct {
	value   int
	minimum int
	next    *StackNode
}

type MinStack struct {
	top     *StackNode
	minimum int
}

func Constructor() MinStack {
	return MinStack{
		top:     nil,
		minimum: 0,
	}
}

func (s *MinStack) Push(val int) {
	if s.top == nil {
		s.top = &StackNode{val, val, nil}
	} else {
		node := &StackNode{val, min(val, s.GetMin()), s.top}
		s.top = node
	}
	if val < s.minimum {
		s.minimum = val
	}
}

func (s *MinStack) Pop() {
	s.top = s.top.next
}

func (s *MinStack) Top() int {
	return s.top.value
}

func (s *MinStack) GetMin() int {
	return s.top.minimum
}
