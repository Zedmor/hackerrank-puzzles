"""
Given an integer, write a function to determine if it is a power of two.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return True if n>1 and not(n&(n-1)) else False


        # def powergenerator(n):
        #     number = int(math.sqrt(n))-1
        #     while number < n:
        #         yield 2 ** number
        #         number += 1
        #
        # print(list(powergenerator(n)))
        #
        # if n in list(powergenerator(math.sqrt(n))):
        #     return True
        # else:
        #     return False


a = Solution()
print(a.isPowerOfTwo(536870913
                    ))
