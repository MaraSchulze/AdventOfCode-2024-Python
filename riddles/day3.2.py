from get_input import get_input, get_test_input
import re
from operator import mul


# get input
inp = get_input(__file__)

# massage input
s = "".join(inp)

# get list of matches
pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches_it = re.finditer(pattern, s)

# get do-dont intervals
dos_it = re.finditer("do\(\)", s)
donts_it = re.finditer("don't\(\)", s)

# combine all 3 iterators into one labeled list
intervals = [("mul", match.start(), match.group()) for match in matches_it]
intervals += [("do", match.start()) for match in dos_it]
intervals += [("dont", match.start()) for match in donts_it]

# sort intervals after 2nd projection
intervals.sort(key=lambda x: x[1])

# sum up
allow = True
result = 0
for point in intervals:
	if point[0] == "do":
		allow = True
	elif point[0] == "dont":
		allow = False
	else:
		if allow == True:
			result += eval(point[2])

# print result
print(result)
