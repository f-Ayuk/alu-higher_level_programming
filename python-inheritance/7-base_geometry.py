#!/usr/bin/python3
"""python script based on 6-based_geometry"""


class BaseGeometry:
    """A class that represents a base geometry."""

    def area(self):
        """A method that raises an exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
