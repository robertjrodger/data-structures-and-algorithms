from typing import Optional


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinarySearchTree:
    """
    Binary tree (either 1) empty or 2) two disjoin BTs) in symmetric order (every node's key is
    larger than all keys in left subtree and smaller than all keys in right subtree).

    Time complexity:
        Worst case: O(N) for both insert and search (think linear chain)
        Average: O(1.39 lg N) for both insert and search

    Note:
        + optimal key deletion is long-standing open problem!
        + balanced search trees guarantee O(lg N) performance for all operations
    """
    def __init__(self):
        self.root: optional[Node] = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, current, key, value):
        if current is None:
            return Node(key, value)
        elif current.key > key:
            current.left = self._put(current.left, key, value)
        elif current.key < key:
            current.right = self._put(current.right, key, value)
        else:
            current.value = value
        current.count = 1 + self._size(current.left) + self._size(current.right)
        return current

    def get(self, key):
        current = self.root
        while current is not None:
            if current.key > key:
                current = current.left
            elif current.key < key:
                current = current.right
            else:
                return current.value
        return None  # not found

    def delete(self, key):
        pass

    def min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

    def size(self):
        return self._size(self.root)

    def _size(self, current):
        if current is None:
            return 0
        else:
            return current.count

    def floor(self, key):
        "Biggest BST key that is smaller than or equal to given key"
        floor_node = self._floor(self.root, key)
        if floor_node is None:
            return None
        else:
            return floor_node.key

    def _floor(self, current, key):
        if current is None:
            return None
        elif current.key == key:
            return current
        elif current.key > key:
            return self._floor(current.left, key)
        else:
            right_floor_node = self._floor(current.right, key)
            if right_floor_node is not None:
                return right_floor_node
            else:
                return current

    def ceil(self, key):
        "Smallest BST key that is larger than or equal to given key"
        ceil_node = self._ceil(self.root, key)
        if ceil_node is None:
            return None
        else:
            return ceil_node.key

    def _ceil(self, current, key):
        if current is None:
            return None
        elif current.key == key:
            return current
        elif current.key < key:
            return self._ceil(current.right, key)
        else:
            left_ceil_node = self._ceil(current.left, key)
            if left_ceil_node is not None:
                return left_ceil_node
            else:
                return current

    def rank(self, key):
        "Number of nodes less than the key"
        return self._rank(self.root, key)

    def _rank(self, current, key):
        if current is None:
            return 0
        elif current.key == key:
            return self._size(current.left)
        elif current.key > k:
            return self._rank(current.left, key)
        else:
            return 1 + self._size(current.left) + self._rank(current.right)

    def get_ordered_keys(self):
        ordered_keys = []
        return self._get_ordered_keys(self.root, ordered_keys)

    def _get_ordered_keys(self, current, ordered_keys):
        if current is None:
            return ordered_keys
        ordered_keys = self._get_ordered_keys(current.left, ordered_keys)
        ordered_keys.append(current.key)
        ordered_keys = self._get_ordered_keys(current.right, ordered_keys)
        return ordered_keys

    def reverse(self):
        self.root = self._reverse(self.root)

    def _reverse(self, current):
        if current is not None:
            current.left, current.right = self._reverse(current.right), self._reverse(current.left)
        return current
