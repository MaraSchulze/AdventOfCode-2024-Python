from get_input import get_input, get_test_input


# get input
inp = get_input(__file__)
lan = [line.split("-") for line in inp]

# fill network
d = {}
for connection in lan:
	a, b = connection
	d[a] = d[a].union({b}) if a in d else {b}
	d[b] = d[b].union({a}) if b in d else {a}

# find triples
triples = set()
for a in d:
	for b in d[a]:
		if b == a:
			continue
		for c in d[b]:
			if c == b:
				continue
			if a in d[c]:
				triple = [a, b, c]
				triple.sort()
				triples.add(tuple(triple))

# scan for computers beginning with t
result_list = [(a, b, c) for a, b, c in triples if a[0] == "t" or b[0] == "t" or c[0] == "t"]
result = len(result_list)

# print result
print(result)
