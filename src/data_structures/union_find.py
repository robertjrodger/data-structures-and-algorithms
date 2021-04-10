class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size_of_tree = [1] * n

    def union(self, p: int, q: int):
        root_p = self._find_root(p)
        root_q = self._find_root(q)
        if root_p != root_q:
            size_of_p_tree = self.size_of_tree[root_p]
            size_of_q_tree = self.size_of_tree[root_q]
            if size_of_p_tree > size_of_q_tree:
                self.parents[root_q] = root_p
                self.size_of_tree[root_p] += size_of_q_tree
            else:
                self.parents[root_p] = root_q
                self.size_of_tree[root_q] += size_of_p_tree

    def connected(self, p: int, q: int):
        return self._find_root(p) == self._find_root(q)

    def _find_root(self, p: int):
        current_node = p
        while (parent_node := self.parents[current_node]) != current_node:
            current_node = parent_node
        return current_node
