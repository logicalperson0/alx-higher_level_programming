#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
try:
    print(add_integer({3, 4, 5}, "ALX"))
except Exception as e:
    print(e)

try:
    print(add_integer(245, 400, 300, 10))
except Exception as e:
    print(e)
try:
    print(add_integer(-5))
except Exception as e:
    print(e)
try:
    print(add_integer(-9.4, -4))
except Exception as e:
    print(e)
