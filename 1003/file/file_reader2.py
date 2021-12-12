filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in file_object:
        print(line.rstrip())






