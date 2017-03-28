"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
from collections import defaultdict


class Solution(object):

    # This class represents a directed graph
    # using adjacency list representation
    class Graph(object):

        def __init__(self, vertices):
            # No. of vertices
            self.V = vertices

            # default dictionary to store graph
            self.graph = defaultdict(set)

            self.allpaths = []

            # function to add an edge to graph

        def addEdge(self, u, v):
            self.graph[u].add(v)

        def dfs_paths(self, start, goal):
            stack = [(start, [start])]
            while stack:
                (vertex, path) = stack.pop()
                for next in self.graph[vertex] - set(path):
                    if next == goal:
                        self.allpaths.append(path + [next])
                    else:
                        stack.append((next, path + [next]))



    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        trie = defaultdict(dict)
        for word in wordDict:
            word += '$'
            cur_dict = trie
            for letter in word:
                if letter in cur_dict:
                    cur_dict = cur_dict[letter]
                else:
                    cur_dict[letter] = {}
                    cur_dict = cur_dict[letter]
        intervals = []
        for i in range(len(s)):
            cur_dict = trie
            offset = 0
            while '$' in cur_dict or s[offset + i] in cur_dict:
                if '$' in cur_dict.keys():
                    intervals.append((i, i + offset,))
                if s[offset + i] in cur_dict:
                    cur_dict = cur_dict[s[offset + i]]
                    offset += 1
                else:
                    break
                if i + offset > len(s) - 1:
                    if '$' in cur_dict.keys():
                        intervals.append((i, i + offset,))
                    break

        graph = self.Graph(len(s)+1)
        for interval in intervals:
            graph.addEdge(*interval)
        graph.dfs_paths(0, len(s))
        paths = graph.allpaths
        solution = []
        string = []
        for path in paths:
            for i in range(len(path) - 1):
                string.append(s[path[i]:path[i + 1]])
            solution.append(' '.join(string))
            string = []
        return solution

#
#
print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, dic))
#
# # # #
print(Solution().wordBreak("aaaaaaa",
                           ["aaaa", "aa", "a"]))

# # #
print(Solution().wordBreak("abcd",
                           ["a", "abc", "b", "cd"]))
# #
print(Solution().wordBreak("aaaaaaa",
                           ["aaaa", "aa"]))
# # #
#
print(Solution().wordBreak("aaaaaaa",
                           ["aaaa", "aaa"]))
print(Solution().wordBreak("a", []))
