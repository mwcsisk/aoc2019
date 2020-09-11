from intcode import intcomp, getints
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
        Returns the noun and verb that create a given target number in position 0 of an Intcode string''')
    parser.add_argument("target", type=int)
    parser.add_argument("filepath")
    args = parser.parse_args()

    # File processing
    try:
        with open(args.filepath, "r") as f:
            try:
                array = getints(f.readline())
            except ValueError:
                print("Error. File must only contain comma-separated integers.")
                exit(1)
    except FileNotFoundError:
        print(f"No such file { args.filepath }")
        exit(1)
    
    for i in range(0,99):
        for j in range(0,99):
            test = array.copy()
            test[1] = i
            test[2] = j
            try:
                test = intcomp(test)
            except IndexError:
                continue
            if test[0] == args.target:
                array = test
                break
    
    print(f"Noun: { array[1] }")
    print(f"Verb: { array[2] }")
    print(f"100 * noun + verb: { 100 * array[1] + array[2] }")
