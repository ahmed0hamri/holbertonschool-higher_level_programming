#!/usr/bin/python3
""" the file for the Square class definition
"""


class Square:
    """a class that creates a square

    Keyword arguments:
    argument -- none
    Return: none
    """


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
