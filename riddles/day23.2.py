from get_input import get_input, get_test_input
from itertools import combinations


def find_password(d):
	for computer in d:
		current = d[computer]
		intersections = []
		for comp in current:
			if comp == computer:
				continue
			intersections.append(current.intersection(d[comp]))

		for n in range(14, 3, -1):
			for comb in combinations(current, n):
				comb_set = set(comb)
				frequency = 0
				for intersection in intersections:
					if comb_set.issubset(intersection):
						frequency += 1
				if frequency >= n - 1:
					password = sorted(list(comb))
					return password
	return None


# get input
inp = get_input(__file__)
lan = [line.split("-") for line in inp]

# fill network
d = {}
for connection in lan:
	a, b = connection
	d[a] = d[a].union({b}) if a in d else {a, b}
	d[b] = d[b].union({a}) if b in d else {a, b}

# find password
password_list = find_password(d)
result = ",".join(password_list)

# print result
print(result)
