from get_input import get_input, get_test_input


def is_raising(report):
	for i in range(1, len(report)):
		if report[i] <= report[i - 1] or report[i] - report[i - 1] > 3:
			return False
	return True


def is_save(report):
	if is_raising(report) or is_raising(list(reversed(report))):
		return True

	# leave out one level
	for i in range(len(report)):
		second_chance = report[:i] + report[i + 1:]
		if is_raising(second_chance) or is_raising(list(reversed(second_chance))):
			return True
	return False


# get input
inp = get_input(__file__)

# massage input
reports = [[int(level) for level in line.split()] for line in inp]

# sum up safeties for reports
result = sum([1 if is_save(report) else 0 for report in reports])

# print result
print(result)
