def solution(arg):
    params, specimens = arg
    chambers, n = map(int, params.split(' '))
    specimens = list(map(int, specimens.split(' ')))

    slots = 2 * int(chambers)

    specimens = [int(s) for s in specimens] + [0] * (slots - len(specimens))

    specimens = sorted(specimens)

    result = []
    for i in range(len(specimens) // 2):
        result.append((specimens[i], specimens[len(specimens) - i - 1]))

    average = sum([sum(t) for t in result]) / chambers

    sum_of_imbalances = sum([abs(sum(t) - average) for t in result])

    out = []
    for i, pair in enumerate(result):
        out.append(f' {i}: {pair[0]} {pair[1]}')
    out.append(f'IMBALANCE = {sum_of_imbalances:.5f}')
    return out
