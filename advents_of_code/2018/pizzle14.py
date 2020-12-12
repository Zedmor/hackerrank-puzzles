def run_sequence(seed):
    pointer1 = 0
    pointer2 = 1

    target = '286051'

    while True:
        new_recepie = seed[pointer1] + seed[pointer2]
        seed += [int(d) for d in str(new_recepie)]
        pointer1 += (1 + seed[pointer1])
        pointer1 = pointer1 % len(seed)
        pointer2 += (1 + seed[pointer2])
        pointer2 = pointer2 % len(seed)
        if len(seed) >= len(target):
            t_str = ''.join(map(str, seed[len(seed) - len(target) - 2:]))
            if target in t_str:
                print(''.join(map(str, seed)).index(target))
                break


def main():
    seed = [3, 7]
    run_sequence(seed)


if __name__ == '__main__':
    main()
