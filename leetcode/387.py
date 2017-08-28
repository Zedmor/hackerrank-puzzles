class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = set()
        for index, char in enumerate(s):
            try:
                s[index+1:].index(char)
            except ValueError:
                if char not in used:
                    return index
            used.add(char)
        return -1

print(Solution().firstUniqChar('cc'))