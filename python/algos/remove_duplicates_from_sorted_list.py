class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
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


def remove_duplicates(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    elif not head.next:
        return head
    else:
        pointer = head
        while pointer is not None:
            while pointer.next is not None and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            pointer = pointer.next
        return head


if __name__ == '__main__':
    assert remove_duplicates(None) is None
    assert remove_duplicates(ListNode(5)) == ListNode(5)
