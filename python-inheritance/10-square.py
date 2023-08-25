#!/usr/bin/python3
"""contains the class BaseGeometry and base subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square geometry."""

    def __init__(self, size):
        """A method that initializes a square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A method that returns the area of the square."""
        return self.__size ** 2
