#!/usr/bin/python3

from sys import argv, exit


def main():
    """Prints the number of and the list of its arguments.

    Returns:
        0 on success 1 otherwise

    """
    if ((len(argv) - 1) == 0):

        print("0 arguments.")

    elif ((len(argv) - 1) == 1):

        print("1 argument:")

        print("{0}: {1}".format((len(argv) - 1), argv[1]))

    else:

        print("{} arguments:".format(len(argv) - 1))

        for arg in range((len(argv) - 1)):

            print("{0}: {1}".format((arg + 1), argv[arg + 1]))

    return (0)


if __name__ == '__main__':
    exit(main())
