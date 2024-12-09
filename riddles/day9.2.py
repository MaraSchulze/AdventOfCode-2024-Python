from get_input import get_input, get_test_input
from collections import defaultdict


def create_disk(diskmap):
	disk = []
	for i in range(0, len(diskmap) - 1, 2):
		id = i // 2
		disk += int(diskmap[i]) * [id]
		disk += int(diskmap[i + 1]) * ["."]
	disk += int(diskmap[-1]) * [id + 1]
	return disk


def get_length_dict(diskmap):
	d = {}
	for i in range(0, len(diskmap) - 1, 2):
		id = i // 2
		d[id] = int(diskmap[i])
	d[id + 1] = int(diskmap[-1])
	return d


def get_space_dict(diskmap):
	space = defaultdict(list)
	position = 0
	for i in range(len(diskmap)):
		if i % 2 == 1:
			current = int(diskmap[i])
			space[current].append(position) 
		position += int(diskmap[i])
	return space


def find_space(space, length):
	# find all spaces that fit
	lengths = []
	for l in range(length, 10):
		if l in space and len(space[l]) != 0:
			lengths.append((space[l][0], l))
	if len(lengths) == 0:
		return None
	
	# update space
	lengths.sort()
	index, space_length = lengths[0]
	new_length = space_length - length
	space[space_length].pop(0)
	space[new_length].append(index + length)
	space[new_length].sort()

	return index


# extract input
inp = get_input(__file__)
diskmap = inp[0]

# create disk
disk = create_disk(diskmap)

# create dict with file lengths. id : length
d = get_length_dict(diskmap)

# create a map of free disk space in dict space
# key is length and value is a list of positions, sorted
space = get_space_dict(diskmap)

# iterate over file ids
for i in range(len(d) - 1, -1, -1):
	length = d[i]

	# find a space that is at least length long and is the most left
	# lengths contains the tuples (position, free space length at that position)
	index1 = find_space(space, length)
	if index1 == None:
		continue

	# move
	index2 = disk.index(i)
	if (index1 > index2):
		continue
	for j in range(d[i]):
		disk[index2 + j] = "."
	for j in range(d[i]):
		disk[index1 + j] = i
		
# sum up result
result = 0
for i in range(len(disk)):
	if disk[i] != ".":
		result += i * disk[i]

# print result
print(result)
