from get_input import get_input, get_test_input


def is_inbounds(i, j):
	return 0 <= i < len(arr) and 0 <= j < len(arr[0])


def find_anti(x, y):
	antenna = arr[x][y]
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			other = arr[i][j]
			if not (i == x and j == y) and other == antenna:
				antis.add((i, j))
				length = 2
				while True:
					a = x - length * (x - i)
					b = y - length * (y - j)
					if is_inbounds(a, b):
						antis.add((a, b))
					else:
						break
					length += 1


# get input
inp = get_input(__file__)
arr = [list(line) for line in inp]

antis = set()
for i in range(len(arr)):
	for j in range(len(arr[0])):
		if arr[i][j].isalnum():
			find_anti(i, j)

result = len(antis)

print(result)