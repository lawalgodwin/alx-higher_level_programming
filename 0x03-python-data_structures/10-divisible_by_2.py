#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Determine the multiples of 2 in a list
    Args:
        my_list: The list

    Returns:
        A list containing the truthiness of each interger
    """

    list_result = []

    for n in my_list:
        list_result.append((n % 2) == 0)

    return list_result
