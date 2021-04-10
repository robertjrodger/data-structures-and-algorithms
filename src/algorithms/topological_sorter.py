from data_structures import Digraph
from data_structures import Stack
from data_structures import Vertex


class TopologicalSorter:
    """
    Only works if the digraph is a DAG (i.e. no loops)!
    """
    def __init__(self, digraph: Digraph):
        self.digraph: Digraph = digraph
        self.marked: set(Vertex) = set()
        self.reverse_postorder: Stack = reverse_postorder
        self.initialized: bool = False

    def initialize(self):
        for vertex in range(digraph.num_vertices):
            if vertex not in self.marked:
                self._dfs(vertex)
                self.reverse_postorder.push(vertex)
        self.initialized = True

    def _dfs(self, current: Vertex):
        self.marked.add(current)
        neighbors = self.digraph.adjacent(current)
        for neighbor in neighbors:
            if neighbor not in self.marked:
                self._dfs(neighbor)
        self.reverse_postorder.push(current)

    def sort(self):
        return self.reverse_postorder
