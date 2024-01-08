#!/usr/bin/python3
"""Defines a class Rect that inherits from BaseGeo."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rect using BaseGeo."""

    def __init__(self, width, height):
        """Intialize a new Rect.

        Args:
            width (int): The width of the new Rect.
            height (int): The height of the new Rect.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

