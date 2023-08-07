#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize the square with a private instance attribute size"""
        self.size = size

    @property
    def size(self):
        """Return the current value of the private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
