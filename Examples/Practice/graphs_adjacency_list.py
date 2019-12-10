'''
Simple Un-ordered un-weighted graph implementation using adjacency list
'''


class Vertices:
    def __init__(self, n):
        self.value = n
        self.neighbours = []

    def add_neighbour(self, b):
        if b.value not in self.neighbours:
            self.neighbours.append(b)


class Graph:
    vertices = []

    def __init__(self):
        pass

    def add_vertices(self, a):
        if a.value not in self.vertices:
            self.vertices.append(a)

    def add_edge(self, a, b):
        a.add_neighbour(b)
        b.add_neighbour(a)

    def print_graph(self):
        for k in self.vertices:
            print(str(k.value) + " : " + " ".join([str(x.value) for x in k.neighbours]))


a = Vertices(10)
b = Vertices(20)
c = Vertices(30)
d = Vertices(40)

g = Graph()
g.add_vertices(a)
g.add_vertices(b)
g.add_vertices(c)
g.add_vertices(d)
g.add_edge(a, b)
g.add_edge(b, c)
g.add_edge(a, c)
g.add_edge(d, c)

g.print_graph()
