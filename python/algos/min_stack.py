from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    minimum: int
    pointer: Node | None = None


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head:
            self.head = Node(val, min(self.head.minimum, val), self.head)
        else:
            self.head = Node(val, val)

    def pop(self) -> None:
        self.head = self.head.pointer

    def top(self) -> int:
        return self.head.test

    def getMin(self) -> int:
        return self.head.minimum
