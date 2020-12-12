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

    def __init__(self, program, opt_input=None, wait_for_input=False):

        self.wait_for_input = wait_for_input

        self.input_address = 0

        self.need_input = False

        self.program = program

        self.program.extend([0] * 100000)

        if opt_input:
            self.inputs = opt_input
        else:
            self.inputs = []

        self.terminated = False

        self.cursor = 0

        self.outputs = []

        self.relative = 0

    def run_software(self):

        if not self.inputs and self.wait_for_input and self.need_input:
            raise ValueError('Provide input')

        if self.need_input:
            self.program[self.input_address] = self.inputs.pop()
            self.need_input = False


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

            print(self.cursor, op)
            self.cursor += self.shifts[op]

            if op == '1':
                self.program[ad[2]] = self.program[ad[0]] + self.program[ad[1]]
            if op == '2':
                self.program[ad[2]] = self.program[ad[0]] * self.program[ad[1]]
            if op == '3':
                try:
                    self.program[ad[0]] = self.inputs.pop()
                except IndexError:
                    self.need_input = True
                    self.input_address = ad[0]
                    if self.wait_for_input:
                        raise ValueError('Provide input')
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
