a = [{3, 5, 6}, {1, 3, 5}, {1, 6}, {1, 3, 5}, {2, 3, 5}]

#print(set.intersection(*a))


dic = []
for el in a:
    dic = dic +list(el)

z = [x for x in dic if dic.count(x)==1]

print(z)