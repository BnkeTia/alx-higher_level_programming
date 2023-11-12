#!/usr/bin/python3
"""Implementation of the base class"""

class Base:
    """Private class attribute of the Base class is initialized to zero"""
    __nb_objects = 0


    """
    A method that initializes the class constructor ('__init__') and
    takes an optional parameter called id.
    if id is not none, then assigne the public instance attribute,
    id with its argument value

    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
