def contains_three_vowels(string):
    """
    >>> contains_three_vowels('aaa')
    True
    >>> contains_three_vowels('aa')
    False
    """
    vovels = 'aeiou'
    return sum([1 if char in vovels else 0 for char in string]) >= 3

def contains_at_least_one_letter(string):
    """
    >>> contains_at_least_one_letter('abcdde')
    True
    >>> contains_at_least_one_letter('aabbccdd')
    True
    """
    first_letter = string[0]
    for letter in string[1:]:
        if first_letter == letter:
            return True
        else:
            first_letter = letter
    return False


def not_contain_strings(string):
    """
    >>> not_contain_strings('ugknbfddgicrmopn')
    True
    >>> not_contain_strings('aaa')
    True
    """
    return ('ab' not in string) and ('cd' not in string) and ('pq' not in string) and ('xy' not in string)

def niceness(string):
    """
    >>> niceness('ugknbfddgicrmopn')
    True
    >>> niceness('aaa')
    True
    >>> niceness('jchzalrnumimnmhp')
    False
    >>> niceness('haegwjzuvuyypxyu')
    False
    >>> niceness('dvszwmarrgswjxmb')
    False
    """

    return contains_three_vowels(string) and contains_at_least_one_letter(string) and not_contain_strings(string)


def main():
    with open('input-4.txt') as file:
        print(sum(map(niceness, file.readlines())))


if __name__ == "__main__":
    main()
