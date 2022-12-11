#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

num = (number) if (number >= 0) else number * (-1)

result = (num % 10, number) if number >= 0 else ((num % 10) * (-1), number)

if (result[0] < 6 and result[0] != 0):

    print(f"Last digit of {result[1]} is {result[0]} and is less than 6 and not 0")

elif (result[0] > 5):

    print(f"Last digit of {result[1]:d} is {result[0]:d} and is greater than 5")

else:
    print(f"Last digit of {result[1]:d} is {result[0]:d} and is 0")
