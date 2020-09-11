import argparse


def intcomp(array):
    i = 0
    while array[i] != 99:
        a = array[array[i + 1]]
        b = array[array[i + 2]]
        array[array[i + 3]] = a + b if array[i] == 1 else a * b
        i = i + 4
    return array

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Takes a comma-separated string of integers and evaluates them based on Intcode rules, printing the resulting string of integers.')
    parser.add_argument("array", help="A comma-separated string of integers to use with the Intcomp ")
    args = parser.parse_args()
    
    try:
        array = [int(i) for i in args.array.split(',')]
    except ValueError:
        print("Invalid array. Array must only contain integers.")
        exit(1)
    
    array = intcomp(array)

    print(array)
