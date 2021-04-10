from collections import defaultdict

Vertex = int


class Digraph:
    def __init__(self, num_vertices: int):
        self.num_vertices: int = num_vertices
        self.adjacency_sets: defaultdict[Vertex, set(Vertex)] = defaultdict(set)

    def add_edge(self, v: Vertex, w: Vertex):
        # Allows for multiple parallel edges between two vertices
        self.adjacency_sets[v].add(w)

    def adjacent(self, v: Vertex):
        return self.adjacency_sets[v]

    def reversed(self):
        reversed = Digraph(self.num_vertices)
        for source, destinations in self.adjacency_sets.items():
            for destination in destinations:
                reversed.add_edge(destination, source)
        return reversed
