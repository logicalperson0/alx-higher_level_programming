#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    tempo = list(set(my_list))

    for i in range(len(tempo)):
        add = add + tempo[i]

    return (add)
