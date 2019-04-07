import re
from functools import reduce


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __repr__(self):
        return str(self.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys() if self.adjacent.keys() else []

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


def hamilton(G, vis=[]):
    if not vis:
        for n in G:
            for p in hamilton(G, [n]):
                yield p
    else:
        dests = set(vis[-1].get_connections()) - set(vis)
        if not dests and len(vis) == G.num_vertices:
            yield vis
        for n in dests:
            for p in hamilton(G, vis + [n]):
                yield p

def calculate_path_length(path):
    sum_of_len = 0
    for i in range(len(path) - 1):
        sum_of_len += path[i].get_weight(path[i+1])
    return sum_of_len


def main():
    """
    >>> main()
    """
    graph = Graph()
    with open('input-9.txt') as file:
        for line in file.readlines():
            _from, _to, dist = re.findall(r'(.+) to (.+) = (\d+)', line)[0]
            # print(_from, _to, dist)
            graph.add_edge(_from, _to, int(dist))
    print(max([(calculate_path_length(path), path) for path in hamilton(graph)], key=lambda a: a[0]))


if __name__ == "__main__":
    main()
