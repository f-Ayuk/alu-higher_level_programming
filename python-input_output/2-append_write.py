#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and
    returns the number of characters added.
    Args:
        filename (str): The name of the file to be appended. Defaults to "".
        text (str): The string to be appended. Defaults to "".
    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
