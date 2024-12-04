from get_input import get_input, get_test_input


def myfind(s, i, j):
	if s[i][j] != "A":
		return 0
	if (s[i-1][j-1] == "M" and s[i+1][j+1] == "S" \
	or s[i-1][j-1] == "S" and s[i+1][j+1] == "M") and \
	(s[i-1][j+1] == "M" and s[i+1][j-1] == "S" \
	or s[i-1][j+1] == "S" and s[i+1][j-1] == "M"):
		return 1
	else:
		return 0


# get input
inp = get_input(__file__)

# massage input
s = [list(line) for line in inp]

# find X-MASes
result = 0
for i in range(1, len(s) - 1):
	for j in range(1, len(s[i]) - 1):
		result += myfind(s, i, j)

# print result
print(result)	
