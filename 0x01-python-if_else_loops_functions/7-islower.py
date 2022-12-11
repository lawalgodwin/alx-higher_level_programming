#!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase

    Args:
        c: The character

    Returns:
        True if lower otherwise False
    """

    return ((ord(c) >= 97) and (ord(c) <= 122))
