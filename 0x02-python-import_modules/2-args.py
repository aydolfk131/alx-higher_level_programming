#!/usr/bin/python3

#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    #importing the sys module
    import sys

    argume = sys.argv
    size = len(argme) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, argume[i]))

    elif size == 0:
        print("{} arguments.".format(size))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, argume[1]))

