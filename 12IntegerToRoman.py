class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = num // 1000 * 1000
        hundreds = num // 100 % 10 * 100
        tens = num // 10 % 10 * 10
        ones = num % 10
        return (''.join([self.roman_enumerator(thousands),
                         self.roman_enumerator(hundreds),
                         self.roman_enumerator(tens),
                         self.roman_enumerator(ones)]))

    def roman_enumerator(self, x):
        if x % 1000 == 0:
            return 'M' * (x // 1000)
        elif x % 100 == 0:
            small, half, big = ('C', 'D', 'M')
            x = x //100
        elif x % 10 == 0:
            small, half, big = ('X', 'L', 'C')
            x = x // 10
        else:
            small, half, big = ('I', 'V', 'X')


        enum = {0: '',
                1: small,
                2: small *2 ,
                3: small *3,
                4: small + half,
                5: half,
                6: half + small,
                7: half + small + small,
                8: half + 3 * small,
                9: small + big,
                10: big
                }
        return (enum[x])


print(Solution().intToRoman(3337))
