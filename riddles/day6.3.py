from get_input import get_input, get_test_input
from itertools import combinations


def get_start():
	for i in range(len(mymap)):
		for j in range(len(mymap[0])):
			if mymap[i][j] == "^":
				return (i, j)
	return None

def step(i, j, direction):
	a, b = direction
	return (i + a, j + b)

def right(direction):
	if direction == N:
		new_dir = E 
	elif direction == E:
		new_dir = S 
	elif direction == S:
		new_dir = W
	else:
		new_dir = N 
	a, b = new_dir
	return new_dir

def inbounds(x, y):
	return 0 <= x < len(mymap) and 0 <= y < len(mymap[0])

def get_next_obst(i, j):
	result = []
	for o in path:
		node, obst = o[0], o[1]
		if node == (i, j):
			result.append(obst)
	return result

# extract input
inp = get_input(__file__)
mymap = [list(line) for line in inp]

# global vars
N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
start = get_start()
direction = N

# get path
i, j = get_start()
direction = N
path = []
while 0 <= i < len(mymap) and 0 <= j < len(mymap[0]):
	i, j = step(i, j, direction)
	if not (0 <= i < len(mymap) and 0 <= j < len(mymap[0])):
		break
	path.append(((i, j), step(i, j, N)))
	path.append(((i, j), step(i, j, S)))
	path.append(((i, j), step(i, j, W)))
	path.append(((i, j), step(i, j, E)))
	a, b = step(i, j, direction)
	if not (0 <= a < len(mymap) and 0 <= b < len(mymap[0])):
		break
	if mymap[a][b] == "#":
		direction = right(direction)

result = 0
cycle = set()
i, j = start
direction = N
test = 1
while inbounds(i, j):
	print(test)
	test += 1

	if inbounds(*step(i, j, direction)) and not(step(i, j, direction) == start and direction == W) and not(step(i, j, direction) == start and direction == W):
		test_i, test_j, test_dir = i, j, right(direction)

		next_obst = get_next_obst(i, j)
		next_obst = [x for x in next_obst if x != start]
		for obst in next_obst:
			o1, o2 = obst
			save = mymap[o1][o2]
			mymap[o1][o2] = "#"
			
			future = set((test_i, test_j, test_dir))
			while inbounds(test_i, test_j):
				a, b = step(test_i, test_j, test_dir)

				if inbounds(a, b) and mymap[a][b] == "#":
					test_dir = right(test_dir)

				test_i, test_j = step(test_i, test_j, test_dir)

				# if test_i == i and test_j == j:
				# 	test_dir = right(test_dir)

				if not inbounds(test_i, test_j):
					break

				if (test_i, test_j, test_dir) in cycle or (test_i, test_j, test_dir) in future:
					result += 1
					# print(i, j)
					break
				future.add((test_i, test_j, test_dir))

			mymap[o1][o2] = save
			cycle.add((i, j, direction))

	a, b = step(i, j, direction)

	i, j = step(i, j, direction)
	if not inbounds(i, j):
		break

	if inbounds(a, b) and mymap[a][b] == "#":
		direction = right(direction)

# print result
print(result)

# first turn!
# start is just in front
# end is special

