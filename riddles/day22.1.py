from get_input import get_input, get_test_input


def calculate_round(secret):
	secret = ((secret * 64) ^ secret) % 16777216
	secret = ((secret // 32) ^ secret) % 16777216
	secret = ((secret * 2048) ^ secret) % 16777216
	return secret


def secret_number(secret, rounds):
	for _ in range(rounds):
		secret = calculate_round(secret)
	return secret


# get input
inp = get_input(__file__)
secrets = [int(line) for line in inp]

# calculate secrets
result = 0
for secret in secrets:
	result += secret_number(secret, 2000)

# print result
print(result)
