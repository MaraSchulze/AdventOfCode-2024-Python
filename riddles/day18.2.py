from get_input import get_input, get_test_input
import sys


def rec(i, j, d, field):
    if not (0 <= i < len(field) and 0 <= j < len(field[0])):
        return False
    if field[i][j] == "#":
        return False
    if i == len(field) - 1 and j == len(field[0]) - 1:
        return True
    if field[i][j] == "x":
        if (i, j) in d:
            return d[(i, j)]
        else:
            return False
        
    field[i][j] = "x"
    is_way = rec(i - 1, j, d, field) or \
        rec(i + 1, j, d, field) or \
        rec(i, j - 1, d, field) or \
        rec(i, j + 1, d, field)
    d[(i, j)] = is_way

    return is_way
    

def clear_field(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "x":
                field[i][j] = "."


# extract input
inp = get_input(__file__)
length, first_bytes = 71, 1024
field = [["." for _ in range(length)] for _ in range(length)]

# set first bytes
for i in range(first_bytes):
    line = inp[i]
    x, y = map(int, line.split(","))
    field[y][x] = "#"

# iterate over rest
sys.setrecursionlimit(5100)

d = {}
for i in range(first_bytes, len(inp)):
    line = inp[i]
    x, y = map(int, line.split(","))
    field[y][x] = "#"
    d.clear()
    is_way = rec(0, 0, d, field)
    clear_field(field)
    if not is_way:
        result = line
        break

# print result
print(result)
