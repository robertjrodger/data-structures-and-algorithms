from collections import deque


class Node:
    def __init__(self, item):
        self.item = item
        self.next: Optional[Node] = None


class Stack:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0

    def push(self, item):
        node = Node(item)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item


class DequeStack:
    def __init__(self):
        self.deque: deque = deque()

    def push(self, item):
        self.deque.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop()

    def is_empty(self):
        return len(self.deque) == 0
