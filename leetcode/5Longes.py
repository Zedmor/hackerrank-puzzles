# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        head = 0
        tail = 0
        from collections import defaultdict
        indexes = defaultdict(list)
        for i, char in enumerate(s):
            indexes[char].append(i)
        # print(indexes)
        # allindexes = []
        dict_allindexes = defaultdict(set)
        for biglist in indexes.values():
            # print(biglist)
            for i in range(len(biglist)):
                for j in range(i, len(biglist)):
                    dict_allindexes[biglist[j] - biglist[i]].add((biglist[i], biglist[j]))
        hypothesis = max(dict_allindexes.keys())
        while dict_allindexes:
            tempkeys = []
            headchain = dict_allindexes[hypothesis]
            orig_hypo = hypothesis
            for el in headchain:
                orig_headchain = el
                if hypothesis <= 2:
                    return s[orig_headchain[0]:orig_headchain[1] + 1]
                tempkeys.append(headchain)
                while hypothesis - 2 in dict_allindexes:
                    test_list = dict_allindexes[hypothesis - 2]
                    el = (el[0] + 1, el[1] - 1)
                    try:
                        # el_index = test_list.index(el)
                        hypothesis -= 2
                        test_list.remove(el)
                        dict_allindexes[hypothesis] = test_list
                        if hypothesis <= 2:
                            return s[orig_headchain[0]:orig_headchain[1] + 1]
                    except KeyError:
                        hypothesis = orig_hypo
                        break
            del dict_allindexes[orig_hypo]
            hypothesis = max(dict_allindexes.keys())


# print(Solution().longestPalindrome("ababababa"))
#
# print(Solution().longestPalindrome('abazazazazza'))
# print(Solution().longestPalindrome('cbbd'))
# print(Solution().longestPalindrome('aaaabaaa'))

u = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#
print(Solution().longestPalindrome(u))
