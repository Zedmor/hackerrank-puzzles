#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (34.34%)
# Total Accepted:    635.5K
# Total Submissions: 1.9M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# Follow up:
# Could you do get and put in O(1) time complexity?
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 3000
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to get and put.
#
#
#

class ListNode:
    def __init__(self, v, left=None, right=None):
        self.val = v
        self.left = left
        self.right = right


import heapq


class LRUCache:

    def __init__(self, capacity: int):
        self.counter = 0
        self.capacity = capacity
        self.tail = None
        self.head = None
        self.cache = {}

    def refresh(self, key):
        ll, __ = self.cache[key]
        if self.tail == ll:
            return

        if ll.left:
            ll.left.right = ll.right
        if ll.right:
            ll.right.left = ll.left
        self.tail.right = ll
        ll.left = self.tail
        self.tail = ll
        if self.head == ll:
            self.head = self.head.right



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        ll, val = self.cache[key]
        self.refresh(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.refresh(key)
            self.cache[key] = (self.cache[key][0], value)
            return
        if self.counter == self.capacity:
            del self.cache[self.head.val]

            self.tail = ListNode(key, left=self.tail)

            if self.head.right:
                self.head = self.head.right
                self.head.left = None
            else:
                self.head = self.tail

            self.tail.left.right = self.tail
            self.cache[key] = (self.tail, value)
        else:
            if not self.head:
                ll = ListNode(key)
                self.head = ll
                self.tail = ll

            else:
                ll = ListNode(key, left=self.tail)
                self.tail.right = ll
                self.tail = ll

            self.cache[key] = (self.tail, value)

            self.counter += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test_lru_cache1():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    assert 1 == lRUCache.get(1)    # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert -1 == lRUCache.get(2)    # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert -1 == lRUCache.get(1)    # return -1 (not found)
    assert 3 == lRUCache.get(3)    # return 3
    assert 4 == lRUCache.get(4)    # return 4


def test_lru_cache2():
    lRUCache = LRUCache(1)
    lRUCache.put(2, 1)
    assert 1 == lRUCache.get(2)
    lRUCache.put(3, 2)
    lRUCache.get(2)
    lRUCache.get(3)


def test_lru_cache3():
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(2, 2)
    assert 2 == lRUCache.get(2)
    lRUCache.put(1, 1)
    lRUCache.put(4, 1)
    assert -1 == lRUCache.get(2)


def test_lru_cache4():
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(3, 2)
    lRUCache.get(3)
    lRUCache.get(2)
    lRUCache.put(4, 3)
    lRUCache.get(2)
    lRUCache.get(3)
    lRUCache.get(4)

# test_lru_cache1()
# test_lru_cache2()
# test_lru_cache3()
# test_lru_cache4()

