#!/usr/bin/python3
"""Rectangle based on 7-base_geometry"""


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
