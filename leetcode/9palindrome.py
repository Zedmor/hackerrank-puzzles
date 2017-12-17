"""
Determine whether an integer is a palindrome. Do this without extra space
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is 0:
            return True
        if x < 0:
            return False
        from math import log10
        while True:
            if x // (10 ** (int(log10(x)))) == x % 10:
                try:
                    if int(log10(x)) != int(log10(x % (10 ** (int(log10(x)))))) + 1 and x % (10 ** (int(log10(x)))) // 10 != 0:
                        digits_to_cut = int(log10(x)) - int(log10(x % (10 ** (int(log10(x)))))) - 1
                        x = x//10
                        for cut_digits in range(digits_to_cut):
                            if x % 10 == 0:
                                x = x // 10
                            else:
                                return False

                        x = x % (10 ** (int(log10(x))))
                    else:
                        x = x % (10 ** (int(log10(x)))) // 10
                except ValueError:
                    if x !=0 and log10(x) < 1:
                        return True

                if x is 0:
                    return True
            else:
                return False


print(Solution().isPalindrome(1001))
