#!/usr/bin/python3
"""
Rectangle class Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle subclass that inherit from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implement area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return width/height"""
        return f"[Rectangle] {self.__width}/{self.__height}"
