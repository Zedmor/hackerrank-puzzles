"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R


P
A   S
Y  I
P L
A
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question.
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        >>> Solution.createsegment('PAYPALISHIRING', 3)

        """
        sol = []
        if not s:
            return ''
        interval = max(numRows+numRows-2, 1)
        for i in range(0, len(s), interval):
            sol.append(self.createsegment(s[i:i+interval], numRows))
        presol = ''.join(list(map(''.join, zip(*sol)))).replace(' ','')
        return presol
    def createsegment(self, substring, n):
        """Creates segment from substring. Len of substr is guaranteed to be
        N + (N-2)
        >>> Solution.createsegment('PAYP', 3)
        ['P', 'AP', 'Y']
        """
        if len(substring) < n+n-2:
            substring = substring + ' '*((n+n-2)-len(substring))
        sol = []
        sol =  list(map(''.join, zip((reversed(substring[
                                                            1:n-1])), \
              substring[n:]))) + [substring[0]]
        if n > 1:
            sol = [substring[n-1]] + sol

        return list(reversed(sol))


if __name__ == "__main__":
    print(Solution().convert('AB', 4))
    # import doctest
    # doctest.testmod()#extraglobs={'t': Solution.convert.createsegment()})