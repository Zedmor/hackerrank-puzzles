"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""


class AllOne(object):
    def __init__(self):
        from collections import defaultdict
        """
        Initialize your data structure here.
        """
        self.intdict = {}
        self.valdictionary = defaultdict(set)
        self.maxvalue = -float('inf')
        self.minvalue = float('inf')

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.intdict:
            if self.intdict[key] == self.minvalue and len(self.valdictionary[
                                                              self.intdict[
                                                                  key]]) == 1:
                self.minvalue += 1
            self.valdictionary[self.intdict[key]].remove(key)
            if self.valdictionary[self.intdict[key]] == set():
                del self.valdictionary[self.intdict[key]]
            if self.intdict[key] == self.maxvalue:
                self.maxvalue += 1
            self.intdict[key] += 1
            self.valdictionary[self.intdict[key]].add(key)
        else:
            self.intdict[key] = 1
            self.valdictionary[self.intdict[key]].add(key)
            if self.minvalue > 1:
                self.minvalue = 1

        if self.intdict[key] > self.maxvalue:
            self.maxvalue = self.intdict[key]

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.intdict:
            if self.intdict[key]>1:
                if self.intdict[key] == self.maxvalue and len(self.valdictionary[
                                                                  self.intdict[
                                                                      key]]) == 1:
                    self.maxvalue -= 1

                if self.intdict[key] == self.minvalue and len(self.valdictionary[
                                                                  self.intdict[
                                                                      key]]) == 1:
                    self.minvalue -= 1

                self.valdictionary[self.intdict[key]].remove(key)
                if self.valdictionary[self.intdict[key]] == set():
                    del self.valdictionary[self.intdict[key]]
                # if 1 not in self.valdictionary:
                #     self.minvalue = min(self.valdictionary.keys())
                # if self.intdict[key] < self.minvalue:
                #     self.minvalue = self.intdict[key]
                self.intdict[key] -= 1
                self.valdictionary[self.intdict[key]].add(key)
                if 1 in self.valdictionary:
                    self.minvalue = 1

            else:
                self.valdictionary[1].remove(key)
                if self.valdictionary[1] == set():
                    del self.valdictionary[1]
                del self.intdict[key]
                self.minvalue=min(self.valdictionary.keys())

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        try:
            return list(self.valdictionary[self.maxvalue])[0]
        except IndexError:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        try:
            return list(self.valdictionary[self.minvalue])[0]
        except IndexError:
            return ""


            # Your AllOne object will be instantiated and called as such:



obj = AllOne()
obj.inc('a')
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('a')
obj.dec('b')

print(obj.getMaxKey())

print(obj.getMinKey())
