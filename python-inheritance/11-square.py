#!/usr/bin/python3
"""Contains the class BaseGeometry and subclass Rectangle"""


class BaseGeometry:
    """A class that represents a base geometry."""

    def area(self):
        """A method that raises an exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates an integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        value = int(value)
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that represents a rectangle geometry."""

    def __init__(self, width, height):
        """A method that initializes a rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """A method that returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class that represents a square geometry."""

    def __init__(self, size):
        """A method that initializes a square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A method that returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """A method that returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
