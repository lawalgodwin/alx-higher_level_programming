#!/usr/bin/python3

import random

number = random.randint(-10, 10)


def main():

    if number.__lt__(0):
        print("{} is negative".format(number))
        return (0)

    elif number.__eq__(0):
        print("{} is zero".format(number))
        return (0)
    print("{} is positive".format(number))

    return (0)


main()
