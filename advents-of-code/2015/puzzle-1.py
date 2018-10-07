def process_char(char):
    return -1 if char == ')' else 1


with open('input-1.txt') as file:
    commands = file.readline()
    command_sequence = map(process_char, commands)
    total = 0
    for i, command in enumerate(command_sequence):
        total += command
        if total < 0:
            print(i + 1)
            break
