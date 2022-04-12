package algos

func removeDuplicatesFromSortedList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	} else if head.Next == nil {
		return head
	} else {
		pointer := head
		for pointer != nil {
			for pointer.Next != nil && pointer.Val == pointer.Next.Val {
				pointer.Next = pointer.Next.Next
			}
			pointer = pointer.Next
		}
		return head
	}
}
