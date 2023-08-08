#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """a class that defines a square by its size"""

    def __int__(self, size=0):
        """Iiinitialize the square with a private instance attribute size"""
        self.size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
