"""

>>> subset_sum([50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40], 150)


>>> subset_sum([20, 15, 10, 5, 5], 25)

"""
from collections import defaultdict

counter = defaultdict(int)


def subset_sum(numbers, target, partial=[], total=0):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        global counter
        counter[len(partial)] += 1
        # print("printsum(%s)=%s" % (partial, target))
        return 0
    if s >= target:
        return 0# if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        total += subset_sum(remaining, target, partial + [n], total)
    return total


def main():
    """
    >>> main()
    """
    subset_sum([50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40], 150)
    print(counter)

if __name__ == '__main__':
    main()
