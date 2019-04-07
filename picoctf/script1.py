string = "01110100 01101111 01111000 01101001 01100011"
for ch in string.split(' '):
    print(chr(int(ch, 2)), end='')

string = "636f6d7075746572"
for ch1,ch2 in string[::]:
    print(ch)
    print(chr(int(ch, 16)), end='')
