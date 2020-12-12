import re

rules = {}

with open('input-12.txt') as f:
    initial_state = f.readline().lstrip('initial state: ')
    f.readline()
    for line in f:
        values = re.findall('(.*) => (.)', line)[0]
        rules[values[0]] = values[1]


initial_state = list(initial_state.rstrip())

n_add = len(initial_state) * 100

additional_pots = list('.' * n_add)

initial_state += additional_pots

indexes = range(-len(additional_pots), len(initial_state))

plantation = additional_pots + initial_state

# print(list(zip(indexes, plantation)))


# print(rules)

r1 = 0
r2 = 0

sim_gen = 50000000000

for generation in range(2000):
    plants = []
    for i in range(0, len(plantation) - 5):
        segment = ''.join(plantation[i:i + 5])
        if rules[segment] == '#':
            plants.append(i+2)
    plantation = list('.' * len(plantation))
    for plant in plants:
        plantation[plant] = '#'
    # print(''.join(plantation))
    result = [t[0] for t in filter(lambda t: t[1] == '#', zip(indexes, plantation))]
    s = sum(result)
    r1 = r2
    r2 = s
    print(generation, s, r2 - r1)
    if generation > 150:
        print(generation, s, r2 - r1)
        print((generation - 150) * 22 + 3833)
        # print(''.join(plantation))
        # break



