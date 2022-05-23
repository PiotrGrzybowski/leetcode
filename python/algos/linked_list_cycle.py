from typing import Optional


class ListNode:
    def __init__(self, x, b=None):
        self.val = x
        self.next = b


def linked_list_cycle(node: ListNode) -> bool:
    if node:
        visited = set()
        while node is not None and node not in visited:
            visited.add(node)
            node = node.next
        return node in visited

    else:
        return False


def linked_list_cycle(node: ListNode) -> bool:
    if node is None:
        return False
    else:
        slow = node
        fast = node
        while slow.next is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == '__main__':
    assert not linked_list_cycle(ListNode(1))

    node = ListNode(1)
    node.next = ListNode(2, node)
    assert linked_list_cycle(node)
