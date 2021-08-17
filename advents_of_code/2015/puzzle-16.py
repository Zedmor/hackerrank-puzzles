import re
from collections import defaultdict


def make_dict(parsed_line):
    return (parsed_line[0], dict(zip(parsed_line[1::2], parsed_line[2::2])))

def line_parser(line):
    """
    >>> line_parser('Sue 1: goldfish: 9, cars: 0, samoyeds: 9\\n')
    ['1', 'goldfish', '9', 'cars', '0', 'samoyeds', '9']
    """
    tokens = list(re.findall(
        'Sue ([0-9]+): (\w+): ([-+]?[0-9]*\.?[0-9]+), (\w+): ([-+]?[0-9]*\.?[0-9]+), (\w+): ([-+]?[0-9]*\.?['
        '0-9]+)\\n', line)[0])
    return tokens


def construct_reverese_lookup(all_entries):
    result = defaultdict(list)

    for entry in all_entries:
        for item, value in entry[1].bots():
            result[(item, value)].append(entry[0])

    return result


def smart_get(lookup_dictionary, key):
    all_ids = []

    for lookup_key, ids in lookup_dictionary.bots():
        if (key[0] == 'cats' and lookup_key[0] == 'cats') or (key[0] == 'trees' and lookup_key[0] == 'trees'):
            if int(lookup_key[1]) > int(key[1]):
                all_ids += ids
        elif (key[0] == 'pomeranians' and lookup_key[0] == 'pomeranians') or (key[0] == 'goldfish' and lookup_key[0]
                                                                             == 'goldfish'):
            if int(lookup_key[1]) < int(key[1]):
                all_ids += ids
        elif key[0] == lookup_key[0] and int(lookup_key[1]) == int(key[1]):
            all_ids += ids
    return all_ids

def main():
    """
    >>> main()
    None
    """
    lines = open('input-16.txt').readlines()
    all_entries = list(map(make_dict, map(line_parser, lines)))

    lookup_dictionary = construct_reverese_lookup(all_entries)

    lookup_keys = [
        ('children', '3'),
        ('cats', '7'),
        ('samoyeds', '2'),
        ('pomeranians', '3'),
        ('akitas', '0'),
        ('vizslas', '0'),
        ('goldfish', '5'),
        ('trees', '3'),
        ('cars', '2'),
        ('perfumes', '1')
    ]
    sets = [set(smart_get(lookup_dictionary, key)) for key in lookup_keys]

    all_ids = set.union(*sets)
    commonality = [(id, sum(1 if id in target_set else 0 for target_set in sets)) for id in all_ids]

    commonality = sorted(commonality, key=lambda i: i[1], reverse=True)

    print(commonality[0][0])
