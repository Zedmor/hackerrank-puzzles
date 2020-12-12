import sys

x, y, z = map(int, [sys.argv[i] for i in (1,2,3)])

substring1 = '-'.join(['la'] * x) 
whole_string = ' '.join([substring1 for i in range(y)])
whole_string += '!' if z == 1 else '.'

print('Everybody sing a song: ' + whole_string)
