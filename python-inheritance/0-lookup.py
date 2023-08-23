#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """a built-in function to return list of names in the object's namespace"""

    return dir(obj)
