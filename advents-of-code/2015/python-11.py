from collections import defaultdict


def first_requirement(password):
    """
    >>> first_requirement('hijklmmn')
    True
    >>> first_requirement('abbceffg')
    False
    """
    for c1, c2, c3 in zip(password[0::1], password[1::1], password[2::1]):
        if ord(c1) == ord(c2) - 1 == ord(c3) - 2:
            return True
    return False


def second_req(password):
    """
    >>> second_req('hijklmmn')
    False
    """
    return 'i' not in password and 'o' not in password and 'l' not in password



def third_req(password):
    """
    >>> third_req('abbceffg')
    True
    >>> third_req('abbcegjk')
    False
    >>> third_req('aaa')
    False
    >>> third_req('ghjaabcc')
    True
    """
    counts1 = defaultdict(int)
    counts2 = defaultdict(int)
    for c1, c2 in zip(password[0::2], password[1::2]):
        if c1 == c2:
            counts1[''.join((c1, c2))] += 1
    for c1, c2 in zip(password[1::2], password[2::2]):
        if c1 == c2:
            counts2[''.join((c1, c2))] += 1

    counts1 = set(counts1.keys())
    counts2 = set(counts2.keys())

    return len(counts1 ^ counts2) > 1


def validate_password(password):
    """
    >>> validate_password('hijklmmn')
    False
    >>> validate_password('abbceffg')
    False
    >>> validate_password('abbcegjk')
    False
    """
    return first_requirement(password) and second_req(password) and third_req(password)

def inc_pass(password):
    """
    >>> inc_pass('abc')
    'abd'
    >>> inc_pass('yzz')
    'zaa'
    >>> inc_pass('ybz')
    'yca'

    """
    carryover = 0
    password = list(password)
    i = len(password) - 1
    while True:
        password[i] = chr(ord(password[i]) + 1)
        carryover = 0
        if ord(password[i]) > 122:
            password[i] = chr(97 + ord(password[i]) - 123)
            carryover = 1
            i -= 1
        if carryover == 0:
            break


    return ''.join(password)



def next_password(password):
    """
    >>> next_password('cqjxxyzz')
    cqjxjnds
    """
    while True:
        password = inc_pass(password)
        if validate_password(password):
            break
    print(password)



