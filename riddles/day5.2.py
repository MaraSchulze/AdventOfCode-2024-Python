from get_input import get_input, get_test_input


def is_incorrect(update):
	ords = get_ords(update, orderings)
	
	for i in range(len(update) - 1):
		for j in range(i + 1, len(update)):
			for l, r in orderings:
				if l == update[j] and r == update[i]:
					return True
	return False


def get_ords(update, orderings):
	result = []
	for o in orderings:
		l, r = o
		if l in update and r in update:
			result.append(o)
	return result


def make_dict(ords):
	d = {}
	for ord in ords:
		l, r = ord
		if l in d:
			d[l] = d[l] + [r]
		else:
			d[l] = [r]
	return d


def mysort(update):
	# get orderings that contain the numbers in update,
	# then make dict with as key the left value and as value a list of right
	# values
	ords = get_ords(update, orderings)
	d = make_dict(ords)
	
	result = []
	for _ in range(len(update) - 1):
		# find the current last number. It will always be the list with 
		# just one element
		for l in d:
			if len(d[l]) == 1:
				start = d[l][0]
				break

		# append the number. The list will be reversed, but we just need the
		# middle value
		result.append(start)

		# remove the current number from all lists
		for key in d:
			if start in d[key]:
				d[key].remove(start)

	# The last remaining number is not identifyable by list length anymore
	# so we take the key of the last number.
	result.append(l)

	# return middle number
	return int(result[len(result) // 2])

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

# apply sorting
result = 0
result_list = [update for update in updates if is_incorrect(update)]
result_list = [mysort(update) for update in result_list]
result = sum(result_list)

# print result
print(result)
