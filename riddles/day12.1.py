from get_input import get_input, get_test_input


def count(i, j, plant, field):
	if not (0 <= i < len(field) and 0 <= j < len(field[0])):
		return (0, 1)
	if field[i][j] == plant.lower():
		return (0, 0)
	if field[i][j] != plant.lower() and field[i][j] != plant:
		return (0, 1)
	field[i][j] = plant.lower()
	north = count(i + 1, j, plant, field)
	south = count(i - 1, j, plant, field)
	west = count(i, j + 1, plant, field)
	east = count(i, j - 1, plant, field)
	return (1 + north[0] + south[0] + west[0] + east[0], 
		 north[1] + south[1] + west[1] + east[1])


# extract input
inp = get_input(__file__)
field = [list(line) for line in inp]

# compute fence
result = 0
for i in range(len(field)):
	for j in range(len(field[0])):
		if field[i][j] != ".":
			area, perimeter = count(i, j, field[i][j], field)
			result += area * perimeter

# print result
print(result)
