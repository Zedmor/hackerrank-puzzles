import re
from collections import namedtuple, defaultdict
from math import ceil

Element = namedtuple('Element', ('name', 'amount'))

def parse(capture):
    return [Element(i.split()[1], int(i.split()[0])) for i in capture]


def make_recepie(sources, target, amount):
        return {frozenset(sources): Element(target, amount)}


class RecepieCollection:
    def __init__(self, recipes):
        self.recipes = recipes
        self.sources = {v.name: k for k, v in recipes.items()}
        self.storage = defaultdict(int)

    def __repr__(self):
        return str(self.recipes)

    def get_sources(self, target, amount):
        sources = self.sources[target]
        coeff = ceil(amount / self.recipes[sources].amount)
        residual = self.recipes[sources].amount * coeff - amount
        self.storage[target] += residual
        return [Element(e.name, e.amount * coeff) for e in sources]


def read_recipes(file_name):
    rec = {}

    with open(file_name) as rec_file:
        for line in rec_file.readlines():
            r = "(\d+\s\w+)+"
            capture = re.findall(r, line)
            capture = parse(capture)
            sources, target = capture[:-1], capture[-1]
            rec.update(make_recepie(sources, *target))

    return RecepieCollection(rec)


coll = read_recipes('day14.txt')

# print(coll)
# print(coll.sources)



start = 1639375
tril = 1000000000000

while True:
    stack = coll.get_sources('FUEL', start)

    counter = 0

    while stack:
        # print(stack)
        el = stack.pop()
        if el.name == 'ORE':
            counter += el.amount
        else:
            element, amount = el
            taking_this_much = 0
            if coll.storage[element] > 0:
                taking_this_much = min(amount, coll.storage[element])
                coll.storage[element] -= taking_this_much
            stack.extend(coll.get_sources(element, amount - taking_this_much))

    if counter <= tril:
        print(start)
        break
    else:
        print(counter)
        start -= 1





print(counter)
print(tril)

# while stack:
#
#


