from get_input import get_input, get_test_input


def rec(i, j, trails, step):
	if not(0 <= i < len(trails) and 0 <= j < len(trails[0])):
		return 0
	if trails[i][j] != step:
		return 0
	if trails[i][j] == 9:
		return 1
	result = 0
	result += rec(i+1, j, trails, step + 1)
	result += rec(i-1, j, trails, step + 1)
	result += rec(i, j+1, trails, step + 1)
	result += rec(i, j-1, trails, step + 1)
	return result

inp = get_input(__file__)
trails = [[int(x) for x in list(line)] for line in inp]

result = 0
for i in range(len(trails)):
	for j in range(len(trails[0])):
		if trails[i][j] == 0:
			result += rec(i, j, trails, 0)
print(result)
