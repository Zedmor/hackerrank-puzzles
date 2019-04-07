import re
from collections import defaultdict


class Ingridient(object):
    def __init__(self, ingridient_record):
        self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories = ingridient_record

    def __repr__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, " \
               f"Durability: {self.durability}, Texture: {self.texture}, Calories: {self.calories}\n"


def line_parser(line):
    """
    >>> line_parser('Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2\\n')
    ['Sugar', '3', '0', '0', '-3', '2']
    """
    tokens = list(re.findall(
        '(\w+): capacity ([-+]?[0-9]*\.?[0-9]+), durability ([-+]?[0-9]*\.?[0-9]+), flavor ([-+]?[0-9]*\.?[0-9]+), texture ([-+]?[0-9]*\.?[0-9]+), calories (\d+)\\n',
        line)[0])
    return tokens


def calculate_cookie_score(ingridients, amounts):
    """
    >>> bscotch = Ingridient(("Butterscotch", -1, -2, 6, 3, 8))
    >>> cinnamon = Ingridient(("Cinnamon", 2, 3, -2, -1, 3))
    >>> calculate_cookie_score([bscotch, cinnamon],[44,56])
    62842880
    """
    assert len(ingridients) == len(amounts)
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for ing, amnt in zip(ingridients, amounts):
        capacity += ing.capacity * amnt
        durability += ing.durability * amnt
        flavor += ing.flavor * amnt
        texture += ing.texture * amnt
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)
    return capacity * durability * flavor * texture


def main():
    """
    >>> main()
    None
    """
    scores = defaultdict(int)
    lines = open('input-15.txt').readlines()
    ingridients = map(Ingridient, map(line_parser, lines))
    print(list(ingridients))
