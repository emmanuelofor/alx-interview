#!/usr/bin/python3

"""Process and compute metrics from input data received via stdin."""

import sys

def printsts(dic, size):
    """ 
    Display the total file size and counts for each status code.
    
    Args:
        dic (dict): A dictionary holding the counts of each HTTP status code.
        size (int): The total accumulated file size.
    """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))

# Dictionary storing the count for each HTTP status code
sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0  # Tracks the number of lines processed
size = 0  # Total size accumulated from the processed lines

try:
    for line in sys.stdin:
        # After every 10 lines, display the current stats
        if count != 0 and count % 10 == 0:
            printsts(sts, size)

        stlist = line.split()
        count += 1

        # Attempt to add the file size value from the line to the total
        try:
            size += int(stlist[-1])
        except:
            pass

        # If a recognized status code is found, increment its count
        try:
            if stlist[-2] in sts:
                sts[stlist[-2]] += 1
        except:
            pass
    # Display the stats after all lines are processed
    printsts(sts, size)

# In case of a keyboard interruption, display the current stats before exiting
except KeyboardInterrupt:
    printsts(sts, size)
    raise
