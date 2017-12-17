import re


class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        self.code = code
        if not code or code[0] !='<':
            return False

        self.get_tags()

        if len(self.tokens) < 2 or self.tokens[0] != self.tokens[-1][1:]:
            return False


        itag = 0
        while itag < len(self.tokens):
            tag = self.tokens[itag]
            if '![CDATA[' in tag:
                if itag > 0 and itag < len(self.tokens) -1:
                    self.tokens.pop(itag)
                    itag-=1
                else:
                    return False
            itag+=1

        stack = []

        while self.tokens:
            token = self.tokens.pop(0)
            if token[0] != '/':
                if len(token) <1 or len(token) > 9 or not re.match('^[A-Z]*$', token):
                    return False
                stack.append(token)
            else:
                if not stack or stack.pop() != token[1:]:
                    return False

        return True if not stack else False

    def get_tags(self):
        """
        :return: all tags as list
        """
        left = 0
        right = 0
        self.tokens = []
        while right < len(self.code)-1:
            while self.code[left] != "<":
                left += 1
                right += 1
                if right == len(self.code):
                    self.tokens = []
                    return
            in_cdata = False
            while True:
                right+=1
                if right == len(self.code):
                    break
                if ((right - left) == 8) and self.code[left:right+1] =='<![CDATA[':
                    in_cdata = True
                if self.code[right] == ">" and not in_cdata:
                    break
                if in_cdata and self.code[right-3:right]=="]]>":
                    break
            if right<= len(self.code) and left+1 < right:
                self.tokens.append(self.code[left+1:right])
                left = right




print(Solution().isValid("<TAG>sometext</TAG><![CDATA[ABC]]>"))
