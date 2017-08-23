"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
9110
881624
11235813
111222333

123
"""


class Solution(object):
    def int_nozero(self, strnum):
        if len(strnum) > 1:
            if strnum[0] != '0':
                return int(strnum)
            raise ValueError
        else:
            return int(strnum)


    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        found = False
        def recur(num):
            for num1 in range(1,len(num)):
                for num2 in range(num1+1,len(num)):
                    for num3 in range(num2+1, len(num)+1):
                        try:

                            if self.int_nozero(num[:num1]) + self.int_nozero(num[num1:num2]) == self.int_nozero(num[num2:num3]):
                                if num3 == len(num):
                                    return True
                                if recur(num[num1:]):
                                    return True
                        except ValueError:
                            pass

        return recur(num) or False


print(Solution().isAdditiveNumber('99100199'))
