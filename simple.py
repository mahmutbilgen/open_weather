#!/bin/python3
import os

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 3, 5, 4)
result = map(addition, numbers)
print(list(result))

