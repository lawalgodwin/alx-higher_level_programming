def element_at(my_list, idx):
    """A function that retrieves an element from a list
    Args:
        my_list: the list
        idx: the index of the element
    Returns:
        returns the element if found otherwise None
    """
    num_of_elements = len(my_list)

    if (idx < 0 or idx >= num_of_elements):
        return ("None")
    return my_list[idx]
