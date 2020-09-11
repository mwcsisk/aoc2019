from sys import argv

def fuelCalc(mass):
    if mass <= 6:
        return 0
    fuel = mass // 3 - 2
    return fuel + fuelCalc(fuel)

if __name__ == '__main__':
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
                    exit(1)
    except FileNotFoundError:
        print(f"Error: no such file { path }")
        exit(1)

    fuel = 0

    for mass in masses:
        fuel += fuelCalc(mass)

    print(f"The fuel required is { fuel }")
