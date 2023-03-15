#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    t = list(set_1 & set_2)
    x = list(set_1 | set_2)
    z = []

    for i in range(len(x)):
        y = 0
        for y in range(len(t)):
            if x[i] == t[y]:
                continue
            z.append(x[i])
    return (z)
