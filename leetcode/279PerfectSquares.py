# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
from copy import copy
from functools import reduce


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # perfect squares = [1, 4, 9, 16, 25]
        # 1 2 3 0 1 2 3   0 1 2 0
        # 0 0 0 4 4 4 4 8 0 0 0 12
        #                 9 9 9 0
        import math
        import numpy as np
        maxsquare = int(math.sqrt(n))
        possibles = [a for a in range(1,maxsquare+1)]

        bestvalues = np.array([[0] * (n + 1)
                      for i in range(len(possibles))])

        print(possibles)

        def gcd(m, n):
            return n if (m - n) == 0 else gcd(abs(m - n), min(m, n))

        print(reduce((lambda x,y: gcd(x,y)), reversed(possibles)))


        bestvalues[0,] = range(n+1)
        for i, value in enumerate(possibles):
            i +=1
            # if i == len(possibles):
            #     break
            # Increment i, because the first row (0) is the case where no items
            # are chosen, and is already initialized as 0, so we're skipping it
            # i += 1
            for capacity in range(n + 1):
                # Handle the case where the weight of the current item is greater
                # than the "running capacity" - we can't add it to the knapsack
                candidate1 = copy(bestvalues[:,capacity])
                candidate2 = copy(bestvalues[:,capacity])
                # candidate2[i] +=1



                while  candidate2[i-1] * possibles[i-i] >= possibles[i]:
                    candidate2[i] +=1
                    candidate2[i - 1] -= candidate2[i] * possibles[i]
                cand1val = sum(candidate1 * possibles)
                cand2val = sum(candidate2 * possibles)
                if sum(candidate1) < sum(candidate2) and cand1val == capacity:
                    bestvalues[:, capacity] = candidate1
                elif cand2val == capacity:
                    bestvalues[:, capacity] = candidate2


                #if cand2val == capacity
                #
                # if value > capacity:
                #     bestvalues[i][capacity] = bestvalues[i - 1][capacity]
                # else:
                #     # Otherwise, we must choose between two possible candidate values:
                #     # 1) the value of "running capacity" as it stands with the last item
                #     #    that was computed; if this is larger, then we skip the current item
                #     # 2) the value of the current item plus the value of a previously computed
                #     #    set of items, constrained by the amount of capacity that would be left
                #     #    in the knapsack (running capacity - item's weight)
                #     candidate1 = copy(bestvalues[:,capacity-1])
                #     candidate2 = copy(bestvalues[:,capacity-1])
                #     candidate2[i] +=1
                #     if candidate2[i-1]*possibles[i-1] < candidate2[i]*possibles[i]:
                #         candidate2[i - 1] = 0
                #     cand1val = sum(candidate1 * possibles)
                #     cand2val = sum(candidate2 * possibles)
                #
                #
                #     # candidate1 = bestvalues[i - 1][capacity]
                #     # candidate2 = bestvalues[i - 1][capacity - value] + value
                #
                #     # Just take the maximum of the two candidates; by doing this, we are
                #     # in effect "setting in stone" the best value so far for a particular
                #     # prefix of the items, and for a particular "prefix" of knapsack capacities
                #     # bestvalues[i][capacity] = max(candidate1, candidate2)
                #     if sum(candidate1) < sum(candidate2) and cand1val == capacity:
                #         bestvalues[:, capacity] = candidate1
                #     elif cand2val == capacity:
                #         bestvalues[:, capacity] = candidate2
                #     #bestvalues[:,capacity] = lambda candidate:
        print(np.array(bestvalues))
        reconstruction = []
        i = len(possibles)
        j = n
        while i > 0:
            if bestvalues[i][j] != bestvalues[i - 1][j]:
                reconstruction.append(possibles[i - 1])
                j -= possibles[i - 1]
            i -= 1

        reconstruction.reverse()

        print(bestvalues[len(possibles)][n], reconstruction)

        # Reverse the reconstruction list, so that it is presented
        # in the order that it was given


a = Solution()
print(a.numSquares(12))
