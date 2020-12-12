#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (43.92%)
# Total Accepted:    183.3K
# Total Submissions: 400.5K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n[[],[1],[2],[2],[],[1],[2],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
#
#
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each
# element must have the same probability of being returned.
#
#
#
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();
#
#
#
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.items_map = {}
        self.free_index = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.items_map:
            if not self.free_index:
                self.items.append(val)
                self.items_map[val] = len(self.items) - 1
                return True
            else:
                reused_index = self.free_index.pop()
                self.items[reused_index] = val
                self.items_map[val] = reused_index
                return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.items_map:
            index = self.items_map.pop(val)
            self.items[index] = None
            self.free_index.add(index)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        result = None
        while result is None:
            result = random.choice(self.items)
            if result is None and self.free_index is None:
                break

        return result


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def test_randomized_set(case):
    for command, arg in zip(*case):
        if command == 'RandomizedSet':
            o = RandomizedSet()
            continue
        method = o.__getattribute__(command)
        print(method(*arg))


# test_randomized_set()
case1 = (["RandomizedSet",
          "insert",
          "remove",
          "insert",
          "getRandom",
          "remove",
          "insert",
          "getRandom"], [[], [1], [2], [2], [],
                         [1],
                         [2], []])
# test_randomized_set(case1)

# print()

case2 = ["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"], [[], [0], [0], [0], [], [0],
                                                                                           [0]]

# test_randomized_set(case2)

case3 = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"], [[], [1], [2],
                                                                                                        [2], [], [1],
                                                                                                        [2], []]

# test_randomized_set(case3)

case4 = ["RandomizedSet", "insert", "insert", "remove", "insert", "insert", "insert", "remove", "remove", "insert",
         "remove",
         "insert", "insert", "insert", "insert", "insert", "getRandom", "insert", "remove", "insert", "insert"], [[],
                                                                                                                  [3],
                                                                                                                  [-2],
                                                                                                                  [2],
                                                                                                                  [1],
                                                                                                                  [-3],
                                                                                                                  [-2],
                                                                                                                  [-2],
                                                                                                                  [3],
                                                                                                                  [-1],
                                                                                                                  [-3],
                                                                                                                  [1],
                                                                                                                  [-2],
                                                                                                                  [-2],
                                                                                                                  [-2],
                                                                                                                  [1],
                                                                                                                  [],
                                                                                                                  [-2],
                                                                                                                  [0],
                                                                                                                  [-3],
                                                                                                                  [1]]

# test_randomized_set(case4)
