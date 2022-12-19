#!/usr/bin/python3

def safe_print_integer(value):
    """Print a value as integer
    Args:
        value: The value

    Returns:
    True if printed otherwise False
    """
    try:
        print("{0:d}".format(value))

        return (True)

    except (TypeError, ValueError):
        return (False)
