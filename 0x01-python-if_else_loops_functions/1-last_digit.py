#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number * -1
if number < 0:
    i = num % 10
    i = i * -1
else:
    i = number % 10
if i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif i == 0:
    print(f"Last digit of {number} is {i} and is 0")
elif i < 6 and i != 0:
    print(f"Last digit of {number} is {i} and is less than 6 and not 0")
