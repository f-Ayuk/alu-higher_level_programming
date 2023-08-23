#!/usr/bin/python3
"""same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Instance of a class from the specified class returns boolean"""
    return isinstance(obj, a_class)  # isinstance() checks for an instance of a class or a subclass
