import zipfile

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

with zipfile.ZipFile('channel.zip', 'r') as z:
    zips = z.infolist()
    files = {}
    for zip in zips:
        content = z.read(zip.filename).decode()
        files[before(zip.filename, '.txt')] = (content[content.rfind(
            ' ')+1:], bytes(zip.comment).decode())
    print(files)
    pointer = files['90052']
    while True:
        print(files[pointer[0]][1], end='')
        pointer = files[pointer[0]]
