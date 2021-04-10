from collections import defaultdict

Vertex = int

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices: int = num_vertices
        self.adjacency_sets: defaultdict[Vertex, set(Vertex)] = defaultdict(set)

    def add_edge(self, v: Vertex, w: Vertex):
        # Allows for multiple parallel edges between two vertices
        self.adjacency_sets[v].add(w)
        self.adjacency_sets[w].add(v)

    def adjacent(self, v: Vertex):
        return self.adjacency_sets[v]
