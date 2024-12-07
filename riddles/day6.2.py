from get_input import get_input, get_test_input


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
	return new_dir


def inbounds(i, j):
	return 0 <= i < len(mymap) and 0 <= j < len(mymap[0])


def go():
	result = 0
	i, j = get_start()
	direction = N
	future = set()
	while inbounds(i, j):
		state = (i, j, direction)
		if state in future:
			result += 1
			break
		future.add(state)
		a, b = step(i, j, direction)
		if inbounds(a, b) and mymap[a][b] == "#":
			direction = right(direction)	
		c, d = step(i, j, direction)
		if inbounds(c, d) and mymap[c][d] == "#":
			direction = right(direction)	
		i, j = step(i, j, direction)
	return result

def get_positions():
	result = set()
	i, j = get_start()
	direction = N
	while inbounds(i, j):
		a, b = step(i, j, direction)
		if inbounds(a, b) and mymap[a][b] == "#":
			direction = right(direction)	
		c, d = step(i, j, direction)
		if inbounds(c, d) and mymap[c][d] == "#":
			direction = right(direction)	
		result.add((i, j))
		i, j = step(i, j, direction)
	return result


# global variables
N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
test = 1

# extract input
inp = get_input(__file__)
mymap = [list(line) for line in inp]

# get obstacle positions
positions = get_positions()
positions.remove(get_start())

result = 0
for position in positions:
	i, j = position
	if mymap[i][j] == ".":
		mymap[i][j] = "#"
		result += go()
		mymap[i][j] = "."

# print result
print(result)
