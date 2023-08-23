#!/usr/bin/python3
""""sorting algorithm"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))  #use sorted() to get a new sorted list
