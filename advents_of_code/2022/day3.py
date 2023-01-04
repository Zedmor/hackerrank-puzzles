import string


def priority(c):
    return (string.ascii_lowercase + string.ascii_uppercase).index(c) + 1


def part1(filename):
    priorities = 0
    with open(filename) as inp_file:
        for line in inp_file.readlines():
            line = line.strip()
            first, second = line[:len(line)//2], line[len(line)//2:]
            priorities += sum(priority(c) for c in set(first).intersection(set(second)))
    return priorities

def part2(filename):
    priorities = 0
    with open(filename) as inp_file:
        counter = 0
        buffer = []
        for line in inp_file.readlines():
            line = line.strip()
            buffer.append(set(line))
            counter += 1
            if counter == 3:
                priorities += priority(set.intersection(*buffer).pop())
                counter = 0
                buffer = []


    return priorities


def test_part1():
    assert part1("day3.txt") == 157

def test_part2():
    assert part2("day3.txt") == 70

def test_part2_full():
    assert part2("day3_full.txt") == 70

def test_part1_full():
    assert part1("day3_full.txt") == 7850

def test_priority():
    assert priority("p") == 16
    assert priority("L") == 38
    assert priority("v") == 22