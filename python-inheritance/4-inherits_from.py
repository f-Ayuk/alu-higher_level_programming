#!/usr/bin/python3
"""# issubclass() checks if a class is a subclass of another class"""


def inherits_from(obj, a_class):
    """Returns boolean if the object is an instance of specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
