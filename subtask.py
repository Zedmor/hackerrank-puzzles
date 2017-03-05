import itertools
from functools import reduce

import numpy as np
from collections import Counter


field = [[1,0,10],
[1,1,1],
[1,0,0],
[10,1,0] ,
[1,10,0]]


field = np.array(field)

allcombos = list(itertools.combinations(list(range(len(field))), 2))

# print(allcombos)

transp = []

for ind,elem in enumerate(field):
    transp.append(2** elem*(ind+1))#2**(ind*np.array(elem))

red = reduce(np.dot,transp)

for item in red:
    print(bin(item))

for combo in allcombos:
    target = ([field[i] for i in combo])
    target = list(reduce(np.add, target))
    if (target.count(10)) == 2:
        print(combo)


