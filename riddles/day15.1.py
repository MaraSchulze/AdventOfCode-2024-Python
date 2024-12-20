from get_input import get_input, get_test_input


def get_robot(map):
	for i in range(len(map)):
		for j in range(len(map[0])):
			if map[i][j] == "@":
				return (i, j)
	return None

def get_free(i, j, move, map):
	if move == "^":
		direction = (-1, 0)
	elif move == "v":
		direction = (1, 0)
	elif move == "<":
		direction = (0, -1)
	elif move == ">":
		direction = (0, 1)

	while map[i + direction[0]][j + direction[1]] != "#":
		i += direction[0]
		j += direction[1]
		if map[i][j] == ".":
			return (i, j)
	return (-1, -1)

def shove(i, j, x, y, move, map):
	print(i, j, x, y, move)
	if move == "^":
		direction = (-1, 0)
	elif move == "v":
		direction = (1, 0)
	elif move == "<":
		direction = (0, -1)
	elif move == ">":
		direction = (0, 1)

	while map[x][y] != "@":
		# print("a", x, y)
		x -= direction[0]
		y -= direction[1]
		# print("c", x, y, direction)
		map[x + direction[0]][y + direction[1]] = map[x][y]
	map[x][y] = "."
	# print("b")
	return (x + direction[0], y + direction[1])

def do_move(i, j, move, map):
	x, y = get_free(i, j, move, map)
	if x == -1:
		return (i, j)
	return shove(i, j, x, y, move, map)

def count(map):
	result = 0
	for i in range(len(map)):
		for j in range(len(map[0])):
			if map[i][j] == "O":
				result += i * 100 + j
	return result

inp = get_input(__file__)
breakline = 0
for i in range(len(inp)):
	if inp[i] == "":
		breakline = i
		break
map = [list(line) for line in inp[:breakline]]
moves = "".join(inp[breakline + 1:])
	   
start = get_robot(map)
i, j = start
for k in range(len(moves)):
	move = moves[k]
	i, j = do_move(i, j, move, map)
	# for row in map:
	# 	print(row)
	print(k, len(moves))

result = count(map)
print(result)
