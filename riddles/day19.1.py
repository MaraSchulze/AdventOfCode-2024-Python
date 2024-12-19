from get_input import get_input, get_test_input


def is_possible(design, towels, d):
	if design == "":
		return True
	if design in d:
		return d[design]
	for towel in towels:
		if design.startswith(towel):
			if is_possible(design[len(towel):], towels, d):
				return True
	d[design] = False
	return False


# extract input
inp = get_input(__file__)
towels = [x for x in inp[0].split(", ")]
designs = inp[2:]

# compute possible designs
result = 0
for design in designs:
	result += 1 if is_possible(design, towels, {}) else 0

# print result
print(result)
