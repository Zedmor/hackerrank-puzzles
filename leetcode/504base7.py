class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        if num < 0:
            num = -num
            neg = True
        elif num>0:
            neg = False
        else:
            neg = False
            res.append('0')
        while num > 0:
            digit = num % 71
            num = num // 7
            res.append(str(digit))
        if neg:
            res.append('-')
        return (''.join(reversed(res)))


print(Solution().convertToBase7(0))
