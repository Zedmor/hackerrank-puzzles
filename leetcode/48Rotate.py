from collections import OrderedDict


def make_lookup(n):
    lookup = OrderedDict()
    ind = 0
    for m in range(4):
        for i2 in range(0, n - 1):
            if m == 0:
               lookup[(0, i2)] = ind
            elif m == 1:
                lookup[(i2, n - 1)] = ind
            elif m == 2:
                lookup[(n - 1, n - i2 - 1)] = ind
            else:
                lookup[(n - i2 - 1, 0)] = ind
            ind += 1
    return lookup

def convert_i_j(i, j, lookup, n):

    index_for_lookup = lookup[(i, j)] + 1
    if index_for_lookup > len(lookup) - 1:
        index_for_lookup = index_for_lookup - len(lookup)
    out = list(lookup.keys())[index_for_lookup]

    return out


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix) // 2):
            lookup = make_lookup(n - 2 * i)
            for times in range(n-1 - 2*i):
                stack = matrix[i][i]
                for item in list(lookup.keys())[:-1]:
                    i2, j = item
                    newi2, newj2 = convert_i_j(i2, j, lookup, n)
                    i2 += i
                    j += i
                    stack2 = matrix[newi2 + i][newj2 + i]
                    matrix[newi2 + i][newj2 + i] = stack
                    stack = stack2
                lasti, lastj = list(lookup.keys())[0]
                matrix[lasti + i][lastj + i] = stack2




lookup = make_lookup(3)


# assert convert_i_j(0, 0, lookup, 3) == (0, 2)
# assert convert_i_j(0, 2, lookup, 3) == (2, 2)
# assert convert_i_j(2, 2, lookup, 3) == (2, 0)
# assert convert_i_j(1, 2, lookup, 3) == (2, 1)




input_matrix = [
                   [1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]
               ]

out = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]


Solution().rotate(input_matrix)
assert input_matrix == out

input_matrix = [
                   [5, 1, 9, 11],
                   [2, 4, 8, 10],
                   [13, 3, 6, 7],
                   [15, 14, 12, 16]
               ]

out = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]

Solution().rotate(input_matrix)

assert input_matrix == out
