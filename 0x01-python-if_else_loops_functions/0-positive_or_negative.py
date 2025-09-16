#! /usr/bin/env python3
"""Module for the function positive_or_negative."""

import random
Number = random.randint(-10000, 10000)
if Number == 0:
    print(f"{Number} is zero")
elif Number > 0:
    print(f"{Number} is positive")
else:
    print(f"{Number} is negative")
