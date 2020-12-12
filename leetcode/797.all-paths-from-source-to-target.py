#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (74.04%)
# Total Accepted:    51.1K
# Total Submissions: 68.9K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
#
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
#
#
# Example:
# Input: [[1,2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
#
# Note:
#
#
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
#
#
from copy import copy
from typing import List


class Solution:
    """
    >>> Solution().allPathsSourceTarget([[1,2], [3], [3], []])
    [[0, 1, 3], [0, 2, 3]]

    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []

        def search(node, visited, path=None):
            if not path:
                path = []
            visited.add(node)
            path.append(node)
            if node == len(graph) - 1:
                all_paths.append(path)
            for v in graph[node]:
                search(v, copy(visited), copy(path))

        search(0, set())

        return all_paths

