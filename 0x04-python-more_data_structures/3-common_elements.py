#!/usr/bin/python3
def common_elements(set_1, set_2):
    x = list(set_1)
    y = list(set_2)
    z = []

    for i in range(len(x)):
        if x[i] == y[i]:
            z.append(x[i])
    return z
