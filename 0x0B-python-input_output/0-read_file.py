#!/usr/bin/python3

"""
A module that reads a text file(UTF8) and prints it out to STDOUT
"""


def read_file(filename=""):
    try:
        """Use with statement to ensure file is properly closed after
        being read
        """
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end=' ')
