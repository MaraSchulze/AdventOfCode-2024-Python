from get_input import get_input, get_test_input
from collections import defaultdict
from queue import PriorityQueue


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
	space = defaultdict(PriorityQueue)
	position = 0
	for i in range(len(diskmap)):
		if i % 2 == 1:
			current = int(diskmap[i])
			space[current].put(position) 
		position += int(diskmap[i])
	return space


def find_space(space, length):
	# find all spaces that fit
	lengths = PriorityQueue()
	for l in range(length, 10):
		if l in space and not space[l].empty():
			peek = space[l].get()
			lengths.put((peek, l))
			space[l].put(peek)
	if lengths.empty():
		return None

	# update space
	index, space_length = lengths.get()
	space[space_length].get()
	new_length = space_length - length
	space[new_length].put(index + length)

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
	print(i)
	length = d[i]

	# find a space that is at least length long and is the most left
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
