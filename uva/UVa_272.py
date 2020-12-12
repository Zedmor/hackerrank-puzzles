def solution(arg):
    opened = False
    out = []

    for char in arg:
        if char != '"':
            out.append(char)
        elif opened:
            out.append("''")
            opened = False
        else:
            out.append("``")
            opened = True

    return ''.join(out)
