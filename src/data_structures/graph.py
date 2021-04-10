from collections import defaultdict

Vertex = int

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices: int = num_vertices
        self.adjacency_lists: defaultdict[Vertex, list(Vertex)] = defaultdict(list)

    def add_edge(self, v: Vertex, w: Vertex):
        # Allows for multiple parallel edges between two vertices
        self.adjacency_lists[v].append(w)
        self.adjacency_lists[w].append(v)

    def adjacent(self, v: Vertex):
        return self.adjacency_lists[v]
