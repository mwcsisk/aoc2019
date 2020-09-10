from sys import argv

if len(argv) != 2:
    print("Usage: python script.py <input_filepath>")
    exit(1)

path = argv[1]
masses = []

try:
    with open(path, "r") as f:
        for line in f:
            try:
                line = int(line)
                masses.append(line)
            except ValueError:
                print('Invalid input file. File must only contain integers.')
except FileNotFoundError:
    print(f"Error: no such file { path }")
    exit(1)

print(masses)