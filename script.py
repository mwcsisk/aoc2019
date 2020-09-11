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
    # Argument Parser. Parses CLI arguments and provides help text to user.
    parser = argparse.ArgumentParser(description='''
        Takes a comma-separated string of integers and evaluates them based on Intcode rules, printing the resulting array.''')
    parser.add_argument("array", default=False, nargs='?', help='''
        A comma-separated string of integers to use with the Intcomp''')
    parser.add_argument("-f", "--filepath", default=False, help='''
        The path to a text file containing a comma-separated list of integers for use with the Intcomp''')
    args = parser.parse_args()

    # Program does not accept both a string and a filepath
    if args.array and args.filepath:
        print("Either a string of integers or a filepath may be provided, but not both.")
        exit(1)

    # If program was given a file, open it and put its contents into a list
    elif args.filepath:
        with open(args.filepath, "r") as f:
            try:
                array = [int(i) for i in f.readline().split(',')]
            except ValueError:
                print("Invalid file. File must only contain a string of comma-separated integers.")
                exit(1)
            if f.readline():
                print("File has multiple lines. Processing only the first line.")
    
    # If program was given a string, process it into a list
    else:
        try:
            array = [int(i) for i in args.array.split(',')]
        except ValueError:
            print("Invalid array. Array must only contain integers.")
            exit(1)

    # Run the Intcomp according to Intcode rules and overwrite existing array with the results    
    array = intcomp(array)

    # Print resulting array
    print(array)
