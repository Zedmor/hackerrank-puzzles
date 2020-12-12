from collections import defaultdict


def contains_pair_two_letters(string):
    """
    >>> contains_pair_two_letters('xyxy')
    True
    >>> contains_pair_two_letters('aabcdefgaa')
    True
    >>> contains_pair_two_letters('aaa')
    False
    >>> contains_pair_two_letters('aaaa')
    True
    >>> contains_pair_two_letters('xxyxx')
    True
    """
    all_pairs = defaultdict(int)
    blocked_pairs = defaultdict(int)
    blocked_pair = ('', -1, -1)
    for i in range(len(string) - 1):
        pair = string[i:i + 2]
        if pair != blocked_pair[0]:
            all_pairs[pair] += 1
        elif i not in blocked_pair[1:]:
            all_pairs[pair] += 1
        else:
            blocked_pairs[pair] += 1
        blocked_pair = (pair, i, i+1)
    return len([v for v in all_pairs.values() if v >= 2]) > 0 or len([v for v in blocked_pairs.values() if v >= 2]) > 0


def one_letter_between_two(string):
    """
    >>> one_letter_between_two('xyx')
    True
    >>> one_letter_between_two('abcdefeghi')
    True
    >>> one_letter_between_two('aaa')
    True
    >>> one_letter_between_two('uurcxstgmygtbstg')
    False
    >>> one_letter_between_two('uurcxstgmygtbgtg')
    True

    """
    for i in range(len(string) - 2):
        triplet = string[i:i + 3]
        if triplet[0] == triplet[2]:
            return True
    return False


def niceness(string):
    """
    >>> niceness('qjhvhtzxzqqjkmpb')
    True
    >>> niceness('xxyxx')
    True
    >>> niceness('uurcxstgmygtbstg')
    False
    >>> niceness('ieodomkazucvgmuy')
    False
    >>> niceness('aaaa')
    True
    """

    return one_letter_between_two(string) and contains_pair_two_letters(string)


def main():
    """
    >>> main()
    """
    with open('input-4.txt') as file:
        print(sum(map(niceness, file.readlines())))


if __name__ == "__main__":
    main()
