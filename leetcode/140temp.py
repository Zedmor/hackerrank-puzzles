class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def prefixes(word):
            return [word[:i] for i in range(0, len(word)+1)]
        dicofprefixes = set()
        dic = set(wordDict)
        for word in dic:
            dicofprefixes = dicofprefixes | set(prefixes(word))
        def workon(st, dic):
            lenst = len(st)
            if st == '':
                return ['']
            solution = []
            a = 0
            b = 0
            while b <lenst:
                while st[a:b]  in dicofprefixes and b<lenst:
                    while st[a:b] not in dic and b<lenst:
                        b+=1
                    if st[b:]:
                        workonnibble = workon(st[b:], dic - set([st[a:b]]))
                        if workonnibble != [''] and workonnibble != []:
                            solution.append(st[a:b] +' '+ ''.join(workonnibble))
                        elif workonnibble != [] and st[a:b] in dic and a==0:
                            solution.append(st[a:b])
                    else:
                        if st[a:b] in dic:
                            return [st[a:b]]

                    b+=1
                if b==0:
                    return []
                a=b
            return solution
        return workon(s, dic)

print(Solution().wordBreak("bb", 
["a","b","bbb","bbbb"]))