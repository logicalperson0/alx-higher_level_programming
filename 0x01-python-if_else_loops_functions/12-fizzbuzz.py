#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        x = i % 3
        y = i % 5
        z = i % 15
        if z == 0:
            print("FizzBuzz", end=" ")
        elif y == 0:
            print("Buzz", end=" ")
        elif x == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(i), end=" ")
