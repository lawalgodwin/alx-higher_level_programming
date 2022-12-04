#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace element in a list at a position leaving original list d same

    Args:
        my_list: The list
        idx: the index of the element to be replaced
        element: The new value with which to replace
    Returns:
        returns the new list
    """

    num_of_elements = len(my_list)

    if (idx < 0 or idx >= num_of_elements):
        return (my_list)
# make a shallow copy of the original list

    new_list = my_list[:]

    new_list[idx] = element

    return new_list
