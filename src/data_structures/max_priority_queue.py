class MaxPriorityQueue:

    def __init__(self, size):
        self.size = size
        self.heap = [None] * (size + 1)  # working with 1-indicies makes the math easier
        self.root_idx = 1
        self.insertion_idx = self.root_idx

    def insert(self, item):
        if self.insertion_idx > self.size:
            print("Max priority queue is already full; rejecting insert request")
            return
        self.heap[self.insertion_idx] = item
        self._swim(self.insertion_idx)
        self.insertion_idx += 1

    def delete_max(self):
        if self.is_empty():
            return None
        heap = self.heap
        item = heap[1]
        heap[1] = heap[self.insertion_idx - 1]
        heap[self.insertion_idx - 1] = None
        self._sink(1)
        self.insertion_idx -= 1
        return item

    def is_empty(self):
        return self.heap[self.root_idx] is None

    def _swim(self, idx):
        heap = self.heap
        while idx > self.root_idx and heap[idx // 2] < heap[idx]:
            self._exchange(idx // 2, idx)
            idx = idx // 2

    def _sink(self, idx):
        heap = self.heap
        size = self.size
        while 2 * idx <= size:
            child_idx = 2 * idx
            if heap[child_idx] is None and heap[child_idx + 1] is None:
                break
            elif heap[child_idx] is not None and heap[child_idx + 1] is None:
                if heap[child_idx] > heap[idx]:
                    self._exchange(idx, child_idx)
                break
            elif heap[child_idx] is None and heap[child_idx + 1] is not None:
                if heap[child_idx + 1] > heap[idx]:
                    self._exchange(idx, child_idx + 1)
                break
            else:
                if heap[child_idx] < heap[child_idx + 1]:
                    child_idx += 1
                if heap[idx] >= heap[child_idx]:
                    break  # if the parent node is bigger than both children nodes, do nothing
                else:
                    self._exchange(idx, child_idx)
                    idx = child_idx

    def _exchange(self, i, j):
        heap = self.heap
        heap[i], heap[j] = heap[j], heap[i]
