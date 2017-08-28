


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
        """
        ab = format(a, 'b')
        bb = format(b, 'b')

        maxlen = max(len(ab),len(bb))
        carry = 0
        result = []
        if ab:
            if ab[0]=='-':
                result.append('-')
                ab=ab[1:]
        if bb:
            if bb[0]=='-':
                result.append('-')
                bb=bb[1:]
        for i in range(maxlen):
            try:
                bita = int(ab[-i])
            except IndexError:
                bita = carry
            try:
                bitb = int(bb[-i])
            except IndexError:
                bitb = carry
            if bita==bitb==carry==0:
                result.append('0')
            elif bita==bitb==0 and carry==1:
                result.append('1')
                carry = 0
            elif (bita ^ bitb) and (carry==0):
                result.append('1')
            elif (bita ^ bitb) and (carry==1):
                result.append('1')
                carry = 0
            elif bita==bitb==1:
                result.append('0')
                carry = 1
        if carry==1:
            result.append('1')
        print(int(''.join(list(reversed(result))),2))

        print(ab,bb)

print(Solution().getSum(610,10))