from functools import reduce


def add_binary_nums(x, y):
    x = x.replace(' ', '')
    y = y.replace(' ', '')
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0: result = '1' + result

    return result.zfill(max_len)


def decode_binary_string(s):
    return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))


nums = ['00100000 00101100 00101001 00101100',
        '00100000 00110000 00100000 00100000',
        '00100000 00110000 00110000 00100000',
        '01100000 00110000 01110000 01100000',
        '01100001 00100000 00100000 00100000']

a = 0
z = ''
for element in nums:
    for char in element.split(" "):
        # print(a)
        a += 1
        z += decode_binary_string(char)
        if a %4==0:
            print(z[::-1],end='')
            z=''

print()

result = reduce(add_binary_nums, nums)
print(result)
pre, result = result[:1], result[1:]
# pre = ''
print(pre + ' ' + ' '.join([result[i:i + 8] for i in range(0, len(result), 8)]))
