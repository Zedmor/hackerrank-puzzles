a = [5]

l = 10
d = {}

for i in a:
    if i in d:
        print((d[i], i,))
    else:
        d[l-i] = i

