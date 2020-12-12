#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (57.94%)
# Total Accepted:    347.2K
# Total Submissions: 598.5K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
# from leetcode.treetools import list2tree

# '[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
#
#
#
#
#
# Example:
#
#
#
#
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
#
#
#
#
# Note:
#
#
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
#
#
#
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if root:
            self.stack.append(root)
        self.visited = set()
        self.generator = self.generate()

    def generate(self):
        to_print = set()
        while self.stack:
            node = self.stack[0]
            if not node:
                self.stack.pop(0)
                continue
            if node and node in to_print:
                self.stack.pop(0)
                to_print.remove(node)
                yield node.val
                continue
            if node:
                self.stack.insert(0, node.left)
                self.stack.insert(2, node.right)
                self.stack = [i for i in self.stack if i]
                to_print.add(node)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return next(self.generator)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# root = list2tree("[7,3,15,null,null,9,20]")
# iterator = BSTIterator(root)
# assert 3 == iterator.next();    # return 3
# assert 7 == iterator.next();    # return 7
# assert iterator.hasNext(); # return true
# assert 9 == iterator.next();    # return 9
# assert iterator.hasNext(); # return true
# assert 15 == iterator.next();    # return 15
# assert iterator.hasNext(); # return true
# assert 20 == iterator.next();    # return 20
# assert not iterator.hasNext(); # return false
