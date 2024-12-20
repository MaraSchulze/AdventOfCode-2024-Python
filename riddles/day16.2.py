from get_input import get_input, get_test_input


def right(direct):
    d = {N : E, E : S, S : W, W : N}
    return d[direct]

def left(direct):
    d = {N : W, W : S, S : E, E : N}
    return d[direct]
    
def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def go(field, seen):
    nodes = [(len(field) - 2, 1, E, 0)]
    results = []
    while len(nodes) != 0:
        node = nodes.pop(0)
        i, j, d, v = node

        if i == 1 and j == len(field[0]) - 2:
            seen[(i, j, d)] = v
            results.append(node[3])
            continue

        if (i, j, d) in seen and seen[(i, j, d)] < v:
            continue
       
        a, b = tuple_add((i, j), d)
        if field[a][b] != "#":
            node = (a, b, d, v + 1)
            if not (i, j, d) in seen or seen[(i, j, d)] > v + 1:
                seen[(i, j, d)] = v + 1
                nodes.append(node)

        nd = right(d)
        a, b = tuple_add((i, j), nd)
        if field[a][b] != "#":
            node = (a, b, nd, v + 1001)
            if not (i, j, nd) in seen or seen[(i, j, nd)] > v + 1001:
                seen[(i, j, nd)] = v + 1001
                nodes.append(node)

        nd = left(d)
        a, b = tuple_add((i, j), nd)
        if field[a][b] != "#":
            node = (a, b, nd, v + 1001)
            if not (i, j, nd) in seen or seen[(i, j, nd)] > v + 1001:
                seen[(i, j, nd)] = v + 1001
                nodes.append(node)

    return min(results)


def trace_back(pathvalue, bearing, coord, seen, places):
    places.add(coord)

    if pathvalue == 0:
        return
    
    a, b = tuple_add(coord, right(right(bearing)))
    if (a, b, bearing) in seen and seen[(a, b, bearing)] == pathvalue - 1:
        trace_back(pathvalue - 1, bearing, (a, b), seen, places)

    right_direct = right(bearing)
    left_direct = left(bearing)

    a, b = tuple_add(coord, right_direct)
    if (a, b, left_direct) in seen and seen[(a, b, left_direct)] == pathvalue - 1001:
        trace_back(pathvalue - 1001, left_direct, (a, b), seen, places)

    a, b = tuple_add(coord, left_direct)
    if (a, b, right_direct) in seen and seen[(a, b, right_direct)] == pathvalue - 1001:
        trace_back(pathvalue - 1001, right_direct, (a, b), seen, places)


# global variables
N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
seen = {}

# get input
inp = get_input(__file__)
field = [list(line) for line in inp]

# walk the field
pathvalue = go(field, seen) + 1

# trace back ways
places = set()
trace_back(pathvalue, N, (1, len(field) - 2), seen, places)
result = len(places)

# print result
print(result)
