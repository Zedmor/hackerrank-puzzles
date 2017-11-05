from math import log10


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            flag = True
            x = -x
        else:
            flag = False
        y = 0
        for i in range(int(log10(x))+1):
            y*=10
            y += x % 10
            x = x // 10
        if abs(y) > (1 << 31) - 1:
            return 0
        return -y if flag else y

print(Solution().reverse(1563847412))