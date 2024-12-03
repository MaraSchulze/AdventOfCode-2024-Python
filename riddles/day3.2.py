from get_input import get_input, get_test_input
import re
from operator import mul


# get input
inp = get_input(__file__)

# massage input
s = "".join(inp)

# get list of matches
pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.finditer(pattern, s)

# get do-dont intervals
dos_matches = re.finditer("do\(\)", s)
donts_matches = re.finditer("don't\(\)", s)

dos = [match.start() for match in dos_matches] + [0]
donts = [match.start() for match in donts_matches] + [len(s)]

dos.sort()
donts.sort()

intervals = []
index = 0
for start in dos:
	while donts[index] < start:
		index += 1
	intervals.append((start, donts[index]))

# sum up
result = 0
for match in matches:
	for start, end in intervals:
		if start < match.start() < end:
			result += eval(match.group())
			break

# print result
print(result)
