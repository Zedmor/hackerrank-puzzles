#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (53.36%)
# Total Accepted:    46.4K
# Total Submissions: 84.7K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
#
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
#
#
# Note:
#
#
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
#
#
#
#
#
from collections import defaultdict


class Trie:
    def __init__(self, dictionary):
        self._container = defaultdict(list)
        for word in dictionary:
            self.add(word)

    def add(self, word):
        cursor = self._container
        word += '$'
        for letter in word:
            for subdict in cursor[letter]:
                if letter in subdict:
                    cursor = subdict
                    break
            else:
                new_subdict = defaultdict(list)
                cursor[letter].append(new_subdict)
                cursor = new_subdict


    def get(self, word):
        cursor = [self._container]
        for i, letter in enumerate(word + '$'):
            for subdict in sorted(cursor, key=lambda d: next(iter(d))):
                if '$' in subdict:
                    return word[:i]
                if letter in subdict:
                    cursor = subdict[letter]
                    break

            else:
                return word[:i] if i > 0 and '$' in cursor else word
        return word


class Solution:
    """
    # >>> Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
    # 'the cat was rat by the bat'

    >>> Solution().replaceWords(["c","q","ntoso","vz","zy","f","rrq","o","wlzza","k","xm","mvdpx","jxrz","ocnck","gcbnd","fofl","raxbp","g","bbgpb","acac","py","cq","hzey","ku","ubzro","gyuaf","kw","lpi","e","jc","jlr","ggh","qlehz","xj","d","z","cn","h","ki","sddj","uzrbw","izi","aqbge","qxuwp","w","rtvt","y","x","tajl","oo","atxo","zfuh","ej","scmw","zba","yt","n","cm"], "ntxahkgxrsgvatqnz vbwkwndugjtyrr")
    'the cat was rat by the bat'

    """
    def replaceWords(self, d:list, sentence: str) -> str:
        trie = Trie(d)
        result = []
        for word in sentence.split(' '):
            result.append(trie.get(word))
        return ' '.join(result)


