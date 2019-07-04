#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    >>> sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    """
    sorted_arr = sorted(ar)
    counter = 0
    while sorted_arr and len(sorted_arr) >= 2:
        if sorted_arr[0] == sorted_arr[1]:
            sorted_arr.pop(0)
            sorted_arr.pop(0)
            counter += 1
        else:
            sorted_arr.pop(0)
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
