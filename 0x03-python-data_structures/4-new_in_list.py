#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    t = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        for i in range(len(t)):
            if i == idx:
                t[i] = element
                return t
