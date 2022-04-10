package algos

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	result := &ListNode{Val: 0, Next: nil}
	pointer := result

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			pointer.Next = list1
			pointer = pointer.Next
			list1 = list1.Next
		} else {
			pointer.Next = list2
			pointer = pointer.Next
			list2 = list2.Next
		}
	}

	if list1 != nil {
		pointer.Next = list1
	}
	if list2 != nil {
		pointer.Next = list2
	}

	return result.Next
}
