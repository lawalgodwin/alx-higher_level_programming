#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """A fuction that replaces an item in a list
    Args:
        my_list: The list
        idx: the index of the original item in the list
        element: the new element with which to replace
    Returns:
        returns a modified list if successful else returns the original list
    """
    num_of_elements = len(my_list)

    if (idx < 0 or idx >= num_of_elements):
        return (my_list)

    my_list[idx] = element

    return (my_list)
