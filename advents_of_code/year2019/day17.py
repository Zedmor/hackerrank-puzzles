from pprint import pprint

from advents_of_code.common import Computer

with open('advents_of_code/2019/day17.txt') as data:
    program = list(map(int, data.read().split(',')))

c = Computer(program, wait_for_input=True)

while not c.terminated:
    c.run_software()

chars = ''.join([chr(code) for code in c.outputs]).split()

pprint(chars)

coll = 0


for y, row in enumerate(chars):
    for x, col in enumerate(row):
        try:
            if (chars[y][x] == '#'
                    and chars[y - 1][x] == '#'
                    and chars[y + 1][x] == '#'
                    and chars[y][x - 1] == '#'
                    and chars[y][x + 1] == '#'):
                coll += y * x
        except:
            pass

print(coll)
