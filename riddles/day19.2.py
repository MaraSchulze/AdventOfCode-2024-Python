from get_input import get_input, get_test_input


def combinations(design, towels, d):
	if design == "":
		return 1
	if design in d:
		return d[design]
	possiblilities = 0
	for towel in towels:
		if design.startswith(towel):
			possiblilities += combinations(design[len(towel):], towels, d)	
	d[design] = possiblilities
	return possiblilities


# extract input
inp = get_input(__file__)
towels = [x for x in inp[0].split(", ")]
designs = inp[2:]

# compute combinations
result = 0
for design in designs:
	result += combinations(design, towels, {})

print(result)
