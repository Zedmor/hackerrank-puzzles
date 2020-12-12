import re

c = 0

for i in range(165432, 707913):
    s = str(i)
    ls = len(s)
    m = [match[0] for match in re.findall(r'((\w)\2{1,})', s)]
    dupl = any(len(b) == 2 for b in m)
    inc = all(s[i + 1] >= s[i] for i in range(len(s)-1))
    if dupl and inc:
        c += 1
print(c)
