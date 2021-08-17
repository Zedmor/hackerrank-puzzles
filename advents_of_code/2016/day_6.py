from collections import Counter


def decode(messages):
    solution = []
    for all_letters in zip(*messages):
        solution.append(Counter(all_letters).most_common()[-1][0])
    return ''.join(solution)


def test_messages():
    messages = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar"
        ]
    assert decode(messages) == "advent"


def test_real_messages():
    with open("day_6.txt") as inp_file:
        assert decode(inp_file.readlines()) == "z"