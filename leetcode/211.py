"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current_dict = self.container
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['$'] = '$'



    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        flag = True
        word += '$'
        def searchhelper(trie, word):
            if not word:
                return False
            if type(trie) == str:
                return False
            if word in '$':
                if '$' in trie:
                    return True
                else:
                    return False
            else:
                for key, value in trie.items():
                    if word[0] == key or word[0] in '.':
                        if searchhelper(value, word[1:]):
                            return True
            return False

        return searchhelper(self.container, word)

obj = WordDictionary()
# obj.addWord("at")
# obj.addWord("and")
# obj.addWord("an")
# obj.addWord("add")
# obj.addWord("bat")
# obj.addWord("a")
# obj.addWord("ab")
obj.addWord("ran")
obj.addWord("rune")
obj.addWord("runner")

obj.addWord('runs')
obj.addWord('add')
obj.addWord('adds')

obj.addWord('adder')
obj.addWord('addee')


# print(obj.search("a.d."))
# print(obj.search("b."))
# print(obj.search("a.d"))
# print(obj.search("."))

print(obj.search("."))



#[true,true,true,false,true,false,true,true]
