#!/usr/bin/python3
"""comparison function which returns a boolean"""


def is_same_class(obj, a_class):
    """Returns boolean for an instance of the specified class"""
    return type(obj) is a_class  # type() returns the exact type of an object
