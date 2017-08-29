"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        tail = 0
        result = 0
        hash_set = set()
        while head < len(s):
            while len(hash_set) == tail - head and tail < len(s):
                hash_set.add(s[tail])
                tail += 1
            newbeginning = s[head:tail].index(s[tail-1]) + head
            result = len(hash_set) if len(hash_set) > result else result
            head = newbeginning + 1
            hash_set = set(s[head:tail])
        return result


s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))
