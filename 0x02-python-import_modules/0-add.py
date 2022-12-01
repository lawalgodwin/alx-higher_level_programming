#!/usr/bin/python3

from add_0 import add

from sys import exit


def main():

    """My code entrypoint

    Returns:
        returns 0 on success otherwise 1

    """

    a = 1

    b = 2

    print("{0} + {1} = {2}".format(a, b, add(a, b)))

    return (0)


if __name__ == '__main__':
    exit(main())
