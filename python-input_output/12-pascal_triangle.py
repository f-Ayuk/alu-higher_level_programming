#!/usr/bin/python3
'''Creates a function pascal_triangle
'''


def pascal_triangle(n):
    '''Function returns a list of lists of integers
    representing a pascals triangle
    '''
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))
