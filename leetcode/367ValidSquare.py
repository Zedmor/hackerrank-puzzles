'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        leftbound = 0
        rightbound = num
        middle = leftbound + (rightbound - leftbound) // 2
        while middle*middle != num:

            middle = leftbound + (rightbound-leftbound)//2
            if middle*middle < num:
                leftbound += (middle-leftbound)//2
            else:
                rightbound -= (rightbound-middle)//2
            if leftbound + (rightbound - leftbound) // 2 == middle:
                if rightbound*rightbound==num:
                    return True
                else:
                    return False
        return True



print(Solution().isPerfectSquare(1))