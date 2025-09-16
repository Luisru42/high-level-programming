#! /usr/bin/env python3
import random
Number = random.randint(-10000, 10000)
last_digit = abs(Number) % 10
if Number < 0:
    last_digit *= -1
print(f"Last digit of {Number} is {last_digit} and is ", end="")
if last_digit == 0:
    print("0")
elif last_digit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
