from get_input import get_input, get_test_input
from itertools import permutations 


def tuple_add(a, b):
    a1, a2 = a
    b1, b2 = b 
    return (a1 + b1, a2 + b2)


def get_delta(a, b):
    a1, a2 = a
    b1, b2 = b 
    return (b1 - a1, b2 - a2)


def get_delta_string(delta):
    a, b = delta
    out = ""

    if b < 0:
        b = -b
        out += b * "<"
    else:
        out += b * ">"

    if a < 0:
        a = -a
        out += a * "^"
    else:
        out += a * "v"

    return out


def get_permutations(s):
    return list(set(permutations(s)))


def is_allowed(position, moves):
    for move in moves:
        position = tuple_add(position, m[move])
        if position == (0, -2):
            return False
    return True
    

def type_code(code, pad, level):
    if level == 3:
        return len(code)

    length = 0
    i, j = 0, 0
    for char in code:
        delta = get_delta((i, j), pad[char])
        delta_string = get_delta_string(delta)
        possible_codes = get_permutations(delta_string)
        possible_length = float("inf")
        for combination in possible_codes:
            if not is_allowed((i, j), combination):
                continue
            combination = combination + ("A",)
            possible_length = min(possible_length, type_code(combination, pad_directional, level + 1))
        length += possible_length
        i, j = pad[char]
    return length


# get input
inp = get_test_input(__file__)

# pads
pad_numeric = {"A" : (0, 0), "0" : (0, -1), "3" : (-1, 0), "6" : (-2, 0), "9" : (-3, 0), "2" : (-1, -1), "5" : (-2, -1), "8" : (-3, -1), "1" : (-1, -2), "4" : (-2, -2), "7" : (-3, -2)}
pad_directional = {"A" : (0, 0), "^" : (0, -1), "v" : (1, -1), "<" : (1, -2), ">" : (1, 0)}

# compute codes
m = {"^" : (-1, 0), "v" : (1, 0), "<" : (0, -1), ">" : (0, 1)}

result = 0
for code in inp:
    result += type_code(code, pad_numeric, 0) * int(code[:-1])

print(result)
