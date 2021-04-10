from typing import Optional


class Node:
    def __init__(self, item):
        self.item = item
        self.next: Optional[Node] = None


class Queue:
    def __init__(self):
        self.last: Optional[Node] = None
        self.first: Optional[Node] = None
        self.size: int = 0

    def enqueue(self, item):
        node = Node(item)
        if self.size == 0:
            self.last = node
            self.first = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            item = self.first.item
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self.size -= 1
            return item

    def is_empty(self):
        return self.size == 0
