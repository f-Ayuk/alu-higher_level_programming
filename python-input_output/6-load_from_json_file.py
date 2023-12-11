#!/usr/bin/python3
"""Define function load_from_json_file.py"""

import json

def load_from_json_file(filename):
    # Open the file in read mode using the with statement
    with open(filename, 'r') as f:
        # Load the JSON data from the file using the json.load() method
        obj = json.load(f)
    # Return the object
    return obj
