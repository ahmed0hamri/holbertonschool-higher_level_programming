#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = 0  # This line is unnecessary
        self.__height = 0  # This line is unnecessary
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_dimension(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_dimension(value)
        self.__height = value

    def __validate_dimension(self, value):
        if not isinstance(value, int):
            raise TypeError("Dimension must be an integer")
        if value < 0:
            raise ValueError("Dimension must be >= 0")
