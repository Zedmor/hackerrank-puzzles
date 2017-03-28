"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefixstorage = set()

        if strs:
            for i in range(len(strs[0])+1):
                prefixstorage.add(strs[0][:i])

            for string in strs[1:]:
                validprfx = set()
                for i in range(len(string)+1):
                    if string[:i] in prefixstorage:
                        validprfx.add(string[:i])
                prefixstorage = prefixstorage & validprfx
            if prefixstorage:
                return max(prefixstorage, key=len)
        return ""


print(Solution().longestCommonPrefix(['a']))
