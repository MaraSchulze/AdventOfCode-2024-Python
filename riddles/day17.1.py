from get_input import get_input, get_test_input


def combo(operand):
	if operand == 4:
		return registers["A"]
	elif operand == 5:
		return registers["B"]
	elif operand == 6:
		return registers["C"]
	else:
		return operand
	

def adv(operand):
	registers["A"] = registers["A"] // (2**combo(operand))
	registers["IP"] += 2

def bxl(operand):
	registers["B"] = registers["B"] ^ operand
	registers["IP"] += 2

def bst(operand):
	registers["B"] = combo(operand) % 8
	registers["IP"] += 2

def jnz(operand):
	if registers["A"] == 0:
		registers["IP"] += 2
	else:
		registers["IP"] = operand

def bxc(operand):
	registers["B"] = registers["B"] ^ registers["C"]
	registers["IP"] += 2

def out(operand):
	print(combo(operand) % 8, end=",")
	registers["IP"] += 2

def bdv(operand):
	registers["B"] = registers["A"] // (2**combo(operand))
	registers["IP"] += 2

def cdv(operand):
	registers["C"] = registers["A"] // (2**combo(operand))
	registers["IP"] += 2

def execute(instr, operand):
	d = {0 : adv, 1 : bxl, 2 : bst, 3 : jnz, 4 : bxc, 5 : out, 6 : bdv, 7 : cdv}
	next = d[instr]
	next(operand)


# extract input
inp = get_test_input(__file__)
a = int(inp[0].split(":")[1])
b = int(inp[1].split(":")[1])
c = int(inp[2].split(":")[1])
instructions = inp[4].split(":")[1]
instructions = [int(x) for x in instructions.split(",")]

# interpret
registers = {"A" : a, "B" : b, "C" : c, "IP" : 0}

ip = registers["IP"]
while ip < len(instructions):
	instr, operand = instructions[ip], instructions[ip + 1]
	execute(instr, operand)
	ip = registers["IP"]
