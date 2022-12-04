#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list
    Args:
        my_list: The list
        idx: The index of the item to be deleted in the list
    Returns:
        The original list if index is not found else None
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]

    return my_list
