#!/usr/bin/python3

from sys import exit

import calculator_1


def main():
    """My code entrypoint


    Returns:
        Returns 0 on success otherwise 1


    """

    a = 10

    b = 5

    print("{0:d} + {1:d} = {2:d}".format(a, b, calculator_1.add(a, b)))

    print("{0:d} - {1:d} = {2:d}".format(a, b, calculator_1.sub(a, b)))

    print("{0:d} * {1:d} = {2:d}".format(a, b, calculator_1.mul(a, b)))

    print("{0:d} / {1:d} = {2:d}".format(a, b, calculator_1.div(a, b)))

    return (0)


if __name__ == '__main__':
    exit(main())
