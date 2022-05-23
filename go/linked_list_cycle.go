package algos

func linkedListCycle(node *ListNode) bool {
	if node == nil {
		return false
	} else {
		slow := node
		fast := node
		for slow.Next != nil && fast.Next != nil && fast.Next.Next != nil {
			slow = slow.Next
			fast = fast.Next.Next
			if slow == fast {
				return true
			}
		}
		return false
	}
}
