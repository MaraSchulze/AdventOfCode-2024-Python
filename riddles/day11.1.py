from get_input import get_input, get_test_input


inp = get_input(__file__)
stones = [int(x) for x in inp[0].split()]

for _ in range(25):
	i = 0
	current_length = len(stones)
	while i < current_length:
		if stones[i] == 0:
			stones[i] = 1
		elif len(str(stones[i])) % 2 == 1:
			stones[i] *= 2024
		else:
			str_stone = str(stones[i])
			stones[i] = int(str_stone[:len(str_stone) // 2])
			stones.append(int(str_stone[len(str_stone) // 2:]))
		i += 1

# print result
result = len(stones)
print(result)
