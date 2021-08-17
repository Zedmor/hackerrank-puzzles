import hashlib
import string


def generate_hashes(door_id):
    solution = [None] * 8
    index = 0
    while True:
        hash_of_value = hashlib.md5((door_id + str(index)).encode())
        digest = hash_of_value.hexdigest()
        if digest.startswith('00000'):
            position = digest[5]
            value = digest[6]
            try:
                position = int(position)
                if 0 <= position <= 7 and solution[position] is None:
                    solution[position] = value
                    print(solution)
                    if all([v is not None for v in solution]):
                        return ''.join(solution)
            except ValueError:
                pass

        index += 1


def find_password(door_id):
    generator = generate_hashes(door_id)
    result = []
    for i in range(8):
        found_hash = next(generator)
        print(found_hash)
        result.append(found_hash[5])
    return ''.join(result)


def test_find_password():
    door_id = 'abc'
    assert generate_hashes(door_id) == '05ace8e3'


def test_find_password_real():
    door_id = 'reyedfim'
    assert generate_hashes(door_id) == '18f47a30'
