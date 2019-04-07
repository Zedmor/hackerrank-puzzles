import collections
import re
from collections import defaultdict
from copy import copy
from functools import reduce


def step_time(step):

    # return ord(step) - ord('A') + 1
    return ord(step) - ord('A') + 61

class Worker:
    def __init__(self):
        self.task = None
        self.time = 0

    def run(self, task):
        self.task = task
        self.task_time = step_time(task)

    def step(self):
        self.time += 1
        if self.time == self.task_time:
            result = self.task
            self.task = None
            self.time = 0
            return result


    def idle(self):
        return self.task is None


class Pool:
    def __init__(self, num_workers=5):
        self.num_workers = num_workers
        self.workers = [Worker() for c in range(num_workers)]
        self.seconds_last = 0

    def run(self, task):
        for worker in self.workers:
            if worker.idle():
                worker.run(task)
                return True
        else:
            return False

    def step(self):
        self.seconds_last += 1
        finished_tasks = []
        for worker in self.workers:
            if not worker.idle():
                finished_tasks.append(worker.step())
        return filter(None, finished_tasks)

    def queue(self):
        return [w.task for w in self.workers if w.task]

    def available(self):
        return self.num_workers - len(self.queue())



class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)
        self.all_nodes = set(self._graph.keys()).union(
            set().union(*self._graph.values()))

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def sources(self, node):
        return {k for k, v in self._graph.items() if node in v}

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def find_order(self, num_workers):
        pool = Pool(num_workers)
        visited = list()
        while self.all_nodes != set(visited):
            ready_nodes = self.get_ready_nodes(visited, pool).difference(visited)
            if ready_nodes:
                queue = sorted(list(ready_nodes))
                while pool.available() and queue:
                    pool.run(queue.pop(0))
            visited += pool.step()
            queue = []

        return visited, pool.seconds_last

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def get_ready_nodes(self, visited_nodes, pool):
        return set([
            n for n in self.all_nodes
            if self.sources(n).issubset(set(visited_nodes))
        ]) - set(pool.queue())


def parse_vertex(s):
    s, d = re.findall('Step (\w) must be finished before step (\w) can begin.',
                      s)[0]
    return s, d


vertexes = list(map(parse_vertex, open('input-7.txt').readlines()))

g = Graph(vertexes, directed=True)

res = g.find_order(5)

print(''.join(res[0]), res[1])

# sources = [v for v in g.keys() if v not in g.values()]

# print(g)
