# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
n = 4
k = 2
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            # for l in range(k + 1, n + 1):
            print('({}, {}, {})'.format(i, j, k))

print()

i = 0

counters = list(range(1, k))
print(counters)


def arrayprocessing(counters):
    return not set(counters) == {n}


offset = 1

while arrayprocessing(counters):
    while counters[offset] < n:
        for i in range(counters[offset] + 1, n + 1):
            counters[-1] = i
            print(counters)
        counters[offset] += 1
    counters[offset - 1] += 1
    counters[offset] = counters[offset - 1]
    offset -= 1
    if offset == -1:
        print('foo')





    # while counters[i] < n:
    #     while i < len(counters):
    #         print(i)
    #         i += 1



    # last = len(counters)-2
    # while counters[last] < n:
    #     for i in range(counters[-1],n+1):
    #         print(counters[:-1]+[i])
    #     counters[last] +=1

    # print(counters)
