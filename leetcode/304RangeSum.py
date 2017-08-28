'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if matrix:
            self.x = len(matrix[0])
        else:
            self.x = 0
        self.y = len(matrix)

        self.hashsum = {}
        self.hashsum_byrow = {}
        self.hashsum_bycol = {}

    def buildhash(self, row1, row2, col1, col2):
        # Create hashtable
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                inter_sum = sum(self.matrix[i][col1:j + 1])
                for k in range(col1, j + 1):
                    self.hashsum_byrow[(i, k, j)] = inter_sum
                    inter_sum -= self.matrix[i][k]

        for j in range(col1, col2+1):
            for k in range(col1,j + 1):
                for i in range(row1, row2+1):
                    inter_sum = sum([
                                        self.hashsum_byrow[
                                            row, k, j]
                                        for row in
                                        range(row1,i + 1)])
                    for m in range(row1, i + 1):
                        self.hashsum[(m, i, k, j)] = inter_sum
                        inter_sum -= self.hashsum_byrow[
                            m, k, j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        self.buildhash(row1, row2, col1, col2)
        return self.hashsum[row1, row2, col1, col2]


        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)


a = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])

print(a.sumRegion(2, 1, 4, 3))
print(a.sumRegion(1, 1, 2, 2))
print(a.sumRegion(1, 2, 2, 4))
