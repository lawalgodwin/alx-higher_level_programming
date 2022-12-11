#!/usr/bin/python3

def print_last_digit(number):
    """Get the last digit of a number

    Args:
        number: The number

    Return:
        The last digit of a number
    """

    num = (number) if (number >= 0) else number * (-1)

    r = num % 10

    print(r, end='')

    return (r)
