import datetime
import re


def convert_string(s, source_base, target_base):
    """
    >>> convert_string('FF', 16, 10)
    '255'

    >>> convert_string('FF', 16, 2)
    '11111111'

    >>> convert_string('11111111', 2, 10)
    '255'

    >>> convert_string('11111111', 2, 16)
    'FF'

    :param s:
    :param base:
    :return:
    """
    conv_table = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    conv_table.update({str(i): i for i in range(11)})

    rev_table = {str(v): k for k, v in conv_table.items()}

    s = [conv_table[c] for c in s]

    decimal = 0

    for p, d in enumerate(reversed(s)):
        decimal += (source_base ** p) * d

    target = []
    while decimal > 0:
        target.insert(0, rev_table[str(decimal % target_base)])
        decimal = decimal // target_base

    return ''.join(target)


def find_day_of_date(dt):
    """
    >>> find_day_of_date('2020/04/19')
    Sunday

    :param dt:
    :return:
    """
    dt = datetime.datetime.strptime(dt, '%Y/%m/%d')
    print(dt.strftime('%A'))

def replace_string(s):
    """
    >>> replace_string('a70 and z72 will be replaced, but aa24 and a872 will not')
    '*** and *** will be replaced, but aa24 and a872 will not'

    :param s:
    :return:
    """
    s = re.sub('[\s]\w\d{2}\s', ' *** ', s)
    s = re.sub('^\w\d{2}$', '***', s)
    return re.sub('^\w\d{2}', '***', s)

