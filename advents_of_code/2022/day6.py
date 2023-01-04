def marker(stream):
    cursor = 0
    chars = list(stream[cursor: cursor + 14])
    while cursor < len(stream) - 14:
        if len(set(chars)) == 14:
            return cursor + 14
        cursor += 1
        chars.pop(0)
        chars.append(stream[cursor + 13])


def test_streams():

    assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert marker("nppdvjthqldpwncqszvftbrmjlhg") == 6

    assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

def test_file():
    assert marker(open("day6.txt").readline()) == 5