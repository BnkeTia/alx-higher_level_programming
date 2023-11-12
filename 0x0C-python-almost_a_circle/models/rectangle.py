#!/usr/bin/python3
"""importing the base model"""
from models.base import Base

"""constructing a class Rectangle that inherits from a class Base"""


class Rectangle(Base):
    """Method definition for the rectangle class with designated parameters

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Definition of private instance attribute width using getter and setter

    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be a positive integer")
        self.__width = value

    """Definition of private attribute height."""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be a positive integer")
        self.__height = value

    """Definition of private attribute x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("X must be an integer")
        if value < 0:
            raise ValueError("X cannot be negative")
        self.__x = value

    """Definition of the private attribute y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("Y must be an integer")
        if value < 0:
            raise ValueError("Y cannot be negative")
        self.__y = value
