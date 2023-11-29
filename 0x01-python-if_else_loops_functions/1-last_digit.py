#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    last_num = number % -10
else:
    last_num = number % 10

if last_num > 5:
    print(f"{number} is positive")
elif last_num == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
