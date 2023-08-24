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
        validates that value is an integer greater than 0"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
