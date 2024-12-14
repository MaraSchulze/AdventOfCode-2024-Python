from get_input import get_input, get_test_input


def move(robot, n, m, loops):
	p, v = robot
	py, px = list(p)
	vy, vx = list(v)
	new_x = (px + loops * vx) % n
	new_y = (py + loops * vy) % m
	return (new_x, new_y)


def quadrant(field, x1, x2, y1, y2):
	count = 0
	for i in range(x1, x2):
		for j in range(y1, y2):
			count += field[i][j]
	return count
			

# extract input
inp = get_input(__file__)
inp = [line.split() for line in inp]
inp = [(p[2:].split(","), v[2:].split(",")) for p, v in inp]
robots = [(list(map(lambda s : int(s), p)), list(map(lambda s : int(s), v))) for p, v in inp]
n, m = 103, 101

# iterate over 10000 possibilities and find a row of 15 x
for loop in range(0, 10000):
	found = False
	field = [[0 for _ in range(m)] for _ in range(n)]

	for robot in robots:
		x, y = move(robot, n, m, loop)
		field[x][y] += 1

	for row in field:
		row_str = "".join(["x" if x > 0 else " " for x in row])
		if row_str.find("xxxxxxxxxxxxxxx") != -1:
			print("found", loop)
			found = True

	if found == True:
		for row in field:
			row_str = "".join(["x" if x > 0 else " " for x in row])
			print(row_str)
