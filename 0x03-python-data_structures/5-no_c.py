#!/usr/bin/python3

def no_c(my_string):
    '''A  function that removes all characters "c" and "C" from a string
    Args:
        my_string: the string

    Returns:
        Returns the new string
    '''
    new_string = ""
    if my_string:
        for c in my_string:
            if (c == 'c' or c == 'C'):
                new_string = new_string + ""
                continue
            new_string = new_string + c
    return new_string
