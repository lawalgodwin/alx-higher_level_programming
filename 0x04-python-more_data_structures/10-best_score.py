#!/usr/bin/python3

def best_score(a_dictionary):
    """Get the key with the max value in a dictionary.

    Args:
        a_dictionary: The dictionary

    Returns:
        The key if there is a dictionary else 'None'
    """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
