import itertools
import re
from collections import defaultdict
from operator import attrgetter


class ComparableMixin(object):
    def _compare(self, other, method):
        try:
            return method(self._cmpkey(), other._cmpkey())
        except (AttributeError, TypeError):
            # _cmpkey not implemented, or return different type,
            # so I can't compare with "other".
            return NotImplemented

    def __lt__(self, other):
        return self._compare(other, lambda s,o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s,o: s <= o)

    def __eq__(self, other):
       return self._compare(other, lambda s,o: s == o)

    def __ge__(self, other):
        return self._compare(other, lambda s,o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s,o: s > o)

    def __ne__(self, other):
        return self._compare(other, lambda s,o: s != o)

class Deer(ComparableMixin):
    def __init__(self, deer_record):
        self.name, (self.speed, self.travel_time, self.timeout) = deer_record[0], list(map(int, deer_record[1:]))
        self.distance = 0
        self.staying = False
        self.timer = 0

    def _cmpkey(self):
        return self.distance

    def __repr__(self):
        return f"Deer {self.name} travelled {self.distance}"

    def go(self):
        if not self.staying:
            if self.timer < self.travel_time:
                self.distance += self.speed
                self.timer += 1
            else:
                self.staying = not self.staying
                self.timer = 1
        else:
            if self.timer < self.timeout:
                self.timer += 1
            else:
                self.staying = not self.staying
                self.distance += self.speed
                self.timer = 1


def line_parser(line):
    """
    >>> line_parser('Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.\\n')
    ['Vixen', '19', '7', '124']
    """
    tokens = list(re.findall('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.\\n',
                             line)[0])
    return tokens

def distance_calc(deer_record):
    deer = Deer(deer_record)
    for i in range(2504):
        deer.go()
    return deer.distance, deer.name


def find_winner_deer(deers):
    best_result = sorted(deers, key=attrgetter('distance'), reverse=True)[0].distance
    return filter(lambda deer: deer.distance == best_result, deers)


def main():
    """
    >>> main()
    None
    """
    scores = defaultdict(int)
    lines = open('input-14.txt').readlines()
    deer_records = list(map(line_parser, lines))
    deers = list(map(Deer, deer_records))
    for i in range(2504):
        [d.go() for d in deers]
        for deer in find_winner_deer(deers):
            scores[deer.name] += 1
    print(scores)


