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

import itertools


class Solution(object):
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

        # print(intervals)

        nextlist = []
        for i, item in enumerate(intervals):
            for j in range(i, len(intervals)):
                if intervals[j][0] == item[1]:
                    nextlist.append(j)
                    break
                if intervals[j][0] > item[1]:
                    nextlist.append(None)
                    break

        print(list(itertools.zip_longest(nextlist, intervals)))



        treepaths = defaultdict(dict)

        class TreeNode(object):
            def __init__(self, val):
                self.val = val
                self.children = []
            def __str__(self):
                return str(self.val)

        mainnode = TreeNode(0)

        def treebuilder(node, start=0):
            collector = []
            for ind in range(start, len(intervals)):
                if intervals[ind][0]>node.val:
                    break
                if intervals[ind][0] == node.val:
                    a = TreeNode(intervals[ind][1])
                    node.children.append(a)
                    treebuilder(a, ind)
            if not node.children:
                return TreeNode(node.val)
            # node.children = collector

        treebuilder(mainnode)

        # print(mainnode)

        def childrenhasher(f):
            hashtable = {}
            def _f(*args):
                try:
                    return hashtable[args]
                except KeyError:
                    hashtable[args] = result = f(*args)
                    return result
            return _f


        # #@childrenhasher
        # def get_children(root):
        #     return [link for link in intervals if link[0] == root]

        paths = []
        def findchain(root, cur_path=None):
            if not cur_path:
                cur_path = []
            children = root.children
            if not children and root.val==len(s):
                paths.append(cur_path + [root.val])
            else:
                for child in children:
                    findchain(child, cur_path + [root.val])


        findchain(mainnode)


        if paths == [0]:
            paths = []
        # print(paths)
        solution = []

        string = []
        for path in paths:
            for i in range(len(path) - 1):
                string.append(s[path[i]:path[i + 1]])
            solution.append(' '.join(string))
            string = []
        return solution


#

# print(Solution().wordBreak(
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, dic))
# #
# # # # #
# print(Solution().wordBreak("aaaaaaa",
#                            ["aaaa", "aa", "a"]))
#
# # # #
# print(Solution().wordBreak("abcd",
#                            ["a", "abc", "b", "cd"]))
# # #
# print(Solution().wordBreak("aaaaaaa",
#                            ["aaaa", "aa"]))
# # #
# #
# print(Solution().wordBreak("aaaaaaa",
#                            ["aaaa", "aaa"]))
# print(Solution().wordBreak("a", []))
