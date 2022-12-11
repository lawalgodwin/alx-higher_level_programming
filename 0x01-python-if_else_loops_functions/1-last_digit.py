#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

num = (number) if (number >= 0) else number * (-1)

r = (num % 10, number) if number >= 0 else ((num % 10) * (-1), number)

if (r[0] < 6 and r[0] != 0):

    print(f"Last digit of {r[1]} is {r[0]} and is less than 6 and not 0")

elif (r[0] > 5):

    print(f"Last digit of {r[1]} is {r[0]:d} and is greater than 5")

else:
    print(f"Last digit of {r[1]:d} is {r[0]:d} and is 0")
