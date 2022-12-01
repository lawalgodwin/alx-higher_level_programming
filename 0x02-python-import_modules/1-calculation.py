#!/usr/bin/python3

from sys import exit

from calculator_1 import add, mul, sub, div


def main():
    """My code entrypoint


    Returns:
        Returns 0 on success otherwise 1


    """

    a = 10

    b = 5

    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))

    print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))

    print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))

    print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))

    return (0)


if __name__ == '__main__':
    exit(main())
