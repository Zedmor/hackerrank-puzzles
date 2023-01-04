from collections import namedtuple

File = namedtuple("File", ("name", "size"))
Directory = namedtuple("Directory", ("name", "content"))


def process(line, dir_stack, stream):
    if line.startswith('$'):
        if '$ cd /' in line:
            if not dir_stack:
                dir_stack.append(Directory('/', content=[]))
            else:
                dir_stack = [dir_stack[0]]

            return

        if line.startswith('$ cd'):
            new_dir_name = line.replace("$ cd ", "")
            if new_dir_name == "..":
                dir_stack.pop()
            else:
                for item in dir_stack[-1].content:
                    if item.name == new_dir_name:
                        dir_stack.append(item)
                        break
                else:
                    new_directory = Directory(name=new_dir_name, content=[])
                    dir_stack[-1].content.append(new_directory)
                    dir_stack.append(new_directory)
        if line.startswith('$ ls'):
            for new_line in stream:
                new_line = new_line.strip('\n')
                if new_line.startswith("$"):
                    process(new_line, dir_stack, stream)
                elif new_line.startswith("dir"):
                    dir_stack[-1].content.append(
                        Directory(name=new_line.replace("dir ", ""),
                                  content=[]))
                else:
                    size, name = new_line.split(' ')
                    dir_stack[-1].content.append(
                        File(name=name, size=int(size))
                        )

sizes = []


def find_by_size(structure, max_size):
    if isinstance(structure, File):
        return structure.size
    result = sum([find_by_size(s, max_size) for s in structure.content])
    if result <= max_size:
        if structure.name in sizes:
            raise RuntimeError
        sizes.append(result)
    return result


def main():
    dir_stack = []
    with open("day7.txt") as inp_file:
        for line in inp_file:
            line = line.rstrip('\n')
            process(line, dir_stack, inp_file)

    total_occupied = find_by_size(dir_stack[0], float('inf'))
    need_to_free = 30000000 - (70000000 - total_occupied)
    sizes.sort()

    for item in sizes:
        if item >= need_to_free:
            return item


def test_main():
    assert main() == 95437


def test_find_by_size():
    structure = Directory("/",
                          content=[Directory("a",
                                             content=[
                                                 File("b", size=5)
                                                      ]
                                             ),
                                   File("c", size=3)
                                   ]
                          )

    assert find_by_size(structure, 100) == 8