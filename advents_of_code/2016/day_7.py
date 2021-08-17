import re

from pytest import mark


def abba_in(text):
    for cursor in range(len(text) - 3):
        if text[cursor:cursor + 2] == text[cursor + 2: cursor + 4][::-1] and text[cursor] != text[cursor + 1]:
            return True
    return False


def check_tls(addr):
    insides = re.findall(r'\[(\w+)\]', addr)
    outsides = re.findall(r'(\w+)(?=\[|$)', addr)
    return any((abba_in(outside) for outside in outsides)) and not any((abba_in(inside) for inside in insides))


def get_abas(text):
    for cursor in range(len(text) - 2):
        if text[cursor] == text[cursor + 2] and text[cursor] != text[cursor + 1]:
            yield text[cursor:cursor + 3]
    return False


def check_ssl(addr):
    insides = re.findall(r'\[(\w+)\]', addr)
    outsides = re.findall(r'(\w+)(?=\[|$)', addr)
    # True if ABA in any of outsides and BAB in any of insides
    abas = []
    for outside in outsides:
        abas.extend(get_abas(outside))

    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if any([bab in inside for inside in insides]):
            return True
    return False

@mark.parametrize("addr, condition", [
    ("luqpeubugunvgzdqk[jfnihalscclrffkxqz]wvzpvmpfiehevybbgpg[esjuempbtmfmwwmqa]rhflhjrqjbbsadjnyc", False),
    ("abba[mnop]qrst", True),
    ("abcd[bddb]xyyx", False),
    ("aaaa[qwer]tyui", False),
    ("ioxxoj[asdfgh]zxcvbn", True)
    ])
def test_checker(addr, condition):
    assert check_tls(addr) == condition


@mark.parametrize("addr, result", [
    ("aba[bab]xyz", True),
    ("xyx[xyx]xyx", False),
    ("aaa[kek]eke", True),
    ("zazbz[bzb]cdb", True)
    ])
def test_ssl_checker(addr, result):
    assert check_ssl(addr) == result


def test_abba_in():
    assert abba_in('ioxxoj')
    assert not abba_in('abc')


def test_main_run():
    with open("day_7.txt") as inp_file:
        assert sum([int(check_tls(addr)) for addr in inp_file.readlines()]) == 0


def test_main_run_ssl():
    with open("day_7.txt") as inp_file:
        assert sum([int(check_ssl(addr)) for addr in inp_file.readlines()]) == 0