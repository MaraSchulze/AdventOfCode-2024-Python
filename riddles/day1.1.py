from get_input import get_input, get_test_input


# get input
inp = get_input(__file__)

# extract input
l1 = [int(line.split()[0]) for line in inp]
l2 = [int(line.split()[1]) for line in inp]

# sort lists
l1.sort()
l2.sort()

# sum up differences
result = sum([abs(l1[i] - l2[i]) for i in range(len(inp))])

# print result
print(result)
