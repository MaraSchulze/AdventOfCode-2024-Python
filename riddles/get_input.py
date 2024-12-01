import os


def get_input(file):
	file_name = os.path.basename(file)
	day = file_name[3:file_name.find(".")]

	with open("../inputs/" + day, "r") as f:
		inp = f.readlines()
		inp = [line.strip() for line in inp]

	return inp

def get_test_input(file):
	file_name = os.path.basename(file)
	day = file_name[3:file_name.find(".")]

	with open("../inputs/test" + day, "r") as f:
		inp = f.readlines()
		inp = [line.strip() for line in inp]

	return inp
