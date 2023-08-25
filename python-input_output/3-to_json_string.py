#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string).
    Args:
        my_obj (object): The object to be serialized.
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
