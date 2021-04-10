from data_structures import Graph
from data_structures import Queue
from data_structures import Vertex


class BreadthFirstPaths:
    def __init__(self, graph: Graph, source: Vertex):
        self.graph: Graph = graph
        self.source: Vertex = source
        self.marked: set(Vertex) = set()
        self.edge_to: dict[Vertex, Vertex] = dict()
        self.initialized: bool = False

    def initialize(self):
        self._bfs()
        self.initialized = True

    def _bfs(self):
        search_queue = Queue()
        search_queue.enqueue(self.source)
        self.marked.add(self.source)
        while not search_queue.is_empty():
            current = search_queue.dequeue()
            neighbors = self.graph.adjacent(current)
            for neighbor in neighbors:
                if neighbor not in self.marked:
                    search_queue.enqueue(neighbor)
                    self.marked.add(neighbor)
                    self.edge_to[neighbor] = current

    def has_path_to(self, target: Vertex):
        if not self.initialized:
            print("Must be initialized first!")
            return
        return target in self.marked

    def path_to(self, target: Vertex):
        if not self.initialized:
            print("Must be initialized first!")
            return
        if not self.has_path_to(target):
            return None
        path = [target]
        current_vertex = target
        while (current_vertex := self.edge_to[current_vertex]) != self.source:
            path.append(current_vertex)
        path.append(self.source)
        path.reverse()
        return path

