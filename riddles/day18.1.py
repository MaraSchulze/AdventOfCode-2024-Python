from get_input import get_input, get_test_input
import sys


def rec(i, j, steps, d, field):
	if not (0 <= i < len(field) and 0 <= j < len(field[0])):
		return
	if field[i][j] == "#":
		return
	if (i, j) in d and d[(i, j)] <= steps:
		return
	else:
		d[(i, j)] = steps
	rec(i - 1, j, steps + 1, d, field)
	rec(i + 1, j, steps + 1, d, field)
	rec(i, j - 1, steps + 1, d, field)
	rec(i, j + 1, steps + 1, d, field)
	

# extract input
inp = get_input(__file__)
field = [["." for _ in range(71)] for _ in range(71)]
for i in range(1024):
	line = inp[i]
	x, y = map(int, line.split(","))
	field[y][x] = "#"

# compute path length
sys.setrecursionlimit(5100)
d = {}
rec(0, 0, 0, d, field)
result = d[(len(field) - 1, len(field[0]) - 1)]

# print result
print(result)
