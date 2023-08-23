#!/usr/bin/python3
"""comparison function which returns a boolean"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class; otherwise False"""
    return type(obj) is a_class  # type() returns the exact type of an object
