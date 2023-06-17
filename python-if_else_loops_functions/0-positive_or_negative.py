#!/usr/bin/python3
import random
number = random.randint(-10, 10)
"""
This script generates a random number and prints whether it is positive, zero, or negative.
"""
if number > 0:
    print(f'{number} is positive')
elif number == 0:
    print(f'{number} is zero')
else: 
    print(f'{number} is negative')  
