#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            x = 32
        else:
            x = 0
        print("{:c}".format(ord(str[i]) - x), end="")
    print()
