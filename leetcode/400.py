"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        #def helpernumdigit(n):
        number = 0
        numdigit = 0
        while numdigit+int(math.log10(number+1))+1 <= (n-1):
            number +=1
            numdigit+=int(math.log10(number))+1

        targnum = str(number+1)
        targdigit = targnum[n-1-numdigit]
        return targnum
        return int(targdigit)
        # print(number, numdigit)

for u in range(1,1000):
    print(u, Solution().findNthDigit(u))