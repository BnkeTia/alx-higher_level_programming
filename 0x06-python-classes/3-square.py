#!/usr/bin/python3
"""
class that defines the area of a square
"""


class Square:
    """
    A class that defines a square.

    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculate area of square

        """

        return self.__size ** 2
