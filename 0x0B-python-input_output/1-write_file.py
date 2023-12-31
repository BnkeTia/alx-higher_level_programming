#!/usr/bin/python3

"""
A module that writes a string to a text file (UTF8) and
return the number of characters written.

"""


def write_file(filename="", text=""):
    """
    Return: The number of characters written to the file

    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
