#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (63.13%)
# Total Accepted:    156.6K
# Total Submissions: 235.7K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
#
# Example
#
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#
#
#
from copy import copy
from typing import List


class Solution:
    """
    >>> Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    """
    def put_item(self, positions, position, bag):
        if position == len(positions):
            return positions
        for variant in bag:
            if variant[1] > position:
                continue
            if self.check_place(positions, position, variant):
                new_positions = copy(positions)
                new_positions[position] = variant
                new_bag = copy(bag)
                new_bag.remove(variant)
                r = self.put_item(new_positions, position + 1, new_bag)
                if r:
                    return r


    def check_place(self, positions, position, variant):
        counter = 0
        for el in positions[:position]:
            if el[0] >= variant[0]:
                counter += 1
                if counter > variant[1]:
                    return False
        return counter == variant[1]

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # backtracking
        setbag = set([tuple(e) for e in people])
        positions = [-1] * len(people)
        result = self.put_item(positions, 0, setbag)
        return [list(e) for e in result]
