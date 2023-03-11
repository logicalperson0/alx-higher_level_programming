#!/usr/bin/python3
def no_c(my_string):
    stri = []
    stry = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            stri.append(my_string[i])
    return stry.join(stri)
