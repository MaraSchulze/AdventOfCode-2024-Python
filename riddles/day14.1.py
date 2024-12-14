from get_input import get_input, get_test_input


def move(robot, n, m, loops):
	p, v = robot
	py, px = p
	vy, vx = v
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
robots = [(map(lambda s : int(s), p), map(lambda s : int(s), v)) for p, v in inp]
n, m = 103, 101
field = [[0 for _ in range(m)] for _ in range(n)]

# move robots
for robot in robots:
	x, y = move(robot, n, m, 100)
	field[x][y] += 1

# count quadrants
result = 1
result *= quadrant(field, 0, n // 2, 0, m // 2)
result *= quadrant(field, 0, n // 2, m // 2 + 1, m)
result *= quadrant(field, n // 2 + 1, n, 0, m // 2)
result *= quadrant(field, n // 2 + 1, n, m // 2 + 1, m)

# print result
print(result)
