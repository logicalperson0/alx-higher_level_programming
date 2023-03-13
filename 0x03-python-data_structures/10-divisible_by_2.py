#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    chk_list = []

    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            chk_list.append(True)
        else:
            chk_list.append(False)

    return chk_list
