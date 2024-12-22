from get_input import get_input, get_test_input


def formula(i, b_start):
    if i == 0:
        return b_start
    a = 0
    for j in range(i):
        a = (a + bs[j]) * 8
    a += b_start
    return a


# get input
inp = get_input(__file__)
program = inp[4][9:]
program = [int(x) for x in program.split(",")]
program.reverse()

# compute a
bs = []

backtrack = False
i = 0
while i < 17:
    if backtrack:
        i -= 2
        j_start = bs[i] + 1
        bs.pop(-1)
    else:
        j_start = 0

    if i == 16:
        print(a)
        break

    backtrack = True
    for b_start in range(j_start, 8):
        if i == 0 and b_start == 0:
            continue

        a = formula(i, b_start)

        b = a % 8
        b = b ^ 3
        c = a // 2**b
        b = b ^ c
        b = b ^ 3
        out = b % 8

        if out == program[i]:
            bs.append(b_start)
            backtrack = False
            break

    i += 1
