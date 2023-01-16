#!/usr/bin/python3

"""Text indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, str):

        raise TypeError("text must be a string")

    text = text.strip().replace('.', '.\n')
    text = text.replace('?', '?\n').replace(':', ':\n')

    lines = text.split('\n')

    for line in lines:

        if line == lines[-1]:

            print(line.strip(), end='')
            break

        print(line.strip(), end='\n\n')
