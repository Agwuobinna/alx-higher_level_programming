#!/usr/bin/python3

"""This module contains ``Square`` class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Creates a Square.
        Args:
            size(int): the size of the `square`
            x(int): The x axis of the `square`
            y(int): The y axis of the `square`
            id(int|Any): The id of the `square`
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                       self.y, self.width)

    @property
    def size(self):
        """Returns the size of the `square`."""

        return super().width

    @size.setter
    def size(self, value):
        """Sets the square size.
        Args:
            size(int): The size of the square
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes.
        Args:
            args(*): A variadic arguments represented as tuple
            kwargs(**): A variadic arguments represented as dictionary
        """

