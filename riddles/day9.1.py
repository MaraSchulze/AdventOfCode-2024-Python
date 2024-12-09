from get_input import get_input, get_test_input


# extract input
inp = get_input(__file__)
diskmap = inp[0]
disk = []
for i in range(0, len(diskmap) - 1, 2):
	disk += int(diskmap[i]) * [i // 2]
	disk += int(diskmap[i + 1]) * ["."]
disk += int(diskmap[-1]) * [i // 2 + 1]

# move files
index = 0
while True:
	print(len(disk))
	if not ("." in disk):
		break
	while disk[-1] == ".":
		disk.pop(-1)
	index = disk.index(".", index)
	disk[index] = disk[-1]
	disk.pop(-1)

# get result
result = 0
for i in range(len(disk)):
	result += i * disk[i]

# print result
print(result)
