from get_input import get_input, get_test_input


def count_area(i, j, plant, field):
	if not (0 <= i < len(field) and 0 <= j < len(field[0])):
		return 0
	if field[i][j] != plant:
		return 0
	field[i][j] = plant.lower()
	north = count_area(i + 1, j, plant, field)
	south = count_area(i - 1, j, plant, field)
	west = count_area(i, j + 1, plant, field)
	east = count_area(i, j - 1, plant, field)
	return (1 + north + south + west + east)


def is_inbounds(i, j):
	return 0 <= i < len(field) and 0 <= j < len(field[0])


def count_perimeter(plant, field):
	perimeter = 0
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j] != plant:
				continue

			north = field[i - 1][j] if is_inbounds(i - 1, j) else "."
			south = field[i + 1][j] if is_inbounds(i + 1, j) else "."
			west = field[i][j - 1] if is_inbounds(i, j - 1) else "."
			east = field[i][j + 1] if is_inbounds(i, j + 1) else "."
			northwest= field[i - 1][j - 1] if is_inbounds(i - 1, j - 1) else "."
			northeast = field[i - 1][j + 1] if is_inbounds(i - 1, j + 1) else "."
			southwest = field[i + 1][j - 1] if is_inbounds(i + 1, j - 1) else "."

			perimeter += 1 if north != plant else 0
			perimeter += 1 if south != plant else 0
			perimeter += 1 if west != plant else 0
			perimeter += 1 if east != plant else 0

			perimeter -= 1 if north != plant and west == plant and northwest != plant else 0
			perimeter -= 1 if south != plant and west == plant and southwest != plant else 0
			perimeter -= 1 if west != plant and north == plant and northwest != plant else 0
			perimeter -= 1 if east != plant and north == plant and northeast != plant else 0
	return perimeter


def delete_area(plant, field):
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j] == plant:
				field[i][j] = "."


# extract input
inp = get_input(__file__)
field = [list(line) for line in inp]

# compute fence
result = 0
for i in range(len(field)):
	for j in range(len(field[0])):
		if field[i][j] != ".":
			plant = field[i][j]
			area = count_area(i, j, plant, field)
			perimeter = count_perimeter(plant.lower(), field)
			result += area * perimeter
			delete_area(plant.lower(), field)

# print result
print(result)
