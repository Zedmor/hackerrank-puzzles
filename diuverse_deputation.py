#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'diverseDeputation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER w
#

from itertools import permutations

def check_for_man_and_woman(set_of_candidates):
    woman_counter = 0
    man_counter = 0
    for el in set_of_candidates:
        if 'w' in el:
            woman_counter += 1
        else:
            man_counter += 1
    return man_counter > 0 and woman_counter > 0

def diverseDeputation(m, w):
    """
    >>> diverseDeputation(3, 0)
    0
    >>> diverseDeputation(2, 2)
    4

    """
    all_candidates = []
    for i in range(m):
        all_candidates.append('m{}'.format(i))
    for i in range(w):
        all_candidates.append('w{}'.format(i))
    perms = permutations(all_candidates, 3)

    unique = set([frozenset(el) for el in perms])
    filtered = filter(check_for_man_and_woman, unique)
    print(len(list(filtered)))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())

    w = int(input().strip())

    result = diverseDeputation(m, w)

    fptr.write(str(result) + '\n')

    fptr.close()
