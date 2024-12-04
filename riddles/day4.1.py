from get_input import get_input, get_test_input


def myfind(s, i, j):
	directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	word = "XMAS"
	found = 0

	# look into every of the 8 directions
	for direction in directions:
		x, y = direction
		# look at every of the 4 letters in word
		for distance in range(0, 4):
			ii = i + distance * x 
			jj = j + distance * y
			if not (0 <= ii < len(s) and 0 <= jj < len(s[0])) or s[ii][jj] != word[distance]:
				break
		else:
			found += 1
	
	return found


# get input
inp = get_input(__file__)

# massage input
s = [list(line) for line in inp]

# find XMASes
result = 0
for i in range(len(s)):
	for j in range(len(s[i])):
		result += myfind(s, i, j)

# print result
print(result)	
