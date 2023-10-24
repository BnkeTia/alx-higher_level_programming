#!/usr/bin/python3
import math
"""
python class magicclass

"""


class MagicClass:
    """
    A class that represents a magical circle with radius.

    Attributes:
        radius (int or float): The radius of the magical circle.

    Methods:
        __init__(self, radius=0): Initializes a new instance of the MagicClass.
        area(self): Computes the area of the magical circle.
        circumference(self): Computes the circumference of the magical circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (int or float): The radius of the magical circle.

        Raises:
            TypeError: If the provided radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the magical circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes and returns the circumference of the magical circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
