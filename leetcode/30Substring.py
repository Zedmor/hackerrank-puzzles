"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
from collections import defaultdict
from copy import copy


class TrieNode(object):
    def __init__(self, v):
        self.value = v
        self.count = 1
        self.children = {}


def makeTrie(list_words):
    root = TrieNode('^')
    start_root = root
    for word in list_words:
        root = start_root
        for letter in word + '$':
            if letter in root.children:
                found_node = root.children[letter]
                found_node.count += 1
                root = found_node
            else:
                child = TrieNode(letter)
                root.children[letter] = child
                root = child

    return start_root


class Solution:
    from collections import defaultdict
    from copy import copy
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # root = makeTrie(words)
        if not words:
            return 0
        res = []
        w_len = len(words[0])
        hashmap = defaultdict(int)
        for word in words:
            hashmap[word] += 1
        tot_len = len(words) * len(words[0])
        for i in range(len(s) - tot_len + 1):
            new_hashmap = copy(hashmap)
            j = i
            counter = 0
            while new_hashmap[s[j:j+w_len]] > 0:
                if new_hashmap[s[j:j+w_len]] > 0:
                    counter +=1
                new_hashmap[s[j:j+w_len]] -= 1
                j += w_len
            if counter == len(words):
               res.append(i)
        return res



words = ['foo', 'bar']
s = 'barfoothefoobarman'

print(Solution().findSubstring(s, words))
