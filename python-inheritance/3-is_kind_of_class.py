#!/usr/bin/python3
"""same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Instance of a class that inherited from the specified class returns boolean"""
    return isinstance(obj, a_class)  # isinstance() checks if an object is an instance of a class or a subclass
