#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
# https://leetcode.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (47.86%)
# Total Accepted:    143.5K
# Total Submissions: 299.5K
# Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
#
# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split its set of nodes into two
# independent subsets A and B, such that every edge in the graph has one node
# in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for
# which the edge between nodes i and j exists.  Each node is an integer between
# 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i]
# does not contain i, and it doesn't contain any element twice.
#
#
# Example 1:
#
#
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and {1,
# 3}.
#
#
#
# Example 2:
#
#
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two
# independent subsets.
#
#
#
#
# Constraints:
#
#
# 1 <= graph.length <= 100
# 0 <= graph[i].length < 100
# 0 <= graph[i][j] <= graph.length - 1
# graph[i][j] != i
# All the values of graph[i] are unique.
# The graph is guaranteed to be undirected. 
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])
    False

    >>> Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]])
    True

    >>> Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
    False
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        u = set()
        v = set()

        u_stack = []
        v_stack = []
        visited = set()
        while len(visited) < len(graph):
            missing_nums = list(set(range(len(graph))) - visited)
            if missing_nums:
                u_stack.append(missing_nums[0])

            while u_stack or v_stack:
                if u_stack:
                    e = u_stack.pop()
                    if e not in visited:
                        u.add(e)
                        visited.add(e)
                        for el in graph[e]:
                            if el in u:
                                return False
                            v.add(el)
                            v_stack.append(el)
                if v_stack:
                    e = v_stack.pop()
                    if e not in visited:
                        visited.add(e)
                        v.add(e)
                        for el in graph[e]:
                            if el in v:
                                return False
                            u.add(el)
                            u_stack.append(el)
        return True
