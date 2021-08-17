import re
from functools import reduce
from operator import mul
from typing import List


class Item:

    def __repr__(self):
        return f"I am item {self.id} with items {self.chips}"

    def __init__(self, id):
        self.id = id
        self.chips = []


class Output(Item):
    def __init__(self, id):
        super().__init__(id)


class Bot(Item):
    def __repr__(self):
        return f"I am bot {self.id} with items {self.chips}"

    def __init__(self, id):
        super().__init__(id)
        self.low: Item = None
        self.high: Item = None


class Factory:

    def __init__(self):
        self.bots: dict = {}
        self.bins: dict = {}
        self.result = None

    def step(self, target):
        found = False
        for bot in self.bots.values():
            if len(bot.chips) == 2:
                found = True
                low, high = sorted(bot.chips)
                bot.chips = []
                bot.low.chips.append(low)
                bot.high.chips.append(high)

        if not found:
            self.result = -1


    @staticmethod
    def builder(rules):
        f = Factory()
        for rule in rules:
            if 'value' in rule:
                v, b = re.findall('\d+', rule)
                bot = f.bots.setdefault(int(b), Bot(int(b)))
                bot.chips.append(int(v))
            elif 'gives' in rule:
                groups = re.findall("bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", rule)[0]
                b, item_type_l, l, item_type_h, h = groups
                bot = f.bots.setdefault(int(b), Bot(int(b)))
                if item_type_l == 'bot':
                    bot.low = f.bots.setdefault(int(l), Bot(int(l)))
                else:
                    bot.low = f.bins.setdefault(int(l), Output(int(l)))

                if item_type_h == 'bot':
                    bot.high = f.bots.setdefault(int(h), Bot(int(h)))
                else:
                    bot.high = f.bins.setdefault(int(h), Output(int(h)))

        return f



def test_example():
    example = """
    value 5 goes to bot 2
    bot 2 gives low to bot 1 and high to bot 0
    value 3 goes to bot 1
    bot 1 gives low to output 1 and high to bot 0
    bot 0 gives low to output 2 and high to output 0
    value 2 goes to bot 2
    """
    f = Factory.builder(example.split('\n'))

    while not f.result:
        f.step({5, 2})
    assert f.result == 2


def test_real():
    with open("day_10.txt") as inp_file:
        f = Factory.builder(inp_file.readlines())

    step = 0
    while not f.result:
        print(f'Step {step}')
        f.step({61, 17})
        step += 1
    v = 1
    for bin in (0, 1, 2):
        v *= reduce((lambda x, y: x * y), f.bins[bin].chips)
    print(v)
    assert f.result == 2


