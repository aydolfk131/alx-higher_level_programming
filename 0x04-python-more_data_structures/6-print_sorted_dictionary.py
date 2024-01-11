#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    y = sorted(a_dictionary)
    for i in y:
        print("{}: {}".format(i, a_dictionary[i]))


