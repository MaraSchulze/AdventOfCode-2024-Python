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
	a, b = new_dir
	return new_dir

def inbounds(x, y):
	return 0 <= x < len(mymap) and 0 <= y < len(mymap[0])

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
# exract input
inp = get_test_input(__file__)
mymap = [list(line) for line in inp]

c, d = get_start()
i, j = c, d
direction = N
test = 0
while 0 <= i < len(mymap) and 0 <= j < len(mymap[0]):
	i, j = step(i, j, direction)
	if not (0 <= i < len(mymap) and 0 <= j < len(mymap[0])):
		break
	mymap[i][j] = "X"
	test += 1
	a, b = step(i, j, direction)
	if not (0 <= a < len(mymap) and 0 <= b < len(mymap[0])):
		break
	if mymap[a][b] == "#":
		direction = right(direction)
print(test)
# for row in mymap:
# 	print(row)
# print()

result = 0
for x in range(len(mymap)):
	for y in range(len(mymap[0])):
		if mymap[x][y] != "^" and mymap[x][y] != "#":
			if (inbounds(x - 1, y) and mymap[x - 1][y] == "X" or inbounds(x + 1, y) and mymap[x + 1][y] == "X" or inbounds(x, y - 1) and mymap[x][y - 1] == "X" or inbounds(x, y + 1) and mymap[x][y + 1] == "X"):
				save = mymap[x][y]
				mymap[x][y] = "o"
			else:
				continue
		else:
			continue

		found = False
		cycle = []
		i, j = c, d
		direction = N
		while 0 <= i < len(mymap) and 0 <= j < len(mymap[0]):
			i, j = step(i, j, direction)
			if not (0 <= i < len(mymap) and 0 <= j < len(mymap[0])):
				break
			
			if (i, j, direction) in cycle:
				found = True
				break
			cycle.append((i, j, direction))

			a, b = step(i, j, direction)
			if not (0 <= a < len(mymap) and 0 <= b < len(mymap[0])):
				break
			if mymap[a][b] == "#" or mymap[a][b] == "o":
				direction = right(direction)
		
		# if found == True:
		# 	print(found, x, y)
		# 	for row in mymap:
		# 		print(row)
		if found == True:
			result += 1
		mymap[x][y] = save
		print(x, y, found)


print(result)
