from get_input import get_input, get_test_input


def apply_modifications(field):
    items = {"#" : "##", "." : "..", "O" : "[]", "@" : "@."}
    for i in range(len(field)):
        new_row = ""
        for c in field[i]:
            new_row += items[c]
        field[i] = new_row
    return field
    

def get_robot(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "@":
                return (i, j)
    return None


def get_direction(move):
    moves = {"^" : (-1, 0), "v" : (1, 0), "<" : (0, -1), ">" : (0, 1)}
    return moves[move]


def get_frontier(items, direction):
    return [tuple_add(item, direction) for item in items]


def get_things(frontier, field):
    return [field[f[0]][f[1]] for f in frontier]


def complete_boxes(frontier, direction, field):
    if direction == (0, -1) or direction == (0, 1):
        return frontier

    new_frontier = frontier[:]
    for i, j in frontier:
        if field[i][j] == "]" and not (i, j - 1) in frontier:
            new_frontier.append((i, j - 1))
        if field[i][j] == "[" and not (i, j + 1) in frontier:
            new_frontier.append((i, j + 1))
    new_frontier.sort()
    return new_frontier


def move_items(items, direction, field):
    for i, j in items:
        a, b = tuple_add((i, j), direction)
        field[a][b] = field[i][j]
        field[i][j] = "."


def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def move_robot(robot, items, direction, field):
    frontier = get_frontier(items, direction)
    frontier_things = get_things(frontier, field)

    if "#" in frontier_things:
        return robot
    
    if "[" in frontier_things or "]" in frontier_things:
        new_frontier = complete_boxes(frontier, direction, field)
        new_frontier = [f for f in new_frontier if field[f[0]][f[1]] != "."]
        move_robot(robot, new_frontier, direction, field)

    if all(s == "." for s in get_things(frontier, field)):
        move_items(items, direction, field)
        return tuple_add(robot, direction)
    else:
        return robot


def count_box_coordinates(field):
    result = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "[":
                result += i * 100 + j
    return result


# extract input
inp = get_input(__file__)

for i in range(len(inp)):
    if inp[i] == "":
        emptyline = i

field = inp[:emptyline]
moves = "".join(inp[emptyline + 1:])

field = apply_modifications(field)
field = [list(line) for line in field]

# move robot
robot = get_robot(field)
for move in moves:
    robot = move_robot(robot, [robot], get_direction(move), field)

# count and print result
result = count_box_coordinates(field)
print(result)
