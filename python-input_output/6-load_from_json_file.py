#!/usr/bin/python3
"""Define function load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
