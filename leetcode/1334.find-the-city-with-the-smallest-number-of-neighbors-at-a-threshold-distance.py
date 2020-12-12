#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
#
# algorithms
# Medium (42.82%)
# Total Accepted:    9.2K
# Total Submissions: 21.3K
# Testcase Example:  '4\n[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]\n4'
#
# There are n cities numbered from 0 to n-1. Given the array edges where
# edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge
# between cities fromi and toi, and given the integer distanceThreshold.
#
# Return the city with the smallest number of cities that are reachable through
# some path and whose distance is at most distanceThreshold, If there are
# multiple such cities, return the city with the greatest number.
#
# Notice that the distance of a path connecting cities i and j is equal to the
# sum of the edges' weights along that path.
#
#
# Example 1:
#
#
#
#
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold =
# 4
# Output: 3
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2] 
# City 1 -> [City 0, City 2, City 3] 
# City 2 -> [City 0, City 1, City 3] 
# City 3 -> [City 1, City 2] 
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we
# have to return city 3 since it has the greatest number.
#
#
# Example 2:
#
#
#
#
# Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
# distanceThreshold = 2
# Output: 0
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 2 for each city are:
# City 0 -> [City 1] 
# City 1 -> [City 0, City 4] 
# City 2 -> [City 3, City 4] 
# City 3 -> [City 2, City 4]
# City 4 -> [City 1, City 2, City 3] 
# The city 0 has 1 neighboring city at a distanceThreshold = 2.
#
#
#
# Constraints:
#
#
# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti, distanceThreshold <= 10^4
# All pairs (fromi, toi) are distinct.
#
#
from collections import defaultdict
from typing import List

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

class Solution:
    """
    >>> Solution().findTheCity(6, [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]], 417)
    5

    >>> Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)
    3

    >>> Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)
    0


    """
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = Graph()
        for e in edges:
            fromi, toi, weighti = e
            g.add_node(fromi)
            g.add_node(toi)
            g.add_edge(fromi, toi, weighti)
            g.add_edge(toi, fromi, weighti)

        def dijsktra(graph, initial):
            visited = {initial: 0}
            path = {}

            nodes = set(graph.nodes)

            while nodes:
                min_node = None
                for node in nodes:
                    if node in visited:
                        if min_node is None:
                            min_node = node
                        elif visited[node] < visited[min_node]:
                            min_node = node

                if min_node is None:
                    break

                nodes.remove(min_node)
                current_weight = visited[min_node]

                for edge in graph.edges[min_node]:
                    weight = current_weight + graph.distances[(min_node, edge)]
                    if edge not in visited or weight < visited[edge]:
                        visited[edge] = weight
                        path[edge] = min_node

            return visited, path

        nodes_within_distance = {}
        for i in range(n):
            nodes_within_distance[i] = 0
            visited, path = dijsktra(g, i)
            for target, distance in visited.items():
                if target != i and distance <= distanceThreshold:
                    nodes_within_distance[i] += 1

        nodes_within_distance = sorted(list(nodes_within_distance.items()), key=lambda z: z[1])
        min_distance = nodes_within_distance[0][1]
        nodes = [n[0] for n in nodes_within_distance if n[1] == min_distance]

        return max(nodes)







