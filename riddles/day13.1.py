from get_input import get_input, get_test_input


def get_tokens(A, B, prize):
	x, y = 0, 0
	tokens = 0
	px, py = prize
	while x <= px and y <= py:
		delta_x, delta_y = px - x, py - y
		bx, by = B
		x_time, y_time = delta_x // bx, delta_y // by
		if delta_x % bx == 0 and delta_y % by == 0 and x_time == y_time:
			tokens += x_time
			return tokens
		ax, ay = A
		x += ax 
		y += ay
		tokens += 3
	return 0


inp = get_input(__file__)

result = 0
for i in range(len(inp)):
	if i % 4 == 0:
		line = inp[i][9:].split(",")
		A = (int(line[0][3:]), int(line[1][3:]))
	if i % 4 == 1:
		line = inp[i][9:].split(",")
		B = (int(line[0][3:]), int(line[1][3:]))
	if i % 4 == 2:
		line = inp[i][6:].split(",")
		prize = (int(line[0][3:]), int(line[1][3:]))
		print(A, B, prize)
	if i % 4 == 3:
		result += get_tokens(A, B, prize)

print(result)
