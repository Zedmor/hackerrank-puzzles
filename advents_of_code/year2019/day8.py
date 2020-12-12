from itertools import permutations

class Amplifier:

    def __init__(self, phase_setting):
        self.program = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]

        # self.program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

        self.inputs = [phase_setting]

        self.terminated = False

        self.cursor = 0

        self.output = self.run_software()

    def run_software(self):

        # program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

        while True:

            if self.program[self.cursor] == 99:
                self.terminated = True
                return

            command = self.program[self.cursor]
            try:
                op1 = self.program[self.program[self.cursor + 1]]
            except IndexError:
                pass
            try:
                op2 = self.program[self.program[self.cursor + 2]]
            except IndexError:
                pass
            command = str(command)
            if len(command) == 3 and command[0] == '1':
                op1 = self.program[self.cursor + 1]
            if len(command) == 4:
                if command[1] == '1':
                    op1 = self.program[self.cursor + 1]
                if command[0] == '1':
                    op2 = self.program[self.cursor + 2]
            if len(command) >= 2:
                command = command[-1]
            if command == '1':
                self.program[self.program[self.cursor + 3]] = op1 + op2
                self.cursor += 4
            if command == '2':
                self.program[self.program[self.cursor + 3]] = op1 * op2
                self.cursor += 4
            if command == '3':
                try:
                    self.program[self.program[self.cursor + 1]] = self.inputs.pop(0)
                    self.cursor += 2
                except IndexError:
                    return
            if command == '4':
                self.cursor += 2
                self.output = op1
                return op1
            if command == '5':
                if op1 != 0:
                    self.cursor = op2
                else:
                    self.cursor += 3
            if command == '6':
                if op1 == 0:
                    self.cursor = op2
                else:
                    self.cursor += 3
            if command == '7':
                if int(op1) < int(op2):
                    self.program[self.program[self.cursor + 3]] = 1
                else:
                    self.program[self.program[self.cursor + 3]] = 0
                self.cursor += 4
            if command == '8':
                if int(op1) == int(op2):
                    self.program[self.program[self.cursor + 3]] = 1
                else:
                    self.program[self.program[self.cursor + 3]] = 0
                self.cursor += 4

seq = [5,6,7,8,9]

values = []

last_amp_signal = 0

for perm in list(permutations(seq)):
    amplifiers = [Amplifier(s) for s in perm]

    amplifiers[0].inputs.append(0)

    while not all([a.terminated for a in amplifiers]):
        for i, amp in enumerate(amplifiers):
            if amp.output is not None:
                if i < len(amplifiers) - 1:
                    amplifiers[i + 1].inputs.append(amp.output)
                else:
                    amplifiers[0].inputs.append(amp.output)
                last_amp_signal = amplifiers[-1].output if amplifiers[-1].output is not None else last_amp_signal
                amp.output = None

            amp.run_software()

    values.append(last_amp_signal)

print(max(values))
