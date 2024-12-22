from get_input import get_input, get_test_input


def calculate_round(secret):
	secret = ((secret * 64) ^ secret) % 16777216
	secret = ((secret // 32) ^ secret) % 16777216
	secret = ((secret * 2048) ^ secret) % 16777216
	return secret


def generate_sequences(secret, differences, bananas):
	secrets = []
	secrets.append(secret)
	bananas.append(int(str(secret)[-1]))

	for i in range(2000):
		secret = calculate_round(secret)
		secrets.append(secret)
		bananas.append(int(str(secret)[-1]))
		differences.append(bananas[i] - bananas[i - 1])


def put(seller_nr, change, banana, changes):
	if change in changes:
		if changes[change][seller_nr] == None:
			changes[change][seller_nr] = banana
	else:
		l = len(sellers) * [None]
		l[seller_nr] = banana
		changes[change] = l 


def generate_changes(seller_nr, differences, bananas, changes):
	for i in range(len(differences) - 4):
		change = tuple(differences[i:i + 4])
		banana = bananas[i + 3]
		put(seller_nr, change, banana, changes)


# get input
inp = get_input(__file__)
sellers = [int(line) for line in inp]

# calculate sequences and changes
changes = {}

for i in range(len(sellers)):
	differences = []
	bananas = []
	secret = sellers[i]
	generate_sequences(secret, differences, bananas)
	generate_changes(i, differences, bananas, changes)

# get maximum change
result = 0
for prices in changes.values():
	prices = [x for x in prices if x != None]
	result = max(result, sum(prices))

# print(result)
print(result)
