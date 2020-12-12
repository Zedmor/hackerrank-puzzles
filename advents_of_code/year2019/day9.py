from itertools import permutations

class Computer:

    shifts = {
        '1': 4,
        '2': 4,
        '3': 2,
        '4': 2,
        '5': 3,
        '6': 3,
        '7': 4,
        '8': 4,
        '9': 2
    }

    def __init__(self, opt_input=None, program=None):
        self.program = program

        self.program.extend([0] * 100000)

        if opt_input:
            self.inputs = [opt_input]

        self.terminated = False

        self.cursor = 0

        self.outputs = []

        self.relative = 0

    def run_software(self):

        while True:
            if self.program[self.cursor] == 99:
                self.terminated = True
                return

            preparsed_command = str(self.program[self.cursor]).rjust(5, '0')

            ad = []

            for pos, mode in enumerate(reversed(preparsed_command[:3])):
                ad.append({'0': self.program[pos + self.cursor + 1],
                           '1': self.cursor + pos + 1,
                           '2': self.program[pos + self.cursor + 1] + self.relative
                           }[mode])

            op = preparsed_command[-1]

            self.cursor += self.shifts[op]

            if op == '1':
                self.program[ad[2]] = self.program[ad[0]] + self.program[ad[1]]
            if op == '2':
                self.program[ad[2]] = self.program[ad[0]] * self.program[ad[1]]
            if op == '3':
                try:
                    self.program[ad[0]] = self.inputs.pop()
                except IndexError:
                    return
            if op == '4':
                self.outputs.append(self.program[ad[0]])
                return
            if op == '5':
                if self.program[ad[0]] != 0:
                    self.cursor = self.program[ad[1]]
            if op == '6':
                if self.program[ad[0]] == 0:
                    self.cursor = self.program[ad[1]]
            if op == '7':
                self.program[ad[2]] = 1 if int(self.program[ad[0]]) < int(self.program[ad[1]]) else 0
            if op == '8':
                self.program[ad[2]] = 1 if int(self.program[ad[0]]) == int(self.program[ad[1]]) else 0

            if op == '9':
                self.relative += self.program[ad[0]]


