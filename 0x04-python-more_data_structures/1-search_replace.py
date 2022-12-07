#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """A fuction that replaces all occurrence of a value in a list

    Args:
        my_list: The list
        search: The value to be replaced
        replace: The value with which to replace

    Returns:
        Returns a new list with the replaced value
    """

    new_list = list(map(lambda x: x if x != search else replace, my_list))

    return new_list


if __name__ == '__main__':

    search_replace()
