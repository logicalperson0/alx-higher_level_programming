#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [1, 2, 3],
        [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, 5))
print(matrix_divided(matrix, 2))
print(matrix_divided([[2], [6]], 1))
print(matrix_divided([[3]], 1))
print(matrix_divided([[-20], [-100]], 10))
print(matrix_divided(matrix, -98234))
print(matrix_divided(matrix, -5.5))
print(matrix_divided(matrix, -7.7))

try:
    print(matrix_divided([[3, 6, 7], [12, 445, 6767, 33221]], 13))
except Exception as e:
    print(e)

j = [["s", "School", 2, 4], [4, 5, 6, "t"], ["p", "r"]]
try:
    print(matrix_divided(j, 10))
except Exception as e:
    print(e)

c = [[3, 6, 7, 90], [12, 445, 6767, 33221], [30]]
try:
    print(matrix_divided(c, 5))
except Exception as e:
    print(e)

try:
    print(matrix_divided(None, -7.7))
except Exception as e:
    print(e)

s = [[]]
try:
    print(matrix_divided(s, 10))
except Exception as e:
    print(e)

s = [[], []]
try:
    print(matrix_divided(s, 10))
except Exception as e:
    print(e)

j = [(1, 2, 3), [4, 5, 6], [7, 8, 9]]
try:
    print(matrix_divided(j, 101))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix))
except Exception as e:
    print(e)

try:
    print(matrix_divided(div))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix, "1405"))
except Exception as e:
    print(e)

print(matrix_divided([[3, 4, -9], [-3, 8, -10]], 3))
print(matrix)
