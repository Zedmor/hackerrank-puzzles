import hashlib

def find_hash(param):
    """
    >>> find_hash('iwrupvqb')
    1048970
    """
    for i in range(100000000):
        m = hashlib.md5()
        to_hash = param + str(i)
        m.update(to_hash.encode('utf-8'))
        if m.hexdigest()[:6] == '000000':
            return i


def main():
    print(find_hash('iwrupvqb'))

if __name__ == "__main__":
    main()
