class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        running_total = 0
        while s and s[0] == 'M':
            running_total +=1000
            s=s[1:]
        i = 0
        triplets =(('C', 'D', 'M'), ('X', 'L', 'C'), ('I', 'V', 'X'))
        while s:
            number = 0
            if len(s) >=3 and s[:3] in self.get_nums(*triplets[i]):
                number = self.get_nums(*triplets[i])[s[:3]]
                s = s[3:]

            elif len(s) >=2 and s[:2] in self.get_nums(*triplets[i]):
                number = self.get_nums(*triplets[i])[s[:2]]
                s = s[2:]
            elif s and s[:1] in self.get_nums(*triplets[i]):
                number = self.get_nums(*triplets[i])[s[:1]]
                s = s[1:]
            else:
                i+=1
            running_total += number * 10** (2-i)
        return running_total

    def get_nums(self, small, half, big):
        enum = {
                small: 1,
                small *2:2,
                small *3:3,
                small + half :4,
                half:5,
                half + small:6,
                half + small + small:7,
                half + 3 * small:8,
                small + big:9,
                big:10
                }
        return enum

print(Solution().romanToInt("MCMXCVI"))