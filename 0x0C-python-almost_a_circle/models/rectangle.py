#!/usr/bin/python3

"""This module contains `Rectangle` class."""


from models.base import Base


class Rectangle(Base):
    """The `Rectangle` class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates a `Rectangle`.
        Args:
            width(int): The `Rectangle` width
            height(int): The `Rectangle` height
            x(int): The `Rectangle` x
            y(int): The `Rectangle` y
            id(int): The `Rectangle` id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the `Rectangle` `width`."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets `Rectangle` width.
        Args:
            value(int): The `width` of the `Rectangle`
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the `Rectangle` `height`."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the `Rectangle` `height`.

