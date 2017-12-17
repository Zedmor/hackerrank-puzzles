class Solution(object):
    def isMatch(self, s, p):
        """
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).

        The function prototype should be:
        bool isMatch(const char *s, const char *p)

        :type s: str
        :type p: str
        :rtype: bool
        """
        found = self.string_match(s, p)
        return found

    def string_match(self, string, pattern):
        pattern_cursor = 0
        string_cursor = 0
        offset = 0
        previous_char = ''
        if not pattern:
            return True
        if not string:
            return pattern == string
        while pattern_cursor < len(pattern):
            if string_cursor == len(string):
                return False
            elif pattern[pattern_cursor] == '*':
                if self.match_char(string[string_cursor], previous_char):
                    string_cursor += 1
                    offset +=1
                else:
                    # string_cursor = string_cursor - 1
                    pattern_cursor += 1
                    previous_char = ''
                    offset = 0
            elif pattern_cursor < len(pattern) -1 and pattern[pattern_cursor + 1] == '*':
                string_cursor += 1
                previous_char = pattern[pattern_cursor]
                pattern_cursor += 1
            elif self.match_char(string[string_cursor], pattern[pattern_cursor]):
                string_cursor += 1
                previous_char = pattern[pattern_cursor]
                pattern_cursor += 1
            else:
                return False

            if string_cursor == len(string):
                if pattern_cursor == len(pattern):
                    return True
                if pattern[pattern_cursor] == '*' and pattern_cursor == len(pattern) - 1:
                    return True
                options = []
                for i_offset in range(offset, 0, -1):
                    options.append(self.string_match(string[string_cursor-i_offset:], pattern[pattern_cursor+1:]))
                if True in options:
                    return True
                return False
        return False

    def match_char(self, string_char, previous_char):
        return string_char == previous_char or previous_char == '.'


s = Solution()

print(s.string_match("aaaaaaaaaaaaab",
"a*a*a*a*a*a*a*a*a*a*a*a*b"))

# q = [
#     ('aa', 'a'),
#     ("aa", "aa"),
#     ("aaa", "aa"),
#     ("aa", "a*"),
#     ("aa", ".*"),
#     ("ab", ".*"),
#     ("aab", "c*a*b")]
#
# a = [False, True, False, True, True, True, True]
#
# for req, resp in zip(q, a):
#     assert s.isMatch(*req) == resp
