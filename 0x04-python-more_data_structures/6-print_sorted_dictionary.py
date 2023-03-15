#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorting = sorted(a_dictionary.items())

    for key, value in sorting:
        print("{}: {}".format(key, value))
