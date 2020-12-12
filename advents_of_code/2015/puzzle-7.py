import re
from collections import defaultdict
from enum import Enum

graph = {}
operations = {}
sources = defaultdict(list)


class Operation(Enum):
    AND = 0
    OR = 1
    LSHIFT = 2
    RSHIFT = 3
    NOT = 4


def parse_edge(line):
    """
    >>> parse_edge('asdas -> 4454')
    """
    cmd = re.findall('(.+) -> (.+)', line)[0]
    target = cmd[1]
    and_or = re.findall('(.+) (AND|OR|RSHIFT|LSHIFT) (.+)', cmd[0])
    _not = re.findall('NOT (.+)', cmd[0])
    direct = re.findall('.+', cmd[0])
    if and_or:
        and_or = and_or[0]
        operation = (and_or[0], Operation.__getattr__(and_or[1]), and_or[2])

    elif _not:
        operation = (Operation.NOT, _not[0])
    elif direct:
        try:
            operation = int(direct[0])
        except ValueError:
            operation = direct[0]
    else:
        raise ValueError(line)

    graph[target] = operation
    operations[operation] = target
    try:
        line_sources = [s for s in operation if type(s) != Operation]
        for source in line_sources:
            sources[source].append((operation, target))
    except TypeError:
        pass


def search(param):
    try:
        return int(param)
    except ValueError:
        return int(graph[param])


def resolve(operation):
    if type(operation) == int:
        return operation

    if Operation.NOT in operation:
        return ~search(operation[1])
    elif Operation.LSHIFT in operation:
        return search(operation[0]) << search(operation[2])
    elif Operation.RSHIFT in operation:
        return search(operation[0]) >> search(operation[2])
    elif Operation.AND in operation:
        return search(operation[0]) & search(operation[2])
    elif Operation.OR in operation:
        return search(operation[0]) | search(operation[2])
    else:
        raise ValueError(operation)


def solve_graph():
    solved = False
    while type(graph['a'] != int):
        solved = True
        stack = [(key, val) for key, val in graph.items() if type(val) is int]
        if len(stack) == 338:
            # print([(key, val) for key, val in graph.items() if type(val) != int])
            print(graph['lx'])
            break
        # print(len(stack))
        while stack:
            source = stack.pop()
            new_list = []
            for operation, target in sources[source[0]]:
                if source[0] == 'b':
                    if type(operation) == tuple and 'b' in operation:
                        operation = tuple(op if op != 'b' else 956 for op in operation)
                        print(operation)
                try:
                    resolved_operation = resolve(operation)
                    if resolved_operation < 0:
                        resolved_operation += 2**16
                    # operations[operation] = resolved_operation
                    # graph[source[0]]
                    new_list.append((resolved_operation, target))
                    graph[target] = resolved_operation
                    if target == 'a':
                        print(resolved_operation)
                except (ValueError, TypeError, UnboundLocalError) as e:
                    new_list.append((operation, target))
                    solved = False
            sources[source[0]] = new_list
    # print(graph['a'])

    # print(operation)
    # print(operations)


def main():
    """
    >>> main()
    """
    with open('input-7.txt') as file:
        for line in file.readlines():
            parse_edge(line)
    solve_graph()

    # print(graph)

if __name__ == "__main__":
    main()
