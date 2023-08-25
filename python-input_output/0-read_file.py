#!/usr/bin/python3
"""function to read text files"""


def read_file(filename=""):
    """A function that reads a text file and prints it to stdout.
    Args:
        filename (str): The name of the file to be read. Defaults to """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
