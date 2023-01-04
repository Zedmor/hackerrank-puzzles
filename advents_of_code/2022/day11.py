import math
import re
from decimal import Decimal
from functools import partial


def build_funcion(function_string):
    def eval_function(old):
        loc = {"old": old}
        exec(function_string, globals(), loc)
        return loc["new"]
    return eval_function


def is_not_prime(n):
    if n <= 1:
        return True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True

    return False


def monkey_test(n, x):
    return int(x) % int(n) == 0


supermodulo = math.prod([7, 17, 11, 13, 19, 2, 5, 3])


class Monkey:

    def __init__(self, id_, items, operation, test, if_true, if_false):
        self.id = id_
        self.items = items
        self.test = test
        self.operation = operation
        self.if_true_monkey = int(if_true)
        self.if_false_monkey = int(if_false)
        self.inspection_counter = 0

    @classmethod
    def from_definition(cls, definition):
        """
        Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        """
        id_ = int(re.findall('\d+', definition[0])[0])
        items = [int(i) for i in re.findall('\d+', definition[1])]
        operation = build_funcion(definition[2].replace('Operation: ', '').strip())
        n = re.findall('\d+', definition[3])[0]
        test = partial(monkey_test, int(n))
        if_true = re.findall('\d+', definition[4])[0]
        if_false = re.findall('\d+', definition[5])[0]
        return cls(id_, items, operation, test, if_true, if_false)


class Zoo:

    def __init__(self):
        self.monkeys = []
        self.round = 0

    def play_all(self):
        while self.round < 10000:
            if self.round % 100 == 0:
                print(f"Round: {self.round}")
            self.play()
            self.round += 1

    def play(self):
        for monkey in self.monkeys:
            while monkey.items:
                item = monkey.items.pop()
                monkey.inspection_counter += 1
                item = monkey.operation(item)
                # item = item // 3
                item %= supermodulo
                if monkey.test(item):
                    self.monkeys[monkey.if_true_monkey].items.append(item)
                else:
                    self.monkeys[monkey.if_false_monkey].items.append(item)

    def result(self):
        monkeys = sorted(self.monkeys, key=lambda m: m.inspection_counter, reverse=True)
        return monkeys[0].inspection_counter * monkeys[1].inspection_counter


def split(l):
    collector = []
    for item in l:
        if item:
            collector.append(item)
        else:
            yield collector
            collector = []
    yield collector

def main():
    with open("day11.txt") as inp_file:
        data = inp_file.read().splitlines()
        zoo = Zoo()
        for source in split(data):
            monkey = Monkey.from_definition(source)
            zoo.monkeys.append(monkey)
    zoo.play_all()
    return zoo.result()

def test_main():
    assert main() == 2713310158