from collections import defaultdict

costs = {"addx": 2, "noop": 1}

class Timer:

    # measurments = [20, 60, 100, 140, 180, 220]
    measurments = [40, 80, 120, 160, 200, 240]

    def __init__(self):
        self.sum_of_signals = 0
        self.state = 0

    def click(self, registers):

        if abs(registers["x"] - self.state % 40) < 2:
            print('#', end='')
        else:
            print('.', end='')
        if self.state in self.measurments:
            print()
        self.state += 1
            # self.sum_of_signals += registers["x"] * self.state

    def run(self, x, registers):
        for i in range(x):
            self.click(registers)


def main():
    print()
    with open("day10.txt") as commands:
        timer = Timer()
        registers = defaultdict(int)
        registers["x"] = 1
        for line in commands:
            line = line.rstrip()
            command = line.split(" ")
            timer.run(costs[command[0]], registers)
            if command[0] == "addx":
                registers["x"] += int(command[1])
    return timer.sum_of_signals


def test_main():
    assert main() == 13140