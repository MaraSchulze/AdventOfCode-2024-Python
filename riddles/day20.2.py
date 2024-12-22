from get_input import get_input, get_test_input
from collections import Counter
import sys


def get_char(char, field):
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j] == char:
				return (i, j)
			

def number(i, j, nr, field):
	if field[i][j] == "#":
		return
	if type(field[i][j]) == int:
		return
	field[i][j] = nr
	number(i - 1, j, nr + 1, field)
	number(i + 1, j, nr + 1, field)
	number(i, j - 1, nr + 1, field)
	number(i, j + 1, nr + 1, field)


def make_next_step(i, j, step, field):
	if step == 0:
		return get_char(0, field)
	if field[i - 1][j] == step:
		return (i - 1, j)
	if field[i + 1][j] == step:
			return (i + 1, j)
	if field[i][j - 1] == step:
			return (i, j - 1)
	if field[i][j + 1] == step:
			return (i, j + 1)
	

def get_field(i, j, field):
	if 0 <= i < len(field) and 0 <= j < len(field[0]) and type(field[i][j]) == int:
		return field[i][j]
	else:
		return 0


def get_neighbours(i, j):
	result = set()
	result.add((i - 1, j))
	result.add((i + 1, j))
	result.add((i, j - 1))
	result.add((i, j + 1))
	return result


def apply_cheat(i, j, step, field):
	cheats = {}

	neighbours_old = get_neighbours(i, j)
	for cheat_length in range(2, 21):
		neighbours_new = set()
		for a,b in neighbours_old:
			current = get_neighbours(a, b)
			neighbours_new.update(current)
			for c, d in current:
				time = get_field(c, d, field)
				if time > step + cheat_length:
					if (i, j, c, d) in cheats:
						continue
					else:
						cheats[(i, j, c, d)] = time - step - cheat_length
		neighbours_old = neighbours_new
	
	return cheats


# set recursion depth higher
sys.setrecursionlimit(10000)

# get input
inp = get_input(__file__)
field = [list(line) for line in inp]

# prepare field
start_i, start_j = get_char("S", field)
end_i, end_j = get_char("E", field)
number(start_i, start_j, 0, field)

# try cheats
all_cheats = {}
race_time = field[end_i][end_j]

i, j = start_i, start_j
for step in range(race_time):
	i, j = make_next_step(i, j, step, field)
	cheats = apply_cheat(i, j, step, field)
	all_cheats.update(cheats)

times = [time for _, time in all_cheats.items()]
times_counter = Counter(times)

result = 0
for key in sorted(times_counter):
	if key >= 100:
		result += times_counter[key]

# print result
print(result)
