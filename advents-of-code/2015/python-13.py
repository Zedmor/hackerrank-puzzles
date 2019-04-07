import itertools
import re
from collections import defaultdict


def line_parser(line):
    """
    >>> line_parser('Alice would lose 57 happiness units by sitting next to Bob.\\n')
    ['Alice', -57, 'Bob']
    >>> line_parser('Alice would gain 71 happiness units by sitting next to Eric.\\n')
    ['Alice', 71, 'Eric']
    """
    tokens = list(re.findall('(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)', line)[0])
    tokens[2] = int(tokens[2]) if tokens[1] == 'gain' else -int(tokens[2])
    tokens.pop(1)
    return tokens

def record_maker(parsed_line):
    """
    >>> record_maker(['Alice', -57, 'Bob'])
    {'Alice': ('Bob', -57)}
    """
    return (parsed_line[0], (parsed_line[2], parsed_line[1]))

def happiness(happiness_dict, seating):
    happiness_value = 0
    for position, person in enumerate(seating):
        happiness_value += happiness_dict[person][seating[position - 1]]
        happiness_value += happiness_dict[person][seating[position + 1 if position < len(seating) - 1 else 0]]
    return happiness_value


def insert_you(func):
    def wrapped_dict(lines):
        new_dict = func(lines)
        guests = new_dict.keys()
        for g in guests:
            new_dict[g]['Hero'] = 0
        new_dict['Hero'] = dict(((g, 0) for g in guests))
        return new_dict
    return wrapped_dict


@insert_you
def build_dict(lines):
    output_dict = defaultdict(dict)
    for line in lines:
        record = record_maker(line_parser(line))
        output_dict[record[0]][record[1][0]] = record[1][1]
    return output_dict

def main():
    """
    >>> main()
    None
    """
    lines = open('input-13.txt').readlines()
    happiness_dict = build_dict(lines)
    print(max(list(map(lambda s: happiness(happiness_dict, s), itertools.permutations(happiness_dict.keys())))))
