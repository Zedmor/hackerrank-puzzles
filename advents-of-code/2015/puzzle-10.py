from functools import reduce


def look_and_say(seq):
    """
    >>> look_and_say('1')
    '11'
    >>> look_and_say('11')
    '21'
    >>> look_and_say('21')
    '1211'
    >>> look_and_say('1211')
    '111221'
    >>> look_and_say('111221')
    '312211'
    """
    cur = seq[0]
    new_seq = []
    ind = 0
    while ind < len(seq):
        counter = 0
        while ind < len(seq) and seq[ind] == cur:
            counter += 1
            ind += 1
        new_seq.append(str(counter))
        new_seq.append(cur)
        if ind < len(seq):
            cur = seq[ind]
    return ''.join(new_seq)


def main():
    """
    >>> main()
    """
    seed = '3113322113'
    for i in range(50):
        seed = look_and_say(seed)
    print(len(seed))


if __name__ == "__main__":
    main()
