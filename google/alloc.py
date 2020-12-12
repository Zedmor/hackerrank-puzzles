def calc_bus_route(n, d, items):

    cursor_col = n - 1
    cussor_row = d

    while cursor_col >= 0:
        while cussor_row > 0:
            if cussor_row % items[cursor_col] == 0:
                cursor_col -= 1
            else:
                cussor_row -= items[cursor_col]

            if cursor_col == -1:
                return cussor_row



assert calc_bus_route(3, 10, [3, 7, 2]) == 6
assert calc_bus_route(4, 100, [11, 10, 5, 50]) == 99
assert calc_bus_route(1, 1, [1]) == 1

t = int(input())

for i in range(1, t + 1):  # Number of cases
    n, d = [int(s) for s in input().split(" ")]

    items = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    result = calc_bus_route(n, d, items)

    print("Case #{}: {}".format(i, result))
    # check out .format's specification for more formatting options
