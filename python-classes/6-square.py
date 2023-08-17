#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:

    # Private instance attributes
    __size = 0
    __position = (0, 0)

    # Property to retrieve the size
    @property
    def size(self):
        return self.__size

    # Property setter to set the size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # Property to retrieve the position
    @property
    def position(self):
        return self.__position

    # Property setter to set the position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if i < 1:
                raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    # Instantiation with optional size and optional position
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    # Public instance method to return the current square area
    def area(self):
        return self.__size * self.__size

    # Public instance method to print the square with the character #:
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__position[1]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
