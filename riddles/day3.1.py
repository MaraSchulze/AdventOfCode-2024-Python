from get_input import get_input, get_test_input
import re
from operator import mul


# get input
inp = get_input(__file__)

# massage input
s = "".join(inp)

# get list of matches
pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, s)

# sum up
result = sum([eval(match) for match in matches])

# print result
print(result)
