import json
import re

def process_object(object):
    if type(object) == list:
        for element in object:
            yield from process_object(element)
    elif type(object) == dict:
        if 'red' not in object.values():
            for value in object.values():
                yield from process_object(value)
    else:
        try:
            a = int(object)
            yield a
        except ValueError:
            pass


def sum_numbers(text):
    """
    >>> sum_numbers('[1,2,3]')
    6
    >>> sum_numbers('{"a":2,"b":4}')
    6
    >>> sum_numbers('[[[3]]]')
    3
    >>> sum_numbers('{"a":{"b":4},"c":-1}')
    3
    >>> sum_numbers('[1,{"c":"red","b":2},3]')
    4
    >>> sum_numbers('{"d":"red","e":[1,2,3,4],"f":5}')
    0
    >>> sum_numbers('[1,"red",5]')
    6

    """
    object = json.loads(text)
    # print(list(process_object(object)))
    return sum(process_object(object))


def main():
    """
    >>> main()
    None
    """
    text = open('input-12.txt').readline()
    print(sum_numbers(text))
