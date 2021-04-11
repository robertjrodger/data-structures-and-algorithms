from algorithms import TopologicalSorter
from data_structures import Digraph
from data_structures import Vertex

Component = int


class StronglyConnectedComponents:
    def __init__(self, digraph: Digraph):
        self.digraph: Digraph = digraph
        self.marked: set(Vertex) = set()
        self.component: dict[Vertex, Component] = dict()
        self.num_components: int = 0
        self.initialized: bool = False

    def initialize(self):
        topological_sorter = TopologicalSorter(self.digraph.reversed())
        topological_sorter.initialize()
        reversed_reverse_postorder = topological_sorter.sort()
        for vertex in reversed_reverse_postorder:
            if vertex not in self.marked:
                self._dfs(vertex)
                self.num_components += 1
        self.initialized = True

    def _dfs(self, current: Vertex):
        self.marked.add(current)
        self.component[current] = self.num_components
        neighbors = self.digraph.adjacent(current)
        for neighbor in neighbors:
            if neighbor not in self.marked:
                self._dfs(neighbor)

    def count(self):
        if not self.initialized:
            print("Must be initialized first!")
            return
        else:
            self.num_components

    def connected(self, v: Vertex, w: Vertex):
        if not self.initialized:
            print("Must be initialized first!")
            return
        else:
            self.component[v] == self.component[w]

    def component(self, v: Vertex):
        return self.component(v)
