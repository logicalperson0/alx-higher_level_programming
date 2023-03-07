#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        i
    else:
        i = i - 32
    print("{:c}".format(i), end="")
