from get_input import get_input, get_test_input


def calculate(left_list, right_list):
	if len(right_list) == 0:
		return left_list
	result = []
	right = right_list[0]
	for left in left_list:
		result.append(left + right)
		result.append(left * right)
		result.append(int(str(left) + str(right)))
	return calculate(result, right_list[1:])


def is_correct(operation):
	testvalue, operands = operation
	return testvalue in calculate([operands[0]], operands[1:])


# extract input
inp = get_input(__file__)
operations = [line.split(":") for line in inp]
operations = [(int(operation[0]), operation[1]) for operation in operations]
operations = [(testvalue, [int(num) for num in operation.split()]) for testvalue, operation in operations]

# compute
result_list = [operation[0] for operation in operations if is_correct(operation)]
result = sum(result_list)

# print result
print(result)
