from typing import Optional
from collections import namedtuple


Interval = namedtuple("Interval", ["low", "high"])


class Node:
    def __init__(self, interval: Interval):
        self.key: int = interval.low  # key
        self.interval: Interval = interval
        self.max: int = interval.high
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def intersects(self, interval):
        return (
            self.interval.low < interval.low < self.interval.high or
            interval.low < self.interval.low < interval.high
        )


class IntervalSearchTree:
    """
    Allows for rapid search of intersecting one-dimensional intervals.
    Assumption: no intervals (including search intervals not stored in tree) have the same left
    coordinate.

    Time complexity:
        All cases: O(lg N)
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def put(self, low, high):
        interval = Interval(low, high)
        self.root = self._put(self.root, interval)

    def _put(self, current_node: Node, interval: Interval):
        if current_node is None:
            return Node(interval)
        key = interval.low
        high = interval.high
        if current_node.key == key:
            print("Cannot insert two intervals with same left coordinate; rejecting!")
            return current_node
        elif current_node.key > key:
            if current_node.max < high:
                current_node.max = high
            current_node.left = self._put(current_node.left, interval)
        else:
            if current_node.max < high:
                current_node.max = high
            current_node.right = self._put(current_node.right, interval)
        return current_node

    def intersects(self, low, high):
        interval = Interval(low, high)
        intervals = []
        if self.root is None:
            return intervals
        else:
            return self._intersects(self.root, interval, intervals)

    def _intersects(self, current_node, search_interval, result_intervals):
        if current_node.intersects(search_interval):
            result_intervals.append(current_node.interval)
        if current_node.left is not None and current_node.left.max > search_interval.low:
            result_intervals = self._intersects(current_node.left, search_interval, result_intervals)
        if current_node.right is not None and current_node.key < search_interval.high:
            result_intervals = self._intersects(current_node.right, search_interval, result_intervals)
        return result_intervals
