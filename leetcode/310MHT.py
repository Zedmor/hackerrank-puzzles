"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Show Hint
Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def DFS(entry, graph):
            # print()
            stack = []
            visited = set()
            distances = []
            if entry not in graph.keys():
                return False
            stack.append((entry, 0))
            while stack:
                v = stack.pop()
                if v[0] not in visited:
                    # print(v, stack)
                    # print(v)
                    distances.append(v[1])
                    visited.add(v[0])
                    for edge in graph[v[0]]:
                        stack.append((edge, v[1] + 1))
            return distances

        from collections import defaultdict
        if not edges:
            return [0]
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # print(graph)
        while len(graph.keys())> 2:
            leaves = [vertex for (vertex,neighbors) in graph.items() if len(neighbors)==1]
            for leaf in leaves:
                graph[graph[leaf][0]].remove(leaf)
                del graph[leaf]
        return list(graph.keys())


        # results = []
        # for i in range(n):
        #     results.append((i, max(DFS(i, graph))))
        # if not results:
        #     return [0]
        # results = sorted(results, key=lambda x:x[1])
        # bestresult = results[0][1]
        # return [x[0] for x in results if x[1]==bestresult]

#
# n = 6
# edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

n = 4
edges = []
print(Solution().findMinHeightTrees(n, edges))
