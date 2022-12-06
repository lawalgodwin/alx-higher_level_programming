#!/usr/bin/python3

import hidden_4


def main():
    """Print all the names defined by the compiled module hidden_4.py
    Returns:
        returns None
    """
    names = dir(hidden_4)

    for n in names:

        if not(n.startswith("__")):

            print(n)


if __name__ == '__main__':

    main()
