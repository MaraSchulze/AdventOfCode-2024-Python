from get_input import get_input, get_test_input


def is_raising(report):
	for i in range(1, len(report)):
		if report[i] <= report[i - 1] or report[i] - report[i - 1] > 3:
			return False
	return True


def is_falling(report):
	for i in range(1, len(report)):
		if report[i] >= report[i - 1] or report[i - 1] - report[i] > 3:
			return False
	return True


def is_save(report):
	return is_raising(report) or is_falling(report)


# get input
inp = get_input(__file__)

# massage input
reports = [[ int(level) for level in line.split()] for line in inp]

# sum up safeties for reports
result = sum([1 if is_save(report) else 0 for report in reports])

# print result
print(result)