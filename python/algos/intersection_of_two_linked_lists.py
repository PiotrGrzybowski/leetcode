class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(first: ListNode, second: ListNode) -> ListNode | None:
    first_pointer = first
    second_pointer = second
    first_length = 0
    second_length = 0

    while first_pointer is not None:
        first_length += 1
        first_pointer = first_pointer.next

    while second_pointer is not None:
        second_length += 1
        second_pointer = second_pointer.next

    difference = abs(first_length - second_length)
    if second_length > first_length:
        tmp = first
        first = second
        second = tmp

    i = 0
    first_pointer = first
    second_pointer = second
    while i < difference:
        first_pointer = first_pointer.next
        i += 1

    while first_pointer is not None and second_pointer is not None and first_pointer is not second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    if first_pointer is second_pointer:
        return first_pointer
    else:
        return None

