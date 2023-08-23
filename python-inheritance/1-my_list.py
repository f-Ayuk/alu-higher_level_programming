#!/usr/bin/python3
""""sorting algorithm"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self)) # sorted() is a built-in function that returns a new sorted list
