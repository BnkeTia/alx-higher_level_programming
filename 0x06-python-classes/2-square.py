#!/usr/bin/python3
"""
This is size validation class for defining a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initiates a new object of the class square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        defines the area of the square.

        """
        return self.__size ** 2
