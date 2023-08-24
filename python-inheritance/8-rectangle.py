#!/usr/bin/python3
"""8-rectangle.py inherits from 7-based_geometry"""


class Rectangle(BaseGeometry):
    """A class that represents a rectangle geometry."""

    def __init__(self, width, height):
        """A method that initializes a rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Attributes:
            __width (int): The width of the rectangle.
            __height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """A method that returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
