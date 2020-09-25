import argparse
from module import map_wire

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''
        Returns the closest intersection of two wires''')
    parser.add_argument("filepath")
    args = parser.parse_args()

    # File processing
    try:
        with open(args.filepath, "r") as f:
            array1 = f.readline().split(',')
            array2 = f.readline().split(',')
    except FileNotFoundError:
        print(f"No such file { args.filepath }")
        exit(1)
    
    # Map the points that each wire occupies
    wire1 = map_wire(array1)
    # print(wire1)
    wire2 = map_wire(array2)
    # print(wire2)

    # Create a list of intersections
    temp = set(wire2)
    intersections = [value for value in wire1 if value in temp]
    intersections.remove((0,0))

    # Get a placeholder point for comparison
    result = intersections[0]

    # Compare all points and return the closest to (0,0)
    for point in intersections:
        if wire1.index(point) + wire2.index(point) < wire1.index(result) + wire2.index(result):
            result = point
    
    print(result)
    print(wire1.index(result) + wire2.index(result))