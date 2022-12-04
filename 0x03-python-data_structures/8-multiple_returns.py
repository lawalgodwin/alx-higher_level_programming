#!/usr/bin/python3

def multiple_returns(sentence):
    """A fuction that gets the length and first char of a string
    Args:
        sentence: the string
    Returns:
        A tuple containing the str length and first char
    """
    if not(sentence):
        return(len(sentence), "None")
    return (len(sentence), sentence[0])
