import re

import pytest
from pytest import mark


def decompress(text):
    text = list(text)
    result = []
    while text:
        if text[0] != '(':
            result.append(text.pop(0))
        else:
            end_marker = text.index(')')
            marker, text = text[:end_marker + 1], text[end_marker + 1:]
            first, second = re.findall(r"(\d+)x(\d+)", ''.join(marker))[0]
            cutout, text = text[:int(first)], text[int(first):]
            for _ in range(int(second)):
                result.extend(list(cutout))

            print(marker)

    return ''.join(result)


def decompress_2(text):
    text = list(text)
    result = 0
    while text:
        if text[0] != '(':
            text.pop(0)
            result += 1
        else:
            end_marker = text.index(')')
            marker, text = text[:end_marker + 1], text[end_marker + 1:]
            first, second = re.findall(r"(\d+)x(\d+)", ''.join(marker))[0]
            cutout, text = text[:int(first)], text[int(first):]
            result += int(second) * decompress_2(cutout)

    return result


@mark.parametrize("inp, target",
             (
                 ("ADVENT", 6),
                 ("A(1x5)BC", 7),
                 ("(3x3)XYZ", 9),
                 ("A(2x2)BCD(2x2)EFG", 11),
                 ("(6x1)(1x3)A", 6),
                 ("X(8x2)(3x3)ABCY", 18)
             ))
def test_inputs(inp, target):
    assert len(decompress(inp)) == target


@mark.parametrize("inp, target",
             (
                 ("(3x3)XYZ", len("XYZXYZXYZ")),
                 ("X(8x2)(3x3)ABCY", len("XABCABCABCABCABCABCY")),
                 ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
                 ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
             ))
def test_decompress_2(inp, target):
    assert decompress_2(inp) == target


def test_puzzle_input():
    with open("day_9.txt") as inp_file:
        line = inp_file.read()
        # print(len(decompress(line)))
        print(decompress_2(line))


