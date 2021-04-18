from typing import Optional


class Node:
    def __init__(self, item):
        self.item = item
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None


class DoublyLinkedList:
    def __init__(self):
        self.left_end: Optional[Node] = None
        self.right_end: Optional[Node] = None
        self.size: int = 0

    def push_left(self, item):
        node = Node(item)
        if self.size == 0:
            self.left_end = node
            self.right_end = node
        else:
            node.right = self.left_end
            self.left_end.left = node
            self.left_end = node
        self.size += 1

    def push_right(self, item):
        node = Node(item)
        if self.size == 0:
            self.right_end = node
            self.left_end = node
        else:
            node.left = self.right_end
            self.right_end.right = node
            self.right_end = node
        self.size += 1

    def pop_left(self):
        if self.size == 0:
            return None
        else:
            item = self.left_end.item
            self.left_end = self.left_end.right
            self.size -= 1
            if self.size == 0:
                self.right_end = None
            return item

    def pop_right(self):
        if self.size == 0:
            return None
        else:
            item = self.right_end.item
            self.right_end = self.right_end.left
            self.size -= 1
            if self.size == 0:
                self.left_end = None
            return item
