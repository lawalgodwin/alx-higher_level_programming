#!/usr/bin/python3

from sys import argv, exit


def main():
    """Prints the result of the addition of all arguments.

    Returns:
        0 on success 1 otherwise

    """

    result = 0

    for arg in range((len(argv) - 1)):
        result = result + int(argv[arg + 1])

    print("{}".format(result))

    return (0)


if __name__ == '__main__':
    exit(main())
