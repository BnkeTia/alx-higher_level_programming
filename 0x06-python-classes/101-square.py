#!/usr/bin/python3
"""
A class module for printing a square object or instance
"""


class Square:
    """
    This class defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size property.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position property.

        Returns:
            tuple: The position of the square as a tuple of 2
            positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position property.

        Args:
            value (tuple): The position of the square as a tuple of
            2 positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the squar
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the specified position and size.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


if __name__ == "__main__":
    my_square = Square(5, (1, 3))
    my_square.my_print()

    print("---")

    my_square.size = 0
    my_square.my_print()

    print("---")

    my_square.size = 5
    my_square.position = (3, 2)
    my_square.my_print()
