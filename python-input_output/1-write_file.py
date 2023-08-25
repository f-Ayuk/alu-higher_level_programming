#!/usr/bin/python3
"""function returns number of characters written to text file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file 
    and returns the number of characters written.
    
    Args:
        filename (str): The name of the file to be written. Defaults to ""
        text (str): The string to be written. Defaults to ""

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
