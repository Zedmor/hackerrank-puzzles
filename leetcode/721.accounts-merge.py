#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (46.88%)
# Total Accepted:    75.2K
# Total Submissions: 158K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
#
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
#
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
#
# Example 1:
#
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
#
#
#
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
#
#
from collections import defaultdict
from typing import List


class Solution:
    """
    >>> Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John","johnnybravo@mail.com"], ["John", "johnsmith@mail.com","john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
    [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['John', 'johnnybravo@mail.com'],['Mary', 'mary@mail.com']]


    >>> Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John","johnnybravo@mail.com"], ["John", "johnsmith@mail.com","john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
    [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['John', 'johnnybravo@mail.com'],['Mary', 'mary@mail.com']]
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(temp, graph, node, visited):
            temp.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    temp = dfs(temp, graph, neighbour, visited)
            return temp

        container = defaultdict(list)
        for item in accounts:
            name, *emails = item
            container[name].append(emails)

        for user, emails_lists in container.items():
            g = defaultdict(list)
            for sublist in emails_lists:
                for i in range(len(sublist)):
                    g[sublist[i]].extend(sublist[:i] + sublist[i+1:])
            visited = set()
            cc = []
            for node in g.keys():
                if node not in visited:
                    visited.add(node)
                    temp = []
                    cc.append(dfs(temp, g, node, visited))
            container[user] = cc


        result = []
        for user, emails_sets in container.items():
            for emails in emails_sets:
                result.append([user] + list(sorted(emails)))
        return result






