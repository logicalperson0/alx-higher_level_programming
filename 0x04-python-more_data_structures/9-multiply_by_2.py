#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictt = a_dictionary.copy()

    for i in a_dictionary:
        dictt[i] = a_dictionary[i] * 2

    return dictt
