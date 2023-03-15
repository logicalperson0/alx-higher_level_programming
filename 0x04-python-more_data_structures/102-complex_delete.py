#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tempo = a_dictionary.copy()
    for i in tempo:
        if value == a_dictionary[i]:
            del a_dictionary[i]

    return a_dictionary
