#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Get only the element(s) in two sets but not in both

    Args:
        set_1: The fisrt set
        set_2: The second set

    Returns:
        Returns a set containing only the common element
    """

    return (set_1 ^ set_2)


if __name__ == '__main__':

    only_diff_elements()
