#!/usr/bin/python3
"""Rectangle based on 7-base_geometry"""


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
