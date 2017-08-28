"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        a = r'^\s*([\+\-]*)([0-9]*)([\.e]|\.e)?([0-9]*)(e{1}[\+\-]?[0-9]+)*\s*$'
        pattern = re.compile(a)
        matchobj = pattern.match(s)
        if not matchobj:
            # special case with .2e81
            a = '^\s*([\+\-\.]*)([0-9]*)([\.e]|\.e)?([0-9]*)(e{1}[\+\-]?[0-9]+)*\s*$'

            pattern = re.compile(a)
            matchobj = pattern.match(s)
            if matchobj and (matchobj.group(2) or matchobj.group(4)):
                pat2 = re.compile(r'\.\.')
                if pat2.match(matchobj.group(0)):
                    return False
                if matchobj.group(5) and 'e' in matchobj.group(3):
                    return False
                if matchobj.group(3) == '.' and '.' in matchobj.group(1):
                    return False
                if re.match(r'^0+$', matchobj.group(2)):
                    return False
                if matchobj.group(1) == '.-' or matchobj.group(1)=='.+' or matchobj.group(1)=='..':
                    return False
                if matchobj.group(1) == matchobj.group(3) == '.':
                    return False
                if matchobj.group(3) == 'e' and matchobj.group(4) =='':
                    return False
                if matchobj.group(3) != 'e' and matchobj.group(2) == matchobj.group(4) =='':
                    return False
                else:
                    return True
            else:
                return False
        if matchobj.group(5) and matchobj.group(3) == 'e':
            return False
        if (matchobj.group(3) == 'e' or matchobj.group(3) == '.e') and (
                matchobj.group(2) == '' or matchobj.group(4) == ''):
            return False
        if matchobj.group(3) == '.' and matchobj.group(
                1) == '' and matchobj.group(4) == '' and matchobj.group(2) == '':
            return False
        if matchobj.group(3) != 'e' and matchobj.group(2) == matchobj.group(
                4) == '':
            return False
        if not (matchobj.group(2)) and not (matchobj.group(3)) and not (
        matchobj.group(4)):
            return False
        return True


a = Solution()
print(a.isNumber(".7.ee95e22"))