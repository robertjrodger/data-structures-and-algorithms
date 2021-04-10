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

    def _put(self, current_node, key, value):
        if current_node is None:
            return Node(key, value)
        elif current_node.key > key:
            current_node.left = self._put(current_node.left, key, value)
        elif current_node.key < key:
            current_node.right = self._put(current_node.right, key, value)
        else:
            current_node.value = value
        current_node.count = 1 + self._size(current_node.left) + self._size(current_node.right)
        return current_node

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
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.key

    def max(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.key

    def size(self):
        return self._size(self.root)

    def _size(self, current_node):
        if current_node is None:
            return 0
        else:
            return current_node.count

    def floor(self, key):
        "Biggest BST key that is smaller than or equal to given key"
        floor_node = self._floor(self.root, key)
        if floor_node is None:
            return None
        else:
            return floor_node.key

    def _floor(self, current_node, key):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._floor(current_node.left, key)
        else:
            right_floor_node = self._floor(current_node.right, key)
            if right_floor_node is not None:
                return right_floor_node
            else:
                return current_node

    def ceil(self, key):
        "Smallest BST key that is larger than or equal to given key"
        ceil_node = self._ceil(self.root, key)
        if ceil_node is None:
            return None
        else:
            return ceil_node.key

    def _ceil(self, current_node, key):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key < key:
            return self._ceil(current_node.right, key)
        else:
            left_ceil_node = self._ceil(current_node.left, key)
            if left_ceil_node is not None:
                return left_ceil_node
            else:
                return current_node

    def rank(self, key):
        "Number of nodes less than the key"
        return self._rank(self.root, key)

    def _rank(self, current_node, key):
        if current_node is None:
            return 0
        elif current_node.key == key:
            return self._size(current_node.left)
        elif current_node.key > k:
            return self._rank(current_node.left, key)
        else:
            return 1 + self._size(current_node.left) + self._rank(current_node.right)

    def get_ordered_keys(self):
        ordered_keys = []
        return self._get_ordered_keys(self.root, ordered_keys)

    def _get_ordered_keys(self, current_node, ordered_keys):
        if current_node is None:
            return ordered_keys
        ordered_keys = self._get_ordered_keys(current_node.left, ordered_keys)
        ordered_keys.append(current_node.key)
        ordered_keys = self._get_ordered_keys(current_node.right, ordered_keys)
        return ordered_keys
