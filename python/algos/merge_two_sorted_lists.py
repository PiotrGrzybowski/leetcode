from typing import Optional


class ListNode:
    """Struct representing a Node in LinkedList."""

    def __init__(self, value=0, next=None) -> None:
        """Node init method."""
        self.val = value
        self.next = next

    def __eq__(self, other):
        if other is self:
            return True
        elif not isinstance(other, ListNode):
            return False
        else:
            pointer = self
            while pointer and other and pointer.val == other.val:
                pointer = pointer.next
                other = other.next

            return pointer is None and other is None


def merge_two_lists(first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into single one."""
    result: ListNode = ListNode(0)
    pointer = result
    while first and second:
        if first.val <= second.val:
            pointer.next = first
            first = first.next
            pointer = pointer.next
        else:
            pointer.next = second
            second = second.next
            pointer = pointer.next

    if first:
        pointer.next = first
    if second:
        pointer.next = second

    return result.next


if __name__ == "__main__":
    assert merge_two_lists(None, None) is None
    assert merge_two_lists(None, ListNode(0, ListNode(2))) == ListNode(0, ListNode(2))
    assert merge_two_lists(ListNode(0, ListNode(2, ListNode(4))), ListNode(0, ListNode(2))) == ListNode(
        0, ListNode(0, ListNode(2, ListNode(2, ListNode(4))))
    )
