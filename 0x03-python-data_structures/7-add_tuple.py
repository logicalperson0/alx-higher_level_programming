#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_x = len(tuple_a)
    len_y = len(tuple_b)

    if len_x == 0:
        i = 0
        j = 0
    elif len_x == 1:
        i = tuple_a[0]
        j = 0
    else:
        i = tuple_a[0]
        j = tuple_a[1]

    if len_y == 0:
        c = 0
        d = 0
    elif len_y == 1:
        c = tuple_b[0]
        d = 0
    else:
        c = tuple_b[0]
        d = tuple_b[1]

    v = (i + c, j + d)
    return v
