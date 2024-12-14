from get_input import get_input, get_test_input


def get_a(A, B, prize, b):
	px, py = prize
	ax, ay = A
	bx, by = B
	numerator = px - b * bx
	denominator = ax
	return numerator / denominator

def get_b(A, B, prize):
	px, py = prize
	ax, ay = A
	bx, by = B
	numerator = px * ay - py * ax 
	denominator = -by * ax + bx * ay 
	return numerator / denominator


def get_tokens(A, B, prize):
	b = get_b(A, B, prize)
	a = get_a(A, B, prize, b)
	if a == int(a) and b == int(b):
		return int(a * 3 + b)
	else:
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
		prize = (int(line[0][3:]) + 10000000000000, int(line[1][3:]) + 10000000000000)
	if i % 4 == 3:
		result += get_tokens(A, B, prize)

print(result)
