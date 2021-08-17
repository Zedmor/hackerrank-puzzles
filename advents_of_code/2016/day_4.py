import collections
import re
from collections import Counter


def patched_most_common(self, n):
    return sorted(self.bots(), key=lambda x: (-x[1], x[0]))[:n]


Counter.most_common = patched_most_common


def parse(room, delete_dashes=True):
    parsed = re.findall(r'((([a-z]+\-))+)(\d+)\[([a-z]+)\]', room)[0]
    letters = parsed[0]
    if delete_dashes:
        letters = parsed[0].replace('-', '')
    sector_id = parsed[-2]
    checksum = parsed[-1]
    return letters, sector_id, checksum


def room_checker(room):
    letters, sector_id, checksum = parse(room)
    c = Counter(letters)
    most_common = ''.join(item[0] for item in c.most_common(5))
    return int(sector_id) if most_common == checksum else 0


def calc_sum(rooms):
    return sum(room_checker(r) for r in rooms)


def decrypt(letters, sector_id):
    letters = list(letters)
    for i in range(int(sector_id)):
        for j in range(len(letters)):
            if letters[j].islower():
                v = ord(letters[j])
                v += 1
                if v > ord('z'):
                    v = ord('a')
                letters[j] = chr(v)
    return ''.join(letters)


def test_decrypt():
    assert decrypt("qzmt-zixmtkozy-ivhz", 343) == "very-encrypted-name"


def test_real_data():
    with open("day_4.txt") as inp_file:
        rooms = inp_file.readlines()
        assert calc_sum(rooms) == 185371
        for room in rooms:
            if room_checker(room):
                letters, sector_id, checksum = parse(room, delete_dashes=False)
                print(decrypt(letters, sector_id), sector_id)


def test_cal_sum():
    rooms = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]"
        ]
    assert calc_sum(rooms) == 1514


def test_room_checker():
    assert room_checker("aaaaa-bbb-z-y-x-123[abxyz]")
    assert room_checker("a-b-c-d-e-f-g-h-987[abcde]")
    assert room_checker("not-a-real-room-404[oarel]")
    assert not room_checker("totally-real-room-200[decoy]")
