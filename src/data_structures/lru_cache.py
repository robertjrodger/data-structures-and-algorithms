from collections import OrderedDict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None


class LRUQueue:
    def __init__(self):
        self.left_end: Optional[Node] = None
        self.right_end: Optional[Node] = None

    def push_left(self, node: Node):
        if self.left_end is None:
            self.left_end = node
            self.right_end = node
        else:
            node.right = self.left_end
            self.left_end.left = node
            self.left_end = node

    def pop_right(self):
        node = self.right_end
        self.right_end = self.right_end.left
        if self.right_end is None:
            self.left_end = None
        else:
            self.right_end.right = None
        return node

    def move_to_left(self, node: Node):
        left = node.left
        right = node.right
        if left is None:
            return
        left.right = right
        if right is not None:
            right.left = left
        node.left = None
        node.right = self.left_end
        self.left_end.left = node
        self.left_end = node


class LRUCache:
    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.current_size: int = 0
        self.data: dict = dict()
        self.queue: LRUQueue = LRUQueue()

    def put(self, key, value):
        node = self.data.get(key)
        if node:
            node.value = value
            self.queue.move_to_left(node)
        else:
            if self.current_size == self.max_size:
                node = self.queue.pop_right()
                self.data.pop(node.key)
                self.current_size -= 1
            node = Node(key, value)
            self.data[key] = node
            self.queue.push_left(node)
            self.current_size += 1

    def get(self, key):
        node = self.data.get(key)
        if node:
            value = node.value
            self.queue.move_to_left(node)
            return value
        else:
            return None


class OrderedDictLRUCache:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.cache: OrderedDict = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        else:
            return None

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            oldest = next(iter(self.cache))
            del self.cache[oldest]
