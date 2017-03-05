"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def checksq(x, y, size, matrix):
            if numrows-y < size or numcol-x < size:
                return False
            for i in range(x,x+size):
                for j in range(y,y+size):
                    if matrix[j][i] == "0":
                        return False
            return True
        if not matrix:
            return 0

        # if len(matrix[0]) ==1:
        #     matrix = [matrix]
        numrows = len(matrix)
        numcol = len(matrix[0])

        sqsz = 0
        for i in range(numcol):
            for j in range(numrows):
                while checksq(i, j, sqsz, matrix):
                    sqsz+=1


        return ((sqsz-1)*(sqsz-1))

matrix = ["10100","10111","11111","10010"]

matrix =["0"]

a = Solution()
print(a.maximalSquare(matrix))
