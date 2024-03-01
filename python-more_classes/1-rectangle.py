#!/usr/bin/python3
"""
    This class creates an empty rectangle
"""


class Rectangle:
    """
    rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
    Property setter for the height attribute, validating that the input is an
    integer and greater than or equal to 0. Raises a TypeError otherwise.
    """

    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


        """
        Property setter for the weight attribute, validating that the input is an
        integer and greater than or equal to 0. Raises a TypeError otherwise.
        """


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width
