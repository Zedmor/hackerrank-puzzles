from abc import ABC


class Figure(ABC):

    @classmethod
    def from_you(cls, code):
        for subcls in cls.__subclasses__():
            if subcls.you == code:
                return subcls()

    @classmethod
    def from_opponent(cls, code):
        for subcls in cls.__subclasses__():
            if subcls.opponent == code:
                return subcls()

    def play(self, f: "Figure"):
        if self < f:
            return self.score
        if self == f:
            return self.score + 3
        if self > f:
            return self.score + 6

    def select(self, target):
        for option in Figure.__subclasses__():
            if target == "X" and self > option():
                return option()
            if target == "Y" and self == option():
                return option()
            if target == "Z" and self < option():
                return option()



class Rock(Figure):

    score = 1

    opponent = "A"
    you = "X"

    def __gt__(self, other):
        return isinstance(other, Scissors)

    def __eq__(self, other):
        return isinstance(other, Rock)

    def __lt__(self, other):
        return isinstance(other, Paper)


class Paper(Figure):

    score = 2
    opponent = "B"
    you = "Y"

    def __gt__(self, other):
        return isinstance(other, Rock)

    def __eq__(self, other):
        return isinstance(other, Paper)

    def __lt__(self, other):
        return isinstance(other, Scissors)


class Scissors(Figure):

    score = 3
    opponent = "C"
    you = "Z"

    def __gt__(self, other):
        return isinstance(other, Paper)

    def __eq__(self, other):
        return isinstance(other, Scissors)

    def __lt__(self, other):
        return isinstance(other, Rock)


def test_creation():

    f = Figure.from_you("X")
    assert isinstance(f, Rock)
    assert isinstance(Figure.from_opponent("C"), Scissors)


def test_comparison():

    assert Rock() > Scissors()
    assert Rock() == Rock()
    assert Rock() < Paper()


def main():
    total = 0
    with open("day2.txt") as inp_file:
        for line in inp_file.readlines():
            a, b = line.strip().split(' ')
            opp = Figure.from_opponent(a)
            you = opp.select(b)
            total += you.play(opp)
        return total


def test_main():
    assert main() == 13682
