#!/usr/bin/python3
for i in range(0, 100):
    print("{:02d}".format(i), end=", ")
    if i + 1 == 99:
        print("{}".format(i + 1))
        break
