#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n_args = len(sys.argv) - 1
    if n_args == 0:
        print("0 arguments.")
    elif n_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n_args))

    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
