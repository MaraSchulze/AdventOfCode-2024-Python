from get_input import get_input, get_test_input


def right(direct):
    d = {N : E, E : S, S : W, W : N}
    return d[direct]

def left(direct):
    d = {N : W, W : S, S : E, E : N}
    return d[direct]
    
def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def go(field):
    nodes = [(len(field) - 2, 1, E, 0)]
    seen = {}
    results = []
    while len(nodes) != 0:
        node = nodes.pop(0)
        i, j, d, v = node

        if i == 1 and j == len(field[0]) - 2:
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


# global variables
N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1),

# get input
inp = get_input(__file__)
field = [list(line) for line in inp]

# walk the field
result = go(field)

# print result
print(result)
