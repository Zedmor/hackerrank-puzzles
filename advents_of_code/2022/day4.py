class Range:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def includes(self, other: "Range"):
        return other.start >= self.start and other.end <= self.end

    def overlap(self, other: "Range"):
        return not(other.start > self.end or other.end < self.start)


def part1():
    counter = 0
    with open("day4.txt") as inp_file:
        for line in inp_file:
            line = line.strip()
            first, second = line.split(',')
            r1 = Range(*first.split('-'))
            r2 = Range(*second.split('-'))
            if r1.overlap(r2) or r2.overlap(r1):
                counter += 1
    return counter



def test_part1():
    assert part1() == 2