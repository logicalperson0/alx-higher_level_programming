#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tem = matrix.copy()

    for i in range(len(tem)):
        tem[i] = list(map(lambda y: y ** 2, matrix[i]))
    return tem
