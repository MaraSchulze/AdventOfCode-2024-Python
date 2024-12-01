from get_input import get_input, get_test_input
from collections import Counter

# get input
inp = get_input(__file__)

# extract input
l1 = [int(line.split()[0]) for line in inp]
l2 = [int(line.split()[1]) for line in inp]

# count list 2 frequencies
d = Counter(l2)

# sum up frequencies
result = sum([l1[i] * d[l1[i]] for i in range(len(inp))])

# print result
print(result)
