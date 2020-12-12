import sys


def find_freq(iterator):
    current = 0
    all_fr = {0}
    while True:
        print("Iteration")
        for line in iterator:
            v = int(line)
            print(v)
            # print(all_fr)
            # print(current, v)
            current += v
            if current in all_fr:
                print(current)
                break
            else:
                all_fr.add(current)

with open('input-1.txt') as f:
    current = 0
    all_fr = {0}
    while True:
        f.seek(0)
        print("Iteration")
        for line in f:
            v = int(line)
            # print(all_fr)
            # print(current, v)
            current += v
            if current in all_fr:
                print(current)
                sys.exit(0)
            else:
                all_fr.add(current)

# print(find_freq([+3, 3,4,-2,-4]))
