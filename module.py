def map_wire(array):
    '''
    Given a list of instructions, plots the points occupied by a wire in a list of tuples. Returns the list.
    '''

    xpos = 0
    ypos = 0
    list1 = []

    # Go through each direction
    for dir in array:
        # print(f"Mapping {dir}")

        # Get the length the wire will travel in this instruction
        length = int(dir[1:])

        # Switchboard
        if dir[0] == 'R':

            # Adds all points between the current position and the end position of this instruction
            result = [(xpos + x, ypos) for x in range(0, length)]
            xpos += length
        elif dir[0] == 'U':
            result = [(xpos, ypos + y) for y in range(0, length)]
            ypos += length
        elif dir[0] == 'L':
            result = [(xpos - x, ypos) for x in range(0, length)]
            xpos -= length
        elif dir[0] == 'D':
            result = [(xpos, ypos - y) for y in range(0, length)]
            ypos -= length
        else:
            print("Error: file contains non-standard directions. Acceptable directions: 'U', 'D', 'L', 'R'")
            exit(1)
        
        # print(result)

        list1 += result
        
        # print(f"Mapped { dir }")
    
    list1.append((xpos,ypos))

    return list1