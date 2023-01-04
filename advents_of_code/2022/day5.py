import re
from collections import namedtuple


class Stack:
    pass


class State:
    def __init__(self, stream):
        self.stacks = [[] for i in range(11)]
        for line in stream:
            line = line.strip('\n')
            if '123' in line.replace(' ', ''):
                # We are done with creating state
                break
            for i, c in enumerate(line):
                if c.isupper():
                    self.stacks[(i - 1) // 4 + 1].insert(0, c)

    def __len__(self):
        return sum(int(len(s) > 0) for s in self.stacks)


Command = namedtuple("Command", ("amount", "from_", "to"))


class Commands:
    def __init__(self, stream):
        self.commands = []
        next(stream)
        for line in stream:
            line = line.strip('\n')
            a, b, c = map(int, re.findall("\d+", line))
            self.commands.append(Command(amount=a, from_=b, to=c))

    def __len__(self):
        return len(self.commands)

    def __iter__(self):
        return iter(self.commands)


def read_file(filename):
    with open(filename) as inp_file:
        state = State(inp_file)
        commands = Commands(inp_file)

    return state, commands


def part1():
    state, commands = read_file("day5.txt")
    for command in commands:
        state.stacks[command.to].extend(list(reversed(
            list(reversed(state.stacks[command.from_]))[:command.amount])))
        state.stacks[command.from_] = state.stacks[command.from_][:-command.amount]
    return ''.join([stack[-1] for stack in state.stacks if stack])


def test_part1():
    assert part1() == "CMZ"


def test_read_state():
    state, commands = read_file("day5.txt")

    assert len(state) == 3
    assert state
    assert len(commands) == 4
