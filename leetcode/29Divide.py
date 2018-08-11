def Add(x, y):
    # Iterate till there is no carry
    while (y != 0):
        # carry now contains common set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1
    return x


def Multiply(x, y):
    result = x
    for i in range(y - 1):
        result = Add(result, x)
    return result


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i = 0
        while Multiply(divisor, i + 1) <= dividend or -Multiply(divisor, i + 1) >= dividend:
            i += 1
        return i if dividend > 0 else -i


print(Solution().divide(1, -1))
