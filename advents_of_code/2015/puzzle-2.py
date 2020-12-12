import re
from functools import reduce


def calc_paper(line):
    """
    >>> calc_paper('2x3x4')
    58
    >>> calc_paper('1x1x10')
    43
    """
    params = list(map(int, re.findall('(\d+)x(\d+)x(\d+)', line)[0]))
    sides = (params[0] * params[1], params[1] * params[2], params[2] * params[0])
    surface = sum(map(lambda a: a * 2, sides))
    smallest_size = min(sides)
    return surface + smallest_size


def calc_ribbon(line):
    """
    >>> calc_ribbon('2x3x4')
    34
    >>> calc_ribbon('1x1x10')
    14
    """
    params = list(map(int, re.findall('(\d+)x(\d+)x(\d+)', line)[0]))
    volume = reduce(lambda x, y: x * y, params)
    string = sum(map(lambda a: a*2, sorted(params)[:2]))

    return volume + string

def main():
    with open('input-2.txt') as file:
        agg_paper = 0
        agg_ribbon = 0
        for line in file:
            agg_paper += calc_paper(line)
            agg_ribbon += calc_ribbon(line)
        print(agg_paper, agg_ribbon)


if __name__ == "__main__":
    main()
