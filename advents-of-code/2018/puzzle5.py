import string


def naive_remover(s):
    """
    >>> naive_remover('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'
    """
    i = 0
    while i < len(s) - 1:
        if s[i].swapcase() == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i = max(i - 1, 0)
        else:
            i += 1
    return s

def main():
    """
    >>> main()
    ''
    """
    with open('input-5.txt') as f:
        inp = f.readline().rstrip()
    # inp = 'dabAcCaCBAcCcaDA'
    attempts = [(c, len(naive_remover(inp.replace(c, '').replace(c.swapcase(), '')))) for c in string.ascii_lowercase]
    print(min(attempts, key=lambda t: t[1]))
    # return naive_remover(inp)
