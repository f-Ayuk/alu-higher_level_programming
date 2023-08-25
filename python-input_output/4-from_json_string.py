#!/usr/bin/python3
"""Python data structure represented by a JSON string"""


import json


def from_json_string(my_str):
    """A function that returns an object represented by a JSON string.
    Args:
        my_str (str): The JSON string to be deserialized.
    Returns:
        object: The object corresponding to the JSON string.
    """
    return json.loads(my_str)
