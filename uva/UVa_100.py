def three_plus_n(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        counter += 1
    return counter


def solution(*args):
    first, last = map(int, args)
    if first > last:
        last, first = first, last

    results = []
    for i in range(int(first), int(last) + 1):
        results.append(three_plus_n(i))

    return f'{args[0]} {args[1]} {max(results)}'


