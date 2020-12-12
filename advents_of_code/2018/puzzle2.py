from collections import Counter, defaultdict


def detect_two_letters(s):
    """
    >>> detect_two_letters('abcdef')
    0
    >>> detect_two_letters('bababc')
    1
    >>> detect_two_letters('abbcde')
    1
    >>> detect_two_letters('abcccd')
    0
    >>> detect_two_letters('krdmtnqjgwfoevnabiiyxlzsph')
    1
    """
    c = Counter(s)
    return 1 if 2 in c.values() else 0


def detect_three_letters(s):
    """
    >>> detect_two_letters('abcdef')
    0
    >>> detect_two_letters('bababc')
    1
    >>> detect_two_letters('abbcde')
    1
    >>> detect_two_letters('abcccd')
    0

    """
    c = Counter(s)
    return 1 if 3 in c.values() else 0


candidates = ['abcde',
              'fghij',
              'klmno',
              'pqrst',
              'fguij',
              'axcye',
              'wvxyz']


def find_boxes(boxes):
    """
    >>> find_boxes(candidates)
    1
    """
    for first_word in boxes:
        for second_word in boxes:
            cnt = 0
            cmn_letters = []
            for i, letter in enumerate(first_word):
                if second_word[i] != letter:
                    cnt += 1
                else:
                    cmn_letters.append(letter)
                if cnt > 1:
                    break
            if cnt == 1:
                print(first_word, second_word)
                print(''.join(cmn_letters))




def main():
    """
    >>> main()
    """
    with open('input-2.txt') as f:
        l = [s.rstrip() for s in f.readlines()]
        new_l = filter(lambda s: detect_three_letters(s) == 1 or detect_two_letters(s) == 1, l)
        find_boxes(l)
