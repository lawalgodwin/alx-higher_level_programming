#!/usr/bin/python3

def safe_print_division(a, b):
    """Print integer division result
    Args:
        a: The dividend
        b: The divisor

    Returns:
        The result of the division or None
    """

    result = None

    try:
        result = (a / b)

        return result

    except ZeroDivisionError:
        result = None

    finally:
        print("Inside result: {}".format(result))
