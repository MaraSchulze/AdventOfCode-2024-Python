from get_input import get_input, get_test_input


def get_ords(update, orderings):
	result = []
	for o in orderings:
		l, r = o
		if l in update and r in update:
			result.append(o)
	return result


def is_correct(update):
	ords = get_ords(update, orderings)
	
	for i in range(len(update) - 1):
		for j in range(i + 1, len(update)):
			for l, r in orderings:
				if l == update[j] and r == update[i]:
					return False
	return True


# get input
inp = get_input(__file__)

# extract input
updates = []
orderings = []
nl_seen = False
for line in inp:
	if line == "":
		nl_seen = True
		continue
	if nl_seen == False:
		orderings.append(line)
	if nl_seen == True:
		updates.append(line)
orderings = [line.split("|") for line in orderings]
updates = [line.split(",") for line in updates]

# get correctly sorted lists and sum up the middle value
result_list = [update for update in updates if is_correct(update)]
result = sum([int(update[len(update) // 2]) for update in result_list])

# print resultk
print(result)
