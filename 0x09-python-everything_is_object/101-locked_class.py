#!/usr/bin/python3

"""
class LockedClass with no object or attribute
"""


class LockedClass:
    """
    fuction prevents the user from dynamically creating instances
    """

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
